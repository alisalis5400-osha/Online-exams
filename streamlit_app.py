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

# القائمة الجانبية أو الاختيار بين الأقسام الرئيسية
app_mode = st.radio(
    "اختر القسم المطلوب:",
    ["📚 بنك الاختبارات التفاعلية", "🤖 مساعد الواجبات الذكي وتصحيحها"]
)

st.markdown("---")

if app_mode == "📚 بنك الاختبارات التفاعلية":
    st.markdown("### 📝 اختر المادة والصف لتأدية الامتحان")

    # اختيار المادة
    subject_name = st.selectbox(
        "اختر المادة",
        ["الدراسات الاجتماعية", "اللغة العربية", "اللغة الإنجليزية"]
    )

    # اختيار المرحلة
    stage_name = st.radio(
        "اختر المرحلة",
        ["المرحلة الابتدائية", "المرحلة الإعدادية"]
    )

    # اختيار الصف بناءً على المرحلة
    if stage_name == "المرحلة الابتدائية":
        grade_name = st.selectbox("اختر الصف", ["الصف الرابع", "الصف الخامس", "الصف السادس"])
    else:
        grade_name = st.selectbox("اختر الصف", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])

    # تحديد اسم ملف الـ HTML بناءً على الاختيارات
    file_name = ""
    display_name = f"{subject_name} - {grade_name}"

    if subject_name == "الدراسات الاجتماعية" and grade_name == "الصف الرابع":
        file_name = "Social-G4.html"
    elif subject_name == "اللغة العربية" and grade_name == "الصف الثاني الإعدادي":
        file_name = "Arabic.prep2.html"
    elif subject_name == "اللغة الإنجليزية" and grade_name == "الصف الثاني الإعدادي":
        file_name = "English.prep2.html"

    # رسالة وتأكيد الامتحان
    if file_name:
        st.success(f"تم تجهيز مسار امتحان ({display_name}) بنجاح ✅")
        
        # رابط GitHub Pages المباشر الصحيح
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

else:
    st.markdown("### 🤖 مساعد الواجبات الذكي وتصحيحها")
    st.markdown("قم برفع صورة الواجب أو المسألة، وسقوم بتصحيحها ومراجعتها وشرح الإجابة خطوة بخطوة للأولاد بذكاء تام! 💡")
    
    uploaded_homework = st.file_uploader("ارفع صورة الواجب هنا (JPG, PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_homework is not None:
        st.image(uploaded_homework, caption="صورة الواجب المرفوع", use_container_width=True)
        st.success("تم استلام الواجب بنجاح! جاري التحليل والتصحيح الفوري... ✨")
        
        # مكان محاكاة أو عرض الشرح والتصحيح
        st.info("""
            **مراجعة وتصحيح المساعد الذكي:**
            - تم تحليل الأسئلة الموجودة في الصورة.
            - جارٍ إعداد نموذج الإجابة الصحيحة مع الشرح المبسط للأبطال. 
            *(يمكنك ربط هذا الجزء بأدوات الذكاء الاصطناعي لتحليل النص وصياغة التصحيح التفصيلي تلقائياً).*
        """)
