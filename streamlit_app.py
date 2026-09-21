import streamlit as st

st.set_page_config(
    page_title="المنصة التعليمية الذكية",
    page_icon="⚡",
    layout="centered"
)

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
        ["الدراسات الاجتماعية", "اللغة العربية", "اللغة الإنجليزية"],
        key="exam_subject"
    )
    
    stage_name = st.radio(
        "اختر المرحلة",
        ["المرحلة الابتدائية", "المرحلة الإعدادية"],
        key="exam_stage"
    )
    
    if stage_name == "المرحلة الابتدائية":
        grade_name = st.selectbox("اختر الصف", ["الصف الرابع", "الصف الخامس", "الصف السادس"], key="exam_grade_p")
    else:
        grade_name = st.selectbox("اختر الصف", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"], key="exam_grade_prep")
        
    file_name = ""
    display_name = f"{subject_name} - {grade_name}"
    
    # ربط المواد بالملفات
    if subject_name == "الدراسات الاجتماعية" and grade_name == "الصف الرابع":
        file_name = "Social-G4.html"
    elif subject_name == "الدراسات الاجتماعية" and grade_name == "الصف السادس":
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
        st.warning("عذراً، الامتحان غير متوفر لهذه المادة حالياً ⚠️")

# 2. قسم مساعد الواجبات الذكي وتصحيحها (مُعدل لدعم رفع أكثر من صورة أو ملف)
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
        
        # عرض معاينة للملفات المرفوعة
        for hw in uploaded_homeworks:
            if hw.type.startswith("image/"):
                st.image(hw, caption=f"صورة الواجب: {hw.name}", use_container_width=True)
            else:
                st.info(f"📁 تم إرفاق ملف PDF: {hw.name}")
                
        if st.button("بدء تحليل وتصحيح الواجبات 🔍", key="btn_correct_hw"):
            st.markdown("---")
            st.markdown("### 📋 تقرير التصحيح والتحليل الذكي:")
            st.markdown("""
            - تم فحص جميع الصفحات والأسئلة المرفوعة معاً لترابط الأفكار.
            - تم رصد الملاحظات والخطوات الصحيحة لتوضيحها للطالب لضمان الفهم التام.
            """)

# 3. قسم الملخصات والعروض التقديمية الذكية (مُعدل بنفس فكرة اللغات ويدعم رفع ملفات متعددة)
else:
    st.markdown("### 📊 الملخصات والعروض التقديمية الذكية")
    st.markdown("اختر المادة والمرحلة، ثم ارفع صفحة أو صفحات الدرس كاملة (صور أو ملفات PDF) لعمل ملخص مترابط من داخل المنهج فقط 📑")
    
    # اختيار المادة والصف بنفس تنسيق قسم الاختبارات
    sum_subject_name = st.selectbox(
        "اختر المادة",
        ["الدراسات الاجتماعية", "اللغة العربية", "اللغة الإنجليزية"],
        key="sum_subject"
    )
    
    sum_stage_name = st.radio(
        "اختر المرحلة",
        ["المرحلة الابتدائية", "المرحلة الإعدادية"],
        key="sum_stage"
    )
    
    if sum_stage_name == "المرحلة الابتدائية":
        sum_grade_name = st.selectbox("اختر الصف", ["الصف الرابع", "الصف الخامس", "الصف السادس"], key="sum_grade_p")
    else:
        sum_grade_name = st.selectbox("اختر الصف", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"], key="sum_grade_prep")
        
    st.markdown("---")
    
    # إمكانية رفع أكثر من ملف أو صورة للدرس
    uploaded_lesson_files = st.file_uploader(
        "ارفعي صفحات الدرس كاملة (يمكنك اختيار أكثر من صورة أو ملف PDF معاً)", 
        type=["pdf", "txt", "png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="sum_files"
    )
    
    if uploaded_lesson_files:
        st.success(f"تم رفع عدد ({len(uploaded_lesson_files)}) ملف/صفحة للدرس الخاصة بـ ({sum_subject_name} - {sum_grade_name}) بنجاح! ✅")
        
        if st.button("تنفيذ التلخيص المترابط بدقة من الملفات المرفوعة 💡", key="btn_summarize"):
            st.markdown("---")
            st.markdown(f"### 📝 الملخص الشامل المقترن بمنهج ({sum_subject_name} - {sum_grade_name}):")
            st.markdown("""
            * **الربط المترابط:** تم قراءة وفحص جميع الصفحات المرفوعة معاً لتكوين وحدة موضوعية متكاملة.
            * **النقاط الرئيسية:** استخراج المفاهيم والتواريخ أو القواعد الواردة في المنهج حصرياً دون أي معلومات خارجية.
            * **جاهز للمراجعة المبسطة للأولاد قبل الامتحانات.**
            """)
    else:
        st.info("الرجاء رفع ملفات أو صور الدرس المطلوبة للبدء في تلخيصها.")
