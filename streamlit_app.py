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

# اختيار النموذج المعتمد لضمان عدم ظهور أخطاء
MODEL_NAME = 'gemini-1.5-flash'

# عنوان المنصة والترحيب
st.title("📚 منصة المناهج التعليمية الذكية - تلخيص ومراجعة")
st.write("أهلاً بكِ! منصتك المتكاملة لمتابعة مناهج أولادك في المراحل (الابتدائية، الإعدادية، والثانوية) وتلخيص الدروس ومراجعتها بدقة عبر الذكاء الاصطناعي.")

# القائمة الجانبية المتقدمة لإعدادات الدرس والمراحل الدراسية
st.sidebar.header("🎯 إعدادات الدرس والمادة")
stage = st.sidebar.selectbox("اختر المرحلة الدراسية:", ["المرحلة الابتدائية", "المرحلة الإعدادية", "المرحلة الثانوية"])
subject = st.sidebar.selectbox("اختر المادة:", [
    "Science", 
    "الدراسات الاجتماعية", 
    "اللغة العربية", 
    "اللغة الإنجليزية", 
    "الرياضيات", 
    "البرمجة والتكنولوجيا", 
    "القيم والأخلاق"
])

# قسم رفع الملفات أو صور الدروس
st.markdown("---")
st.subheader("📁 رفع محتوى الدرس أو صفحة الكتاب")
uploaded_file = st.file_uploader("اختر صورة أو ملف صفحة الدرس (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption=f"صورة الدرس المرفوعة ({subject} - {stage})", use_column_width=True)
    
    # اختيار الوظيفة المطلوبة للمحتوى المرفوع
    action = st.radio(
        "ما الذي ترغبين في تنفيذه لهذا المحتوى؟", 
        [
            "💡 تنفيذ التلخيص الشامل بدقة", 
            "📝 استخراج أهم الأسئلة والتمارين", 
            "🎮 اقتراح لعبة تعليمية تفاعلية للدرس", 
            "🎵 صياغة أغنية أو نشيد بسيط لحفظ القواعد/الكلمات"
        ]
    )
    
    if st.button("🚀 ابدأ المعالجة عبر الذكاء الاصطناعي"):
        with st.spinner("جاري قراءة وتحليل محتوى الدرس بدقة الذكاء الاصطناعي..."):
            try:
                model = genai.GenerativeModel(MODEL_NAME)
                
                # صياغة الموجه الذكي بناءً على طلبك
                if "التلخيص الشامل" in action:
                    prompt = f"أنت معلم خبير في المنهج المصري لمادة {subject} لـ {stage}. قم بقراءة هذه الصورة وقدم تلخيصاً شاملاً ودقيقاً يوضح الأفكار الرئيسية، المفاهيم العلمية، والكلمات الهامة بأسلوب مبسط ومناسب للطلاب."
                elif "الأسئلة والتمارين" in action:
                    prompt = f"بصفتك معلماً لمادة {subject} لـ {stage}، استخرج من هذه الصورة أهم الأسئلة والتدريبات المتوقعة في الامتحانات مع ذكر الإجابات النموذجية."
                elif "لعبة تعليمية" in action:
                    prompt = f"ابتكر فكرة لعبة تعليمية تفاعلية ممتعة وبسيطة لمراجعة محتوى هذا الدرس في مادة {subject} لـ {stage} يمكن تطبيقها في الفصل أو المنزل."
                else:
                    prompt = f"قم بتأليف أغنية قصيرة أو نشيد بسيط وسهل حافظ للكلمات أو القواعد الموجودة في هذه الصفحة لمادة {subject} لـ {stage} لمساعدة الأطفال على حفظها بسهولة."

                response = model.generate_content([prompt, image])
                
                st.success("تمت المعالجة بنجاح! إليك النتيجة:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء المعالجة: {e}")

# قسم المحادثة والمناقشة الحرة حول المناهج والواجبات
st.markdown("---")
st.subheader("💬 مساحة المساعدة والمناقشة الذكية")
user_question = st.text_input("هل لديكِ أي استفسار إضافي، سؤال صعب في الواجب، أو تحتاجين لشرح نقطة معينة لأولادك؟")
if user_question:
    with st.spinner("جاري صياغة الإجابة..."):
        try:
            model = genai.GenerativeModel(MODEL_NAME)
            chat_response = model.generate_content(
                f"أنت مساعد تعليمي متخصص في المناهج المصرية للمراحل (الابتدائية، الإعدادية، الثانوية). أجب عن السؤال التالي بدقة ووضوح وبأسلوب تربوي: {user_question}"
            )
            st.write(chat_response.text)
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
