import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة والتصميم
st.set_page_config(
    page_title="منصة الامتحانات الإلكترونية",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# هيدر شيك للمنصة
st.markdown("""
    <div style="background-color: #1e293b; padding: 20px; border-radius: 12px; text-align: center; color: white; margin-bottom: 25px;">
        <h1 style="margin:0; font-size: 2.2rem;">🎓 منصة الامتحانات الإلكترونية</h1>
        <p style="margin:5px 0 0 0; color: #94a3b8; font-size: 1.05rem;">بنك التدريبات التفاعلي الشامل لجميع المراحل الدراسية</p>
    </div>
""", unsafe_allow_unsafe_cap=True)

# 2. هيكل نظام الامتحانات (المواد -> المرحلتين -> الصفوف -> رابط الامتحان)
EXAMS_DATABASE = {
    "Social Studies (دراسات)": {
        "المرحلة الابتدائية": {
            "الصف السادس الابتدائي": "https://alisalis5400-osha.github.io/Online-exams/Social-G6.html",
            "الصف الخامس الابتدائي": None,
            "الصف الرابع الابتدائي": None,
            "الصف الثالث الابتدائي": None,
            "الصف الثاني الابتدائي": None,
            "الصف الأول الابتدائي": None,
        },
        "المرحلة الإعدادية": {
            "الصف الأول الإعدادي": None,
            "الصف الثاني الإعدادي": None,
            "الصف الثالث الإعدادي": None,
        }
    },
    "Science": {
        "المرحلة الابتدائية": {f"الصف {c} الابتدائي": None for c in ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "السادس"]},
        "المرحلة الإعدادية": {f"الصف {c} الإعدادي": None for c in ["الأول", "الثاني", "الثالث"]}
    },
    "English": {
        "المرحلة الابتدائية": {f"الصف {c} الابتدائي": None for c in ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "السادس"]},
        "المرحلة الإعدادية": {f"الصف {c} الإعدادي": None for c in ["الأول", "الثاني", "الثالث"]}
    },
    "Arabic (لغة عربية)": {
        "المرحلة الابتدائية": {f"الصف {c} الابتدائي": None for c in ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "السادس"]},
        "المرحلة الإعدادية": {f"الصف {c} الإعدادي": None for c in ["الأول", "الثاني", "الثالث"]}
    },
    "French (فرنساوي)": {
        "المرحلة الابتدائية": {f"الصف {c} الابتدائي": None for c in ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "السادس"]},
        "المرحلة الإعدادية": {f"الصف {c} الإعدادي": None for c in ["الأول", "الثاني", "الثالث"]}
    },
    "التربية الدينية": {
        "المرحلة الابتدائية": {f"الصف {c} الابتدائي": None for c in ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "السادس"]},
        "المرحلة الإعدادية": {f"الصف {c} الإعدادي": None for c in ["الأول", "الثاني", "الثالث"]}
    },
    "Math": {
        "المرحلة الابتدائية": {f"الصف {c} الابتدائي": None for c in ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "السادس"]},
        "المرحلة الإعدادية": {f"الصف {c} الإعدادي": None for c in ["الأول", "الثاني", "الثالث"]}
    }
}

# 3. القائمة الجانبية للتحكم والاختيار
st.sidebar.header("📚 اختيارات الامتحان")

# اختيار المادة
subject = st.sidebar.selectbox("1️⃣ اختر المادة:", list(EXAMS_DATABASE.keys()))

# اختيار المرحلة
stage = st.sidebar.radio("2️⃣ اختر المرحلة الدراسية:", ["المرحلة الابتدائية", "المرحلة الإعدادية"])

# اختيار الصف بناءً على المرحلة
grade_options = list(EXAMS_DATABASE[subject][stage].keys())
grade = st.sidebar.selectbox("3️⃣ اختر الصف الدراسي:", grade_options)

# 4. عرض الامتحان أو رسالة تنبيه
quiz_url = EXAMS_DATABASE[subject][stage][grade]

st.subheader(f"📌 {subject} - {stage} ({grade})")

if quiz_url:
    components.iframe(quiz_url, height=800, scrolling=True)
else:
    st.info("💡 قريباً.. جاري إعداد وتجهيز الامتحان الخاص بهذه المادة وهذا الصف الدراسي.")
