import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="المنصة التعليمية الذكية",
    page_icon="⚡",
    layout="wide"
)

# قاعدة بيانات خفيفة للمستخدمين (الاسم والباسورد فقط)
if "users_db" not in st.session_state:
    st.session_state["users_db"] = {
        "admin": {"password": "123", "role": "👑 مدير المنصة (Admin)"},
        "ماما": {"password": "123", "role": "👑 مدير المنصة (Admin)"}
    }

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["user_role"] = ""
    st.session_state["username"] = ""

# شاشة تسجيل الدخول أو إنشاء حساب (اسم وباسورد وبس)
if not st.session_state["logged_in"]:
    st.markdown("""
        <div style="text-align: center; padding: 15px; background-color: #0f172a; border-radius: 12px; margin-bottom: 25px; color: white;">
            <h1 style="margin: 0; font-size: 2.2rem;">⚡ المنصة التعليمية الذكية</h1>
            <p style="color: #94a3b8; font-size: 1.1rem; margin-top: 5px;">تسجيل الدخول للاستخدام الفوري</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        auth_mode = st.radio("اختر العملية:", ["تسجيل الدخول", "إنشاء حساب جديد"], horizontal=True)
        
        # حقول بسيطة جداً: الاسم وباسورد وبس
        username = st.text_input("الاسم:")
        password = st.text_input("كلمة المرور:", type="password")
        
        if auth_mode == "تسجيل الدخول":
            if st.button("دخول", use_container_width=True):
                if username in st.session_state["users_db"] and st.session_state["users_db"][username]["password"] == password:
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.session_state["user_role"] = st.session_state["users_db"][username]["role"]
                    st.success("تم الدخول بنجاح!")
                    st.rerun()
                else:
                    st.error("خطأ في الاسم أو كلمة المرور!")
        else:
            if st.button("إنشاء الحساب الآن", use_container_width=True):
                if username and password:
                    if username in st.session_state["users_db"]:
                        st.warning("هذا الاسم موجود بالفعل، جرب اسماً آخر.")
                    else:
                        st.session_state["users_db"][username] = {"password": password, "role": "student"}
                        st.success("تم إنشاء الحساب بنجاح! انتقل لتسجيل الدخول.")
                else:
                    st.warning("يرجى كتابة الاسم وكلمة المرور.")
    
    st.stop()

# =========================================================
# الواجهة الرئيسية للمنصة (تظهر بعد الدخول بنجاح)
# =========================================================
st.markdown(f"""
    <div style="text-align: center; padding: 15px; background-color: #0f172a; border-radius: 12px; margin-bottom: 25px; color: white;">
        <h1 style="margin: 0; font-size: 2.2rem;">⚡ المنصة التعليمية الذكية</h1>
        <p style="color: #38bdf8; font-size: 1.1rem; margin-top: 5px;">أهلاً بكِ يا فندم ({st.session_state.get('username', '')})</p>
    </div>
""", unsafe_allow_html=True)

if st.sidebar.button("🚪 تسجيل الخروج"):
    st.session_state["logged_in"] = False
    st.rerun()

# الأقسام الرئيسية للمنصة (Tabs)
tab1, tab2, tab3 = st.tabs([
    "🎯 بنك الامتحانات التفاعلية", 
    "🎨 التلخيص والتصميم المعرفي", 
    "📸 تصحيح الواجبات"
])

# ---------------------------------------------------------
# القسم الأول: بنك الامتحانات التفاعلية
# ---------------------------------------------------------
with tab1:
    st.subheader("📝 اختر المادة والصف لتأدية الامتحان")

    EXAMS_DATABASE = {
        "Social Studies (دراسات)": {
            "المرحلة الابتدائية": {
                "الصف الرابع": "https://example.com/exam4",
                "الصف الخامس": "https://example.com/exam5",
                "الصف السادس": "https://example.com/exam6"
            },
            "المرحلة الإعدادية": {
                "الصف الأول الإعدادي": "https://example.com/prep1",
                "الصف الثاني الإعدادي": "https://example.com/prep2",
                "الصف الثالث الإعدادي": "https://example.com/prep3"
            }
        }
    }

    col1, col2, col3 = st.columns(3)
    with col1:
        subject = st.selectbox("1️⃣ اختر المادة:", list(EXAMS_DATABASE.keys()))
    with col2:
        stage = st.radio("2️⃣ اختر المرحلة:", ["المرحلة الابتدائية", "المرحلة الإعدادية"], horizontal=True)
    with col3:
        grade = st.selectbox("3️⃣ اختر الصف:", list(EXAMS_DATABASE[subject][stage].keys()))

    st.markdown("---")
    quiz_url = EXAMS_DATABASE[subject][stage][grade]

    if quiz_url and "example.com" not in quiz_url:
        components.iframe(quiz_url, height=800, scrolling=True)
    else:
        st.info("💡 جاري إعداد وتجهيز الامتحان الخاص بهذه المادة وهذا الصف وسيكون متاحاً قريباً!")

# ---------------------------------------------------------
# القسم الثاني: التلخيص والتصميم المعرفي البصري
# ---------------------------------------------------------
with tab2:
    st.subheader("🎨 التلخيص البصري والتصميم المعرفي الذكي")
    st.write("حولي الدروس والمفاهيم إلى إنفوجرافيك، بامفلت ممتع، أو سيناريو قصصي يعتمد على الفهم البصري السريع!")
    
    visual_type = st.selectbox(
        "🎯 اختر نمط العرض البصري:",
        [
            "📄 بامفلت تفاعلي بألوان ملفتة (Pamphlet)",
            "🗺️ خريطة ذهنية ومفاهيمية (Mind Map)",
            "📊 إنفوجرافيك وتصميم معرفي بصري",
            "📖 سيناريو تطبيقي وقصة ممتعة لتوصيل المعلومة",
            "🔍 تحليل المحتوى (أفكار رئيسية + مفاهيم + خيارات)"
        ]
    )
    
    text_to_summarize = st.text_area("✍️ ادخل نص الدرس أو المفهوم المراد تلخيصه:", height=160, placeholder="اكتب أو الصق نص الدرس هنا...")
    
    if st.button("✨ إنشاء التلخيص البصري الآن"):
        if text_to_summarize:
            st.success(f"جاري تحويل النص إلى: {visual_type}...")
            st.markdown("""
                <div style="background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 15px; color: white; border: 2px solid #38bdf8;">
                    <h2 style="text-align: center; color: #38bdf8; margin-top:0;">🌟 كارت التلخيص البصري السريع 🌟</h2>
                    <hr style="border-top: 1px dashed #94a3b8;">
                    <h4 style="color: #facc15;">📌 النقاط الرئيسية:</h4>
                    <ul>
                        <li><b>المفهوم الأساسي:</b> صياغة بكتل ملونة قصيرة وسهلة الحفظ.</li>
                        <li><b>الصورة الذهنية:</b> ربط المعلومة بمثال معرفي يسهل تذكره في الامتحان.</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ يرجى إدخال نص الدرس أولاً لتوليد الملخص البصري.")

# ---------------------------------------------------------
# القسم الثالث: تصحيح الواجبات
# ---------------------------------------------------------
with tab3:
    st.subheader("📸 تصحيح ورقة الواجب بالذكاء الاصطناعي")
    st.write("قم برفع صورة الواجب المنزلي لتحليل الإجابات، اكتشاف الأخطاء، وشرحها فوراً.")
    
    uploaded_file = st.file_uploader("اختر صورة الواجب:", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="صورة الواجب المرفوعة", use_container_width=True)
        if st.button("🔍 تحليل وتصحيح الأخطاء"):
            st.info("جاري فحص الورقة، تحديد الأخطاء، وإعداد التقرير التوضيحي...")
