import streamlit as st

st.set_page_config(page_title="المنصة التعليمية الذكية", page_icon="⚡", layout="centered")

# تصميم الواجهة الهادئ
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
    </style>
    <div class="main-header">
        <h1>المنصة التعليمية الذكية ⚡</h1>
        <p>(admin) أهلاً بكِ يا فندم</p>
    </div>
""", unsafe_allow_html=True)

# القوائم الرئيسية
tab1, tab2 = st.tabs(["📚 بنك الاختبارات التفاعلية 🎯", "🎨 التلخيص والتصميم المعرفي"])

with tab1:
    st.markdown("### 📝 اختر المادة والصف لتأدية الامتحان")
    
    # اختيار المادة
    subject = st.selectbox("1️⃣ اختر المادة:", ["الدراسات الاجتماعية", "اللغة العربية", "اللغة الإنجليزية"])
    
    # اختيار المرحلة
    stage = st.radio("2️⃣ اختر المرحلة:", ["المرحلة الابتدائية", "المرحلة الإعدادية"])
    
    if stage == "المرحلة الإعدادية":
        grade = st.selectbox("3️⃣ اختر الصف:", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])
        
        if subject == "اللغة العربية" and grade == "الصف الثاني الإعدادي":
            st.success("✅ تم العثور على امتحان اللغة العربية (الصف الثاني الإعدادي) - 30 سؤالاً جاهزاً!")
            
            # زر فتح الامتحان التفاعلي المباشر
            if st.button("🚀 ابدأ امتحان اللغة العربية الآن"):
                st.markdown("""
                    <meta http-equiv="refresh" content="0; url='Arabic.prep2.html'">
                """, unsafe_allow_html=True)
                st.info("جاري تحويلك لصفحة الامتحان...")
        else:
            st.warning("💡 جاري تجهيز الامتحان الخاص بهذه المادة لهذا الصف وسيكون متاحاً قريباً!")
            
    else:
        grade = st.selectbox("3️⃣ اختر الصف:", ["الصف الرابع", "الصف الخامس", "الصف السادس"])
        st.info("💡 جاري تجهيز الامتحانات لهذه المرحلة قريباً!")

with tab2:
    st.info("🛠️ قسم التلخيص والتصميم المعرفي قيد التطوير والاستخدام.")
