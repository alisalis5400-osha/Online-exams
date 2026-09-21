import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(
    page_title="المنصة التعليمية الذكية",
    page_icon="⚡",
    layout="centered"
)

# تهيئة مفتاح الـ Gemini API من أمان Streamlit Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    # بديل مؤقت في حال لم يتم إدخال المفتاح في الـ Secrets بعد
    # يفضل دائماً وضعه في st.secrets لحماية مفتاحك
    pass

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

# قائمة المواد المحدثة
subjects_list = [
    "اللغة العربية", 
    "الدراسات الاجتماعية", 
    "التربية الدينية", 
    "Math", 
    "Science", 
    "اللغة الإنجليزية", 
    "اللغة الفرنسية"
]

# 1. قسم بنك الاختبارات التفاعلية
if app_mode == "📚 بنك الاختبارات التفاعلية":
    st.markdown("### 📝 اختر المادة والصف لتأدية الامتحان")
    
    subject_name = st.selectbox(
        "اختر المادة",
        subjects_list,
        key="exam_subject"
    )
    
    stage_name = st.radio(
        "اختر المرحلة",
        ["المرحلة الابتدائية", "المرحلة الإعدادية"],
        key="exam_stage"
    )
    
    if stage_name == "المرحلة الابتدائية":
        grade_name = st.selectbox(
            "اختر الصف", 
            ["الصف الأول الابتدائي", "الصف الثاني الابتدائي", "الصف الثالث الابتدائي", "الصف الرابع الابتدائي", "الصف الخامس الابتدائي", "الصف السادس الابتدائي"], 
            key="exam_grade_p"
        )
    else:
        grade_name = st.selectbox(
            "اختر الصف", 
            ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"], 
            key="exam_grade_prep"
        )
        
    file_name = ""
    display_name = f"{subject_name} - {grade_name}"
    
    # ربط المواد بالملفات
    if subject_name == "الدراسات الاجتماعية" and grade_name == "الصف الرابع الابتدائي":
        file_name = "Social-G4.html"
    elif subject_name == "الدراسات الاجتماعية" and grade_name == "الصف السادس الابتدائي":
        file_name = "Social-G6.html"
    elif subject_name == "اللغة العربية" and grade_name == "الصف الثاني الإعدادي":
        file_name = "Arabic.prep2.html"
    elif subject_name == "اللغة الإنجليزية" and grade_name == "الصف الثاني الإعدادي":
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
        st.warning("عذراً، الامتحان غير متوفر لهذه المادة/الصف حالياً ⚠️")

# 2. قسم مساعد الواجبات الذكي وتصحيحها
elif app_mode == "🤖 مساعد الواجبات الذكي وتصحيحها":
    st.markdown("### 🤖 مساعد الواجبات الذكي وتصحيحها")
    st.markdown("قم برفع صور الواجب أو ملفات الـ PDF المتعددة، وسأقوم بتحليلها وتصحيحها خطوة بخطوة للأولاد! 💡")
    
    uploaded_homeworks = st.file_uploader(
        "ارفعي صور أو ملفات الواجب هنا (يمكنك اختيار أكثر من ملف/صورة معاً)", 
        type=["jpg", "jpeg", "png", "pdf"],
        accept_multiple_files=True
    )
    
    if uploaded_homeworks:
        st.success(f"تم استلام عدد ({len(uploaded_homeworks)}) ملف/صورة للواجب بنجاح! ✅")
        for hw in uploaded_homeworks:
            if hw.type.startswith("image/"):
                st.image(hw, caption=f"صورة الواجب: {hw.name}", use_container_width=True)
                
        if st.button("بدء تحليل وتصحيح الواجبات 🔍", key="btn_correct_hw"):
            with st.spinner("جاري تحليل الواجب وتصحيحه عبر الذكاء الاصطناعي..."):
                try:
                    # تجهيز الملفات لـ Gemini
                    gemini_inputs = []
                    for hw in uploaded_homeworks:
                        if hw.type.startswith("image/"):
                            gemini_inputs.append(Image.open(hw))
                    
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = "أنت معلم متميز ومساعد ذكي للواجبات المدرسية. قم بتحليل صور الواجب المرفقة، وتصحيح الأخطاء، وشرح الخطوات خطوة بخطوة بأسلوب مبسط ومناسب للأطفال."
                    
                    if gemini_inputs:
                        response = model.generate_content([prompt] + gemini_inputs)
                        st.markdown("---")
                        st.markdown("### 📋 تقرير التصحيح والتحليل الذكي:")
                        st.markdown(response.text)
                    else:
                        st.warning("الرجاء التأكد من رفع صور صحيحة للواجب.")
                except Exception as e:
                    st.error(fحدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")

# 3. قسم الملخصات والعروض التقديمية الذكية (مدعوم بالفعلي عبر Gemini وبمساحة المناقشة)
else:
    st.markdown("### 📊 الملخصات والعروض التقديمية الذكية")
    st.markdown("اختر المادة والصف، ثم ارفع صفحة أو صفحات الدرس كاملة لعمل ملخص مترابط من داخل المنهج فقط 📑")
    
    sum_subject_name = st.selectbox(
        "اختر المادة",
        subjects_list,
        key="sum_subject"
    )
    
    sum_stage_name = st.radio(
        "اختر المرحلة",
        ["المرحلة الابتدائية", "المرحلة الإعدادية"],
        key="sum_stage"
    )
    
    if sum_stage_name == "المرحلة الابتدائية":
        sum_grade_name = st.selectbox(
            "اختر الصف", 
            ["الصف الأول الابتدائي", "الصف الثاني الابتدائي", "الصف الثالث الابتدائي", "الصف الرابع الابتدائي", "الصف الخامس الابتدائي", "الصف السادس الابتدائي"], 
            key="sum_grade_p"
        )
    else:
        sum_grade_name = st.selectbox(
            "اختر الصف", 
            ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"], 
            key="sum_grade_prep"
        )
        
    st.markdown("---")
    
    uploaded_lesson_files = st.file_uploader(
        "ارفعي صفحات الدرس كاملة (يمكنك اختيار أكثر من صورة أو ملف PDF معاً)", 
        type=["pdf", "txt", "png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="sum_files"
    )
    
    if uploaded_lesson_files:
        st.success(f"تم رفع عدد ({len(uploaded_lesson_files)}) ملف/صفحة للدرس الخاصة بـ ({sum_subject_name} - {sum_grade_name}) بنجاح! ✅")
        
        # معاينة مصغرة للملفات المرفوعة
        for file in uploaded_lesson_files:
            if file.type.startswith("image/"):
                st.image(file, caption=file.name, width=150)
            else:
                st.write(f"📄 {file.name}")
        
        if st.button("تنفيذ التلخيص الشامل بدقة 💡", key="btn_summarize"):
            with st.spinner("جاري قراءة وتلخيص محتوى الدرس بدقة عبر الذكاء الاصطناعي..."):
                try:
                    gemini_files = []
                    for file in uploaded_lesson_files:
                        if file.type.startswith("image/"):
                            gemini_files.append(Image.open(file))
                    
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"""
                    أنت معلم خبير ومختص بمنهج وزارة التربية والتعليم لـ ({sum_subject_name}) لـ ({sum_grade_name}).
                    مهمتك هي قراءة محتوى الملفات المرفقة الخاصة بالدرس حصرياً والتزام المنهج بدقة تامة دون إدخال أي معلومات خارجية.
                    قم بعمل:
                    1. ملخص شامل ومترابط يغطي الأفكار الرئيسية للدرس.
                    2. أهم النقاط والقواعد أو التواريخ والمفاهيم لتسهيل المراجعة المبسطة للأولاد قبل الامتحانات.
                    """
                    
                    if gemini_files:
                        response = model.generate_content([prompt] + gemini_files)
                        # حفظ التلخيص الناتج في الذاكرة المؤقتة لنتمكن من مناقشته لاحقاً
                        st.session_state['generated_summary'] = response.text
                        st.session_state['summary_generated'] = True
                    else:
                        st.warning("يرجى التأكد من رفع صور صحيحة للدرس.")
                except Exception as e:
                    st.error(f"حدث خطأ أثناء توليد التلخيص: {e}")

        # عرض التلخيص ومساحة المناقشة والتعديل الفوري
        if st.session_state.get('summary_generated', False):
            st.markdown("---")
            st.markdown(f"### 📝 الملخص الشامل لمنهج ({sum_subject_name} - {sum_grade_name}):")
            st.markdown(st.session_state.get('generated_summary', ''))
            
            st.markdown("---")
            st.markdown("### 💬 مساحة المناقشة والتعديل على الملخص:")
            st.markdown("هل ترغبين في تعديل أو إضافة شيء بالتلخيص؟ اكتبي طلبك (مثال: اختصري أكثر، حوليه لسؤال وجواب، ركزي على نقاط معينة) وسأقوم بتعديله فوراً.")
            
            user_feedback = st.text_input("اكتبي طلبك أو التعديل المطلوب على الملخص هنا:", key="feedback_input")
            if st.button("تحديث التلخيص حسب التعديل المطلوب 🔄", key="btn_update_summary"):
                if user_feedback.strip():
                    with st.spinner("جاري تعديل التلخيص بناءً على طلبك..."):
                        try:
                            model = genai.GenerativeModel('gemini-1.5-flash')
                            chat_prompt = f"""
                            بناءً على التلخيص السابق والمحتوى المرفق لدرس ({sum_subject_name} - {sum_grade_name})، 
                            الطلب الجديد أو التعديل الذي تريده المستخدم هو: "{user_feedback}".
                            قم بتعديل الملخص أو الرد على هذا الطلب بدقة وموضوعية تامة.
                            """
                            chat_response = model.generate_content(chat_prompt)
                            st.markdown("---")
                            st.markdown("### ✨ الملخص بعد التعديل:")
                            st.markdown(chat_response.text)
                        except Exception as e:
                            st.error(f"حدث خطأ: {e}")
                else:
                    st.warning("الرجاء كتابة التعديل المطلوب أولاً.")
    else:
        st.session_state['summary_generated'] = False
        st.info("الرجاء رفع ملفات أو صور الدرس المطلوبة للبدء في تلخيصها ومناقشتها.")
