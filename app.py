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

# 2. Premium Global CSS Style Injection (Gradient background & custom styling)
st.markdown("""
<style>
    /* Menukar warna latar belakang utama dengan tona super clean & soft gradient */
    .stApp {
        background: linear-gradient(180deg, #f8fafd 0%, #edf2f9 100%) !important;
    }
    
    /* Mencantikkan Sidebar dengan Glassmorphism effect */
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        box-shadow: 2px 0px 15px rgba(0,0,0,0.05);
        border-right: 1px solid #e2e8f0;
    }
    
    /* Mengubahsuai elemen tajuk besar expander */
    .streamlit-expanderHeader {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        color: #1e293b !important;
        transition: all 0.3s ease;
    }
    .streamlit-expanderHeader:hover {
        border-color: #3b82f6 !important;
        background: #f8fafc !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Main Dashboard Headers (Dibalut dengan Gradient Jelas & Moden)
st.markdown("""
<div style="
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #3b82f6 100%);
    padding: 30px; 
    border-radius: 16px; 
    box-shadow: 0px 10px 25px rgba(30, 58, 138, 0.15); 
    margin-bottom: 25px;
">
    <h1 style="color: #ffffff; font-weight: 800; font-size: 32px; margin: 0; letter-spacing: -0.5px;">
        📚 MAT633 — Fuzzy Set Theory Exam Panel
    </h1>
    <p style="color: #93c5fd; font-size: 15px; margin: 8px 0 0 0; font-weight: 400; opacity: 0.9;">
       FINAL EXAMINATION QUESTIONS
    </p>
</div>
""", unsafe_allow_html=True)

# 4. Session Mapping Array Configuration
session_mapping = {
    "January 2024": data_jan2024.questions,
    "July 2024": data_july2024.questions,
    "February 2025": data_feb2025.questions,
    "July 2025": data_july2025.questions
}

# 5. Sidebar Controller Architecture
st.sidebar.markdown("""
<div style="padding: 10px 0px;">
    <h3 style="color: #1e293b; font-weight: 700; margin-bottom: 5px;">🧩 Control Center</h3>
    <p style="color: #64748b; font-size: 13px;">Sila pilih sesi akademik di bawah:</p>
</div>
""", unsafe_allow_html=True)

selected_session = st.sidebar.selectbox(
    "Choose Examination Session Slot", 
    list(session_mapping.keys()),
    label_visibility="collapsed"
)
current_questions = session_mapping[selected_session]

# Paparan Sub-Header Sesi Pilihan (Kecerunan Biru Cair Ke Ungu)
st.markdown(f"""
<div style="
    background: linear-gradient(90deg, #eff6ff 0%, #f5f3ff 100%);
    padding: 12px 20px;
    border-left: 5px solid #3b82f6;
    border-radius: 0px 12px 12px 0px;
    margin-bottom: 25px;
">
    <span style="color: #1e3a8a; font-weight: 700; font-size: 18px;">📋 Active Session Slot: {selected_session}</span>
</div>
""", unsafe_allow_html=True)

# 6. Question Grid Generator Loop
for idx, q_block in enumerate(current_questions):
    with st.container():
        col1, col2 = st.columns([1, 2.8])
        
        # Meta-information column panel (Left Card)
        with col1:
            st.markdown(f"""
            <div style="
                background: #ffffff;
                padding: 20px;
                border-radius: 12px;
                border: 1px solid #e2e8f0;
                box-shadow: 0px 4px 6px rgba(0,0,0,0.02);
                height: 100%;
            ">
                <span style="
                    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
                    color: white;
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-size: 13px;
                    font-weight: 700;
                    display: inline-block;
                    margin-bottom: 15px;
                ">
                    📌 {q_block['question_no']}
                </span>
                <div style="margin-top: 5px;">
                    <span style="color: #64748b; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Core Topic Focus</span>
                    <p style="color: #1e293b; font-size: 14px; font-weight: 600; margin-top: 4px; line-height: 1.4;">{q_block['topic']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        # Core Content display column panel (Right Card)
        with col2:
            st.markdown(f"""
            <div style="
                background: #ffffff;
                padding: 22px;
                border-radius: 12px;
                border: 1px solid #e2e8f0;
                box-shadow: 0px 4px 6px rgba(0,0,0,0.02);
            ">
                <h4 style="color: #0f172a; font-weight: 700; margin-top: 0; margin-bottom: 12px; font-size: 16px;">📝 Question Formulation</h4>
            """, unsafe_allow_html=True)
            
            # Memaparkan soalan (Teks biasa + LaTeX dipaparkan secara selamat di luar HTML)
            st.markdown(q_block['question'])
            
            st.markdown("</div>", unsafe_allow_html=True) # Penutup container soalan putih
            
            st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
            
            # Marking Scheme Toggle Container (Gradient Header + Inside Container)
            with st.expander("🔓 Display Official Marking Scheme Key Matrix"):
                # Header hiasan skema jawapan dengan warna gradient hijau-teal
                st.markdown("""
                <div style="
                    background: linear-gradient(135deg, #059669 0%, #10b981 100%);
                    padding: 8px 16px;
                    border-radius: 8px 8px 0px 0px;
                    margin-bottom: 0px;
                ">
                    <span style="color: #ffffff; font-weight: 700; font-size: 13px; letter-spacing: 0.5px;">📝 VERIFIED ANSWER MATRIX</span>
                </div>
                <div style="
                    background: #ffffff;
                    padding: 20px;
                    border: 1px solid #e2e8f0;
                    border-top: none;
                    border-radius: 0px 0px 8px 8px;
                ">
                """, unsafe_allow_html=True)
                
                # Memaparkan jawapan (Sintaks LaTeX diproses di sini dengan selamat tanpa ralat merah)
                st.markdown(q_block['answer'])
                
                st.markdown("</div>", unsafe_allow_html=True) # Penutup sub-container jawapan
                
        # Garisan pemisah hiasan yang sangat halus berbanding garisan kasar asal
        st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; margin: 25px 0;">
            <div style="height: 1px; width: 100%; background: linear-gradient(to right, rgba(226,232,240,0), rgba(226,232,240,1) 50%, rgba(226,232,240,0));"></div>
        </div>
        """, unsafe_allow_html=True)
