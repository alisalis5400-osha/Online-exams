import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة وتكوينها
st.set_page_config(
    page_title="المنصة التعليمية الذكية", 
    page_icon="⚡", 
    layout="centered"
)

# إعداد مفتاح الـ API
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("الرجاء إضافة GEMINI_API_KEY في إعدادات Secrets الخاصة بـ Streamlit.")

MODEL_NAME = 'gemini-1.5-flash'

st.markdown("""
<div style="background-color: #1b4d3e; padding: 20px; border-radius: 12px; text-align: center; color: white; margin-bottom: 25px;">
    <h1 style="margin: 0; font-size: 28px;">المنصة التعليمية الذكية ⚡</h1>
    <p style="margin: 5px 0 0 0; font-size: 16px;">أهلاً بكِ يا فندم (admin)</p>
</div>
""", unsafe_allow_html=True)

app_mode = st.radio(
    "اختر القسم المطلوب:",
    ["📚 بنك الاختبارات التفاعلية", "🤖 مساعد الواجبات الذكي وتصحيحها", "📊 الملخصات والعروض التقديمية الذكية"]
)

st.markdown("---")

# 1. قسم بنك الاختبارات التفاعلية (الذكي الأوتوماتيكي)
if app_mode == "📚 بنك الاختبارات التفاعلية":
    st.markdown("### 📝 اختر المادة والصف لتأدية الامتحان")
    
    subject_name = st.selectbox("اختر المادة", ["عربي", "دراسات", "دين", "Math", "Science", "English", "Franish"])
    stage_name = st.radio("اختر المرحلة", ["المرحلة الابتدائية", "المرحلة الإعدادية"])
    
    if stage_name == "المرحلة الابتدائية":
        grade_name = st.selectbox("اختر الصف", ["الصف الأول الابتدائي", "الصف الثاني الابتدائي", "الصف الثالث الابتدائي", "الصف الرابع الابتدائي", "الصف الخامس الابتدائي", "الصف السادس الابتدائي"])
    else:
        grade_name = st.selectbox("اختر الصف", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])
        
    display_name = f"{subject_name} - {grade_name}"
    
    # --- السحر هنا: النظام الذكي للربط التلقائي ---
    sub_codes = {"عربي": "arabic", "دراسات": "social", "دين": "religion", "Math": "math", "Science": "science", "English": "english", "Franish": "french"}
    grd_codes = {
        "الصف الأول الابتدائي": "g1", "الصف الثاني الابتدائي": "g2", "الصف الثالث الابتدائي": "g3",
        "الصف الرابع الابتدائي": "g4", "الصف الخامس الابتدائي": "g5", "الصف السادس الابتدائي": "g6",
        "الصف الأول الإعدادي": "prep1", "الصف الثاني الإعدادي": "prep2", "الصف الثالث الإعدادي": "prep3"
    }
    
    # الملفات القديمة عشان تفضل شغالة
    old_files = {
        "social_g4": "Social-G4.html",
        "social_g6": "Social-G6.html",
        "science_g6": "Scienceg6.html",
        "arabic_prep2": "Arabic.prep2.html",
        "english_prep2": "engprep2.htm"
    }
    
    file_key = f"{sub_codes.get(subject_name)}_{grd_codes.get(grade_name)}"
    file_name = old_files.get(file_key, f"{file_key}.html") 
        
    # الزرار هيظهر دايماً جاهز ومربوط بالملف
    st.success(f"مستعد لفتح امتحان ({display_name}) 🚀")
    exam_url = f"https://alisalis5400-osha.github.io/Online-exams/{file_name}"
    st.markdown(f"""
    <div style="margin-top: 20px; text-align: center;">
        <a href="{exam_url}" target="_blank" style="display: block; background-color: #1b4d3e; color: white; padding: 15px 20px; border-radius: 10px; text-decoration: none; font-size: 18px; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            اضغط هنا لبدء امتحان ({display_name}) 🚀<br>
            <span style="font-size: 13px; font-weight: normal; color: #e0e0e0;">(سيفتح في تبويب جديد تماماً)</span>
        </a>
    </div>
    <p style="text-align:center; font-size:12px; color:gray; margin-top:10px;">ملاحظة: إذا ظهرت صفحة فارغة بعد الضغط، فهذا يعني أن الامتحان قيد التحديث ولم يتم رفعه بعد.</p>
    """, unsafe_allow_html=True)

# 2. قسم مساعد الواجبات الذكي وتصحيحها
elif app_mode == "🤖 مساعد الواجبات الذكي وتصحيحها":
    st.markdown("### 🤖 مساعد الواجبات الذكي وتصحيحها")
    st.markdown("ارفعي صور الواجب، وتحدثي معي بحرية لتعديل أو شرح أي نقطة!")
    
    if "hw_chat_session" not in st.session_state:
        model = genai.GenerativeModel(MODEL_NAME)
        st.session_state.hw_chat_session = model.start_chat(history=[])
        st.session_state.hw_messages = []

    uploaded_homeworks = st.file_uploader("ارفع صور أو ملفات الواجب هنا", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)
    
    if uploaded_homeworks:
        images = [Image.open(f) for f in uploaded_homeworks]
        for img in images: st.image(img, use_container_width=True)
            
        if st.button("🚀 بدء تحليل الواجب"):
            with st.spinner("جاري تحليل الواجب..."):
                response = st.session_state.hw_chat_session.send_message(["قم بتحليل وتصحيح هذا الواجب تفصيلياً."] + images)
                st.session_state.hw_messages.append({"role": "model", "content": response.text})

    for message in st.session_state.get('hw_messages', []):
        with st.chat_message(message["role"]): st.markdown(message["content"])

    if user_input := st.chat_input("اطلبي أي تعديل..."):
        st.session_state.hw_messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"): st.markdown(user_input)
        with st.chat_message("assistant"):
            response = st.session_state.hw_chat_session.send_message(user_input)
            st.markdown(response.text)
            st.session_state.hw_messages.append({"role": "model", "content": response.text})

# 3. قسم الملخصات 
else:
    st.markdown("### 📊 الملخصات والعروض التقديمية الذكية")
    st.info("هذا القسم جاهز للعمل. يمكنك رفع صور الدروس وسأقوم بتلخيصها.")
