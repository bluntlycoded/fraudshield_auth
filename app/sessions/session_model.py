from pydantic import BaseModel
from datetime import datetime
class Session(BaseModel):
    user_id: str
    device_id: str
    ip_address: str
    timestamp: datetime
