from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime

class UserConfig(BaseModel):
    user_id: str = Field(..., description="ID unik user")
    username: str = Field(..., description="Username unik user")
    email: Optional[EmailStr] = Field(None, description="Alamat email user")
    full_name: Optional[str] = Field("", description="Nama lengkap user")
    hashed_password: Optional[str] = Field(None, description="Password yang sudah di-hash")
    is_active: bool = Field(default=True, description="Status aktif user")
    is_superuser: bool = Field(default=False, description="Apakah user adalah superuser/admin")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Waktu pembuatan user")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata tambahan user")

    @validator('username')
    def validate_username(cls, v):
        if not v or not isinstance(v, str):
            raise ValueError("username harus berupa string dan tidak boleh kosong.")
        return v

class UserLoginInput(BaseModel):
    username: str = Field(..., description="Username user")
    password: str = Field(..., description="Password user (plain, akan di-hash saat proses login)")

class UserLoginResult(BaseModel):
    user_id: Optional[str]
    username: Optional[str]
    access_token: Optional[str]
    success: bool
    error: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)