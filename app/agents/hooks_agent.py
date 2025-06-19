from typing import Callable, Any

# Optional hooks for extensibility
pre_run_hook: Callable[[Any], Any] = lambda input_data: input_data
post_run_hook: Callable[[Any], Any] = lambda output_data: output_data

def set_pre_run_hook(hook: Callable[[Any], Any]) -> None:
    global pre_run_hook
    pre_run_hook = hook

def set_post_run_hook(hook: Callable[[Any], Any]) -> None:
    global post_run_hook
    post_run_hook = hook
