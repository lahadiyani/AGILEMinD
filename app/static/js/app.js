// ============================
// Setup marked.js & Highlight.js
// ============================
marked.setOptions({
    breaks: true,
    gfm: true,
    headerIds: true,
    mangle: false,
    sanitize: true,
    smartLists: true,
    smartypants: true,
    highlight(code, lang) {
        if (lang && hljs.getLanguage(lang)) {
            try {
                return hljs.highlight(code, { language: lang }).value;
            } catch (err) {
                console.warn('Highlight.js error:', err);
            }
        }
        return code;
    }
});

// ============================
// Utility Functions
// ============================

function formatResponse(text) {
    if (!text || typeof text !== 'string') {
        return "<p class='text-gray-500'>⚠️ Invalid or empty response.</p>";
    }
    return marked.parse(text);
}

function setInnerHTML(id, html) {
    const el = document.getElementById(id);
    if (el) {
        el.innerHTML = html;
        setTimeout(() => {
            el.querySelectorAll('pre code').forEach(block => {
                hljs.highlightElement(block);
            });
        }, 0);
    }
}

function setTextContent(id, text) {
    const el = document.getElementById(id);
    if (el) el.textContent = text;
}

function showOutputTab(tab) {
    const sections = {
        preview: 'agent-output',
        raw: 'agent-output-raw',
        logs: 'agent-output-logs'
    };

    Object.entries(sections).forEach(([key, id]) => {
        document.getElementById(id).classList.toggle('hidden', key !== tab);
        document.querySelector(`.button-${key}`).classList.toggle('border-blue-500', key === tab);
        document.querySelector(`.button-${key}`).classList.toggle('bg-blue-50', key === tab);
    });
}

function updateModelControls() {
    const agent = document.getElementById('agent-select').value;
    const controls = document.getElementById('model-controls');
    controls.classList.toggle('hidden', agent !== 'imagegen');
    if (agent !== 'imagegen') {
        document.getElementById('model-select').value = '';
    }
}

// ============================
// Main Agent Runner
// ============================

function runAgent() {
    const agent = document.getElementById('agent-select').value;
    const prompt = document.getElementById('prompt-input').value.trim();
    const model = document.getElementById('model-select').value;

    if (!prompt) {
        const errorMsg = '❌ Error: Please enter a prompt';
        setInnerHTML('agent-output', `<p class="text-red-500">${errorMsg}</p>`);
        setTextContent('json-output', errorMsg);
        setTextContent('logs-output', errorMsg);
        showOutputTab('preview');
        return;
    }

    const loading = '⏳ Processing...';
    setInnerHTML('agent-output', `<p class="text-gray-500">${loading}</p>`);
    setTextContent('json-output', loading);
    setTextContent('logs-output', loading);
    showOutputTab('preview');

    const requestData = { agent_type: agent, prompt };
    if (agent === 'imagegen') requestData.model = model;

    fetch('/agents/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(requestData),
    })
    .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
    })
    .then(data => {
        const rawJson = JSON.stringify(data, null, 2);
        const logs = data.logs || data.log || 'ℹ️ No logs.';

        let previewHtml = '⚠️ No result.';

        const agentResult = data.result?.result;
        const isImageGen = agent === 'imagegen' || data.result?.agent_name?.toLowerCase().includes('imagegen');

        if (isImageGen && agentResult?.image_path) {
            previewHtml = `
                <p><strong>Deskripsi:</strong> ${agentResult.image_description}</p>
                <p><strong>Model:</strong> ${agentResult.model}</p>
                <img src="${agentResult.image_path}" alt="Generated Image" class="mt-4 border rounded shadow max-w-full h-auto" />
            `;
        } else if (typeof agentResult === 'string') {
            previewHtml = formatResponse(agentResult);
        } else if (typeof data.result === 'string') {
            previewHtml = formatResponse(data.result);
        } else if (typeof data.output === 'string') {
            previewHtml = formatResponse(data.output);
        }

        setInnerHTML('agent-output', previewHtml);
        setTextContent('json-output', rawJson);
        setTextContent('logs-output', logs);
        showOutputTab('preview');
    })
    .catch(err => {
        const errorMsg = `❌ Error: ${err.message}`;
        setInnerHTML('agent-output', `<p class="text-red-500">${errorMsg}</p>`);
        setTextContent('json-output', errorMsg);
        setTextContent('logs-output', errorMsg);
        showOutputTab('preview');
    });
}

// ============================
// Event Binding
// ============================

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('agent-select').addEventListener('change', updateModelControls);
    document.querySelector('.button-preview').addEventListener('click', () => showOutputTab('preview'));
    document.querySelector('.button-raw').addEventListener('click', () => showOutputTab('raw'));
    document.querySelector('.button-logs').addEventListener('click', () => showOutputTab('logs'));
});
