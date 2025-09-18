# 🛡️ Daily Threat Report Tool

This tool automates your daily threat intel workflow:

- Collects cyber threat feeds (RSS/Atom)
- Filters for relevant intel (malware, CVEs, APTs, leaks)
- Enriches with MITRE ATT&CK tactics & techniques (heuristic + optional LLM)
- Generates a professional PDF digest
- Emails the report to your analysts

---

## 🚀 Quick Start

```bash
# Set up environment
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Copy and edit configuration
cp config.example.toml config.toml
```

---

## ⚡ Run it any way you like

### Fast & Offline
```bash
python cli.py run -c config.toml --provider none --dry-run
```

### With OpenAI
```bash
export OPENAI_API_KEY=...
python cli.py run -c config.toml --provider openai --model gpt-4o-mini
```

### With Anthropic
```bash
export ANTHROPIC_API_KEY=...
python cli.py run -c config.toml --provider anthropic --model claude-3-haiku-20240307
```

### With Local Ollama
```bash
# Make sure Ollama is running and model is pulled
ollama serve
ollama pull llama3.1

python cli.py run -c config.toml --provider ollama --model llama3.1
```

---

## 🧰 Useful Commands

- **Fetch feeds only (preview items):**
  ```bash
  python cli.py fetch -c config.toml
  ```

- **Test your LLM provider setup:**
  ```bash
  python cli.py test-llm --provider openai --title "CVE-2025-12345 in FooBar" --summary "Remote code execution vulnerability"
  ```

---

## ✨ Features

- Rich terminal output (`rich`)
- Modular CLI with `typer`
- LLM enrichment **merges** with heuristics (never overwrites)
- Backward-compatible `python main.py ...` still works
- Pluggable GenAI backends:
  - OpenAI
  - Anthropic
  - Local Ollama

---

## ⏰ Scheduling

Run it daily with cron (example: 07:30 each morning):

```
30 7 * * * /usr/bin/bash -lc 'cd /path/to/daily-threat-report && source .venv/bin/activate && python cli.py run -c config.toml --provider none >> run.log 2>&1'
```

---

## 📌 Notes

- Expand `mitre_map.yaml` to improve ATT&CK tagging
- Add your own feeds in `config.toml`
- Keep secrets (API keys, SMTP creds) in environment variables or a secrets manager
- For production use, consider deduplication and CVE scoring (EPSS, KEV) before PDF generation
