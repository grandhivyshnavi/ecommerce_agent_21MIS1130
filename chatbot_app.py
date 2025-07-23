import streamlit as st
import pandas as pd
import plotly.express as px
from gemini_agent import question_to_sql, answer_in_sentence
from query_engine import run_sql_query

st.set_page_config(page_title="SalesBot 💬", layout="centered")
st.title("📊 Sales Chatbot (Gemini 2.5 Flash-Lite + SQLite)")

# Button to start a new chat
if st.button("🆕 New Chat"):
    st.session_state.messages = []

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    msg_type = msg.get("type", "text")  # fallback to 'text' if 'type' is missing
    with st.chat_message(msg["role"]):
        if msg_type == "code":
            st.code(msg["content"], language="sql")
        elif msg_type == "table":
            st.table(msg["content"])
        elif msg_type == "chart":
            st.plotly_chart(msg["content"], use_container_width=True)
        else:
            st.markdown(msg["content"])


# Input box
user_question = st.chat_input("Ask about your sales data...")

if user_question:
    # Show user message
    st.chat_message("user").markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question, "type": "text"})

    # Get SQL query
    sql_query = question_to_sql(user_question)

    # Show SQL in chat
    st.chat_message("assistant").code(sql_query, language="sql")
    st.session_state.messages.append({"role": "assistant", "content": sql_query, "type": "code"})

    try:
        # Run SQL
        result = run_sql_query(sql_query)

        if result:
            if len(result) == 1 and len(result[0]) == 1:
                raw_result = result[0][0]
                natural_answer = answer_in_sentence(user_question, raw_result)
                st.chat_message("assistant").markdown(f"💬 {natural_answer}")
                st.session_state.messages.append({
                    "role": "assistant", "content": f"💬 {natural_answer}", "type": "text"
                })
            else:
                # Show result table
                df = pd.DataFrame(result)
                st.chat_message("assistant").table(df)
                st.session_state.messages.append({
                    "role": "assistant", "content": df, "type": "table"
                })

                # Try chart for 2-column data
                if df.shape[1] == 2:
                    try:
                        df.columns = ["Label", "Value"]
                        df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
                        df = df.dropna()

                        if not df.empty:
                            fig = px.bar(df, x="Label", y="Value", title="📊 Chart")
                            st.chat_message("assistant").plotly_chart(fig, use_container_width=True)
                            st.session_state.messages.append({
                                "role": "assistant", "content": fig, "type": "chart"
                            })
                    except Exception as chart_err:
                        st.warning(f"⚠️ Could not generate chart: {chart_err}")
        else:
            msg = "ℹ️ No results found."
            st.chat_message("assistant").markdown(msg)
            st.session_state.messages.append({
                "role": "assistant", "content": msg, "type": "text"
            })

    except Exception as e:
        error_msg = f"❌ SQL Error: {e}"
        st.chat_message("assistant").markdown(error_msg)
        st.session_state.messages.append({
            "role": "assistant", "content": error_msg, "type": "text"
        })
