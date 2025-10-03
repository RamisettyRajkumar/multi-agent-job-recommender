# Where to change things (exact file + line hints)

1. API Keys
   - File: `config.py` (set OPENAI_API_KEY here or export as environment variable `OPENAI_API_KEY`)
2. RAG / Retrieval
   - File: `ai/rag.py` - replace `keyword_search` and `load_docs` with your LangChain + vector DB ingestion and retrieval code.
3. Sample data
   - File: `data/jobs_sample.json` - add your job postings or change text used for matching.
4. UI text and layout
   - File: `streamlit_app.py` - change headings, prompts, or add new Streamlit components.
5. Frontend (optional)
   - Folder: `frontend_react/src/App.js` - edit React UI text. Run `npm install` then `npm start` inside `frontend_react`.
6. Ingestion script
   - File: `scripts/ingest_jobs.py` - put your ingestion pipeline here to build vector indexes.
