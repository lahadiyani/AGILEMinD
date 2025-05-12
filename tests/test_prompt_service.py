import pytest
import os
from app.services.prompt_service import PromptService

@pytest.fixture
def prompt_service():
    return PromptService()

def test_get_prompt_researcher(prompt_service):
    # Test getting researcher prompt
    prompt = prompt_service.get_prompt("researcher")
    
    # Assert prompt content
    assert isinstance(prompt, str)
    assert "research assistant" in prompt.lower()
    assert "analyze" in prompt.lower()

def test_get_prompt_coder(prompt_service):
    # Test getting coder prompt
    prompt = prompt_service.get_prompt("coder")
    
    # Assert prompt content
    assert isinstance(prompt, str)
    assert "coding assistant" in prompt.lower()
    assert "write" in prompt.lower()

def test_get_prompt_planner(prompt_service):
    # Test getting planner prompt
    prompt = prompt_service.get_prompt("planner")
    
    # Assert prompt content
    assert isinstance(prompt, str)
    assert "task planner" in prompt.lower()
    assert "organize" in prompt.lower()

def test_get_prompt_invalid_type(prompt_service):
    # Test getting invalid prompt type
    with pytest.raises(ValueError):
        prompt_service.get_prompt("invalid_type")

def test_format_prompt(prompt_service):
    # Test prompt formatting
    base_prompt = "You are a {role}. {task}"
    formatted_prompt = prompt_service.format_prompt(base_prompt, role="researcher", task="Research AI")
    
    # Assert formatted prompt
    assert isinstance(formatted_prompt, str)
    assert "researcher" in formatted_prompt
    assert "Research AI" in formatted_prompt

def test_prompt_file_exists(prompt_service):
    # Test if prompt files exist
    prompt_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', 'prompts')
    
    # Assert prompt files exist
    assert os.path.exists(os.path.join(prompt_dir, 'researcher_prompts.txt'))
    assert os.path.exists(os.path.join(prompt_dir, 'coder_prompts.txt'))
    assert os.path.exists(os.path.join(prompt_dir, 'planner_prompts.txt'))

def test_prompt_file_content(prompt_service):
    # Test prompt file content
    prompt_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', 'prompts')
    
    # Read and check researcher prompt file
    with open(os.path.join(prompt_dir, 'researcher_prompts.txt'), 'r') as f:
        content = f.read()
        assert "research assistant" in content.lower()
        assert "analyze" in content.lower()
    
    # Read and check coder prompt file
    with open(os.path.join(prompt_dir, 'coder_prompts.txt'), 'r') as f:
        content = f.read()
        assert "coding assistant" in content.lower()
        assert "write" in content.lower()
    
    # Read and check planner prompt file
    with open(os.path.join(prompt_dir, 'planner_prompts.txt'), 'r') as f:
        content = f.read()
        assert "task planner" in content.lower()
        assert "organize" in content.lower() 