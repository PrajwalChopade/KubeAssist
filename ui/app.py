import requests
import streamlit as st
from datetime import datetime

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="KubeAssist",
    page_icon="☸️",
    layout="wide"
)

# ---------- SIDEBAR ----------

with st.sidebar:

    st.title("☸️ KubeAssist")

    st.markdown(
        """
Production RAG over
Kubernetes Documentation

### Features

✅ Hybrid Search

✅ BM25 + Dense

✅ Reranker

✅ Semantic Cache

✅ Multi Query Retrieval

✅ FastAPI Backend
"""
    )

    st.divider()

    st.caption(
        "Built with FastAPI + Qdrant + BGE"
    )

# ---------- HEADER ----------

st.title(
    "☸️ Kubernetes Documentation Copilot"
)

st.caption(
    "Ask questions about Kubernetes"
)

# ---------- CHAT HISTORY ----------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ---------- INPUT ----------

prompt = st.chat_input(
    "Ask a Kubernetes question..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching docs..."
        ):

            try:

                start = datetime.now()

                response = requests.post(
                    API_URL,
                    json={
                        "query": prompt
                    },
                    timeout=120
                )

                result = response.json()

                latency = (
                    datetime.now()
                    - start
                ).total_seconds()

                answer = result["answer"]

                st.markdown(answer)

                st.caption(
                    f"Response time: "
                    f"{latency:.2f}s"
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )