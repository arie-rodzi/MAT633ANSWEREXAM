import streamlit as st

# Step-by-step import of our raw data structure files
import data_jan2024
import data_july2024
import data_feb2025
import data_july2025

st.set_page_config(page_title="MAT633 Examination Database", layout="wide")

st.title("📚 MAT633 - Fuzzy Set Theory Exam Panel")
st.caption("Official Universiti Teknologi MARA Database Registry Dashboard")

# Session Mapping Array Configuration
session_mapping = {
    "January 2024": data_jan2024.questions,
    "July 2024": data_july2024.questions,
    "February 2025": data_feb2025.questions,
    "July 2025": data_july2025.questions
}

# Sidebar Select Box Selection Architecture
selected_session = st.sidebar.selectbox("Choose Examination Session Slot", list(session_mapping.keys()))
current_questions = session_mapping[selected_session]

st.header(f"📋 Session: {selected_session}")
st.markdown("---")

# Iterating fully over arrays exactly as requested without truncations
for idx, q_block in enumerate(current_questions):
    with st.container():
        col1, col2 = st.columns([1, 4])
        with col1:
            st.subheader(f"🏷️ {q_block['question_no']}")
            st.info(f"**Weight:** {q_block['marks']} Marks")
            st.write(f"**Topic Focus:** \n`{q_block['topic']}`")
        with col2:
            st.markdown("### Question Formulation")
            st.markdown(q_block['question'])
            
            with st.expander("🔓 Display Official Marking Scheme Key Matrix"):
                st.markdown(q_block['answer'])
        st.markdown("---")
