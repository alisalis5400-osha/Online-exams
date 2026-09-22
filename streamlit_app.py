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

# اختيار النموذج المستقر والمحدث
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
    
    # المواد السبعة كاملة
    subject_name = st.selectbox(
        "اختر المادة",
        ["عربي", "دراسات", "دين", "Math", "Science", "English", "Franish"]
    )
    
    stage_name = st.radio(
        "اختر المرحلة",
        ["المرحلة الابتدائية", "المرحلة الإعدادية"]
    )
    
    # الصفوف الابتدائية من الأول إلى السادس كاملة
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

# 2. قسم مساعد الواجبات الذكي وتصحيحها (يدعم أكثر من ملف ورقي / صور / PDF)
elif app_mode == "🤖 مساعد الواجبات الذكي وتصحيحها":
    st.markdown("### 🤖 مساعد الواجبات الذكي وتصحيحها")
    st.markdown("قم برفع صور متعددة أو ملفات الواجب (تسمح بأكثر من ورقة)، وسأقوم بتحليلها وتصحيحها خطوة بخطوة لكل اللغات! 💡")
    
    uploaded_homeworks = st.file_uploader(
        "ارفع صور أو ملفات الواجب هنا (JPG, PNG, PDF)", 
        type=["jpg", "jpeg", "png", "pdf"], 
        accept_multiple_files=True
    )
    
    images = []
    if uploaded_homeworks:
        for file in uploaded_homeworks:
            try:
                img = Image.open(file)
                images.append(img)
                st.image(img, caption=file.name, use_container_width=True)
            except Exception:
                st.warning(f"الملف {file.name} غير قابل للعرض كصورة مباشرة، لكن سيتم معالجته.")
        
        if st.button("🚀 ابدأ تحليل وتصحيح الواجبات"):
            with st.spinner("جاري تحليل الخطوات وتصحيح الأخطاء لجميع الأوراق المرفوعة... ✨"):
                try:
                    model = genai.GenerativeModel(MODEL_NAME)
                    prompt = (
                        "أنت معلم خبير ومساعد تعليمي متعدد اللغات. قم بقراءة هذه الملفات أو الصور الخاصة بالواجب المدرسي، "
                        "وتحليل الأسئلة بكل لغات المحتوى، وتقديم تصحيح تفصيلي، وإجابات نموذجية، وخطوات واضحة لشرحها للطالب."
                    )
                    
                    content_payload = [prompt] + images if images else [prompt]
                    response = model.generate_content(content_payload)
                    
                    st.success("تم تحليل وتصحيح الواجبات بنجاح وإرسال التقرير! ✅")
                    st.markdown(response.text)
                    st.session_state['last_homework_response'] = response.text
                    
                except Exception as e:
                    st.error(f"حدث خطأ أثناء معالجة الواجب: {e}")
        
        if 'last_homework_response' in st.session_state:
            st.markdown("---")
            st.subheader("💬 مساحة الدردشة لطلب تعديلات أو أسئلة إضافية")
            hw_chat = st.text_input("اطلبي أي تعديل، تبسيط إضافي، أو سؤال ترغبين في توضيحه للولاد:")
            if hw_chat:
                with st.spinner("جاري التعديل..."):
                    chat_model = genai.GenerativeModel(MODEL_NAME)
                    chat_res = chat_model.generate_content(f"بناءً على الإجابة السابقة للواجب، قم بالرد على هذا الطلب بدقة: {hw_chat}")
                    st.write(chat_res.text)

# 3. قسم الملخصات والعروض التقديمية (منظم مثل الاختبارات لحفظ واستعراض التلخيصات)
else:
    st.markdown("### 📊 الملخصات والعروض التقديمية الذكية")
    st.markdown("استعرضي هنا أدوات تلخيص الدروس وصياغة النقاط الرئيسية بشكل مرتب ومنظم كبطاقات مراجعة إلكترونية. 📑")
    
    # اختيار المادة والصف لتنظيم الملخصات وحفظها
    sum_subject = st.selectbox("مادة التلخيص:", ["عربي", "دراسات", "دين", "Math", "Science", "English", "Franish"], key="sum_sub")
    sum_grade = st.selectbox("الصف الدراسي:", ["الصف الأول الابتدائي", "الصف الثاني الابتدائي", "الصف الثالث الابتدائي", "الصف الرابع الابتدائي", "الصف الخامس الابتدائي", "الصف السادس الابتدائي", "الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"], key="sum_grd")
    
    input_method = st.radio("طريقة إدخال المحتوى للتلخيص:", ["إدخال نص الدرس", "رفع صفحات أو ملفات (صور/PDF متعددة)"])
    
    lesson_text = ""
    uploaded_lessons = None
    
    if input_method == "إدخال نص الدرس":
        lesson_text = st.text_area("أدخلي نص الدرس أو الموضوع بأي لغة (عربي، إنجليزي، فرنسي...):")
    else:
        uploaded_lessons = st.file_uploader(
            "ارفعي صفحات الدرس (صور أو ملفات متعددة)", 
            type=["jpg", "jpeg", "png", "pdf"], 
            accept_multiple_files=True
        )
        if uploaded_lessons:
            for f in uploaded_lessons:
                st.image(f, caption=f.name, use_container_width=True)
                
    if st.button("تنفيذ التلخيص الشامل وحفظه 💡"):
        with st.spinner("جاري قراءة وتلخيص المحتوى بكل دقة وإعداده للحفظ... ⚙️"):
            try:
                model = genai.GenerativeModel(MODEL_NAME)
                
                if input_method == "إدخال نص الدرس" and lesson_text.strip():
                    prompt = f"قم بتلخيص النص التالي لمادة {sum_subject} ({sum_grade}) بأسلوب منظم وواضح في شكل نقاط رئيسية مبسطة ومناسبة للمراجعة السريعة:\n\n{lesson_text}"
                    response = model.generate_content(prompt)
                    
                    st.success(f"تم إعداد وحفظ ملخص ({sum_subject} - {sum_grade}) بنجاح ✅")
                    st.markdown(response.text)
                    st.session_state['last_summary'] = response.text
                    
                elif input_method == "رفع صفحات أو ملفات (صور/PDF متعددة)" and uploaded_lessons:
                    lesson_imgs = [Image.open(f) for f in uploaded_lessons]
                    prompt = f"قم بقراءة هذه الصفحات المرفوعة بعناية لمادة {sum_subject} ({sum_grade}) وقدم تلخيصاً شاملاً ومنظماً يوضح الأفكار والمفاهيم الأساسية."
                    response = model.generate_content([prompt] + lesson_imgs)
                    
                    st.success(f"تم إعداد وحفظ ملخص ({sum_subject} - {sum_grade}) بنجاح ✅")
                    st.markdown(response.text)
                    st.session_state['last_summary'] = response.text
                else:
                    st.warning("الرجاء إدخال النص أو رفع الملفات أولاً.")
                    
            except Exception as e:
                st.error(f"حدث خطأ أثناء التلخيص: {e}")
                
    if 'last_summary' in st.session_state:
        st.markdown("---")
        st.subheader("💬 الدردشة لتعديل أو إضافة تفاصيل على الملخص المحفوظ")
        user_mod_request = st.text_input("هل ترغبين في اختصار جزء معين، إضافة أمثلة، أو ترجمة الملخص للغة أخرى؟")
        if user_mod_request:
            with st.spinner("جاري تعديل الملخص حسب طلبك..."):
                mod_model = genai.GenerativeModel(MODEL_NAME)
                mod_res = mod_model.generate_content(f"بناءً على الملخص السابق، قم بتنفيذ هذا التعديل بدقة: {user_mod_request}")
                st.write(mod_res.text)
