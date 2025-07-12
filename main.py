import pandas as pd
from langchain_community.llms import Ollama

# Initialize Ollama
llm = Ollama(model="llama3")

class CSVAnalyzer:
    def __init__(self):
        self.df = None
        self.history = []  # for storing Q&A history

    def load_csv(self, file_obj):
        self.df = pd.read_csv(file_obj)
        self.history = []

    def ask(self, query: str):
        if self.df is None:
            return "⚠️ No CSV file loaded."

        # Get schema and sample
        schema = "\n".join([f"{col}: {dtype}" for col, dtype in self.df.dtypes.items()])
        sample = self.df.head(3).to_csv(index=False)

        history_text = "\n".join(
            [f"Q: {q}\nA: {a}" for q, a in self.history[-3:]]
        )

        prompt = f"""
You are a helpful data analyst working with CSV files.

Schema:
{schema}

Sample Data:
{sample}

Recent Conversation:
{history_text if history_text else 'None'}

User Question: {query}
Give a direct, concise answer.
"""

        response = llm.invoke(prompt).strip()
        self.history.append((query, response))

        return response

 