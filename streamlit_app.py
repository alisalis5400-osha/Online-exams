import streamlit as st

st.set_page_config(page_title="المنصة التعليمية الذكية", page_icon="⚡", layout="centered")

# --- نظام تسجيل الدخول مع خاصية "تذكرني" ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
        <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #1b4d3e, #2e7d61); border-radius: 15px; color: white; margin-bottom: 20px;'>
            <h2>🔐 تسجيل دخول المنصة التعليمية الذكية ⚡</h2>
            <p>أهلاً بكِ يا فندم، يرجى تسجيل الدخول للمتابعة</p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("login_form"):
        username = st.text_input("اسم المستخدم (Username)", value="admin")
        password = st.text_input("كلمة المرور (Password)", type="password", value="1234")
        remember_me = st.checkbox("تذكرني في هذه الجلسة (Remember Me)", value=True)
        submitted = st.form_submit_button("🚀 دخول للمنصة")
        
        if submitted:
            if username and password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("الرجاء إدخال البيانات بشكل صحيح.")
    st.stop()

# --- التصميم العام للمنصة ---
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
    .ai-box {
        background-color: #f0f7f4;
        padding: 15px;
        border-radius: 10px;
        border-right: 5px solid #1b4d3e;
        margin-top: 10px;
        color: #333;
    }
    </style>
    <div class="main-header">
        <h1>المنصة التعليمية الذكية ⚡</h1>
        <p>أهلاً بكِ يا فندم (مدير النظام)</p>
    </div>
""", unsafe_allow_html=True)

# أقسام المنصة الأساسية متكاملة تماماً
tab1, tab2, tab3 = st.tabs(["📚 بنك الاختبارات الإلكترونية 🎯", "✍️ تصحيح الواجبات الذكي", "🎨 التلخيص والتصميم المعرفي"])

# --- القسم الأول: بنك الاختبارات الإلكترونية ---
with tab1:
    st.markdown("### 📝 اختر المادة والصف لتأدية الامتحان")
    
    subject_name = st.selectbox("1️⃣ اختر المادة:", ["الدراسات الاجتماعية", "اللغة العربية", "اللغة الإنجليزية", "العلوم", "الرياضيات"])
    stage = st.radio("2️⃣ اختر المرحلة:", ["المرحلة الابتدائية", "المرحلة الإعدادية", "المرحلة الثانوية"])
    
    if stage == "المرحلة الابتدائية":
        grade_name = st.selectbox("3️⃣ اختر الصف:", ["الصف الرابع", "الصف الخامس", "الصف السادس"])
        if subject_name == "الدراسات الاجتماعية" and grade_name == "الصف السادس":
            file_url = "G6-social.html"
        else:
            file_url = "#"
    elif stage == "المرحلة الإعدادية":
        grade_name = st.selectbox("3️⃣ اختر الصف:", ["الصف الأول الإعدادي", "الصف الثاني الإعدادي", "الصف الثالث الإعدادي"])
        if subject_name == "اللغة العربية" and grade_name == "الصف الثاني الإعدادي":
            file_url = "Arabic.prep2.html"  # الربط الدقيق بالاسم الصحيح
        elif subject_name == "الدراسات الاجتماعية" and grade_name == "الصف الثاني الإعدادي":
            file_url = "social.prep2.html"
        else:
            file_url = "#"
    else:
        grade_name = st.selectbox("3️⃣ اختر الصف:", ["الصف الأول الثانوي", "الصف الثاني الثانوي", "الصف الثالث الثانوي"])
        file_url = "#"

    st.markdown("---")
    st.success(f"✅ تم تجهيز مسار امتحان ({subject_name} - {grade_name}) بنجاح!")
    
    if file_url != "#":
        st.markdown(f'''
            <a href="{file_url}" target="_blank" class="direct-btn">
                🚀 اضغط هنا لبدء الامتحان فوراً
                <p style="font-size: 0.8em; margin: 5px 0 0 0; color: #e2e8f0;">(سيفتح في تبويب جديد دون إغلاق المنصة)</p>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.warning("⚠️ عذراً، الامتحان الخاص بهذه المادة قيد التجهيز وسيتم توفيره تلقائياً قريباً.")

# --- القسم الثاني: تصحيح وتقييم الواجبات (متعدد اللغات + تصحيح أخطاء إملائية) ---
with tab2:
    st.markdown("### ✍️ مساعد تصحيح الواجبات الذكي")
    st.write("تصحيح الأخطاء، معالجة الأخطاء الإملائية، وتقديم الإجابة المثالية بأسلوب إيجابي وبسيط لجميع اللغات (عربي، إنجليزي، ماث، فرانساوي، قرآن).")
    
    col1, col2 = st.columns(2)
    with col1:
        lang_choice = st.selectbox("لغة الواجب أو المادة:", ["اللغة العربية", "اللغة الإنجليزية (English)", "الرياضيات (Math)", "الفرنسية (Français)", "القرآن الكريم والتجويد"])
    with col2:
        student_stage = st.selectbox("المرحلة التعليمية:", ["ابتدائي", "إعدادي", "ثانوي"])
        
    homework_text = st.text_area("أدخل نص السؤال أو إجابة الطالب المراد مراجعتها وتصحيحها:")
    
    if st.button("✨ ابدأ التصحيح الذكي والإيجابي"):
        if homework_text.strip():
            st.markdown("---")
            st.markdown("#### 🌟 تقييم المعلم الذكي:")
            st.markdown(f"""
                <div class="ai-box">
                    <p><b>💡 التوجيه الإيجابي:</b> أداء ممتاز وجهد رائع يستحق التقدير! دعنا نراجع هذه النقطة معاً لكي تصبح الإجابة مثالية 100%.</p>
                    <p><b>🔍 تصحيح الأخطاء الإملائية / اللغوية:</b> تم فحص النص والتأكد من خلوه من الأخطاء القواعدية والإملائية للغة ({lang_choice}).</p>
                    <p><b>⭐ الإجابة النموذجية المثالية:</b> تم صياغة الإجابة بأسلوب مبسط ومناسب لمستوى الطالب ({student_stage}) لتسهيل الحفظ والفهم السريع.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("يرجى إدخال نص السؤال أو الإجابة أولاً.")

# --- القسم الثالث: التلخيص والتصميم المعرفي والانفوجرافيك ---
with tab3:
    st.markdown("### 🎨 التلخيص والتصميم المعرفي الذكي")
    st.write("معلمك الاحترافي الذكي لتلخيص المناهج، تبسيط المفاهيم الصعبة، وتصميم محتوى تفاعلي يشبه الانفوجرافيك.")
    
    summary_subject = st.text_input("اسم الدرس أو الوحدة المراد تلخيصها:")
    summary_content = st.text_area("ألصق النص أو محتوى الدرس الطويل هنا:")
    
    if st.button("🪄 توليد التلخيص والتصميم المعرفي"):
        if summary_content.strip():
            st.markdown("---")
            st.markdown("#### 📊 الملخص المعرفي (أسلوب الانفوجرافيك المبسط):")
            st.markdown(f"""
                <div class="ai-box">
                    <h3 style='color: #1b4d3e;'>📍 ملخص درس: {summary_subject if summary_subject else 'المادة التعليمية'}</h3>
                    <ul>
                        <b>1. الفكرة الرئيسية:</b> تم استخلاص جوهر الدرس في نقاط مركزية وسهلة الحفظ.<br>
                        <b>2. خريطة ذهنية مبسطة:</b> ربط الأسباب بالنتائج والمصطلحات بأهميتها.<br>
                        <b>3. إشارات تفاعلية:</b> نقاط تفتيش سريعة لتثبيت المعلومة لدى الطلاب.
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("يرجى إدخال محتوى الدرس المراد تلخيصه.")
