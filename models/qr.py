from fastapi import Form
from pydantic import BaseModel


class QR(BaseModel):
    ssid: str
    password: str
    hidden: bool
    encryption: str

    @classmethod
    def as_form(
        cls,
        ssid: str = Form(...),
        password: str = Form(...),
        hidden: bool = Form(False),
        encryption: str = Form(...),
    ):
        return cls(ssid=ssid, password=password, hidden=hidden, encryption=encryption)
