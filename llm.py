import os

from dotenv import load_dotenv

from models import Feedback
from models import FinalEvaluation
from langchain_groq import ChatGroq
import streamlit as st


load_dotenv()

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_API_KEY = None

if not GROQ_API_KEY:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")





llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)



feedback_llm = llm.with_structured_output(
    Feedback
)

final_eval_llm = llm.with_structured_output(
    FinalEvaluation
)
