import streamlit as st

# إعدادات الصفحة الأساسية لتظهر بشكل مرتب ويدعم اللغة العربية
st.set_page_config(
    page_title="منصة تحدي المعلوماتية",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تعديل الاتجاه ليدعم العربية من اليمين إلى اليسار (RTL)
st.markdown("""
    <style>
    .reportview-container .main .block-container{ max-width: 800px; }
    div[data-testid="stMarkdownContainer"] { text-align: right; direction: rtl; }
    div[data-testid="stWidgetLabel"] { text-align: right; direction: rtl; }
    .stRadio > label { text-align: right; direction: rtl; }
    </style>
""", unsafe_allow_html=True)

# 1. عنوان الصفحة في المنتصف العلوي
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💻 تمارين ومنهاج المعلوماتية 💻</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #888888;'>مرحباً بك في منصة ترسيخ الدروس لسنوات الأولى ثانوي (آداب)</h3>", unsafe_allow_html=True)
st.write("---")

# 2. هيكلة البيانات (المجالات والدروس والأسئلة)
data = {
    "المجال الأول: بيئة التعامل مع الحاسوب": {
        "درس: تجميع الحاسوب وعتاده": [
            {
                "question": "أين يتم تخزين البيانات بشكل مؤقت وتزول بزوال التيار الكهربائي؟",
                "options": ["القرص الصلب (HDD)", "الذاكرة الحية (RAM)", "المعالج (CPU)"],
                "answer": "الذاكرة الحية (RAM)"
            },
            {
                "question": "ما هو المكون الذي يعتبر 'عقل' الحاسوب والمسؤول عن معالجة البيانات؟",
                "options": ["لوحة الأم (Motherboard)", "مزود الطاقة", "المعالج (CPU)"],
                "answer": "المعالج (CPU)"
            }
        ],
        "درس: نظام التشغيل وحماية الحاسوب": [
            {
                "question": "أي مما يلي يعتبر نظام تشغيل للحاسوب؟",
                "options": ["Microsoft Word", "Windows 10", "Google Chrome"],
                "answer": "Windows 10"
            }
        ]
    },
    "المجال الثاني: المكتبية (Bureautique)": {
        "درس: معالج النصوص (MS Word)": [
            {
                "question": "ما هو اختصار لوحة المفاتيح المستخدم لنسخ (Copy) نص محدد؟",
                "options": ["Ctrl + V", "Ctrl + X", "Ctrl + C"],
                "answer": "Ctrl + C"
            },
            {
                "question": "لتنسيق العناوين الكبيرة وجعلها واضحة في برنامج Word نستخدم:",
                "options": ["إدراج جدول", "تغيير حجم الخط ونوعه", "رسم بياني"],
                "answer": "تغيير حجم الخط ونوعه"
            }
        ],
        "درس: المجدول (MS Excel)": [
            {
                "question": "تُستخدم الجداول والبرامج الحسابية مثل Excel أساساً لـ:",
                "options": ["كتابة الرسائل الطويلة", "الحسابات الآلية ورسم المخططات البيانية", "تعديل الصور"],
                "answer": "الحسابات الآلية ورسم المخططات البيانية"
            }
        ]
    },
    "المجال الثالث: تقنيات الويب": {
        "درس: لغة HTML وتصميم الصفحات": [
            {
                "question": "ما هو الوسم (Tag) المستخدم لإنشاء عنوان رئيسي كبير في لغة HTML؟",
                "options": ["<p>", "<h1>", "<a>"],
                "answer": "<h1>"
            },
            {
                "question": "الوسم <p> في لغة HTML يُستخدم لإدراج:",
                "options": ["صورة متحركة", "رابط لموقع آخر", "فقرة نصية"],
                "answer": "فقرة نصية"
            }
        ]
    }
}

# 3. اختيار المجال (تظهر الخيارات بشكل واضح)
مجالات = list(data.keys())
اختيار_المجال = st.selectbox("📌 اختر المجال الدراسي الذي تريد مراجعته:", مجالات)

# 4. اختيار الدرس بناءً على المجال المختار
الدروس = list(data[اختيار_المجال].keys())
اختيار_الدرس = st.selectbox("📖 اختر الدرس الذي درسته لتثبيت معلوماتك:", الدروس)

st.write("---")
st.markdown(f"<h4 style='color: #2196F3;'>✏️ اختبار تفاعلي في: {اختيار_الدرس}</h4>", unsafe_allow_html=True)

# الحصول على أسئلة الدرس المحدد
الأسئلة = data[اختيار_المجال][اختيار_الدرس]

# إنشاء نموذج (Form) لجمع إجابات الطالب
with st.form(key="quiz_form"):
    user_answers = {}
    
    # عرض الأسئلة على الطالب
    for i, q in enumerate(الأسئلة):
        st.write(f"**السؤال {i+1}:** {q['question']}")
        # عرض الخيارات كـ Radio Buttons
        user_answers[i] = st.radio(f"اختر الإجابة الصحيحة للسؤال {i+1}:", q['options'], key=f"q_{i}", label_visibility="collapsed")
        st.write("")
        
    # زر إنهاء الاختبار وإظهار النتيجة
    submit_button = st.form_submit_button(label="🎯 عرض النتيجة والتقييم")

# 5. حساب النتيجة والتقييم بعد الضغط على الزر
if submit_button:
    score = 0
    total_questions = len(الأسئلة)
    
    for i, q in enumerate(الأسئلة):
        if user_answers[i] == q['answer']:
            score += 1
            
    # حساب النسبة المئوية للنجاح
    percentage = (score / total_questions) * 100
    
    st.write("---")
    st.markdown("<h3 style='text-align: center;'>📊 نتيجتك النهائية</h3>", unsafe_allow_html=True)
    
    # عرض النتيجة بالألوان حسب المستوى
    if percentage == 100:
        st.success(f"ممتاز جداً! علاماتك كاملة: {score} من {total_questions} (نسبة {percentage:.0f}%)")
        st.balloons() # إطلاق بالونات احتفالية عند الإجابة الكاملة الصحيحة لتبهر الأستاذة!
    elif percentage >= 50:
        st.info(f"عمل جيد! لقد نجحت: {score} من {total_questions} (نسبة {percentage:.0f}%) - يمكنك المحاولة مجدداً للحصول على العلامة الكاملة.")
    else:
        st.error(f"تحتاج إلى مراجعة الدرس مجدداً. علاماتك: {score} من {total_questions} (نسبة {percentage:.0f}%)")
