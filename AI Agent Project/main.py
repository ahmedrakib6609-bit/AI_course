import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType

from tools import search_tool, wiki_tool, save_tool

# -------------------- LOAD .ENV --------------------
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please add it.")

# -------------------- GOOGLE GEMINI LLM --------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    google_api_key=gemini_api_key
)

# -------------------- TOOLS --------------------
tools = [search_tool, wiki_tool, save_tool]  # DuckDuckGo safe now

# -------------------- AGENT --------------------
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True,
    max_iterations=4
)

print("\n🔵 ChatGPT-like Agent Activated!\n")
print("Type your question (type 'exit' to quit)...\n")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Agent: Goodbye!")
        break

    # -------------------- FORCE SHORT OPINION --------------------
    query = "Answer briefly and give an opinion if subjective: " + query

    try:
        result = agent.invoke({"input": query})
        print("\nAgent:", result["output"])
    except Exception as e:
        print("Error:", e)
