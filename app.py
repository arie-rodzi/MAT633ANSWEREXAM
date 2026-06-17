import streamlit as st

# Step-by-step import of our raw data structure files
import data_jan2024
import data_july2024
import data_feb2025
import data_july2025

# 1. Page Configuration Framework (Edisi Khas Premium)
st.set_page_config(
    page_title="MAT633 Executive Vault", 
    page_icon="💎",
    layout="wide"
)

# 2. Advanced Premium CSS Injection (Midnight Velvet & Liquid Gold Theme)
st.markdown("""
<style>
    /* Latar belakang utama dengan tona minimalis eksklusif */
    .stApp {
        background: linear-gradient(135deg, #fdfbf7 0%, #f4f7fc 100%) !important;
    }
    
    /* Transformasi Sidebar dengan Glassmorphic Border Ringan */
    section[data-testid="stSidebar"] {
        background-color: #0f172a !important; /* Gelap Premium */
        box-shadow: 5px 0px 25px rgba(0,0,0,0.15);
        border-right: 2px solid #e2e8f0;
    }
    
    /* Mengubah warna teks dalam sidebar agar putih/emas */
    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] h3 {
        color: #f1f5f9 !important;
    }
    
    /* Hiasan premium untuk pengepala Expander (Lelaran Lembut) */
    .streamlit-expanderHeader {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        color: #0f172a !important;
        padding: 14px 18px !important;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.02) !important;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .streamlit-expanderHeader:hover {
        border-color: #d97706 !important; /* Gold Border on Hover */
        background: #fffbeb !important;
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# 3. Super Wow Master Header with Your Name & Developer Tag
st.markdown("""
<div style="
    background: linear-gradient(135deg, #020617 0%, #0f172a 60%, #1e1b4b 100%);
    padding: 35px 40px; 
    border-radius: 24px; 
    box-shadow: 0px 15px 35px rgba(15, 23, 42, 0.25); 
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
    border-left: 8px solid #d97706; /* Emas */
">
    <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: #d97706; opacity: 0.1; filter: blur(50px); border-radius: 50%;"></div>
    
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <h1 style="color: #ffffff; font-weight: 900; font-size: 36px; margin: 0; letter-spacing: -1px; font-family: 'Inter', sans-serif;">
                💎 MAT633 — Intelligence System Analytics
            </h1>
            <p style="color: #94a3b8; font-size: 15px; margin: 8px 0 0 0; font-weight: 500;">
                Advanced Fuzzy Set Theory Core Repository Vault
            </p>
        </div>
        <div style="
            background: rgba(217, 119, 6, 0.1); 
            border: 1px solid rgba(217, 119, 6, 0.3);
            padding: 10px 20px;
            border-radius: 14px;
            text-align: right;
            backdrop-filter: blur(10px);
            margin-top: 10px;
        ">
            <span style="color: #f59e0b; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; display: block;">System Architecture By</span>
            <span style="color: #ffffff; font-size: 18px; font-weight: 800; letter-spacing: 0.5px;">✨ AMIRUL AMIN ✨</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Data Session Mapping Setup
session_mapping = {
    "January 2024": data_jan2024.questions,
    "July 2024": data_july2024.questions,
    "February 2025": data_feb2025.questions,
    "July 2025": data_july2025.questions
}

# 5. Ultra-Modern Sidebar Config
st.sidebar.markdown("""
<div style="padding: 15px 5px; text-align: center; border-bottom: 1px solid #1e293b; margin-bottom: 20px;">
    <div style="font-size: 40px; margin-bottom: 10px;">🌟</div>
    <h3 style="margin: 0; font-size: 18px; font-weight: 800; letter-spacing: 0.5px;">AMIRUL'S HUB</h3>
    <span style="color: #64748b; font-size: 11px; text-transform: uppercase; font-weight: 600;">Secure Access Terminal</span>
</div>
<p style="color: #94a3b8; font-size: 12px; font-weight: 500; margin-left: 5px; margin-bottom: 5px;">SELECT REPOSITORY SLOT:</p>
""", unsafe_allow_html=True)

selected_session = st.sidebar.selectbox(
    "Choose Examination Session Slot", 
    list(session_mapping.keys()),
    label_visibility="collapsed"
)
current_questions = session_mapping[selected_session]

# Sub-Header Slot Aktif (Kecerunan Soft Gold ke Beige)
st.markdown(f"""
<div style="
    background: linear-gradient(90deg, #fffbeb 0%, #fafaf9 100%);
    padding: 14px 24px;
    border-left: 5px solid #d97706;
    border-radius: 6px 16px 16px 6px;
    margin-bottom: 30px;
    box-shadow: 0px 4px 10px rgba(217, 119, 6, 0.03);
">
    <span style="color: #78350f; font-weight: 800; font-size: 16px; letter-spacing: 0.3px;">🗂️ DEPLOYED ARCHIVE SLOT: {selected_session}</span>
</div>
""", unsafe_allow_html=True)

# 6. Question Core Card Grid Generation Loop
for idx, q_block in enumerate(current_questions):
    with st.container():
        col1, col2 = st.columns([1, 2.7])
        
        # Left Side: Meta Card (No marks parameters)
        with col1:
            st.markdown(f"""
            <div style="
                background: #ffffff;
                padding: 24px;
                border-radius: 16px;
                border: 1px solid #e2e8f0;
                box-shadow: 0px 8px 20px rgba(0,0,0,0.01);
                height: 100%;
                border-top: 4px solid #0f172a;
            ">
                <span style="
                    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
                    color: #f8fafc;
                    padding: 5px 14px;
                    border-radius: 20px;
                    font-size: 12px;
                    font-weight: 800;
                    display: inline-block;
                    margin-bottom: 20px;
                    letter-spacing: 0.5px;
                    box-shadow: 0px 3px 8px rgba(0,0,0,0.08);
                ">
                    ⚡ {q_block['question_no']}
                </span>
                <div>
                    <span style="color: #94a3b8; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 4px;">Fuzzy Domain Matrix</span>
                    <p style="color: #0f172a; font-size: 15px; font-weight: 700; line-height: 1.4; margin: 0;">{q_block['topic']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        # Right Side: Content Card
        with col2:
            st.markdown(f"""
            <div style="
                background: #ffffff;
                padding: 26px;
                border-radius: 16px;
                border: 1px solid #e2e8f0;
                box-shadow: 0px 8px 20px rgba(0,0,0,0.01);
            ">
                <h4 style="color: #1e293b; font-weight: 800; margin-top: 0; margin-bottom: 15px; font-size: 16px; letter-spacing: -0.2px;">📝 SYSTEM QUESTION STATEMENT</h4>
            """, unsafe_allow_html=True)
            
            # Paparan Formula/Teks Soalan yang diproses secara selamat di luar ralat merah HTML
            st.markdown(q_block['question'])
            
            st.markdown("</div>", unsafe_allow_html=True) # Penutup container soalan
            
            st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)
            
            # Interactive Answer Panel (Emas/Mewah)
            with st.expander("🔓 REVEAL RESOLUTION EVALUATION MATRIX"):
                st.markdown("""
                <div style="
                    background: linear-gradient(135deg, #b45309 0%, #d97706 100%);
                    padding: 10px 18px;
                    border-radius: 10px 10px 0px 0px;
                    margin-bottom: 0px;
                ">
                    <span style="color: #ffffff; font-weight: 800; font-size: 13px; letter-spacing: 0.8px;">⚡ GOLDEN SOLUTION SPECS</span>
                </div>
                <div style="
                    background: #ffffff;
                    padding: 24px;
                    border: 1px solid #e2e8f0;
                    border-top: none;
                    border-radius: 0px 0px 12px 12px;
                    box-shadow: 0px 10px 20px rgba(0,0,0,0.02);
                ">
                """, unsafe_allow_html=True)
                
                # Paparan Skema Jawapan Matematik Kompleks Tanpa Sebarang Ralat Merah
                st.markdown(q_block['answer'])
                
                st.markdown("</div>", unsafe_allow_html=True) # Penutup container jawapan
                
        # Garisan pemisah seni abstrak ultra halus
        st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; margin: 30px 0;">
            <div style="height: 1px; width: 100%; background: linear-gradient(to right, rgba(217,119,6,0), rgba(217,119,6,0.2) 50%, rgba(217,119,6,0));"></div>
        </div>
        """, unsafe_allow_html=True)
