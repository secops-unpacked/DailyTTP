# Daily Threat Report Tool

Collects cyber threat intel, enriches with MITRE tags, generates PDF, and emails to analysts.

Use `cli.py` to run with different providers.

**Quick start**
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp config.example.toml config.toml

**Run it any way you like:**
# Fast & offline
python cli.py run -c config.toml --provider none --dry-run

# OpenAI
export OPENAI_API_KEY=...
python cli.py run -c config.toml --provider openai --model gpt-4o-mini

# Anthropic
export ANTHROPIC_API_KEY=...
python cli.py run -c config.toml --provider anthropic --model claude-3-haiku-20240307

# Local Ollama
# (ollama serve; ollama pull llama3.1)
python cli.py run -c config.toml --provider ollama --model llama3.1

Nice touches baked in:
	•	Pretty terminal output via rich
	•	Subcommands: fetch to preview items, test-llm to validate your provider
	•	LLM enrichment merges with heuristics rather than replacing them
	•	Backward-compatible python main.py ... still works
