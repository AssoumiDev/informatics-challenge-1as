import streamlit as st

# إعدادات الصفحة الاحترافية
st.set_page_config(
    page_title="منصة تحدي المعلوماتية 1AS",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم واجهة مبهرة متغيرة تدعم اللغة العربية (RTL)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stSidebarNav"] {
        font-family: 'Cairo', sans-serif;
    }
    
    div[data-testid="stMarkdownContainer"] {
        text-align: right;
        direction: rtl;
    }
    
    div[data-testid="stWidgetLabel"] {
        text-align: right;
        direction: rtl;
    }
    
    .main-title {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }
    
    .question-box {
        background-color: #f8f9fa;
        border-right: 6px solid #2196F3;
        padding: 20px;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# قاعدة البيانات: 10 أسئلة حقيقية مقسمة وموزعة بدقة
data = {
    "المجال الأول: بيئة التعامل مع الحاسوب": {
        "تجميع الحاسوب وأنظمة التشغيل": [
            {"question": "أين يتم تخزين البيانات والبرامج الجاري تنفيذها بشكل مؤقت، وتزول بمجرد انقطاع التيار الكهربائي؟", "options": ["القرص الصلب (Hard Disk)", "الذاكرة الحية (RAM)", "الذاكرة الميتة (ROM)"], "answer": "الذاكرة الحية (RAM)"},
            {"question": "ما هو المكون الذي يمثل 'عقل' الحاسوب ويقوم بجميع العمليات الحسابية والمنطقية وتسيير البيانات؟", "options": ["المعالج (CPU)", "اللوحة الأم (Motherboard)", "بطاقة الشاشة (GPU)"], "answer": "المعالج (CPU)"},
            {"question": "أي مما يلي لا يعتبر نظام تشغيل (Operating System) للحواسيب أو الهواتف؟", "options": ["Windows 10", "Linux", "Microsoft Word"], "answer": "Microsoft Word"},
            {"question": "ما هي الوظيفة الأساسية لبرامج مضادات الفيروسات (Antivirus)؟", "options": ["Antivirus حماية وتطهير الجهاز", "تسريع تصفح الإنترنت", "تنسيق النصوص والملفات"], "answer": "Antivirus حماية وتطهير الجهاز"}
        ]
    },
    "المجال الثاني: المكتبية (Bureautique)": {
        "تطبيقات معالج النصوص والمجدول": [
            {"question": "في برنامج معالج النصوص MS Word، ما هو اختصار لوحة المفاتيح المستخدم لنسخ (Copy) نص محدد؟", "options": ["Ctrl + V", "Ctrl + X", "Ctrl + C"], "answer": "Ctrl + C"},
            {"question": "ما هو البرنامج المكتبي الأنسب لإجراء العمليات الحسابية المعقدة، تنظيم الميزانيات، ورسم المخططات البيانية؟", "options": ["Microsoft Excel (المجدول)", "Microsoft PowerPoint", "Microsoft Word"], "answer": "Microsoft Excel (المجدول)"},
            {"question": "عند استخدام اختصار لوحة المفاتيح (Ctrl + Z) في برامج المكتبية، ما هي العملية التي يتم تنفيذها؟", "options": ["حفظ الملف تلقائياً", "التراجع عن آخر خطوة قام بها المستخدم", "فتح ملف جديد فارغ"], "answer": "التراجع عن آخر خطوة قام بها المستخدم"}
        ]
    },
    "المجال الثالث: تقنيات الويب": {
        "لغة HTML وتصميم الصفحات": [
            {"question": "في لغة HTML الأساسية لإنشاء صفحات الويب، ما هو الوسم (Tag) المستخدم لإدراج عنوان رئيسي عريض وكبير؟", "options": ["<p>", "<h1>", "<a>"], "answer": "<h1>"},
            {"question": "الوسم <p> في لغة HTML يُستخدم لبناء وإدراج عنصر مهم في الصفحة، ما هو؟", "options": ["فقرة نصية (Paragraph)", "رابط تشعبي لموقع آخر", "صورة متحركة أو ثابتة"], "answer": "فقرة نصية (Paragraph)"},
            {"question": "أي من البرامج التالية يُصنف كـ 'متصفح إنترنت' (Web Browser) يُستخدم لفتح وعرض صفحات الويب الرقمية؟", "options": ["Google Chrome", "Google Search", "Gmail"], "answer": "Google Chrome"}
        ]
    }
}

# إدارة التنقل بين الواجهات باستخدام session_state
if "step" not in st.session_state:
    st.session_state.step = "main"  # الواجهة الافتراضية
    st.session_state.selected_field = None
    st.session_state.selected_lesson = None
    st.session_state.current_q = 0
    st.session_state.score = 0

# --- الواجهة الأولى: الشاشة الرئيسية للمجالات ---
if st.session_state.step == "main":
    st.markdown("""
        <div class="main-title">
            <h1 style="margin:0; font-size: 28px; font-weight: bold;">⚡ المنصة الرقمية لتحدي المعلوماتية ⚡</h1>
            <p style="margin:5px 0 0 0; font-size: 16px; opacity: 0.9;">مرحباً بك! اختر مجالاً دراسياً لتحدي معلوماتك وتغيير الواجهة</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: right; color: #1e3c72;'>📌 الخطوة 1: اختر المجال الدراسي المستهدف:</h3>", unsafe_allow_html=True)
    st.write("")
    
    for مجال in data.keys():
        if st.button(f"📂 {مجال}", use_container_width=True):
            st.session_state.selected_field = مجال
            st.session_state.step = "lessons"
            st.rerun()

# --- الواجهة الثانية: شاشة اختيار الدروس ---
elif st.session_state.step == "lessons":
    st.markdown(f"""
        <div class="main-title">
            <h1 style="margin:0; font-size: 24px; font-weight: bold;">📖 {st.session_state.selected_field}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: right; color: #1e3c72;'>📌 الخطوة 2: اختر المحور الدراسي لبدء الاختبار التفاعلي:</h3>", unsafe_allow_html=True)
    st.write("")
    
    دروس = data[st.session_state.selected_field]
    for درس in دروس.keys():
        if st.button(f"📝 {درس}", use_container_width=True):
            st.session_state.selected_lesson = درس
            st.session_state.step = "quiz"
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.rerun()
            
    if st.button("⬅️ العودة للمجالات الرئيسية", type="secondary"):
        st.session_state.step = "main"
        st.rerun()

# --- الواجهة الثالثة: شاشة عرض الأسئلة (سؤال بسؤال) ---
elif st.session_state.step == "quiz":
    الأسئلة = data[st.session_state.selected_field][st.session_state.selected_lesson]
    عدد_الأسئلة = len(الأسئلة)
    q_index = st.session_state.current_q
    
    st.markdown(f"""
        <div class="main-title" style="padding: 15px;">
            <h2 style="margin:0; font-size: 20px;">✏️ تحدي: {st.session_state.selected_lesson}</h2>
            <p style="margin:5px 0 0 0; font-size: 14px;">السؤال {q_index + 1} من أصل {عدد_الأسئلة}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # عرض السؤال الحالي فقط في بطاقة مخصصة
    q_data =  الأسئلة[q_index]
    st.markdown(f'<div class="question-box">{q_data["question"]}</div>', unsafe_allow_html=True)
    
    # اختيار الإجابة
    اختيار = st.radio("اختر الإجابة التي تراها صحيحة:", q_data["options"], key=f"quiz_q_{q_index}")
    
    st.write("---")
    
    # زر الانتقال للسؤال التالي
    if st.button("التالي ➡️", use_container_width=True):
        # احتساب النقاط
        if اختيار == q_data["answer"]:
            st.session_state.score += 1
            
        # الانتقال للسؤال القادم أو صفحة النتيجة
        if q_index + 1 < عدد_الأسئلة:
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.session_state.step = "result"
            st.rerun()

# --- الواجهة الرابعة: شاشة لوحة النتائج والتقييم النهائي ---
elif st.session_state.step == "result":
    الأسئلة = data[st.session_state.selected_field][st.session_state.selected_lesson]
    عدد_الأسئلة = len(الأسئلة)
    score = st.session_state.score
    percentage = (score / عدد_الأسئلة) * 100
    
    st.markdown("""
        <div class="main-title">
            <h1 style="margin:0; font-size: 26px; font-weight: bold;">📊 لوحة النتائج والتقييم البيداغوجي</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    if percentage == 100:
        st.success(f"🏆 مستوى عبقري ومبهر! العلامة كاملة: {score} من {عدد_الأسئلة} (نسبة {percentage:.0f}%)")
        st.balloons()
    elif percentage >= 70:
        st.info(f"✨ مستوى ممتاز! لقد نجحت بتفوق وأجبت على: {score} من {عدد_الأسئلة} (نسبة {percentage:.0f}%)")
        st.snow()
    elif percentage >= 50:
        st.warning(f"👍 مستوى مقبول (ناجح): {score} من {عدد_الأسئلة} (نسبة {percentage:.0f}%) - نقترح إعادة المحاولة للحصول على العلامة الكاملة.")
    else:
        st.error(f"📚 تحتاج إلى مراجعة كراسك والتركيز أكثر. النتيجة الحالية: {score} من {عدد_الأسئلة} (نسبة {percentage:.0f}%)")
        
    st.write("---")
    
    # زر إعادة التحدي من البداية
    if st.button("🔄 العودة إلى الواجهة الرئيسية وتجربة تحدي آخر", use_container_width=True, type="primary"):
        st.session_state.step = "main"
        st.session_state.selected_field = None
        st.session_state.selected_lesson = None
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.rerun()

