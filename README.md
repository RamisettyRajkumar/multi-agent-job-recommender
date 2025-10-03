# multi-agent-job-recommender
This project is an AI-powered multi-agent system designed to help recruiters and candidates streamline the hiring process. It combines job description analysis, resume parsing, candidate-job matching, and skill gap identification into one interactive application
🚀 Features

Multi-Agent Framework:

Job Summarizer Agent – Extracts key skills & responsibilities from job descriptions.

Resume Parser Agent – Processes uploaded resumes and extracts candidate profiles.

Matching Agent – Compares candidate skills with job requirements using semantic similarity (RAG + vector database).

Skill Gap Analyzer Agent – Identifies missing skills and recommends a personalized learning path.

Scheduler Agent (optional) – Helps plan interviews based on availability.


UI/UX:

Streamlit frontend for quick prototyping.

React-based minimal dashboard for modern UI.


Tech Stack:

Frontend: Streamlit + React

AI/LLM Integration: LangChain, Retrieval-Augmented Generation (RAG)

Database: SQLite + Vector DB (Chroma/FAISS placeholder)

Resume Parsing: Python + NLP libraries

Deployment: Streamlit Cloud-ready

How It Works

1. Upload a job description (JSON or text).


2. Upload a candidate resume (PDF/TXT).


3. Agents run:

Extract job skills.

Parse candidate profile.

Match candidate to job.

Show skill gaps + personalized recommendations.



4. Results displayed in the dashboard.



📖 Example Use Case

Recruiter uploads “Data Analyst Job Description”.

Candidate uploads resume.

System shows:

✅ Skills matched (SQL, Python, Tableau).

⚠ Missing skills (Statistics, Power BI).

📚 Suggested learning path (Kaggle courses, Power BI tutorials).
