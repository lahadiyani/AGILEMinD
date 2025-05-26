from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, validator
from datetime import datetime

class PromptConfig(BaseModel):
    prompt_name: str = Field(..., description="Nama unik prompt (misal: coder_prompts, planner_prompts, researcher_prompts)")
    file_name: str = Field(..., description="Nama file prompt di direktori prompts (misal: coder_prompts.txt)")
    description: Optional[str] = Field("", description="Deskripsi singkat prompt")
    variables: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Variabel yang digunakan dalam prompt (jika ada)")
    is_active: bool = Field(default=True, description="Status aktif prompt")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Waktu pembuatan konfigurasi prompt")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata tambahan prompt")

    @validator('file_name')
    def validate_file_name(cls, v):
        if not v.endswith('.txt'):
            raise ValueError("file_name harus berupa file .txt")
        return v

class PromptLoadInput(BaseModel):
    file_name: str = Field(..., description="Nama file prompt yang akan di-load")

class PromptLoadResult(BaseModel):
    prompt_name: str
    file_name: str
    content: Optional[str] = None
    success: bool
    error: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)