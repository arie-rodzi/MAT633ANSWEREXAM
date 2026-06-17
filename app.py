import streamlit as st

# Step-by-step import of our raw data structure files
import data_jan2024
import data_july2024
import data_feb2025
import data_july2025

# 1. Page Configuration Framework (Must be the very first Streamlit command)
st.set_page_config(
    page_title="MAT633 Examination Database", 
    page_icon="📚",
    layout="wide"
)

# 2. Main Dashboard Headers
st.title("📚 MAT633 - Fuzzy Set Theory Exam Panel")
st.caption("Official Universiti Teknologi MARA Database Registry Dashboard")

# 3. Session Mapping Array Configuration
session_mapping = {
    "January 2024": data_jan2024.questions,
    "July 2024": data_july2024.questions,
    "February 2025": data_feb2025.questions,
    "July 2025": data_july2025.questions
}

# 4. Sidebar Controller Architecture
st.sidebar.header("Navigation Hub")
selected_session = st.sidebar.selectbox(
    "Choose Examination Session Slot", 
    list(session_mapping.keys())
)
current_questions = session_mapping[selected_session]

st.header(f"📋 Session: {selected_session}")
st.markdown("---")

# 5. Question Grid Generator Loop
# Note: Iterating fully over lists without truncations as requested
for idx, q_block in enumerate(current_questions):
    with st.container():
        col1, col2 = st.columns([1, 3])
        
        # Meta-information column panel
        with col1:
            st.subheader(f"🏷️ {q_block['question_no']}")
            st.write(f"**Topic Focus:**")
            st.code(q_block['topic'], language="text")
            
        # Core Content display column panel
        with col2:
            st.markdown("### Question Formulation")
            st.markdown(q_block['question'])
            
            # Marking Scheme Toggle Container
            with st.expander("🔓 Display Official Marking Scheme Key Matrix"):
                st.markdown(q_block['answer'])
                
        st.markdown("<br><hr style='border: 1px dashed #dedede;'><br>", unsafe_html=True)
