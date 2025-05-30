import shutil
import time
from fastapi.testclient import TestClient
from app.main import app, BASE_DIR, UPLOAD_DIR

from PIL import Image

client = TestClient(app)


def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers['content-type']

def test_post_home():
    response = client.post("/")
    assert response.status_code == 200
    assert "application/json" in response.headers['content-type']
    assert response.json() == {"hello": "world"}

valid_iamge_extensions = ['png', 'jpeg', 'jpg']

def test_echo_upload():
    img_saved_path = BASE_DIR / "images"

    for path in img_saved_path.glob("*"):
        try:
            img = Image.open(path)
        except:
            img = None

        response = client.post("/img-echo", files={"file": open(path, 'rb')})

        if img is not None:
            assert response.status_code == 200
        else:
            assert response.status_code == 400
    # time.sleep(3)
    shutil.rmtree(UPLOAD_DIR)