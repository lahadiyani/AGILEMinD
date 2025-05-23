from typing import Optional, Dict, Any, List, Literal
from pydantic import BaseModel, Field, validator
from datetime import datetime

class MemoryConfig(BaseModel):
    memory_type: Literal["faiss", "elasticsearch", "chroma"] = Field(..., description="Tipe backend memory vectorstore")
    params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Parameter inisialisasi backend memory")
    is_active: bool = Field(default=True, description="Status aktif memory store")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Waktu pembuatan konfigurasi memory")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata tambahan memory")

    @validator('memory_type')
    def validate_memory_type(cls, v):
        allowed = {"faiss", "elasticsearch", "chroma"}
        if v not in allowed:
            raise ValueError(f"memory_type '{v}' tidak valid. Pilihan: {allowed}")
        return v

class MemoryDocument(BaseModel):
    content: str = Field(..., description="Isi dokumen/text yang disimpan")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata dokumen (misal: source, tags, dsb)")
    embedding: Optional[List[float]] = Field(None, description="Vektor embedding dokumen (jika diperlukan)")

class MemoryAddInput(BaseModel):
    docs: List[MemoryDocument] = Field(..., description="Daftar dokumen yang akan ditambahkan ke memory")

class MemorySearchInput(BaseModel):
    query: str = Field(..., description="Query text atau vektor untuk pencarian similarity")
    top_k: int = Field(default=5, description="Jumlah hasil teratas yang diambil")
    filters: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Filter metadata opsional")

class MemorySearchResult(BaseModel):
    results: List[Dict[str, Any]] = Field(..., description="Hasil pencarian similarity (list dokumen dengan skor, metadata, dsb)")
    success: bool = Field(..., description="Status keberhasilan operasi")
    error: Optional[str] = Field(None, description="Pesan error jika gagal")
    timestamp: datetime = Field(default_factory=datetime.utcnow)