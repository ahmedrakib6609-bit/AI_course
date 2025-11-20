## 🌟 AI Agent Project

- A clean, modular, production-ready AI Agent System powered by Google Gemini, LangChain, and custom-built research tools.
This agent can search the web, fetch Wikipedia data, save outputs, and provide intelligent conversational responses—similar to a lightweight ChatGPT.
----
## ✨ Key Highlights
- 🚀 Google Gemini LLM (gemini-2.5-flash) for reasoning
- 🔎 DuckDuckGo & Wikipedia integrated research tools
- 💾 Auto-save outputs to a text file (research_output.txt)
- 🧠 REACT-style reasoning using LangChain
- 🔐 Secured API key handling via .env
- 🧩 Modular architecture (main.py, tools.py, research_agent.py)
--
## 📂 Project Structure
- AI Agent Project/
- │── README.md               # Documentation
- │── main.py                 # Interactive CLI agent
- │── tools.py                # DuckDuckGo, Wikipedia, Save tool
- │── research_output.txt     # Auto-generated logs
- │── requirements.txt
- └── .env                    # Environment config (GEMINI_API_KEY)

## 🧠 How the Agent Works

**Load .env**
- Loads your GEMINI_API_KEY securely
- Initialize Gemini LLM
- ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
- Load Custom Tools
- DuckDuckGo Search
- Wikipedia Summary
- Save-to-file Tool
- Create REACT-based Agent
- Think, Search, Read Wikipedia
- Save research automatically
- Provide short answers + opinions
---
## ⚡ CLI Interaction:

Run in terminal, type your question, get answers
Exit with 'exit' or 'quit'

## ⚙️ Installation & Setup
**1️⃣ Clone Repository**
git clone https://github.com/<your-username>/AI-Course
cd "AI Course/AI Agent Project"

**2️⃣ Create Virtual Environment**
Windows
python -m venv venv
venv\Scripts\activate

Mac/Linux
python3 -m venv venv
source venv/bin/activate

**3️⃣ Install Dependencies**
pip install -r requirements.txt

**4️⃣ Create .env File**
GEMINI_API_KEY="your_api_key_here"

**▶️ Run the Agent**
python main.py


You will see:

🔵 ChatGPT-like Agent Activated!
Type your question (type 'exit' to quit)...

Then type your query:

You: What is AI?
The agent will search, reason, and answer automatically.
## ✅ Note: This project is terminal/CLI-based, not a web application.

**Centered in GitHub Markdown:**

<p align="center">
  <img src="./images/agent_demo.png" width="700">
</p>

## 📦 Requirements
langchain==0.3.0
langchain-community==0.3.0
langchain-google-genai==2.0.0
google-ai-generativelanguage==0.7.0
python-dotenv==1.0.1
duckduckgo-search==5.2.2
wikipedia==1.4.0

## 🚀 Future Enhancements (Optional)

- (These features are NOT in the current project — only future ideas)
- Memory-enabled long-term agent
- Vector DB (FAISS/Chroma) integration
- Web UI with Streamlit
- Automated research agent
- Logging & analytics

## 👨‍💻 Author

Md. Rakib Ahmed
