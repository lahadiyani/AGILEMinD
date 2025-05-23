from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, validator
from datetime import datetime

class LoaderConfig(BaseModel):
    loader_name: str = Field(..., description="Nama unik loader, sesuai registry (misal: pdf_loader)")
    params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Parameter untuk inisialisasi loader")
    is_active: bool = Field(default=True, description="Status aktif loader")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Waktu pembuatan konfigurasi loader")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata tambahan loader")

    @validator('loader_name')
    def validate_loader_name(cls, v):
        if not v or not isinstance(v, str):
            raise ValueError("loader_name harus berupa string dan tidak boleh kosong.")
        return v

class LoaderRunInput(BaseModel):
    source: str = Field(..., description="Path atau sumber data yang akan di-load")
    params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Parameter runtime opsional")

class LoaderRunResult(BaseModel):
    loader_name: str
    source: str
    output: Any
    success: bool
    error: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)