from app.llms.registry_llm import get_llm

class BuilderLLM:
    @staticmethod
    def build_llm(config: dict):
        """
        Build and return an LLM instance from config dictionary.

        Args:
            config (dict): Configuration with keys 'llm_name' and optional 'params'.

        Returns:
            BaseLLM: An instance of the specified LLM.
        """
        if "llm_name" not in config:
            raise ValueError("Missing 'llm_name' in LLM config")
        llm_name = config["llm_name"]
        params = config.get("params", {})
        return get_llm(llm_name, **params)  