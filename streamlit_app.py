import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة وتكوينها
st.set_page_config(
    page_title="المنصة التعليمية الذكية", 
    page_icon="⚡", 
    layout="centered"
)

# إعداد مفتاح الـ API بأمان من الـ Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("الرجاء إضافة GEMINI_API_KEY في إعدادات Secrets الخاصة بـ Streamlit.")

MODEL_NAME = 'gemini-1.5-flash'

# تصميم العنوان الرئيسي للمنصة
st.markdown("""
<div style="background-color: #1b4d3e; padding: 20px; border-radius: 12px; text-align: center; color: white; margin-bottom: 25px;">
    <h1 style="margin: 0; font-size: 28px;">المنصة التعليمية الذكية ⚡</h1>
    <p style="margin: 5px 0 0 0; font-size: 16px;">أهلاً بكِ يا فندم (admin)</p>
</div>
""", unsafe_allow_html=True)

# قائمة التنقل بين أقسام المنصة
app_mode = st.radio(
    "اختر القسم المطلوب:",
    [
        "📚 بنك الاختبارات التفاعلية",
        "🤖 مساعد الواجبات الذكي وتصحيحها",
        "📊 الملخصات والعروض التقديمية الذكية"
    ]
)

st.markdown("---")

# 1. قسم بنك الاختبارات التفاعلية
if app_mode == "📚 بنك الاختبارات التفاعلية":
    st.markdown("### 📝 اختر المادة والصف لتأدية الامتحان")
    
    subject_name = st.selectbox(
        "اختر المادة",
        ["عربي", "دراسات", "دين", "Math", "Science", "English", "Franish"]
    )
    
    stage_name = st.radio(
        "اختر المرحلة",
        ["المرحلة الابتدائية", "المرحلة الإعدادية"]
    )
    
    if stage_name == "المرحلة الابتدائية":
        grade_name = st.selectbox("اختر الصف", ["الصف الأول الابتدائي", "الصف الثاني الابتدائي", "الصف الثالث الابتدائي", "الصف الرابع الابتدائي", "الصف الخامس الابتدائي", "الصف السادس الابتدائي"])
    else:
        grade_name = st.selectbox("اختر الصف", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])
        
    file_name = ""
    display_name = f"{subject_name} - {grade_name}"
    
    if subject_name == "دراسات" and grade_name == "الصف الرابع الابتدائي":
        file_name = "Social-G4.html"
    elif subject_name == "دراسات" and grade_name == "الصف السادس الابتدائي":
        file_name = "Social-G6.html"
    elif subject_name == "عربي" and grade_name == "الصف الثاني الإعدادي":
        file_name = "Arabic.prep2.html"
    elif subject_name == "English" and grade_name == "الصف الثاني الإعدادي":
        file_name = "engprep2.htm"
        
    if file_name:
        st.success(f"تم تجهيز مسار امتحان ({display_name}) بنجاح ✅")
        exam_url = f"https://alisalis5400-osha.github.io/Online-exams/{file_name}"
        st.markdown(f"""
        <div style="margin-top: 20px; text-align: center;">
            <a href="{exam_url}" target="_blank" style="display: block; background-color: #1b4d3e; color: white; padding: 15px 20px; border-radius: 10px; text-decoration: none; font-size: 18px; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                اضغط هنا لبدء امتحان ({display_name}) 🚀<br>
                <span style="font-size: 13px; font-weight: normal; color: #e0e0e0;">(سيفتح في تبويب جديد تماماً)</span>
            </a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("عذراً، الامتحان التفاعلي قيد التحديث لهذه المادة حالياً ⚠️ يمكنك استخدام أقسام التحليل والتلخيص بالأسفل.")

# 2. قسم مساعد الواجبات الذكي وتصحيحها (بذاكرة محادثة مستمرة)
elif app_mode == "🤖 مساعد الواجبات الذكي وتصحيحها":
    st.markdown("### 🤖 مساعد الواجبات الذكي وتصحيحها")
    st.markdown("ارفعي صور الواجب، وتحدثي معي بحرية لتعديل أو شرح أي نقطة بناءً على الصور المرفوعة! 💡")
    
    if "hw_chat_session" not in st.session_state:
        model = genai.GenerativeModel(MODEL_NAME)
        st.session_state.hw_chat_session = model.start_chat(history=[])
    
    if "hw_messages" not in st.session_state:
        st.session_state.hw_messages = []

    uploaded_homeworks = st.file_uploader(
        "ارفع صور أو ملفات الواجب هنا (JPG, PNG, PDF)", 
        type=["jpg", "jpeg", "png", "pdf"], 
        accept_multiple_files=True,
        key="hw_uploader"
    )
    
    if uploaded_homeworks:
        images = [Image.open(f) for f in uploaded_homeworks]
        for img in images:
            st.image(img, use_container_width=True)
            
        if st.button("🚀 بدء تحليل الواجب"):
            with st.spinner("جاري تحليل الواجب..."):
                prompt = "أنت معلم خبير. قم بقراءة وتحليل هذه الصور الخاصة بالواجب المدرسي وتقديم تصحيح تفصيلي وخطوات واضحة."
                response = st.session_state.hw_chat_session.send_message([prompt] + images)
                st.session_state.hw_messages.append({"role": "user", "content": "[تم إرفاق صور الواجب للتحليل]"})
                st.session_state.hw_messages.append({"role": "model", "content": response.text})

    # عرض تاريخ المحادثة للواجبات
    for message in st.session_state.hw_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # صندوق محادثة مستمر
    if user_input := st.chat_input("اطلبي أي تعديل، ترجمة، أو توضيح إضافي للواجب..."):
        st.session_state.hw_messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        with st.chat_message("assistant"):
            with st.spinner("جاري الرد..."):
                response = st.session_state.hw_chat_session.send_message(user_input)
                st.markdown(response.text)
                st.session_state.hw_messages.append({"role": "model", "content": response.text})

# 3. قسم الملخصات والعروض التقديمية (بذاكرة محادثة مستمرة ومرتبة بالمواد والصفوف)
else:
    st.markdown("### 📊 الملخصات والعروض التقديمية الذكية")
    st.markdown("استعرضي هنا أدوات تلخيص الدروس مع إمكانية التعديل والدردشة المستمرة حول نفس محتوى الصور أو النصوص المرفوعة. 📑")
    
    sum_subject = st.selectbox("مادة التلخيص:", ["عربي", "دراسات", "دين", "Math", "Science", "English", "Franish"], key="sum_sub")
    sum_grade = st.selectbox("الصف الدراسي:", ["الصف الأول الابتدائي", "الصف الثاني الابتدائي", "الصف الثالث الابتدائي", "الصف الرابع الابتدائي", "الصف الخامس الابتدائي", "الصف السادس الابتدائي", "الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"], key="sum_grd")
    
    if "sum_chat_session" not in st.session_state:
        model = genai.GenerativeModel(MODEL_NAME)
        st.session_state.sum_chat_session = model.start_chat(history=[])
        st.session_state.sum_messages = []

    input_method = st.radio("طريقة إدخال المحتوى للتلخيص:", ["إدخال نص الدرس", "رفع صفحات أو ملفات (صور/PDF متعددة)"])
    
    lesson_text = ""
    uploaded_lessons = None
    
    if input_method == "إدخال نص الدرس":
        lesson_text = st.text_area("أدخلي نص الدرس أو الموضوع بأي لغة:")
    else:
        uploaded_lessons = st.file_uploader(
            "ارفعي صفحات الدرس (صور أو ملفات متعددة)", 
            type=["jpg", "jpeg", "png", "pdf"], 
            accept_multiple_files=True,
            key="sum_uploader"
        )
        if uploaded_lessons:
            for f in uploaded_lessons:
                st.image(f, use_container_width=True)
                
    if st.button("تنفيذ التلخيص الشامل وحفظه 💡"):
        with st.spinner("جاري قراءة وتلخيص المحتوى بكل دقة..."):
            try:
                if input_method == "إدخال نص الدرس" and lesson_text.strip():
                    prompt = f"قم بتلخيص النص التالي لمادة {sum_subject} ({sum_grade}) بأسلوب منظم وواضح في شكل نقاط رئيسية مبسطة:\n\n{lesson_text}"
                    response = st.session_state.sum_chat_session.send_message(prompt)
                    st.session_state.sum_messages.append({"role": "user", "content": f"تلخيص النص: {lesson_text[:50]}..."})
                    st.session_state.sum_messages.append({"role": "model", "content": response.text})
                    
                elif input_method == "رفع صفحات أو ملفات (صور/PDF متعددة)" and uploaded_lessons:
                    lesson_imgs = [Image.open(f) for f in uploaded_lessons]
                    prompt = f"قم بقراءة هذه الصفحات المرفوعة بعناية لمادة {sum_subject} ({sum_grade}) وقدم تلخيصاً شاملاً ومنظماً يوضح الأفكار والمفاهيم الأساسية."
                    response = st.session_state.sum_chat_session.send_message([prompt] + lesson_imgs)
                    st.session_state.sum_messages.append({"role": "user", "content": "[تم إرفاق صور الصفحات للتلخيص]"})
                    st.session_state.sum_messages.append({"role": "model", "content": response.text})
                else:
                    st.warning("الرجاء إدخال النص أو رفع الملفات أولاً.")
            except Exception as e:
                st.error(f"حدث خطأ أثناء التلخيص: {e}")

    # عرض تاريخ محادثة الملخصات
    for message in st.session_state.get('sum_messages', []):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # صندوق محادثة مستمر للتلخيصات
    if sum_input := st.chat_input("اطلبي تعديل الملخص، ترجمته، أو إضافة أمثلة..."):
        if "sum_chat_session" in st.session_state:
            st.session_state.sum_messages.append({"role": "user", "content": sum_input})
            with st.chat_message("user"):
                st.markdown(sum_input)
                
            with st.chat_message("assistant"):
                with st.spinner("جاري تعديل الملخص حسب طلبك..."):
                    response = st.session_state.sum_chat_session.send_message(sum_input)
                    st.markdown(response.text)
                    st.session_state.sum_messages.append({"role": "model", "content": response.text})
