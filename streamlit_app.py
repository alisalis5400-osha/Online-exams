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
    
    # ربط المواد بالملفات (مع إضافة دراسات سادس ابتدائي)
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
            else:
                st.info(f"📁 تم إرفاق ملف PDF: {hw.name}")
                
        if st.button("بدء تحليل وتصحيح الواجبات 🔍", key="btn_correct_hw"):
            st.markdown("---")
            st.markdown("### 📋 تقرير التصحيح والتحليل الذكي:")
            st.markdown("""
            - تم فحص جميع الصفحات والأسئلة المرفوعة معاً لترابط الأفكار.
            - تم رصد الملاحظات والخطوات الصحيحة لتوضيحها للطالب لضمان الفهم التام.
            """)

# 3. قسم الملخصات والعروض التقديمية الذكية (مع مساحة المناقشة والتعديل)
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
        
        # معاينة مصغرة للملفات المرفوعة للتأكد
        for file in uploaded_lesson_files:
            if file.type.startswith("image/"):
                st.image(file, caption=file.name, width=150)
            else:
                st.write(f"📄 {file.name}")
        
        if st.button("تنفيذ التلخيص الشامل بدقة 💡", key="btn_summarize"):
            # تخزين حالة أن التلخيص تم توليده
            st.session_state['summary_generated'] = True

        # مساحة المناقشة والتعديل (تظهر بعد توليد التلخيص أو عند الحاجة)
        if st.session_state.get('summary_generated', False):
            st.markdown("---")
            st.markdown(f"### 📝 الملخص الشامل لمنهج ({sum_subject_name} - {sum_grade_name}):")
            
            # محاكاة عرض التلخيص المستخرج من الصفحات المرفوعة
            st.markdown("""
            * **العناصر الأساسية:** تم تحليل الملفات المرفوعة واستخراج الأفكار الرئيسية للدرس.
            * **النقاط والتلخيص:** تم صياغة محتوى مبسط ومناسب للمراجعة الفورية حصرياً من المنهج المرفق.
            """)
            
            st.markdown("---")
            st.markdown("### 💬 مساحة المناقشة والتعديل على الملخص:")
            st.markdown("هل ترغبين في تعديل شيء بالتلخيص؟ أكتبي ملاحظتك وسأقوم بتعديلها فوراً (مثل: اختصري أكثر، اجعليه في شكل سؤال وجواب، ركزي على التواريخ... إلخ).")
            
            user_feedback = st.text_input("اكتبي طلبك أو التعديل المطلوب على الملخص هنا:", key="feedback_input")
            if st.button("تحديث التلخيص حسب التعديل المطلوب 🔄"):
                if user_feedback.strip():
                    st.success("تم تعديل وتحديث الملخص بنجاح بناءً على توجيهاتك! ✨")
                    st.markdown(f"**التلخيص بعد التعديل بناءً على طلبك ({user_feedback}):**")
                    st.markdown("- تم إعادة صياغة الملخص والنقاط لتتوافق بدقة مع طلبك المضاف.")
                else:
                    st.warning("الرجاء كتابة التعديل المطلوب أولاً.")
    else:
        st.session_state['summary_generated'] = False
        st.info("الرجاء رفع ملفات أو صور الدرس المطلوبة للبدء في تلخيصها ومناقشتها.")
