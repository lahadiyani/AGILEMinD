// ============================
// Setup marked.js & Highlight.js
// ============================
marked.setOptions({
    breaks: true,
    gfm: true,
    headerIds: true,
    mangle: false,
    sanitize: false,
    smartLists: true,
    smartypants: true,
    xhtml: false,
    highlight(code, lang) {
        if (lang && hljs.getLanguage(lang)) {
            try {
                return hljs.highlight(code, { language: lang }).value;
            } catch (err) {
                console.error('Highlight error:', err);
            }
        }
        return code;
    }
});

// ============================
// Utils
// ============================

function formatResponse(text) {
    return marked.parse(text || "");
}

function clearPrompt() {
    document.getElementById('prompt-input').value = '';
}

function setInnerHTML(id, html) {
    document.getElementById(id).innerHTML = html;
}

function setTextContent(id, text) {
    document.getElementById(id).textContent = text;
}

// ============================
// UI Output Tabs Handler
// ============================

function showOutputTab(tab) {
    const sections = {
        preview: 'agent-output',
        raw: 'agent-output-raw',
        logs: 'agent-output-logs'
    };

    Object.values(sections).forEach(id => document.getElementById(id).classList.add('hidden'));
    document.getElementById(sections[tab]).classList.remove('hidden');

    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('border-blue-500', 'bg-blue-50'));
    document.querySelector(`.button-${tab}`).classList.add('border-blue-500', 'bg-blue-50');
}

// ============================
// Model Controls Toggle
// ============================

function updateModelControls() {
    const agent = document.getElementById('agent-select').value;
    const controls = document.getElementById('model-controls');
    const modelSelect = document.getElementById('model-select');

    if (agent === 'imagegen') {
        controls.classList.remove('hidden');
    } else {
        controls.classList.add('hidden');
        modelSelect.value = '';
    }
}

// ============================
// Main Agent Handler
// ============================

function runAgent() {
    const agent = document.getElementById('agent-select').value;
    const prompt = document.getElementById('prompt-input').value;
    const model = document.getElementById('model-select').value;

    if (!prompt) {
        const errorMsg = '❌ Error: Please enter a prompt';
        setInnerHTML('agent-output', `<p class="text-red-500">${errorMsg}</p>`);
        setTextContent('json-output', errorMsg);
        setTextContent('logs-output', errorMsg);
        showOutputTab('preview');
        return;
    }

    // Initial loading
    const loadingMsg = '⏳ Processing...';
    setInnerHTML('agent-output', `<p class="text-gray-500">${loadingMsg}</p>`);
    setTextContent('json-output', loadingMsg);
    setTextContent('logs-output', loadingMsg);
    showOutputTab('preview');

    // Build request
    const requestData = {
        agent_type: agent,
        prompt
    };
    if (agent === 'imagegen') {
        requestData.model = model;
    }

    fetch('/agents/run', {
        method: 'POST',
        body: JSON.stringify(requestData),
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => {
        if (!response.ok) throw new Error(`Status: ${response.status}`);
        return response.json();
    })
    .then(data => {
        setTextContent('json-output', JSON.stringify(data, null, 2));
        setTextContent('logs-output', data.logs || data.log || 'No logs available.');

        if (data.error || data.status === 'error') {
            setInnerHTML('agent-output', `<p class="text-red-500">❌ Error: ${data.error}</p>`);
            showOutputTab('preview');
            return;
        }

        // If image response
        if (data.result?.image_path) {
            const imgHTML = `
                <div class="text-center">
                    <img src="${data.result.image_path}" alt="Generated Image" class="max-w-full rounded-lg shadow-lg"
                        onerror="this.onerror=null; this.src=''; this.alt='Failed to load image'; this.parentElement.innerHTML += '<p class=\'text-red-500 mt-2\'>❌ Failed to load image</p>';" />
                    <p class="mt-2 text-sm text-gray-600">Generated image for prompt: "${prompt}"</p>
                    ${(agent === 'imagegen') ? `<p class="text-sm text-gray-500">Using model: ${model || 'Default Model'}</p>` : ''}
                </div>`;
            setInnerHTML('agent-output', imgHTML);
            clearPrompt();
            showOutputTab('preview');
            return;
        }

        // If text response
        const formatted = formatResponse(data.result || data.response || '');
        const responseHTML = `
            <div class="space-y-4">
                <div class="text-sm text-gray-600">Agent: ${data.agent_name || data.agent_type || agent}</div>
                <div class="text-sm text-gray-600">Prompt: "${prompt}"</div>
                ${(agent === 'imagegen') ? `<div class="text-sm text-gray-600">Model: ${model || 'Default Model'}</div>` : ''}
                <div class="mt-4 markdown-content">${formatted}</div>
            </div>`;
        setInnerHTML('agent-output', responseHTML);

        // Re-highlight all code blocks
        document.querySelectorAll('.markdown-content pre code').forEach(block => hljs.highlightBlock(block));

        clearPrompt();
        showOutputTab('preview');
    })
    .catch(error => {
        const errMsg = `❌ Error: ${error}`;
        setInnerHTML('agent-output', `<p class="text-red-500">${errMsg}</p>`);
        setTextContent('json-output', errMsg);
        setTextContent('logs-output', errMsg);
        showOutputTab('preview');
    });
}

// ============================
// DOM Ready Event
// ============================

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.button-preview').addEventListener('click', () => showOutputTab('preview'));
    document.querySelector('.button-raw').addEventListener('click', () => showOutputTab('raw'));
    document.querySelector('.button-logs').addEventListener('click', () => showOutputTab('logs'));

    showOutputTab('preview');

    const agentSelect = document.getElementById('agent-select');
    agentSelect.addEventListener('change', updateModelControls);
    updateModelControls();
});
