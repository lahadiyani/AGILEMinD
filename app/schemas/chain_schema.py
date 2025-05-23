from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, validator
from datetime import datetime

class ChainStepConfig(BaseModel):
    step_name: str = Field(..., description="Nama unik step dalam chain")
    agent_name: str = Field(..., description="Nama agent yang menjalankan step ini (harus terdaftar di AGENT_REGISTRY)")
    input_keys: Optional[List[str]] = Field(default_factory=list, description="Daftar input yang dibutuhkan step")
    output_keys: Optional[List[str]] = Field(default_factory=list, description="Daftar output yang dihasilkan step")
    params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Parameter tambahan untuk step/agent")

class ChainConfig(BaseModel):
    chain_name: str = Field(..., description="Nama unik chain (harus terdaftar di CHAIN_REGISTRY)")
    description: Optional[str] = Field("", description="Deskripsi singkat chain")
    steps: List[ChainStepConfig] = Field(..., description="Urutan step dalam chain")
    chain_params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Parameter tambahan untuk chain")
    is_active: bool = Field(default=True, description="Status aktif chain")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Waktu pembuatan chain")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata tambahan chain")

    @validator('chain_name')
    def validate_chain_name(cls, v):
        if not v or not isinstance(v, str):
            raise ValueError("chain_name harus berupa string dan tidak boleh kosong.")
        return v

class ChainRunInput(BaseModel):
    input_data: Any = Field(..., description="Input utama untuk chain")

class ChainRunResult(BaseModel):
    chain_name: str
    input_data: Any
    output: Any
    success: bool
    error: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)