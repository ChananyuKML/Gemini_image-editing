
# Gemini Image Editing

Edit image using image and prompt

## build

Clone the project
```bash
  git clone https://github.com/ChananyuKML/Gemini_image-editing.git
```

Build using docker
```bash
  docker build -t app .  
```

Run app
```bash
  docker run -p 8000:8000 app
```

## Example request
![Original image](image/car.png)
```json
{
  "prompt": "turn the car blue", // prompt for editing
  "image": "iVBORw0KGgoAAAANSUhEUgAABFQAAAK9CA..." // image to edit
}
```

## Example response
![Edited image](image/edited.png)
```json
{
  "image":"iVBORw0KGgoAAAANSUhEUgAABQAAAAMgCAIAAADz..." // edited image
}
```




