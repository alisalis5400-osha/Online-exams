import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="منصة الاختبارات التفاعلية",
    page_icon="🎓",
    layout="wide"
)

# 2. قاموس الامتحانات المتاحة (تقدري تضيفي أي امتحان جديد هنا بسهولة)
EXAMS = {
    "🌍 دراسات اجتماعية - الصف السادس": "https://alisalis5400-osha.github.io/Online-exams/Social-G6.html",
    # "🔬 علوم - الصف السادس": "https://alisalis5400-osha.github.io/Online-exams/Science-G6.html",
    # "🇬🇧 إنجليزي - الصف الخامس": "https://alisalis5400-osha.github.io/Online-exams/English-G5.html",
}

# 3. القائمة الجانبية لتصفح واختيار الامتحانات
st.sidebar.title("📌 قائمة الامتحانات")
st.sidebar.markdown("اختر الامتحان الذي تريد تأديته:")

selected_exam_name = st.sidebar.radio(
    "الامتحانات المتاحة:",
    list(EXAMS.keys())
)

# 4. عرض الامتحان المختار في منتصف الشاشة
st.title(f"📚 {selected_exam_name}")
st.markdown("---")

# جلب رابط الامتحان المختار وعرضه داخل المنصة
current_quiz_url = EXAMS[selected_exam_name]
components.iframe(current_quiz_url, height=800, scrolling=True)
