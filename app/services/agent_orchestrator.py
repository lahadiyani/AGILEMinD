# app/services/agent_orchestrator.py

from app.llms.registry import get_llm

class AgentOrchestrator:
    def __init__(self, agent_name=None):
        self.agent_name = agent_name

    def run(self, agent_type, prompt):
        """
        Menjalankan agen berdasarkan tipe agent dan prompt.
        """
        # Memilih agen berdasarkan tipe
        if agent_type == "pollinations":
            return self.run_pollinations(prompt)
        elif agent_type == "openai":
            return self.run_openai(prompt)
        else:
            return {"status": "error", "message": "Unsupported agent type"}

    def run_pollinations(self, prompt):
        """
        Menjalankan agen Pollinations.AI untuk menghasilkan teks atau gambar.
        """
        llm = get_llm("pollinations")
        if prompt.startswith("image:"):
            image_prompt = prompt[len("image:"):].strip()  # Ambil prompt untuk gambar
            image_data = llm.generate_image(image_prompt)
            if isinstance(image_data, str) and image_data.startswith("Error:"):
                return {"status": "error", "message": image_data}
            return {"status": "success", "result": image_data}
        else:
            text_data = llm.generate(prompt)
            if isinstance(text_data, str) and text_data.startswith("Error:"):
                return {"status": "error", "message": text_data}
            return {"status": "success", "result": text_data}

    def run_openai(self, prompt):
        """
        Menjalankan agen OpenAI (misalnya GPT-3/4) untuk menghasilkan teks.
        """
        llm = get_llm("openai")
        text_data = llm.generate(prompt)
        return {"status": "success", "result": text_data}

    def list_all_agents(self):
        """
        Menyediakan daftar agen yang tersedia.
        """
        return [{"name": "researcher"}, {"name": "coder"}, {"name": "planner"}, {"name": "pollinations"}]
