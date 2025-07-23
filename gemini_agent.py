import google.generativeai as genai
import os

# Seting up the Gemini API key
genai.configure(api_key="AIzaSyDyPDQICiK0_4gSu-tck8tTWGD9NazwWnU")

model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

def question_to_sql(prompt: str) -> str:
    system_prompt = """
You are a helpful SQL assistant. Generate a valid **SQLite** SQL query for the user's question using only these tables:

1. ad_sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
2. total_sales(date, item_id, total_sales, total_units_ordered)
3. eligibility(eligibility_datetime_utc, item_id, eligibility, message)

Guidelines:
- Use only these tables and columns.
- Use JOINs only when required.
- Do not include explanations.
- Return only the SQL, nothing else.

Question: {}
SQL:
""".format(prompt)

    response = model.generate_content(system_prompt)
    content = response.text.strip()

    # Extract first SQL-looking line
    for line in content.split("\n"):
        if line.strip().lower().startswith("select"):
            return line.strip()
    return "ERROR: No SQL found."

def answer_in_sentence(question: str, result: str) -> str:
    prompt = f"""
You are a helpful assistant. Turn the result of a database query into a natural, human-readable answer.

Question: {question}
Result: {result}

Answer:
"""
    response = model.generate_content(prompt)
    return response.text.strip()
