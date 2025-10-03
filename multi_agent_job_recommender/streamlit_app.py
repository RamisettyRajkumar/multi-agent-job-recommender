# streamlit_app.py - Multi-Agent Job Recommender (starter)
import streamlit as st
from pathlib import Path
import os
import json

st.set_page_config(page_title='Multi-Agent Job Recommender', layout='wide')

st.title('Multi-Agent Job Recommender & Skill Gap Analyzer (Starter)')
st.markdown('Upload your resume (txt) or paste job description to see a quick demo of summarization and retrieval.')

uploaded = st.file_uploader('Upload resume (.txt preferred)', type=['txt'])
job_text = st.text_area('Paste job description here', height=200)

from ai import rag

def naive_summarize(text):
    import re
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    return ' '.join(sentences[:3]) if sentences else text[:300]

if st.button('Analyze'):
    if job_text.strip() == '' and not uploaded:
        st.error('Please provide a job description or upload a resume.')
    else:
        st.subheader('Job Summary')
        try:
            # Try to use OpenAI via LangChain if available
            from langchain.llms import OpenAI
            from config import OPENAI_API_KEY
            if OPENAI_API_KEY:
                llm = OpenAI(temperature=0)
                summary = llm('Summarize this job description:\n\n' + job_text)
            else:
                summary = naive_summarize(job_text)
        except Exception:
            summary = naive_summarize(job_text)
        st.write(summary)

        st.subheader('Retrieved similar jobs (keyword fallback)')
        results = rag.keyword_search(job_text)
        if results:
            for r in results:
                st.markdown(f"**{r['title']}** — {r['description']}")
        else:
            st.info('No similar jobs found in sample data. Add more jobs to data/jobs_sample.json or run scripts/ingest_jobs.py to build a vector DB.')

st.markdown('---')
st.info('See CHANGE_LOCATIONS.md and RUN_INSTRUCTIONS.md for exact edit locations and bilingual run steps.')
