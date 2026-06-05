import os

from dotenv import load_dotenv

from models import Feedback
from models import FinalEvaluation
from langchain_groq import ChatGroq
import streamlit as st


load_dotenv()

GROQ_API_KEY = (
    st.secrets.get("GROQ_API_KEY")
    or os.getenv("GROQ_API_KEY")
)

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found in .env"
    )




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
