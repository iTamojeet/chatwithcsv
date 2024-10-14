#Step 01: Import All the Required Libraries
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_groq import ChatGroq

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with your CSV 📈")
    st.header("Ask your CSV 📈")
    csv_file = st.file_uploader("Upload a CSV file", type = "csv")
    if csv_file is not None:
        agent = create_csv_agent(
            ChatGroq(model="llama-3.1-70b-versatile"),
            csv_file,
            verbose=True,
            allow_dangerous_code=True,
            agent_executor_kwargs={"handle_parsing_errors": True}

        )
        user_question  = st.text_input("Ask a question about your CSV: ")
        if user_question is not None and user_question !="":
            st.write(f"Your Question was {user_question}")
            with st.spinner(text = "In Tamojeet Progress ...."):
                st.write(agent.run(user_question))
if __name__ == "__main__":
    main()