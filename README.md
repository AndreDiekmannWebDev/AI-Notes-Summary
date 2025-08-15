# 🧠 AI Notes Summarizer (Offline)

![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![Mode](https://img.shields.io/badge/Modi-Schnell_/_Präzise-blue)

Ein kostenloser, **offline** laufender Text-Summarizer mit **Streamlit** + **HuggingFace Transformers**.  
Läuft komplett lokal – keine API-Keys nötig, keine Kosten.

---

## 🚀 Features
- **2 Modi**:
  - **Offline schnell** → kompakteres Modell, schnellere Ergebnisse
  - **Offline präzise** → größeres Modell, bessere Qualität
- **Chunking** → Lange Texte werden in kleinere Abschnitte geteilt, separat zusammengefasst und am Ende verdichtet.
- **Cache** → Modelle werden nur einmal geladen, für schnelle Wiederholungen.

---

## 📸 Screenshot
*(Optional – hier später Screenshot/GIF einfügen)*

---

## 🛠 Installation & Start

```bash
# 1. Virtuelle Umgebung erstellen
python -m venv .venv
# Windows:
.venv\Scripts\activate

# 2. Abhängigkeiten installieren
pip install -r requirements.txt

# 3. App starten
streamlit run app.py

.
├── app.py               # Haupt-App
├── requirements.txt     # Python-Abhängigkeiten
├── README.md            # Projektdokumentation
└── .gitignore           # Ignorierte Dateien

Verwendete Technologien

Streamlit – Web-App Framework für Python

Transformers – NLP-Modelle

PyTorch – Deep Learning Framework

Idee

Erstellt, um lokale Textzusammenfassungen ohne externe API-Kosten zu ermöglichen.
Perfekt für schnelle Notizen, Meeting-Transkripte oder Dokumentenauswertungen.
