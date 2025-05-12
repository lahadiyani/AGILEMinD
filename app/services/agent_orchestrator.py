from app.tools.pollination import generate_text, generate_image

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
        if prompt.startswith("image:"):
            image_prompt = prompt[len("image:"):].strip()  # Ambil prompt untuk gambar
            image_data = generate_image(image_prompt)
            if isinstance(image_data, str) and image_data.startswith("Error:"):
                return {"status": "error", "message": image_data}
            return {"status": "success", "result": image_data}
        else:
            text_data = generate_text(prompt)  # Ambil hasil teks dari Pollinations
            if isinstance(text_data, str) and text_data.startswith("Error:"):
                return {"status": "error", "message": text_data}
            return {"status": "success", "result": text_data}

    def run_openai(self, prompt):
        """
        Menjalankan agen OpenAI (misalnya GPT-3/4) untuk menghasilkan teks.
        """
        pass  # Implementasi untuk agen OpenAI

    def list_all_agents(self):
        """
        Menyediakan daftar agen yang tersedia.
        """
        return [{"name": "researcher"}, {"name": "coder"}, {"name": "planner"}, {"name": "pollinations"}]
