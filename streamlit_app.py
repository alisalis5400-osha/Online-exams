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
    st.markdown("### 📝 اختر المادة والصف لتأدية الامتحان")
    
    subject_name = st.selectbox("اختر المادة", ["عربي", "دراسات", "دين", "Math", "Science", "English", "French"])
    stage_name = st.radio("اختر المرحلة", ["المرحلة الابتدائية", "المرحلة الإعدادية"])
    
    if stage_name == "المرحلة الابتدائية":
        grade_name = st.selectbox("اختر الصف", ["الصف الأول الابتدائي", "الصف الثاني الابتدائي", "الصف الثالث الابتدائي", "الصف الرابع الابتدائي", "الصف الخامس الابتدائي", "الصف السادس الابتدائي"])
    else:
        grade_name = st.selectbox("اختر الصف", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])
        
    display_name = f"{subject_name} - {grade_name}"
    
    # ربط مباشر لملف Science الصف السادس بالاسم الموجود عندك تماماً
    if subject_name == "Science" and grade_name == "الصف السادس الابتدائي":
        file_name = "Science chapter2 g6.html"
    else:
        sub_codes = {"عربي": "arabic", "دراسات": "social", "دين": "religion", "Math": "math", "Science": "science", "English": "english", "French": "french"}
        grd_codes = {
            "الصف الأول الابتدائي": "g1", "الصف الثاني الابتدائي": "g2", "الصف الثالث الابتدائي": "g3",
            "الصف الرابع الابتدائي": "g4", "الصف الخامس الابتدائي": "g5", "الصف السادس الابتدائي": "g6",
            "الصف الأول الإعدادي": "prep1", "الصف الثاني الإعدادي": "prep2", "الصف الثالث الإعدادي": "prep3"
        }
        file_name = f"{sub_codes.get(subject_name, 'science')}_{grd_codes.get(grade_name, 'g6')}.html"
        
    st.success(f"مستعد لفتح امتحان ({display_name}) 🚀")
    exam_url = f"https://alisalis5400-osha.github.io/Online-exams/{file_name}"
    st.markdown(f"""
    <div style="margin-top: 20px; text-align: center;">
        <a href="{exam_url}" target="_blank" style="display: block; background-color: #1b4d3e; color: white; padding: 15px 20px; border-radius: 10px; text-decoration: none; font-size: 18px; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            اضغط هنا لبدء امتحان ({display_name}) 🚀<br>
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
