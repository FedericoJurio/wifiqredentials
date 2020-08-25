import base64
import io

import qrcode
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.qr import QR

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def generate_qr(request: Request, qr: QR = Depends(QR.as_form)):
    data = f"WIFI:T:{qr.encryption};S:{qr.ssid};P:{qr.password};{'H:true' if qr.hidden else ''};"
    qr = qrcode.QRCode()
    qr.add_data(data)
    img = qr.make_image(fill_color="black", back_color="transparent")
    img_byte_array = io.BytesIO()
    img.save(img_byte_array)
    img_byte_array = img_byte_array.getvalue()
    base64_img = "data:image/png;base64," + base64.b64encode(img_byte_array).decode("utf-8")
    return templates.TemplateResponse("qr.html", {"request": request, "qr": base64_img})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
