import streamlit as st
from main import CSVAnalyzer

# Create a persistent CSVAnalyzer instance
if "analyzer" not in st.session_state:
    st.session_state.analyzer = CSVAnalyzer()

analyzer = st.session_state.analyzer

st.set_page_config(page_title="📊 CSV AI Analyzer", layout="wide")
st.title("🧠 CSV AI Analyzer using Ollama")

uploaded = st.file_uploader("📁 Upload CSV", type="csv")

if uploaded and "file_uploaded" not in st.session_state:
    analyzer.load_csv(uploaded)
    st.session_state.file_uploaded = True
    st.success("✅ CSV Loaded!")

if st.session_state.get("file_uploaded", False):
    query = st.text_input("🔍 Ask a question about the CSV")

    if st.button("Analyze") and query.strip():
        result = analyzer.ask(query)
        st.write("📤 **Answer:**")
        st.write(result)

    if analyzer.history:
        st.markdown("### 🕘 Recent Q&A History")
        for q, a in reversed(analyzer.history[-5:]):
            st.markdown(f"**Q:** {q}")
            st.markdown(f"**A:** {a}")
            st.markdown("---")
 