import os, re
import streamlit as st
from transformers import pipeline

# ---------- Grundeinstellungen ----------
st.set_page_config(page_title="AI Notes Summarizer (Offline)", layout="centered")
st.title("🧠 AI Notes Summarizer – Offline")
st.write("Zusammenfassen ohne API-Key. Wähle **Offline schnell** für Tempo oder **Offline präzise** für Qualität.")

# ---------- Modelle laden (mit Cache) ----------
@st.cache_resource
def load_summarizer(model_name: str):
    # Lädt das Modell nur einmal (schneller bei erneutem Start)
    return pipeline("summarization", model=model_name)

MODEL_FAST = "sshleifer/distilbart-cnn-12-6"   # kompakter & schneller
MODEL_PRECISE = "facebook/bart-large-cnn"      # größer & genauer (langsamer)

mode_model = st.selectbox(
    "Modell",
    ["Offline schnell (empfohlen)", "Offline präzise"],
    index=0,
    help="Schnell = kompakteres Modell • Präzise = größer, hochwertiger, langsamer"
)
model_name = MODEL_FAST if mode_model.startswith("Offline schnell") else MODEL_PRECISE
summarizer_offline = load_summarizer(model_name)

# ---------- Eingaben ----------
text = st.text_area("Text einfügen", height=260, placeholder="Füge hier einen längeren Text ein …")
col1, col2 = st.columns(2)
with col1:
    max_len = st.slider("Maximale Länge (Tokens, grob)", 80, 200, 130, 10)
with col2:
    min_len = st.slider("Minimale Länge (Tokens, grob)", 20, 80, 40, 5)

# ---------- Heuristik (Fallback) ----------
def heuristic_summary(txt, max_sentences=5):
    sents = re.split(r'(?<=[.!?]) +', txt.strip())
    sents = [s for s in sents if s.strip()]
    scored = sorted(sents, key=len, reverse=True)
    return " ".join(scored[:max_sentences]) if scored else ""

# ---------- Utility: lange Texte stückeln ----------
def chunk_text(txt, max_chars=2000):
    chunks, buf, count = [], [], 0
    for sent in re.split(r'(?<=[.!?]) +', txt):
        if count + len(sent) > max_chars and buf:
            chunks.append(" ".join(buf))
            buf, count = [], 0
        buf.append(sent); count += len(sent)
    if buf: chunks.append(" ".join(buf))
    return chunks

# ---------- Offline-KI-Zusammenfassung ----------
def offline_summary(txt, max_len=130, min_len=40):
    chunks = chunk_text(txt)
    outs = []
    for ch in chunks:
        out = summarizer_offline(ch, max_length=max_len, min_length=min_len, do_sample=False)
        outs.append(out[0]["summary_text"])
    joined = " ".join(outs)
    # Bei mehreren Teilzusammenfassungen optional final verdichten
    if len(chunks) > 1 and len(joined) > 500:
        out2 = summarizer_offline(joined, max_length=max_len, min_length=min_len, do_sample=False)
        return out2[0]["summary_text"]
    return joined

# ---------- Button-Block ----------
if st.button("Zusammenfassen"):
    if not text.strip():
        st.warning("Bitte Text einfügen.")
    else:
        with st.spinner(f"Erzeuge Zusammenfassung mit {mode_model}..."):
            out = offline_summary(text, max_len, min_len)

        st.markdown(f"### Ergebnis ({mode_model})")
        # Optional: Bulletpoints, wenn die Zusammenfassung lang genug ist
        bullets = [b.strip().rstrip(".") for b in re.split(r"[.•]\s+|[\n\r]+", out) if b.strip()]
        if len(bullets) > 1 and len(out) > 120:
            for b in bullets:
                st.write(f"- {b}.")
        else:
            st.write(out)

st.caption("Hinweis: Beim ersten Start lädt das Modell. Kleinere Blöcke = schneller. "
           "'Offline schnell' ist kompakter, 'Offline präzise' hochwertiger.")


