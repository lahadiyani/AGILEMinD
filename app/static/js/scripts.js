// Configure marked.js options
marked.setOptions({
    breaks: true,  // Convert line breaks to <br>
    gfm: true,     // GitHub Flavored Markdown
    headerIds: true,
    mangle: false,
    sanitize: false,
    smartLists: true,
    smartypants: true,
    xhtml: false
});

// Add syntax highlighting to code blocks
marked.setOptions({
    highlight: function(code, lang) {
        if (lang && hljs.getLanguage(lang)) {
            try {
                return hljs.highlight(code, { language: lang }).value;
            } catch (err) {}
        }
        return code;
    }
});

// Cache for available models
let availableModels = {
    image: [],
    text: []
};

// Load available models when the page loads
document.addEventListener('DOMContentLoaded', function() {
    loadAvailableModels();
    
    // Add event listener for agent selection change
    document.getElementById('agent-select').addEventListener('change', function() {
        updateModelControls();
    });
});

function loadAvailableModels() {
    // Load image models
    fetch('/api/agents/models/image')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                availableModels.image = data.models;
            }
        })
        .catch(error => console.error('Error loading image models:', error));

    // Load text models
    fetch('/api/agents/models/text')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                availableModels.text = data.models;
            }
        })
        .catch(error => console.error('Error loading text models:', error));
}

function updateModelControls() {
    const agentSelect = document.getElementById('agent-select');
    const modelControls = document.getElementById('model-controls');
    const modelSelect = document.getElementById('model-select');
    
    // Clear existing options
    modelSelect.innerHTML = '<option value="">Default Model</option>';
    
    // Show/hide model controls based on agent type
    if (agentSelect.value === 'pollinations') {
        modelControls.classList.remove('hidden');
        
        // Add image models
        availableModels.image.forEach(model => {
            const option = document.createElement('option');
            option.value = model;
            option.textContent = model;
            modelSelect.appendChild(option);
        });
    } else {
        modelControls.classList.add('hidden');
    }
}

function clearPrompt() {
    document.getElementById('prompt-input').value = '';
}

function runAgent() {
    const agent = document.getElementById('agent-select').value;
    const prompt = document.getElementById('prompt-input').value;
    const model = document.getElementById('model-select').value;

    if (!prompt) {
        document.getElementById('agent-output').innerHTML = '<p class="text-red-500">❌ Error: Please enter a prompt</p>';
        return;
    }

    // Show loading state
    document.getElementById('agent-output').innerHTML = '<p class="text-gray-500">⏳ Processing...</p>';

    // Prepare request data
    const requestData = {
        prompt: prompt,
        agent_type: agent
    };

    // Add model if selected
    if (model) {
        requestData.model = model;
    }

    fetch(`/api/agents/${agent}`, {
        method: 'POST',
        body: JSON.stringify(requestData),
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => {
        if (!response.ok) throw new Error(`Status: ${response.status}`);
        return response.json();
    })
    .then(data => {
        if (data.error) {
            document.getElementById("agent-output").innerHTML = `<p class="text-red-500">❌ Error: ${data.error}</p>`;
            return;
        }

        if (agent === "pollinations" && prompt.startsWith("buatkan saya gambar")) {
            // Handle image response
            const imagePath = data.image_path;
            document.getElementById("agent-output").innerHTML = `
                <div class="text-center">
                    <img src="${imagePath}" alt="Generated Image" class="max-w-full rounded-lg shadow-lg" 
                         onerror="this.onerror=null; this.src=''; this.alt='Failed to load image'; this.parentElement.innerHTML += '<p class=\'text-red-500 mt-2\'>❌ Failed to load image</p>';" />
                    <p class="mt-2 text-sm text-gray-600">Generated image for prompt: "${prompt}"</p>
                    ${model ? `<p class="text-sm text-gray-500">Using model: ${model}</p>` : ''}
                </div>`;
        } else {
            // Handle text response with markdown rendering
            const formattedResponse = formatResponse(data.response);
            document.getElementById("agent-output").innerHTML = `
                <div class="space-y-4">
                    <div class="text-sm text-gray-600">Agent: ${data.agent_type || agent}</div>
                    <div class="text-sm text-gray-600">Prompt: "${prompt}"</div>
                    ${model ? `<div class="text-sm text-gray-600">Model: ${model}</div>` : ''}
                    <div class="mt-4 markdown-content">${formattedResponse}</div>
                </div>`;
            
            // Apply syntax highlighting to any code blocks
            document.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightBlock(block);
            });
        }

        // Clear the prompt input after successful response
        clearPrompt();
    })
    .catch(error => {
        document.getElementById('agent-output').innerHTML = `<p class="text-red-500">❌ Error: ${error}</p>`;
    });
}

function formatResponse(text) {
    try {
        // Try to render as markdown first
        return marked.parse(text);
    } catch (error) {
        console.warn('Markdown parsing failed, falling back to HTML:', error);
        // Fallback to basic HTML formatting if markdown parsing fails
        return text
            .split('\n')
            .map(line => {
                // Basic formatting for common patterns
                if (line.startsWith('# ')) {
                    return `<h1 class="text-2xl font-bold mt-6 mb-4">${line.substring(2)}</h1>`;
                }
                if (line.startsWith('## ')) {
                    return `<h2 class="text-xl font-bold mt-5 mb-3">${line.substring(3)}</h2>`;
                }
                if (line.startsWith('### ')) {
                    return `<h3 class="text-lg font-bold mt-4 mb-2">${line.substring(4)}</h3>`;
                }
                if (line.startsWith('- ')) {
                    return `<li class="ml-4">${line.substring(2)}</li>`;
                }
                if (line.startsWith('1. ')) {
                    return `<li class="ml-4">${line.substring(3)}</li>`;
                }
                if (line.trim() === '') {
                    return '<br>';
                }
                return `<p class="my-2">${line}</p>`;
            })
            .join('');
    }
}
