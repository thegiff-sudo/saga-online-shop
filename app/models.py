from pydantic import BaseModel, Field
from typing import List, Optional

class OrderItemInput(BaseModel):
    product_id: str
    quantity: int = Field(gt=0, default=1)

class OrderCreateRequest(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: Optional[str] = ""
    address: str
    city: str
    state: str
    pincode: str
    payment_method: str = "UPI Online"
    coupon_code: Optional[str] = ""
    items: List[OrderItemInput]

class CouponRequest(BaseModel):
    code: str
    subtotal: float

class PincodeRequest(BaseModel):
    pincode: str

class StatusUpdateRequest(BaseModel):
    status: str
