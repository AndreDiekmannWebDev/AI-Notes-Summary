# 🧠 AI Notes Summarizer

Verdichtet lange Notizen zu prägnanten Kernaussagen. Funktioniert **offline heuristisch** oder mit **OpenAI-API**.

## Quickstart
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## OpenAI (optional)
Setze deinen API-Key als Umgebungsvariable:
```bash
export OPENAI_API_KEY=dein_key   # macOS/Linux
setx OPENAI_API_KEY dein_key     # Windows (neu starten)
```
