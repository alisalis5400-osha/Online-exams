<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بنك الأسئلة المقالية الشامل - الدراسات الاجتماعية</title>
    <style>
        * { box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #f0f4f8; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .quiz-container { background: #ffffff; width: 100%; max-width: 850px; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); padding: 25px; border: 2px solid #e1e8ed; }
        .header { text-align: center; border-bottom: 3px solid #2563eb; padding-bottom: 15px; margin-bottom: 25px; }
        .header h1 { color: #1e293b; margin: 0 0 5px 0; font-size: 24px; }
        .header p { color: #64748b; margin: 0; font-size: 15px; }
        .controls { display: flex; flex-wrap: wrap; gap: 10px; justify-content: space-between; align-items: center; margin-bottom: 20px; background: #eff6ff; padding: 15px; border-radius: 10px; }
        .btn-action { background-color: #059669; color: white; border: none; padding: 10px 18px; font-size: 14px; font-weight: bold; border-radius: 8px; cursor: pointer; }
        .btn-action:hover { background-color: #047857; }
        .btn-blue { background-color: #2563eb; }
        .btn-blue:hover { background-color: #1d4ed8; }
        .question-card { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 20px; margin-bottom: 20px; }
        .question-title { font-size: 17px; font-weight: bold; color: #0f172a; margin-bottom: 12px; }
        .type-tag { display: inline-block; background-color: #dbeafe; color: #1e40af; padding: 3px 10px; border-radius: 6px; font-size: 13px; margin-bottom: 8px; font-weight: bold; }
        textarea { width: 100%; height: 85px; padding: 10px; border: 2px solid #cbd5e1; border-radius: 8px; font-size: 15px; resize: vertical; margin-bottom: 10px; }
        textarea:focus { border-color: #2563eb; outline: none; }
        .feedback-box { display: none; background-color: #f0fdf4; border-right: 4px solid #16a34a; padding: 12px 15px; border-radius: 6px; font-size: 15px; color: #14532d; margin-top: 10px; line-height: 1.6; }
        .action-container { text-align: center; margin-top: 30px; }
        .submit-btn { background-color: #2563eb; color: white; border: none; padding: 14px 35px; font-size: 18px; font-weight: bold; border-radius: 10px; cursor: pointer; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); }
        .submit-btn:hover { background-color: #1d4ed8; }
    </style>
</head>
<body>

<div class="quiz-container">
    <div class="header">
        <h1>📝 بنك التدريبات المقالية الشامل - الصف السادس الابتدائي</h1>
        <p>التدريب المكثف والتثبيت التلقائي للمعلومات والكتابة</p>
    </div>

    <div class="controls">
        <span id="exam-info" style="font-weight: bold; color: #1e3a8a;">عرض الأسئلة الحالي: <span id="q-count">20</span> سؤال</span>
        <div>
            <button class="btn-action" onclick="generateExam(20)">🎲 20 سؤال عشوائي</button>
            <button class="btn-action btn-blue" onclick="generateExam(masterQuestionBank.length)">📚 حل البنك بالكامل</button>
        </div>
    </div>

    <div id="quiz-body"></div>

    <div class="action-container">
        <button id="submit-btn" class="submit-btn" onclick="correctExam()">عرض الإجابات النموذجية والإرشادات 🚀</button>
    </div>
</div>

<script>
// بنك الأسئلة الشامل (يمكنك إضافة أي عدد من الأسئلة في هذه القائمة بسهولة)
const masterQuestionBank = [
    // أسئلة بم تفسر
    { type: "بم تفسر", q: "تغطية الثلوج لبعض القمم الجبلية في الوطن العربي مثل جبال لبنان؟", modelAnswer: "لأنه كلما ارتفعنا 150 متراً فوق مستوى سطح البحر تنخفض درجة الحرارة درجة واحدة مئوية." },
    { type: "بم تفسر", q: "تؤثر اتجاه الكتل الجبلية في توزيع كمية الأمطار؟", modelAnswer: "لأن سفوح الجبال المواجهة للرياح المحملة ببخار الماء تكون أغزر مطراً من الجوانب الداخلية (منطقة ظل المطر)." },
    { type: "بم تفسر", q: "نمو الغابات المعتدلة فوق المنحدرات الجبلية في إقليم البحر المتوسط؟", modelAnswer: "بسبب غزارة الأمطار الشتوية." },
    { type: "بم تفسر", q: "تعتبر حشائش السافانا حديقة حيوان طبيعية؟", modelAnswer: "لأنه يعيش فيها حيوانات أكلة للعشب (كالزراف والأفيال) وحيوانات أكلة لللحوم (كالأسود والنمار)." },
    { type: "بم تفسر", q: "يعاني الوطن العربي من مشكلة ندرة المياه العذبة؟", modelAnswer: "بسبب قلة سقوط الأمطار، وزيادة عدد السكان، واستخدام طرق الري التقليدية وسوء إدارة المياه." },
    { type: "بم تفسر", q: "أهمية استخدام طرق الري الحديثة مثل الرش والتنقيط؟", modelAnswer: "لترشيد استهلاك المياه العذبة والحد من ضياعها ومواجهة أزمة النقص المائي." },
    { type: "بم تفسر", q: "يعاني الوطن العربي من مشكلة التصحر؟", modelAnswer: "بسبب أسباب طبيعية (كالقت وزحف الرمل) وأسباب بشرية (كقطع الأشجار، الرعي الجائر، والتوسع العمراني)." },
    { type: "بم تفسر", q: "يعاني الوطن العربي من مشكلة تلوث الهواء؟", modelAnswer: "بسبب عوادم السيارات، غازات المصانع، حرق النفايات، والعواصف الرملية." },
    { type: "بم تفسر", q: "أهمية بناء السدود والمخرات في مواجهة السيول؟", modelAnswer: "السدود لحجز المياه والاستفادة منها في الزراعة، والمخرات لتصريف مياه السيول وحماية الأرواح والمنشآت." },
    { type: "بم تفسر", q: "إطلاق مصر لمبادرة زراعة 100 مليون شجرة مثمرة؟", modelAnswer: "لتنقية الهواء، زيادة المساحات الخضراء، تقليل التلوث، ومواجهة التغيرات المناخية." },
    { type: "بم تفسر", q: "إطلاق السعودية لمبادرة زراعة 450 مليون شجرة وإنشاء مدينة نيوم الخضراء؟", modelAnswer: "للحد من التلوث، الاعتماد على الطاقة النظيفة، ومواجهة التغيرات المناخية." },
    { type: "بم تفسر", q: "قيام المصريين القدماء بإنشاء مخرات للسيول؟", modelAnswer: "لتصريف مياه السيول وتوجيهها بعيداً عن البيوت والمنشآت للحفاظ على الأرواح واستغلال المياه." },
    { type: "بم تفسر", q: "تشكل السيول تهديداً كبيراً على حياة الإنسان؟", modelAnswer: "لأنها تدفقات مائية سريعة وفجائية تؤدي لتدمير البيوت والممتلكات والخسائر البشرية." },
    { type: "بم تفسر", q: "تلوث الهواء يؤثر سلباً على صحة الإنسان؟", modelAnswer: "لأنه يؤدي لاستنشاق غازات سامة وأتربة تسبب أمراض الجهاز التنفسي وحالات الخنق." },
    { type: "بم تفسر", q: "استخدام النقل المستدام في الدول العربية؟", modelAnswer: "للحد من انبعاثات عوادم السيارات الضارة وتقليل تلوث الهواء." },

    // أسئلة ما النتائج المترتبة على
    { type: "ما النتائج المترتبة على", q: "نمو حشائش الاستبس في إقليم البحر المتوسط؟", modelAnswer: "أدى إلى تربية الماعز والأغنام عليها وممارسة نشاط الرعي." },
    { type: "ما النتائج المترتبة على", q: "اختلاف كمية الأمطار في الإقليم المداري؟", modelAnswer: "تدرج حشائش السافانا في الطول حسب كمية المطر." },
    { type: "ما النتائج المترتبة على", q: "حدوث موجات الجفاف الشديدة (مثل الصومال)؟", modelAnswer: "نقص الغذاء، جفاف المراعي، انتشار المجاعات والأمراض، وتأثر النشاط الزراعي." },
    { type: "ما النتائج المترتبة على", q: "قطع الأشجار والرعي الجائر؟", modelAnswer: "تدهور القدرة الإنتاجية للأراضي الزراعية وزيادة انتشار ظاهرة التصحر." },
    { type: "ما النتائج المترتبة على", q: "حدوث السيول في مناطق تجمعات السكان؟", modelAnswer: "تدمير المباني والطرق، إتلاف المحاصيل، وخسائر بشرية ومادية كبيرة." },
    { type: "ما النتائج المترتبة على", q: "التغيرات المناخية في الوطن العربي؟", modelAnswer: "ارتفاع درجات الحرارة، زيادة تكرار الجفاف والسيول، انخفاض إنتاجية الأراضي، وتهديد الأمن الغذائي." },
    { type: "ما النتائج المترتبة على", q: "زيادة النشاط الصناعي دون ضوابط بيئية؟", modelAnswer: "زيادة الانبعاثات الضارة وتفاقم مشكلة تلوث الهواء والتغير المناخي." },
    { type: "ما النتائج المترتبة على", q: "استخدام التكنولوجيا الحديثة في التنبؤ بالسيول؟", modelAnswer: "الاستعداد المبكر وتقليل الخسائر في الأرواح والممتلكات وإخلاء المناطق الخطرة." },

    // أسئلة دلل على صحة العبارة
    { type: "دلل على صحة العبارة", q: "يختلف النبات الطبيعي في الإقليم الصحراوي حسب كمية المطر.", modelAnswer: "حيث تنمو الأعشاب القصيرة في المناطق قليلة المطر، بينما تنمو النباتات الشوكية (كالصبار) في المناطق نادرة المطر." },
    { type: "دلل على صحة العبارة", q: "تؤثر التغيرات المناخية على الأنشطة الاقتصادية والبيئية.", modelAnswer: "حيث تؤدي لتنوع المحاصيل وتنشيط السياحة البيئية، وفي المقابل تتسبب في تدهور الأراضي والجفاف." },
    { type: "دلل على صحة العبارة", q: "تبذل الدول العربية جهوداً لمواجهة ندرة المياه.", modelAnswer: "من خلال ترشيد الاستهلاك، إعادة تدوير مياه الصرف الصحي، استخدام أساليب الري الحديثة، وحملات التوعية." },
    { type: "دلل على صحة العبارة", q: "تبذل الدول العربية جهوداً للحد من تلوث الهواء.", modelAnswer: "من خلال زيادة المساحات الخضراء، الاعتماد على الطاقة المتجددة، واستخدام النقل المستدام." },
    { type: "دلل على صحة العبارة", q: "السيول تسبب خسائر بشرية ومادية كبيرة.", modelAnswer: "حيث تتدمر الطرق والمنشآت وتتلف المحاصيل الزراعية وتتسبب في وفيات بين السكان." },
    { type: "دلل على صحة العبارة", q: "تستغل بعض الدول التكنولوجيا في مواجهة الأزمات البيئية.", modelAnswer: "من خلال استخدام الإنذار المبكر والأقمار الصناعية للتنبؤ بموعد السيول والجفاف." },

    // أسئلة ما المقصود بـ
    { type: "ما المقصود بـ", q: "الجفاف؟", modelAnswer: "فترة زمنية يقل فيها سقوط الأمطار مما يؤدي للإضرار بالزراعة والرعي ونقص الغذاء." },
    { type: "ما المقصود بـ", q: "السيول؟", modelAnswer: "أمطار غزيرة فجائية تتجمع في الأودية الجافة وتتدفق بسرعة شديدة نحو المناطق المنخفضة." },
    { type: "ما المقصود بـ", q: "التصحر؟", modelAnswer: "تدهور الأراضي الزراعية وتناقص قدرتها على الإنتاج النباتي أو فقدانها بالكامل." },

    // أسئلة ماذا يحدث لو
    { type: "ماذا يحدث لو", q: "وقعت معظم مساحة الوطن العربي في الإقليم المداري؟", modelAnswer: "لأصبح مناخ معظم الوطن العربي حاراً ممطراً صيفاً وجافاً شتاءً، ولنمت حشائش السافانا في معظم أراضيه." },
    { type: "ماذا يحدث لو", q: "وقعت معظم مساحة الوطن العربي في إقليم البحر المتوسط؟", modelAnswer: "لأصبح المناخ حاراً جافاً صيفاً ودافئاً ممطراً شتاءً ولنمت الغابات المعتدلة وازدادت المساحات الزراعية." },
    { type: "ماذا يحدث لو", q: "اعتمدت جميع الدول العربية على الطاقة المتجددة؟", modelAnswer: "سينخفض انبعاث الغازات الضارة، ويقل تلوث الهواء، ونحد من أزمة التغير المناخي." },
    { type: "ماذا يحدث لو", q: "استخدمت معظم دول الوطن العربي أساليب الري الحديثة؟", modelAnswer: "سيتم ترشيد استهلاك المياه العذبة، والحفاظ على الموارد المائية، والحد من ندرة المياه." },

    // أسئلة ما العلاقة بين / واقترح
    { type: "ما العلاقة بين", q: "التغيرات المناخية والمشكلات البيئية؟", modelAnswer: "التغيرات المناخية تؤدي لزيادة حدّة وتكرار المشكلات البيئية مثل التصحر، الجفاف الشديد، وتكرار السيول." },
    { type: "ما العلاقة بين", q: "التكنولوجيا الحديثة ومشكلة السيول؟", modelAnswer: "تساعد التكنولوجيا والأقمار الصناعية في التنبؤ المبكر بالسيول لاتخاذ الاحتياطات وبناء السدود." },
    { type: "اقترح أساليب", q: "لمواجهة مشكلة تلوث الهواء في المدن العربية؟", modelAnswer: "التوسع في زراعة الأشجار والمساحات الخضراء، الاعتماد على وسائل النقل المستدام، واستخدام الطاقة الشمسية والرياح." }
];

let currentQuestions = [];

function generateExam(count) {
    let selected = [];
    if (count >= masterQuestionBank.length) {
        selected = [...masterQuestionBank];
    } else {
        const shuffled = [...masterQuestionBank].sort(() => 0.5 - Math.random());
        selected = shuffled.slice(0, count);
    }
    
    currentQuestions = selected;
    document.getElementById('q-count').innerText = currentQuestions.length;

    const container = document.getElementById('quiz-body');
    container.innerHTML = '';

    currentQuestions.forEach((item, index) => {
        const card = document.createElement('div');
        card.className = 'question-card';
        card.innerHTML = `
            <span class="type-tag">${item.type}</span>
            <div class="question-title">س${index + 1}: ${item.q}</div>
            <textarea id="ans-${index}" placeholder="اكتب إجابتك النموذجية هنا يا بطل..."></textarea>
            <div class="feedback-box" id="feed-${index}">
                <strong>💡 الإجابة النموذجية والأدق:</strong><br>
                ${item.modelAnswer}<br>
                <span style="color: #047857; font-weight: bold; display: block; margin-top: 5px;">🌟 ممتااااز! قارن إجابتك بالإجابة النموذجية لتضمن الدرجة النهائية!</span>
            </div>
        `;
        container.appendChild(card);
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function correctExam() {
    currentQuestions.forEach((_, index) => {
        document.getElementById(`feed-${index}`).style.display = 'block';
    });
    alert("تم عرض الإجابات النموذجية لجميع الأسئلة! قارن إجابتك واحرص على كتابة المفاتيح الرئيسية في كل إجابة. 🌟");
}

// بدء التشغيل باختيار 20 سؤال عشوائي
generateExam(20);
</script>

</body>
</html>
