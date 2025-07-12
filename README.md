 # 🧠 CSV AI Analyzer using Ollama + LangChain + Streamlit

This is an intelligent CSV file analyzer built with **LangChain**, **Ollama**, and **Streamlit**. It allows you to upload a CSV file and ask **natural language questions** about its contents — including structure, statistics, missing values, column names, and more.

It works entirely **offline**, using local large language models (LLMs) via **Ollama**, such as `llama3`.

---

## ✨ Features

- 📁 Upload any CSV file
- 🤖 Ask plain English questions about your data
- 🧠 Uses LangChain to generate context-aware prompts
- 📊 Shows schema and sample data to LLM
- 🔁 Maintains chat history for contextual understanding
- ⚡ Powered by local LLMs (no internet needed)
- 💡 Fast, interactive UI with Streamlit

---

## 🏗️ Project Structure

csv_analyzer_llm/
├── app.py              # Streamlit UI
├── main.py             # Core logic using LangChain + Ollama
├── requirements.txt    # Dependencies

 ---

## 🛠️ Installation

### 1. 📦 Install Python Dependencies

```bash
pip install -r requirements.txt

```
### 2. ⚙️ Install & Run Ollama
Download and install Ollama:

🔗 https://ollama.com/download

Then open a terminal and run:

```
ollama run llama3
```

### 3. Run the Streamlit app:

```
streamlit run app.py
```
Then open your browser to:  http://localhost:8501


