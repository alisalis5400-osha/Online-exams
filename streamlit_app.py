import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="منصة المناهج التعليمية", page_icon="📚", layout="wide")

# إعداد مفتاح الـ API من Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("الرجاء إضافة GEMINI_API_KEY في إعدادات Secrets الخاصة بـ Streamlit.")

# واجهة التطبيق
st.title("📚 منصة تلخيص ومراجعة المناهج التعليمية")
st.write("أهلاً بكِ! قومي برفع صفحة الدرس أو الكتاب للبدء في التلخيص الشامل وحل التمارين بدقة.")

# اختيار النموذج المحدث
MODEL_NAME = 'gemini-2.5-flash'

# رفع الملفات أو الصور
uploaded_file = st.file_uploader("اختر صورة أو ملف الدرس (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة المرفوعة للدرس", use_column_width=True)
    
    if st.button("💡 تنفيذ التلخيص الشامل بدقة"):
        with st.spinner("جاري قراءة وتلخيص محتوى الدرس بدقة عبر الذكاء الاصطناعي..."):
            try:
                # استخدام النموذج المحدث
                model = genai.GenerativeModel(MODEL_NAME)
                prompt = (
                    "أنت معلم متخصص في المناهج التعليمية. قم بقراءة هذه الصورة الخاصة بالدرس "
                    "وقدم تلخيصاً شاملاً ودقيقاً باللغة العربية، يوضح الأفكار الرئيسية، المفاهيم العلمية، "
                    "والنقاط الهامة بطريقة مبسطة ومناسبة للطلاب."
                )
                response = model.generate_content([prompt, image])
                
                st.success("تم التلخيص بنجاح! ةإليك التفاصيل:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء توليد التلخيص: {e}")
