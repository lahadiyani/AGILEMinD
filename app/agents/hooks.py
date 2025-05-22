from typing import Callable

# Optional hooks for extensibility
pre_run_hook: Callable[[str], str] = lambda input_text: input_text
post_run_hook: Callable[[str], str] = lambda output_text: output_text
