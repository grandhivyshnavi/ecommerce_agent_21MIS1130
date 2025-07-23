# ecommerce_agent_21MIS1130

**Summary:**
This project is a conversational chatbot interface that allows users to ask natural language questions about their sales data. Using Gemini 2.5 Flash-Lite, the chatbot dynamically generates SQL queries, retrieves results from a local SQLite database (sales.db), and presents answers in a natural, interactive format—complete with tables, charts, and human-readable text responses.


**File Descriptions**

**1. chatbot_app.py**
Main Streamlit application that powers the chatbot interface. It allows users to input natural language questions about sales data and interactively shows SQL queries, tables, charts, and text answers using Gemini 2.5 and SQLite.

**2. csvtosql.py**
Loads CSV files (Ad_Sales_Metrics.csv, Total_Sales_Metrics.csv, and Eligibility_Table.csv) into an SQLite database (sales.db) by converting them into corresponding SQL tables.

**3. gemini_agent.py**
Contains helper functions that interact with the Gemini 2.5 Flash-Lite model. It:

-> Converts user questions into SQL queries (question_to_sql)

-> Transforms raw query results into natural language responses (answer_in_sentence)

**4. query_engine.py**
Handles execution of SQL queries on the sales.db SQLite database and returns the result.

**5. test_llm.py**
A basic terminal-based test script to input a question, generate the SQL using Gemini, and view the resulting query and its database output without using the Streamlit UI.

**6. list.py**
Lists all available Gemini models using the Generative AI API, displaying model names, descriptions, and token limits. Useful for verifying API access and available model configurations.
