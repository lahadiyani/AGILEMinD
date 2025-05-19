# Cara Membuat Custom Agent

Custom agent memungkinkan Anda mengatur perilaku agent sesuai kebutuhan aplikasi Anda.

## Langkah-langkah

1. **Buat Kelas Agent Baru**
   Turunkan dari `BaseAgent` yang ada di `app/agents/base_agent.py`.

   ```python
   from app.agents.base_agent import BaseAgent

   class MyCustomAgent(BaseAgent):
       def __init__(self, name, llm, prompt, tools=None, memory=None, description=None, logging_enabled=True):
           super().__init__(
               name=name,
               llm=llm,
               prompt=prompt,
               tools=tools,
               memory=memory,
               description=description,
               logging_enabled=logging_enabled
           )

       def postprocess(self, response):
           # (Opsional) manipulasi hasil dari LLM sebelum dikembalikan
           return response.strip()
   ```

2. **Siapkan LLM, Prompt, dan Tools**
   Buat instance LLM, siapkan prompt, dan (opsional) tools yang ingin digunakan.

   ```python
   from app.llms.openai_llm import OpenAILLM  # Contoh LLM
   llm = OpenAILLM(api_key="YOUR_API_KEY")
   prompt = "Jawab pertanyaan berikut: {input}"
   tools = []  # Daftar tools jika diperlukan
   ```

3. **Instansiasi dan Jalankan Agent**
   Buat agent dan jalankan dengan input.

   ```python
   agent = MyCustomAgent(name="MyAgent", llm=llm, prompt=prompt, tools=tools)
   hasil = agent.run("Apa itu custom agent?")
   print(hasil)
   ```

4. **(Opsional) Daftarkan ke Registry**
   Agar agent bisa digunakan secara dinamis, daftarkan ke registry.

   ```python
   from app.agents.registry import register_agent
   register_agent("MyCustomAgent", MyCustomAgent)
   ```

## Tips

- Pastikan agent Anda mengimplementasikan semua metode yang diperlukan oleh `BaseAgent`.
- Gunakan parameterisasi prompt untuk fleksibilitas.
- Uji agent secara terpisah sebelum integrasi ke chain.
