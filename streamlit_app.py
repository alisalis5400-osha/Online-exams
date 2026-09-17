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
    subject_name = st.selectbox("1️⃣ اختر المادة:", ["الدراسات الاجتماعية", "اللغة العربية", "اللغة الإنجليزية", "العلوم", "الرياضيات"])
    
    # تحويل اسم المادة المختارة إلى اختصار إنجليزي ليتطابق مع أسماء الملفات
    subject_map = {
        "الدراسات الاجتماعية": "social",
        "اللغة العربية": "Arabic",
        "اللغة الإنجليزية": "English",
        "العلوم": "science",
        "الرياضيات": "math"
    }
    subj_code = subject_map.get(subject_name, "exam")

    # 2. اختيار المرحلة
    stage = st.radio("2️⃣ اختر المرحلة:", ["المرحلة الابتدائية", "المرحلة الإعدادية", "المرحلة الثانوية"])
    
    if stage == "المرحلة الابتدائية":
        grade_name = st.selectbox("3️⃣ اختر الصف:", ["الصف الرابع", "الصف الخامس", "الصف السادس"])
        grade_code = {"الصف الرابع": "G4", "الصف الخامس": "G5", "الصف السادس": "G6"}.get(grade_name, "G4")
    elif stage == "المرحلة الإعدادية":
        grade_name = st.selectbox("3️⃣ اختر الصف:", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])
        grade_code = {"الصف الأول الإعدادي": "prep1", "الصف الثاني الإعدادي": "prep2", "الصف الثالث الإعدادي": "prep3"}.get(grade_name, "prep2")
    else:
        grade_name = st.selectbox("3️⃣ اختر الصف:", ["الصف الأول الثانوي", "الصف الثاني الثانوي", "الصف الثالث الثانوي"])
        grade_code = {"الصف الأول الثانوي": "sec1", "الصف الثاني الثانوي": "sec2", "الصف الثالث الثانوي": "sec3"}.get(grade_name, "sec1")

    # بناء اسم الملف تلقائياً بناءً على الاختيارات (مثال: Arabic.prep2.html أو G6.social.html)
    # يمكنك اعتماد صيغة موحدة مثل: Subject.Grade.html
    file_name = f"{subj_code}.{grade_code}.html"
    alt_file_name = f"{grade_code}.{subj_code}.html" # احتياطي لو بدأتِ الصف ثم المادة

    st.markdown("---")
    st.success(f"✅ تم تجهيز مسار الامتحان بنجاح لهذا الصف!")
    
    # زر ديناميكي يفتح الملف مباشرة
    btn_html = f'''
        <a href="{file_name}" target="_blank" class="exam-btn">
            🚀 اضغط هنا لبدء امتحان ({subject_name} - {grade_name})
        </a>
    '''
    st.markdown(btn_html, unsafe_allow_html=True)
    st.caption(f"📁 اسم الملف المرتبط في المستودع: `{file_name}` (تأكدي فقط من رفع الامتحان بهذا الاسم تماماً ليعمل فوراً).")

with tab2:
    st.info("🛠️ قسم التلخيص والتصميم المعرفي قيد الاستخدام.")
