import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة وتكوينها
st.set_page_config(
    page_title="منصة المناهج التعليمية الذكية", 
    page_icon="📚", 
    layout="wide"
)

# إعداد مفتاح الـ API بأمان من الـ Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("الرجاء إضافة GEMINI_API_KEY في إعدادات Secrets الخاصة بـ Streamlit.")

# عنوان المنصة والترحيب
st.title("📚 منصة المناهج التعليمية الذكية - تلخيص ومراجعة")
st.write("أهلاً بكِ! منصتك المتكاملة لمساعدة أولادك في تلخيص الدروس ومراجعة المناهج الدراسية بدقة عبر الذكاء الاصطناعي.")

# القائمة الجانبية لتحديد المرحلة الدراسية والمادة
st.sidebar.header("🎯 إعدادات الدرس")
stage = st.sidebar.selectbox("اختر المرحلة الدراسية:", ["المرحلة الابتدائية", "المرحلة الإعدادية", "المرحلة الثانوية"])
subject = st.sidebar.selectbox("اختر المادة:", ["Science", "الدراسات الاجتماعية", "اللغة العربية", "اللغة الإنجليزية", "الرياضيات"])

# اختيار النموذج المعتمد
MODEL_NAME = 'gemini-1.5-flash'

# قسم رفع الملفات أو صور الدروس
st.markdown("---")
st.subheader("📁 رفع محتوى الدرس أو صفحة الكتاب")
uploaded_file = st.file_uploader("اختر صورة صفحة الدرس (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption=f"صورة الدرس المرفوعة ({subject} - {stage})", use_column_width=True)
    
    # خيارات التفاعل مع المحتوى
    action = st.radio("ما الذي ترغبين في تنفيذه لهذا الدرس؟", ["تنفيذ التلخيص الشامل بدقة", "استخراج أهم الأسئلة والتمارين", "شرح مبسط وموجه للطلاب"])
    
    if st.button("🚀 ابدأ المعالجة عبر الذكاء الاصطناعي"):
        with st.spinner("جاري قراءة وتحليل محتوى الدرس بدقة..."):
            try:
                model = genai.GenerativeModel(MODEL_NAME)
                
                # صياغة الموجه بناءً على اختيار المستخدمة
                if action == "تنفيذ التلخيص الشامل بدقة":
                    prompt = f"أنت معلم خبير في المنهج المصري لمادة {subject} لـ {stage}. قم بقراءة هذه الصورة وقدم تلخيصاً شاملاً ودقيقاً يوضح الأفكار الرئيسية والمفاهيم العلمية بأسلوب مبسط ومناسب للطلاب."
                elif action == "استخراج أهم الأسئلة والتمارين":
                    prompt = f"بصفتك معلماً لمادة {subject} لـ {stage}، استخرج من هذه الصورة أهم الأسئلة والتدريبات المتوقعة في الامتحانات مع ذكر الإجابات النموذجية."
                else:
                    prompt = f"قم بشرح محتوى هذه الصفحة لمادة {subject} ({stage}) بطريقة شيقة ومبسطة جداً ومناسبة للفهم السريع."

                response = model.generate_content([prompt, image])
                
                st.success("تمت المعالجة بنجاح! إليك النتيجة:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء المعالجة: {e}")

# قسم المحادثة والمناقشة الحرة حول الدرس
st.markdown("---")
st.subheader("💬 مساحة المناقشة الذكية للدرس")
user_question = st.text_input("هل لديكِ أي استفسار إضافي أو سؤال ترغبين في طرحه حول الدرس؟")
if user_question:
    with st.spinner("جاري صياغة الإجابة..."):
        try:
            model = genai.GenerativeModel(MODEL_NAME)
            chat_response = model.generate_content(f"أنت مساعد تعليمي للمناهج الدراسية. أجب عن هذا السؤال بدقة واختصار: {user_question}")
            st.write(chat_response.text)
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
