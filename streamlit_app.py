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
    .exam-btn {
        display: block;
        width: 100%;
        padding: 14px;
        background-color: #1b4d3e;
        color: white;
        text-align: center;
        text-decoration: none;
        font-size: 1.2em;
        border-radius: 8px;
        margin-top: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .exam-btn:hover {
        background-color: #2e7d61;
        color: white;
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
        # تحديد اسم الملف بدقة حسب المادة والصف الابتدائي
        if subject_name == "الدراسات الاجتماعية" and grade_name == "الصف السادس":
            file_name = "G6-social.html"
        else:
            file_name = "exam.html"
    else:
        grade_name = st.selectbox("3️⃣ اختر الصف:", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])
        # تحديد اسم الملف بدقة حسب المادة والصف الإعدادي
        if subject_name == "اللغة العربية" and grade_name == "الصف الثاني الإعدادي":
            file_name = "Arabic.prep2"  # الاسم الموجود في مستودعك تماماً
        elif subject_name == "الدراسات الاجتماعية" and grade_name == "الصف الثاني الإعدادي":
            file_name = "social.prep2.html"
        else:
            file_name = "exam.html"

    st.markdown("---")
    st.success(f"✅ تم تجهيز مسار الامتحان بنجاح لهذا الصف!")
    
    # زر ديناميكي يفتح الملف الصحيح مباشرة
    btn_html = f'''
        <a href="{file_name}" target="_blank" class="exam-btn">
            🚀 اضغط هنا لبدء امتحان ({subject_name} - {grade_name})
        </a>
    '''
    st.markdown(btn_html, unsafe_allow_html=True)
    st.caption(f"📁 اسم الملف المرتبط: `{file_name}`")

with tab2:
    st.info("🛠️ قسم التلخيص والتصميم المعرفي قيد الاستخدام.")
