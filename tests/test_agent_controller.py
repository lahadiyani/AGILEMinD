import pytest
from unittest.mock import patch, MagicMock
from app.controllers.agent_controller import AgentController
from app.services.prompt_service import PromptService
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def agent_controller(app):
    with app.app_context():
        return AgentController()

@pytest.fixture
def mock_prompt_service():
    return MagicMock(spec=PromptService)

def test_pollinations_image_success(agent_controller):
    # Mock the generate_image function
    with patch('app.tools.pollination.generate_image') as mock_generate:
        # Setup mock response
        mock_generate.return_value = b'fake_image_data'
        
        # Test image generation
        response = agent_controller.pollinations_image("buatkan saya gambar kucing")
        
        # Assert response structure
        assert response['status'] == 'success'
        assert 'image_path' in response

def test_pollinations_image_error(agent_controller):
    # Mock the generate_image function to return an error
    with patch('app.tools.pollination.generate_image') as mock_generate:
        mock_generate.return_value = "Error: Failed to generate image"
        
        # Test error handling
        response = agent_controller.pollinations_image("invalid prompt")
        
        # Assert error response
        assert response['status'] == 'error'
        assert 'error' in response

def test_process_agent_request_researcher(agent_controller, mock_prompt_service):
    # Mock the generate_text function
    with patch('app.tools.pollination.generate_text') as mock_generate:
        # Setup mock response
        mock_generate.return_value = "Research findings..."
        
        # Test researcher agent
        response = agent_controller.process_agent_request("researcher", "Research AI trends")
        
        # Assert response structure
        assert response['status'] == 'success'
        assert 'response' in response
        assert 'agent_type' in response
        assert response['agent_type'] == 'researcher'

def test_process_agent_request_coder(agent_controller, mock_prompt_service):
    # Mock the generate_text function
    with patch('app.tools.pollination.generate_text') as mock_generate:
        # Setup mock response
        mock_generate.return_value = "def example_function(): pass"
        
        # Test coder agent
        response = agent_controller.process_agent_request("coder", "Create a Python function")
        
        # Assert response structure
        assert response['status'] == 'success'
        assert 'response' in response
        assert 'agent_type' in response
        assert response['agent_type'] == 'coder'

def test_process_agent_request_planner(agent_controller, mock_prompt_service):
    # Mock the generate_text function
    with patch('app.tools.pollination.generate_text') as mock_generate:
        # Setup mock response
        mock_generate.return_value = "Project timeline..."
        
        # Test planner agent
        response = agent_controller.process_agent_request("planner", "Plan a project")
        
        # Assert response structure
        assert response['status'] == 'success'
        assert 'response' in response
        assert 'agent_type' in response
        assert response['agent_type'] == 'planner'

def test_process_agent_request_invalid_type(agent_controller):
    # Test invalid agent type
    response = agent_controller.process_agent_request("invalid_type", "Some prompt")
    
    # Assert error response
    assert response['status'] == 'error'
    assert 'error' in response
    assert 'Unsupported agent type' in response['error'] 