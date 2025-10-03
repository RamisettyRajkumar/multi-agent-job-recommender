# Simple retrieval (fallback) for demonstration.
import json
from pathlib import Path

def load_docs(path='data/jobs_sample.json'):
    p = Path(path)
    if not p.exists():
        return []
    data = json.loads(p.read_text(encoding='utf-8'))
    return data.get('jobs', [])

def keyword_search(query, docs=None, top_k=3):
    """A very simple keyword search for demo. Replace with LangChain + vector DB in production."""
    if docs is None:
        docs = load_docs()
    q = query.lower().split()
    scored = []
    for d in docs:
        text = (d.get('title','') + ' ' + d.get('description','')).lower()
        score = sum(1 for token in q if token in text)
        scored.append((score, d))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for s,d in scored if s>0][:top_k]
