import streamlit as st

st.set_page_config(page_title="المنصة التعليمية الذكية", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #1b4d3e, #2e7d61);
        padding: 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    /* تصميم زر احترافي يفتح الرابط في صفحة جديدة بشكل مضمون */
    .direct-btn {
        display: block;
        width: 100%;
        padding: 15px;
        background-color: #1b4d3e;
        color: white !important;
        text-align: center;
        text-decoration: none !important;
        font-size: 1.2em;
        font-weight: bold;
        border-radius: 8px;
        margin-top: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .direct-btn:hover {
        background-color: #2e7d61;
    }
    </style>
    <div class="main-header">
        <h1>المنصة التعليمية الذكية ⚡</h1>
        <p>(admin) أهلاً بكِ يا فندم</p>
    </div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📚 بنك الاختبارات التفاعلية 🎯", "🎨 التلخيص والتصميم المعرفي"])

with tab1:
    st.markdown("### 📝 اختر المادة والصف لتأدية الامتحان")
    
    # 1. اختيار المادة
    subject_name = st.selectbox("1️⃣ اختر المادة:", ["الدراسات الاجتماعية", "اللغة العربية", "اللغة الإنجليزية"])
    
    # 2. اختيار المرحلة
    stage = st.radio("2️⃣ اختر المرحلة:", ["المرحلة الابتدائية", "المرحلة الإعدادية"])
    
    if stage == "المرحلة الابتدائية":
        grade_name = st.selectbox("3️⃣ اختر الصف:", ["الصف الرابع", "الصف الخامس", "الصف السادس"])
        if subject_name == "الدراسات الاجتماعية" and grade_name == "الصف السادس":
            file_url = "G6-social.html"
        else:
            file_url = "#"
    else:
        grade_name = st.selectbox("3️⃣ اختر الصف:", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])
        if subject_name == "اللغة العربية" and grade_name == "الصف الثاني الإعدادي":
            file_url = "Arabic.prep2"
        elif subject_name == "الدراسات الاجتماعية" and grade_name == "الصف الثاني الإعدادي":
            file_url = "social.prep2.html"
        else:
            file_url = "#"

    st.markdown("---")
    st.success(f"✅ تم تجهيز مسار الامتحان بنجاح لهذا الصف!")
    
    # استخدام عنصر HTML مباشر مع target="_blank" لضمان فتح الامتحان في تبويب جديد دون إعادة تحميل المنصة
    if file_url != "#":
        st.markdown(f'''
            <a href="{file_url}" target="_blank" class="direct-btn">
                🚀 اضغط هنا لبدء امتحان ({subject_name} - {grade_name})
            <p style="font-size: 0.8em; margin: 5px 0 0 0; color: #ddd;">(سيتم فتح الامتحان في صفحة جديدة)</p>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.warning("⚠️ عذراً، الامتحان غير متوفر لهذه المادة حالياً.")

with tab2:
    st.info("🛠️ قسم التلخيص والتصميم المعرفي قيد الاستخدام.")
