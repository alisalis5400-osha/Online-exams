import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="المنصة التعليمية الذكية", page_icon="⚡", layout="centered")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

MODEL_NAME = 'gemini-1.5-flash'

st.markdown("""
<div style="background-color: #1b4d3e; padding: 20px; border-radius: 12px; text-align: center; color: white; margin-bottom: 25px;">
    <h1 style="margin: 0; font-size: 28px;">المنصة التعليمية الذكية ⚡</h1>
    <p style="margin: 5px 0 0 0; font-size: 16px;">أهلاً بكِ يا فندم (admin)</p>
</div>
""", unsafe_allow_html=True)

app_mode = st.radio("اختر القسم المطلوب:", ["📚 بنك الاختبارات التفاعلية", "🤖 مساعد الواجبات الذكي وتصحيحها", "📊 الملخصات والعروض التقديمية الذكية"])
st.markdown("---")

if app_mode == "📚 بنك الاختبارات التفاعلية":
    st.markdown("### 📝 بنك الاختبارات التفاعلية الشامل")
    
    # قائمة بكل الامتحانات المتاحة لدينا على المنصة
    exams_dict = {
        "Science - الصف السادس الابتدائي (Chapter 2: Respiration الشامل)": "Science chapter2 g6.html",
        "Science - الصف السادس الابتدائي (امتحان الفصل الأول والثاني)": "science_g6.html",
        "Social Studies - الصف السادس الابتدائي": "Social-G6.html",
        "Social Studies - الصف الرابع الابتدائي": "Social-G4.html",
        "Arabic - الصف الثاني الإعدادي": "Arabic.prep2.html",
        "English - الصف الثاني الإعدادي": "engprep2.htm"
    }
    
    selected_exam_title = st.selectbox("اختر الامتحان المطلوب:", list(exams_dict.keys()))
    file_name = exams_dict[selected_exam_title]
    
    st.success(f"مستعد لفتح: ({selected_exam_title}) 🚀")
    exam_url = f"https://alisalis5400-osha.github.io/Online-exams/{file_name}"
    
    st.markdown(f"""
    <div style="margin-top: 20px; text-align: center;">
        <a href="{exam_url}" target="_blank" style="display: block; background-color: #1b4d3e; color: white; padding: 15px 20px; border-radius: 10px; text-decoration: none; font-size: 18px; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            اضغط هنا لبدء الامتحان 🚀<br>
            <span style="font-size: 13px; font-weight: normal; color: #e0e0e0;">(سيفتح في تبويب جديد تماماً)</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

elif app_mode == "🤖 مساعد الواجبات الذكي وتصحيحها":
    st.markdown("### 🤖 مساعد الواجبات الذكي وتصحيحها")
    uploaded_homeworks = st.file_uploader("ارفع صور أو ملفات الواجب هنا", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)
    if uploaded_homeworks:
        for f in uploaded_homeworks: st.image(Image.open(f), use_container_width=True)
else:
    st.markdown("### 📊 الملخصات والعروض التقديمية الذكية")
    st.info("هذا القسم جاهز للعمل.")
