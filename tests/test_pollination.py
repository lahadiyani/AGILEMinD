import pytest
from unittest.mock import patch, MagicMock
from app.tools.pollination import generate_image, generate_text

def test_generate_image_success():
    # Mock the requests.get function
    with patch('requests.get') as mock_get:
        # Setup mock response
        mock_response = MagicMock()
        mock_response.content = b'fake_image_data'
        mock_response.headers = {'content-type': 'image/jpeg'}
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Test image generation
        result = generate_image("test image prompt")
        
        # Assert result
        assert isinstance(result, bytes)
        assert result == b'fake_image_data'

def test_generate_image_error():
    # Mock the requests.get function to raise an exception
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("API Error")
        
        # Test error handling
        result = generate_image("invalid prompt")
        
        # Assert error message
        assert isinstance(result, str)
        assert result.startswith("Error:")

def test_generate_text_success():
    # Mock the requests.get function
    with patch('requests.get') as mock_get:
        # Setup mock response
        mock_response = MagicMock()
        mock_response.text = "Generated text response"
        mock_response.headers = {'content-type': 'text/plain'}
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Test text generation
        result = generate_text("test text prompt")
        
        # Assert result
        assert isinstance(result, str)
        assert result == "Generated text response"

def test_generate_text_error():
    # Mock the requests.get function to raise an exception
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("API Error")
        
        # Test error handling
        result = generate_text("invalid prompt")
        
        # Assert error message
        assert isinstance(result, str)
        assert result.startswith("Error:")

def test_generate_image_invalid_content_type():
    # Mock the requests.get function with invalid content type
    with patch('requests.get') as mock_get:
        # Setup mock response with invalid content type
        mock_response = MagicMock()
        mock_response.content = b'fake_data'
        mock_response.headers = {'content-type': 'text/plain'}
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Test invalid content type handling
        result = generate_image("test prompt")
        
        # Assert error message
        assert isinstance(result, str)
        assert "Unexpected content type" in result

def test_generate_text_invalid_content_type():
    # Mock the requests.get function with invalid content type
    with patch('requests.get') as mock_get:
        # Setup mock response with invalid content type
        mock_response = MagicMock()
        mock_response.text = "fake data"
        mock_response.headers = {'content-type': 'image/jpeg'}
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Test invalid content type handling
        result = generate_text("test prompt")
        
        # Assert error message
        assert isinstance(result, str)
        assert "Unexpected content type" in result 