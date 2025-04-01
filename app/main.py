import pathlib
import io
import uuid
from fastapi import (
    FastAPI,
    HTTPException,
    Request,
    File,
    UploadFile,
    )
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from .config import DEBUG, ECHO_ACTIVE
from PIL import Image

print("DEBUG", DEBUG)

BASE_DIR = pathlib.Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
def home_view(request: Request):
    print(request)
    return templates.TemplateResponse("home.html", {"request": request, "abc": "testing"})

@app.post("/")
def home_detail_view():
    return {"hello": "world"}

@app.post("/img-echo/", response_class=FileResponse)
async def img_echo_view(file:UploadFile = File(...)):
    if not ECHO_ACTIVE:
        raise HTTPException(detail="Invalid endpoint", status_code=400)
    UPLOAD_DIR.mkdir(exist_ok=True)
    bytes_str = io.BytesIO(await file.read())
    try:
        img = Image.open(bytes_str)
    except:
        raise HTTPException(detail="Invalid image", status_code=400)
    fname = pathlib.Path(file.filename)
    fext = fname.suffix # .jp, .txt
    dest = UPLOAD_DIR / f"{uuid.uuid1()}{fext}"
    img.save(dest)
    return dest