# Cara Membuat Custom Chain

Custom chain digunakan untuk mengatur alur proses data atau prompt secara fleksibel dengan menggabungkan beberapa agent.

## Langkah-langkah

1. **Buat Kelas Chain Baru**
   Turunkan dari `BaseChain` yang ada di `app/chains/base_chain.py`.

   ```python
   from app.chains.base_chain import BaseChain

   class MyCustomChain(BaseChain):
       def __init__(self, agents, context=None, logging_enabled=True):
           super().__init__(agents=agents, context=context, logging_enabled=logging_enabled)

       def preprocess_input(self, input_data):
           # (Opsional) manipulasi input sebelum diproses agent pertama
           return input_data

       def postprocess_output(self, output_data):
           # (Opsional) manipulasi output setelah semua agent selesai
           return output_data
   ```

2. **Siapkan Daftar Agent**
   Buat dan siapkan agent yang ingin digunakan dalam chain.

   ```python
   from app.agents.custom.coder_agent import CoderAgent
   from app.agents.custom.planner_agent import PlannerAgent

   coder = CoderAgent(name="Coder", ...)
   planner = PlannerAgent(name="Planner", ...)
   agents = [planner, coder]
   ```

3. **Gunakan Chain di Aplikasi**
   Integrasikan chain ke dalam workflow aplikasi Anda.

   ```python
   my_chain = MyCustomChain(agents=agents)
   hasil = my_chain.run("Input untuk chain")
   print(hasil)
   ```

## Tips

- Gunakan parameterisasi pada agent dan context untuk fleksibilitas.
- Chain dapat dikombinasikan dengan chain lain untuk workflow kompleks.
- Override `preprocess_input` dan `postprocess_output` jika perlu manipulasi data sebelum/akhir.
