from gemini_agent import question_to_sql
from query_engine import run_sql_query

question = input("Ask your question: ")
sql_query = question_to_sql(question)

print("\nGenerated SQL:\n", sql_query)

result = run_sql_query(sql_query)
print("\nResult:\n", result)
