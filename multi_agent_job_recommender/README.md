# Multi-Agent Job Recommendation & Skill Gap Analyzer

**What it is:** A starter codebase (Streamlit + optional React frontend) that demonstrates uploading resumes, pasting job descriptions, generating quick summaries, and a placeholder RAG pipeline that can be extended to LangChain/FAISS/Chroma for production.

**Highlights (what you'll find in this folder):**
- `streamlit_app.py` — main Streamlit application (UI + simple analysis).
- `ai/rag.py` — simple RAG-like retrieval fallback (keyword search) and placeholders for LangChain integration.
- `data/` — sample job + resume placeholders.
- `config.py` — where API keys (OPENAI_API_KEY) are read from environment variables.
- `frontend_react/` — minimal React skeleton (optional) to demo a richer frontend.
- `scripts/ingest_jobs.py` — helper to ingest jobs into a vector store (placeholder).
- `CHANGE_LOCATIONS.md` — exact places to edit when you change settings or keys.
- `RUN_INSTRUCTIONS.md` — step-by-step run instructions (English + Telugu, line-by-line).

This is a starter pack to impress recruiters — it mixes UI + AI integration points for quick hands-on demos.
