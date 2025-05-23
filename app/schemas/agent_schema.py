from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, validator
from datetime import datetime

class AgentInitParams(BaseModel):
    name: str = Field(..., description="Nama unik agent")
    description: Optional[str] = Field("", description="Deskripsi singkat agent")
    prompt: Optional[str] = Field(None, description="Prompt template agent")
    llm: Optional[str] = Field(None, description="Nama LLM yang digunakan agent")
    memory: Optional[str] = Field(None, description="Tipe/ID memory yang digunakan agent")
    tools: List[str] = Field(default_factory=list, description="Daftar tools yang digunakan agent")
    logging_enabled: bool = Field(default=True, description="Aktifkan logging untuk agent")

class AgentConfig(BaseModel):
    agent_name: str = Field(..., description="Nama class agent, sesuai registry (misal: CoderAgent)")
    params: AgentInitParams = Field(..., description="Parameter inisialisasi agent")
    is_active: bool = Field(default=True, description="Status aktif agent")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Waktu pembuatan agent")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata tambahan agent")

    @validator('agent_name')
    def validate_agent_name(cls, v):
        if not v or not isinstance(v, str):
            raise ValueError("agent_name harus berupa string dan tidak boleh kosong.")
        return v

class AgentRunInput(BaseModel):
    input_text: str = Field(..., description="Input utama untuk agent")

class AgentRunResult(BaseModel):
    agent_name: str
    input_text: str
    output: Any
    success: bool
    error: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)