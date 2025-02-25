from pydantic import BaseModel
class Device(BaseModel):
    device_id: str
    user_id: str
    device_name: str
    trusted: bool
