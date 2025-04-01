import pathlib
import pytesseract
from PIL import Image

BASE_DIR = pathlib.Path(__file__).parent
IMG_DIR = BASE_DIR / "images"
img1_path = IMG_DIR / "skype.png"
img2_path = IMG_DIR / "skype.png"

img = Image.open(img1_path)

preds = pytesseract.image_to_string(img)
predictions = [ x for x in preds.split("\n")]

print(predictions)