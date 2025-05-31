from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, validator
from datetime import datetime

class ToolConfig(BaseModel):
    tool_name: str = Field(..., description="Nama unik tool, sesuai registry (misal: CustomTool, PollinationTool)")
    description: Optional[str] = Field("", description="Deskripsi singkat tool")
    params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Parameter konfigurasi tool")
    is_active: bool = Field(default=True, description="Status aktif tool")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Waktu pembuatan konfigurasi tool")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata tambahan tool")

    @validator('tool_name')
    def validate_tool_name(cls, v):
        if not v or not isinstance(v, str):
            raise ValueError("tool_name harus berupa string dan tidak boleh kosong.")
        return v

class ToolRunInput(BaseModel):
    args: Optional[list] = Field(default_factory=list, description="Argumen positional untuk tool")
    kwargs: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Argumen keyword untuk tool")

class ToolRunResult(BaseModel):
    tool_name: str
    args: Optional[list]
    kwargs: Optional[Dict[str, Any]]
    output: Any
    success: bool
    error: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)