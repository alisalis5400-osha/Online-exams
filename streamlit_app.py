import streamlit as st

st.set_page_config(
    page_title="منصة الاختبارات الإلكترونية", layout="wide"
)

st.title("📱 منصة الاختبارات الإلكترونية التفاعلية")
st.write(
    "مرحباً بك! اختر الاختبار المطلوب للبدء، وسيتم فتح الاختبار في صفحة مستقلة ذات تصحيح فوري وتغذية راجعة."
)

st.markdown("---")

# قائمة الامتحانات وروابطها الثابتة على GitHub Pages
exams_list = [
    {
        "title": "📑 بنك التدريبات الشامل - الدراسات الاجتماعية",
        "desc": "تدريب مكثف على أسئلة وحدات الوطن العربي والتغيرات المناخية",
        "link": "https://alisalis5400-osha.github.io/Online-exams/social-exam.html",
    },
]

# عرض الامتحانات كبطاقات تفاعلية
for exam in exams_list:
    with st.container():
        st.subheader(exam["title"])
        st.write(exam["desc"])
        st.link_button("🚀 ابدأ الاختبار الآن", exam["link"])
        st.markdown("---")
