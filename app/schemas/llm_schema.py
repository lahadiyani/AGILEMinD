from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, validator
from datetime import datetime

class LLMConfig(BaseModel):
    llm_name: str = Field(..., description="Nama unik LLM, sesuai registry (misal: openai, pollinations, mistral)")
    model_name: Optional[str] = Field(None, description="Nama model spesifik (misal: gpt-4, mistral-tiny, v2)")
    api_key: Optional[str] = Field(None, description="API key jika diperlukan")
    base_url: Optional[str] = Field(None, description="Base URL endpoint LLM jika custom/self-hosted")
    params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Parameter tambahan untuk LLM (misal: temperature, max_tokens, dsb)")
    is_active: bool = Field(default=True, description="Status aktif LLM")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Waktu pembuatan konfigurasi LLM")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata tambahan LLM")

    @validator('llm_name')
    def validate_llm_name(cls, v):
        allowed = {"openai", "pollinations", "mistral"}
        if v not in allowed:
            raise ValueError(f"llm_name '{v}' tidak valid. Pilihan: {allowed}")
        return v

class LLMRunInput(BaseModel):
    prompt: str = Field(..., description="Prompt yang akan dikirim ke LLM")
    model: Optional[str] = Field(None, description="Model yang digunakan (override jika perlu)")
    params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Parameter runtime opsional")

class LLMRunResult(BaseModel):
    llm_name: str
    prompt: str
    output: Any
    success: bool
    error: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)