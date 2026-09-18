"""Sample FastAPI Application with Seeded Bug.
Bug: Missing validation for empty phone number leading to an unhandled ValueError / HTTP 500.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI(title="Sample User Management Service")

# In-memory store
users_db: List[Dict[str, Any]] = []


class UserCreate(BaseModel):
    name: str
    email: str
    phone: str


def format_phone_number(raw_phone: str) -> str:
    """Formats 10-digit raw phone number into standard format +1 (XXX) XXX-XXXX."""
    digits = "".join(ch for ch in raw_phone if ch.isdigit())
    if len(digits) != 10:
        # Unhandled ValueError triggers 500 error when phone is empty or invalid
        raise ValueError(f"Phone number must contain exactly 10 digits, got '{raw_phone}'")
    return f"+1 ({digits[:3]}) {digits[3:6]}-{digits[6:]}"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    # SEEDED BUG: Missing validation for empty or blank phone number.
    # It should check `if not user.phone or not user.phone.strip(): raise HTTPException(status_code=400, detail="Phone cannot be empty")`
    # Currently, calling format_phone_number raises an unhandled ValueError causing a 500 Internal Server Error.
    formatted_phone = format_phone_number(user.phone)

    record = {
        "id": len(users_db) + 1,
        "name": user.name.strip(),
        "email": user.email.strip(),
        "phone": formatted_phone,
    }
    users_db.append(record)
    return record


@app.get("/users")
def get_users():
    return users_db
