from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from PIL import Image
from io import BytesIO
import base64
import os


app = FastAPI()

client = genai.Client(api_key="YOUR-API-KEY")

# --------------------
# Request / Response
# --------------------

class EditRequest(BaseModel):
    prompt: str
    image: str  # base64

class EditResponse(BaseModel):
    image: str  # base64

# --------------------
# Helper functions
# --------------------

def base64_to_pil(b64: str) -> Image.Image:
    try:
        data = base64.b64decode(b64)
        return Image.open(BytesIO(data))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 image")

def image_to_base64(img: Image.Image) -> str:
    buf = BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")


# --------------------
# Endpoint
# --------------------

@app.post("/edit")
def edit_image(req: EditRequest):
    input_image = base64_to_pil(req.image)

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[req.prompt, input_image],
    )

    for part in response.parts:
        if part.inline_data:
            image_bytes = part.inline_data.data
            return {
                "image": base64.b64encode(image_bytes).decode("utf-8")
            }

    raise HTTPException(status_code=500, detail="No image returned from Gemini")
