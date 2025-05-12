import pytest
import os
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

# Create test directories if they don't exist
@pytest.fixture(autouse=True)
def setup_test_directories():
    # Create test directories
    test_dirs = [
        os.path.join(project_root, 'app', 'static', 'assets'),
        os.path.join(project_root, 'tests', 'fixtures')
    ]
    
    for directory in test_dirs:
        os.makedirs(directory, exist_ok=True)
    
    yield
    
    # Cleanup after tests
    for directory in test_dirs:
        if os.path.exists(directory):
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)

# Mock environment variables
@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    monkeypatch.setenv('FLASK_APP', 'app')
    monkeypatch.setenv('FLASK_ENV', 'testing')
    monkeypatch.setenv('OPENAI_API_KEY', 'test_api_key')
    monkeypatch.setenv('POLLINATIONS_API_KEY', 'test_api_key') 