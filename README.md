 # 🧠 CSV AI Analyzer using Ollama and LangChain  

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
├── app.py                 # Streamlit UI             
├── main.py                # Core logic using LangChain + Ollama    
├── requirements.txt       # Dependencies          


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

-----

## 🧠 How It Works

1. **Upload a CSV file**

2. **The app loads the file into a Pandas DataFrame**

3. It extracts:
   - 📄 **Sample data**
   - 💬 **Chat history**

4. A prompt is built and passed to the **Ollama** model (`llama3`) using **LangChain**

5. The model returns a **human-readable answer**

6. Chat history is **retained** to provide context for follow-up questions

---

## 💡 Example Questions

- What are the column names?
- How many missing values are there?
- What's the average value in a numeric column?
- Show unique values in a specific column
- Give a summary of this dataset

---

## 🚀 Technologies Used

- **LangChain**: For prompt management and LLM interaction
- **Ollama**: Local LLM engine running `llama3`
- **Streamlit**: Interactive user interface
- **Pandas**: For CSV data manipulation

---------------

### 🔮 Future Enhancements
✅ Add support for multiple CSV file uploads     
✅ Enable cross-dataset querying and comparison      
✅ Add interactive SQL query runner
