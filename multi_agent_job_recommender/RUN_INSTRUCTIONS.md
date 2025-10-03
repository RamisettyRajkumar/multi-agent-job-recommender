# Run instructions - Multi-Agent Job Recommender
(Each step is written in English followed by Telugu on the next line)

1) Prepare Python environment
   - English: Open a terminal. Create and activate a virtualenv:
     ```bash
     python3 -m venv venv
     source venv/bin/activate   # macOS/Linux
     venv\Scripts\activate    # Windows (PowerShell)
     ```
   - Telugu: టెర్మినల్ ఓపెన్ చేయండి. virtualenv సృష్టించి యాక్టివేట్ చేయండి:
     ```bash
     python3 -m venv venv
     source venv/bin/activate   # macOS/Linux
     venv\Scripts\activate    # Windows (PowerShell)
     ```

2) Install dependencies
   - English:
     ```bash
     pip install -r requirements.txt
     pip install streamlit
     ```
   - Telugu:
     ```bash
     పైప్ ఇన్స్టాల్ చేయండి: pip install -r requirements.txt
     మరియు streamlit కూడా: pip install streamlit
     ```

3) Set OpenAI API key (optional, only if you will use OpenAI)
   - English: Set your API key as environment variable:
     ```bash
     export OPENAI_API_KEY="your_openai_key"   # macOS/Linux
     setx OPENAI_API_KEY "your_openai_key"     # Windows (PowerShell)
     ```
   - Telugu: OpenAI కీ అవసరమైతే ఇలా సెట్చేయండి:
     ```bash
     export OPENAI_API_KEY="your_openai_key"   # macOS/Linux
     setx OPENAI_API_KEY "your_openai_key"     # Windows (PowerShell)
     ```

4) Run the Streamlit app
   - English:
     ```bash
     streamlit run streamlit_app.py
     ```
   - Telugu:
     ```bash
     streamlit run streamlit_app.py
     ```

5) Edit points (where to change code)
   - English: Edit `config.py` for keys, `ai/rag.py` to switch to vector DB, `data/jobs_sample.json` to add jobs.
   - Telugu: కీస్ కోసం `config.py` మార్చండి, vector DB కోసం `ai/rag.py` మార్చండి, జాబ్స్ కోసం `data/jobs_sample.json` మార్చండి.
