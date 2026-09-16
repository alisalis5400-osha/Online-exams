import streamlit as st

st.set_page_config(
    page_title="منصة الاختبارات الإلكترونية", layout="wide"
)

st.title("📱 مركز الاختبارات الإلكترونية التفاعلية")
st.write(
    "اختر الامتحان المطلوب للبدء، وسيتم فتح الامتحان في صفحة مستقلة ذات تصحيح فوري."
)

st.markdown("---")

# عرض بطاقة الامتحان الجديد
with st.container():
    st.subheader("📑 اختبار الدراسات الاجتماعية - الصف السادس الابتدائي")
    st.write(
        "بنك أسئلة شامل يتضمن أسئلة الخرائط والأجزاء المقالية مع التصحيح الفوري والأجوبة النموذجية."
    )

    # زر يفتح اللينك الثابت للملف الجديد
    st.link_button(
        "🚀 ابدأ الاختبار الآن",
        "https://alisalis5400-osha.github.io/Online-exams/G6-social.html.",
    )

st.markdown("---")
