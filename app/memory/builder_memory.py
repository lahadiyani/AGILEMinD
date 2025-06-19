import os
from memory.registry_memory import RegistryMemory
from memory.utils_memory import summarize_if_needed, should_promote
from memory.base_memory import BaseMemory
from memory.store_memory import PostgresMemory, InMemoryBuffer
from typing import Optional

class MemoryBuilder:
    def __init__(self, namespace: Optional[str] = None):
        self.namespace = namespace or "default"
        self.registry = self._init_registry(self.namespace)
        self.stm: BaseMemory = self.registry.get("stm")
        self.ltm: BaseMemory = self.registry.get("ltm")

    def _init_registry(self, namespace: str) -> RegistryMemory:
        dsn = os.getenv("PGVECTOR_DSN", "postgresql://user:pass@localhost/db")
        reg = RegistryMemory()
        reg.register("stm", InMemoryBuffer(max_len=100))
        reg.register("ltm", PostgresMemory(dsn=dsn, namespace=namespace))
        return reg

    def process(self, user_input: str) -> str:
        self.stm.add("user", user_input, {"role": "user"})

        stm_data = self.stm.retrieve(user_input, limit=10)
        ltm_data = self.ltm.retrieve(user_input, limit=5)
        context = stm_data + ltm_data

        prompt = self._compose_prompt(user_input, context)
        response = self._call_llm(prompt)

        self.stm.add("assistant", response, {"role": "assistant"})

        if should_promote(user_input, response):
            summary = summarize_if_needed(user_input, response)
            self.ltm.add("summary", summary, {"original": user_input, "via": "auto"})

        return response

    def _compose_prompt(self, user_input: str, memories: list) -> str:
        formatted = "\n".join(f"[{r}] {c}" for r, c, m in memories)
        return f"{formatted}\n\n[User]: {user_input}"

    def _call_llm(self, prompt: str) -> str:
        import openai
        result = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Kamu adalah asisten yang membantu berdasarkan konteks sebelumnya."},
                {"role": "user", "content": prompt}
            ]
        )
        return result["choices"][0]["message"]["content"]

    def clear_all(self):
        self.stm.clear()
        self.ltm.clear()
