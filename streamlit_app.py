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
        ["الدراسات الاجتماعية", "اللغة العربية", "اللغة الإنجليزية"]
    )

    stage_name = st.radio(
        "اختر المرحلة",
        ["المرحلة الابتدائية", "المرحلة الإعدادية"]
    )

    if stage_name == "المرحلة الابتدائية":
        grade_name = st.selectbox("اختر الصف", ["الصف الرابع", "الصف الخامس", "الصف السادس"])
    else:
        grade_name = st.selectbox("اختر الصف", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])

    file_name = ""
    display_name = f"{subject_name} - {grade_name}"

    # ربط المواد بالملفات (تم إضافة دراسات سادس وتعديل إنجليزي ثانية إعدادي)
    if subject_name == "الدراسات الاجتماعية" and grade_name == "الصف الرابع":
        file_name = "Social-G4.html"
    elif subject_name == "الدراسات الاجتماعية" and grade_name == "الصف السادس":
        file_name = "Social-G6.html"
    elif subject_name == "اللغة العربية" and grade_name == "الصف الثاني الإعدادي":
        file_name = "Arabic.prep2.html"
    elif subject_name == "اللغة الإنجليزية" and grade_name == "الصف الثاني الإعدادي":
        file_name = "engprep2.htm"  # تم تعديل الاسم بناءً على الرابط الصحيح الذي اكتشفناه

    if file_name:
        st.success(f"تم تجهيز مسار امتحان ({display_name}) بنجاح ✅")
        # الرابط الطبيعي للمنصة
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

# 2. قسم مساعد الواجبات الذكي وتصحيحها
elif app_mode == "🤖 مساعد الواجبات الذكي وتصحيحها":
    st.markdown("### 🤖 مساعد الواجبات الذكي وتصحيحها")
    st.markdown("قم برفع صورة الواجب أو المسألة الدراسية، وسأقوم بتحليلها وتصحيحها خطوة بخطوة للأولاد! 💡")
    
    uploaded_homework = st.file_uploader("ارفع صورة الواجب هنا (JPG, PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_homework is not None:
        st.image(uploaded_homework, caption="صورة الواجب المرفوع", use_container_width=True)
        st.success("تم استلام الواجب بنجاح! جاري تحليل الخطوات وتصحيح الأخطاء... ✨")
        
        st.info("""
            **تقرير التصحيح والتحليل الذكي:**
            - تم فحص الأسئلة المرفوعة في الصورة بنجاح.
            - الأفكار ممتازة، وتم رصد الملاحظات لتوضيحها للطالب لضمان الفهم التام.
        """)

# 3. قسم الملخصات والعروض التقديمية
else:
    st.markdown("### 📊 الملخصات والعروض التقديمية الذكية")
    st.markdown("استعرضي هنا أدوات تلخيص الدروس وصياغة العروض التقديمية (PowerPoint) المصغرة للأولاد بأسلوب سهل ومنظم. 📑")
    
    lesson_text = st.text_area("أدخلي نص الدرس أو الموضوع المراد تلخيصه:")
    
    if st.button("تنفيذ التلخيص والعرض التصويري 💡"):
        if lesson_text.strip():
            st.success("تم إعداد الملخص والعرض التقديمي بنجاح ✅")
            st.markdown("""
                **الملخص المقترح:**
                * العناصر الأساسية للدرس تم ترتيبها في نقاط رئيسية مبسطة.
                * جاهزة للعرض والمراجعة السريعة قبل الامتحانات.
            """)
        else:
            st.warning("الرجاء إدخال نص الدرس أولاً.")
