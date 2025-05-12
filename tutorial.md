# AGILEMinD Framework Tutorial: Building a Journal Searcher AI

## Overview
AGILEMinD is a flexible framework for building AI agents that can handle various tasks through a unified interface. This tutorial will guide you through creating a Journal Searcher AI agent that can search and analyze academic papers.

## Prerequisites
- Python 3.8+
- Flask
- Basic understanding of Python and REST APIs
- Access to academic paper APIs (e.g., arXiv, Semantic Scholar)

## Project Structure
```
app/
├── controllers/
│   └── journal_controller.py
├── services/
│   ├── journal_service.py
│   └── prompt_service.py
├── tools/
│   └── journal_search.py
├── prompts/
│   └── journal_searcher_prompts.txt
└── static/
    └── js/
        └── journal_scripts.js
```

## Step 1: Create the Journal Search Tool
First, create a tool to interact with academic paper APIs.

```python
# app/tools/journal_search.py
import requests
from typing import Dict, List, Optional

class JournalSearchTool:
    def __init__(self):
        self.base_url = "https://api.semanticscholar.org/v1"
        self.headers = {
            "Accept": "application/json"
        }

    def search_papers(self, query: str, limit: int = 5) -> Dict:
        """Search for academic papers using the query."""
        try:
            response = requests.get(
                f"{self.base_url}/paper/search",
                params={"query": query, "limit": limit},
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"Error searching papers: {str(e)}"}

    def get_paper_details(self, paper_id: str) -> Dict:
        """Get detailed information about a specific paper."""
        try:
            response = requests.get(
                f"{self.base_url}/paper/{paper_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"Error getting paper details: {str(e)}"}
```

## Step 2: Create the Prompt Template
Create a prompt template for the Journal Searcher AI.

```text
# app/prompts/journal_searcher_prompts.txt
You are a Journal Searcher AI, specialized in finding and analyzing academic papers. Your task is to:

1. Search for relevant papers based on the user's query
2. Analyze and summarize the key findings
3. Provide insights and connections between papers
4. Suggest related research directions

Format your response as follows:

# Search Results
- List of relevant papers with titles and authors

# Key Findings
- Summary of main findings from the papers

# Analysis
- Critical analysis of the research
- Connections between different papers

# Future Directions
- Suggestions for further research
- Related topics to explore

Please provide comprehensive and well-structured research findings.
```

## Step 3: Create the Journal Service
Create a service to handle the business logic.

```python
# app/services/journal_service.py
from app.tools.journal_search import JournalSearchTool
from app.services.prompt_service import PromptService

class JournalService:
    def __init__(self):
        self.search_tool = JournalSearchTool()
        self.prompt_service = PromptService()

    def search_journals(self, query: str, model: Optional[str] = None) -> Dict:
        """Search and analyze academic papers."""
        try:
            # Get search results
            search_results = self.search_tool.search_papers(query)
            if "error" in search_results:
                return {"status": "error", "error": search_results["error"]}

            # Get base prompt
            base_prompt = self.prompt_service.get_prompt("journal_searcher")
            
            # Format the prompt with search results
            formatted_prompt = f"{base_prompt}\n\nSearch Results:\n{search_results}"
            
            # Generate analysis using Pollinations API
            analysis = generate_text(formatted_prompt, model)
            
            return {
                "status": "success",
                "search_results": search_results,
                "analysis": analysis
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
```

## Step 4: Create the Controller
Create a controller to handle HTTP requests.

```python
# app/controllers/journal_controller.py
from flask import current_app
from app.services.journal_service import JournalService

class JournalController:
    def __init__(self):
        self.journal_service = JournalService()

    def search_journals(self, query: str, model: Optional[str] = None) -> Dict:
        """Handle journal search requests."""
        try:
            result = self.journal_service.search_journals(query, model)
            return result
        except Exception as e:
            current_app.logger.error(f"Error in journal search: {e}")
            return {"status": "error", "error": str(e)}
```

## Step 5: Add Frontend JavaScript
Create the frontend interface for the Journal Searcher.

```javascript
// app/static/js/journal_scripts.js
function searchJournals() {
    const query = document.getElementById('search-input').value;
    const model = document.getElementById('model-select').value;

    if (!query) {
        document.getElementById('search-output').innerHTML = 
            '<p class="text-red-500">❌ Please enter a search query</p>';
        return;
    }

    // Show loading state
    document.getElementById('search-output').innerHTML = 
        '<p class="text-gray-500">⏳ Searching journals...</p>';

    // Prepare request data
    const requestData = {
        query: query,
        model: model
    };

    fetch('/api/journals/search', {
        method: 'POST',
        body: JSON.stringify(requestData),
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'error') {
            document.getElementById('search-output').innerHTML = 
                `<p class="text-red-500">❌ Error: ${data.error}</p>`;
            return;
        }

        // Format and display results
        const formattedResults = formatJournalResults(data);
        document.getElementById('search-output').innerHTML = formattedResults;
    })
    .catch(error => {
        document.getElementById('search-output').innerHTML = 
            `<p class="text-red-500">❌ Error: ${error}</p>`;
    });
}

function formatJournalResults(data) {
    const { search_results, analysis } = data;
    
    return `
        <div class="space-y-6">
            <div class="search-results">
                <h3 class="text-lg font-semibold mb-2">Search Results</h3>
                ${formatSearchResults(search_results)}
            </div>
            
            <div class="analysis">
                <h3 class="text-lg font-semibold mb-2">Analysis</h3>
                <div class="markdown-content">
                    ${formatResponse(analysis)}
                </div>
            </div>
        </div>
    `;
}
```

## Step 6: Add Routes
Add the necessary routes to your Flask application.

```python
# app/routes/journal_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.journal_controller import JournalController

journal_bp = Blueprint('journal', __name__)
journal_controller = JournalController()

@journal_bp.route('/api/journals/search', methods=['POST'])
def search_journals():
    data = request.get_json()
    query = data.get('query')
    model = data.get('model')
    
    if not query:
        return jsonify({"status": "error", "error": "Query is required"}), 400
        
    result = journal_controller.search_journals(query, model)
    return jsonify(result)
```

## Usage Example

1. Start the Flask application:
```bash
flask run
```

2. Access the Journal Searcher interface at `http://localhost:5000`

3. Enter a search query, for example:
```
"machine learning applications in healthcare"
```

4. The Journal Searcher will:
   - Search for relevant papers
   - Analyze the findings
   - Provide a structured summary
   - Suggest related research directions

## Customization Tips

1. **Adding New Features**
   - Extend the `JournalSearchTool` class to support more APIs
   - Add new methods to the `JournalService` for different types of analysis
   - Create new prompt templates for specific use cases

2. **Improving Results**
   - Implement caching for frequently searched papers
   - Add filters for publication date, journal, etc.
   - Include citation analysis and impact metrics

3. **Enhancing the UI**
   - Add visualization for paper relationships
   - Implement paper recommendation system
   - Add export functionality for search results

## Best Practices

1. **Error Handling**
   - Always implement proper error handling in API calls
   - Provide meaningful error messages to users
   - Log errors for debugging

2. **Performance**
   - Cache API responses when possible
   - Implement pagination for large result sets
   - Use async operations for long-running tasks

3. **Security**
   - Validate all user inputs
   - Implement rate limiting for API calls
   - Secure API keys and sensitive data

## Conclusion
The AGILEMinD framework provides a flexible foundation for building AI agents. By following this tutorial, you've created a Journal Searcher AI that can help researchers find and analyze academic papers. You can extend this further by adding more features, improving the analysis, or integrating with additional APIs.
