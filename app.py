import streamlit as st

# --- 1. إعدادات المتصفح الأساسية ---
st.set_page_config(
    page_title="Informatics Challenge 1AS",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. تصميم الواجهة والألوان باستخدام CSS لتدعم اللغة العربية ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    html, body, [data-testid="stSidebarNav"] { font-family: 'Cairo', sans-serif; }
    div[data-testid="stMarkdownContainer"] { text-align: right; direction: rtl; }
    div[data-testid="stWidgetLabel"] { text-align: right; direction: rtl; }
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
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. قاعدة البيانات الرقمية (كافة المجالات والدروس والأسئلة لـ 1 ثانوي) ---
data = {
    "المجال الأول: بيئة التعامل مع الحاسوب": {
        "تجميع الحاسوب وعتاده الداخلي": [
            {"question": "أين يتم تخزين البيانات والبرامج الجاري تنفيذها بشكل مؤقت، وتزول بمجرد انقطاع التيار الكهربائي؟", "options": ["القرص الصلب (Hard Disk)", "الذاكرة الحية (RAM)", "الذاكرة الميتة (ROM)"], "answer": "الذاكرة الحية (RAM)"},
            {"question": "ما هو المكون الذي يمثل 'عقل' الحاسوب ويقوم بجميع العمليات الحسابية والمنطقية وتسيير البيانات؟", "options": ["المعالج (CPU)", "اللوحة الأم (Motherboard)", "بطاقة الشاشة (GPU)"], "answer": "المعالج (CPU)"},
            {"question": "أي من المكونات التالية يعتبر وحدة إدخال فقط للبيانات في الحاسوب؟", "options": ["الشاشة", "لوحة المفاتيح (Keyboard)", "الطابعة"], "answer": "لوحة المفاتيح (Keyboard)"}
        ],
        "أنظمة التشغيل وحماية الحاسوب": [
            {"question": "أي مما يلي لا يعتبر نظام تشغيل (Operating System) للحواسيب أو الهواتف؟", "options": ["Windows 10", "Linux", "Microsoft Word"], "answer": "Microsoft Word"},
            {"question": "ما هي الوظيفة الأساسية لبرامج مضادات الفيروسات (Antivirus)؟", "options": ["حماية وتطهير الجهاز من البرامج الخبيثة", "تسريع تصفح الإنترنت", "تنسيق النصوص والملفات"], "answer": "حماية وتطهير الجهاز من البرامج الخبيثة"},
            {"question": "تُستخدم 'لوحة التحكم' (Control Panel) في نظام الويندوز لـ:", "options": ["كتابة البحوث المدرسية", "ضبط إعدادات النظام والعتاد والشبكات", "تصفح مواقع الويب"], "answer": "ضبط إعدادات النظام والعتاد والشبكات"}
        ],
        "الشبكات المحلية (LAN)": [
            {"question": "ما هي الفائدة الأساسية من ربط الحواسيب داخل مخبر الإعلام الآلي في شبكة محلية (LAN)؟", "options": ["زيادة حجم الشاشة", "مشاركة الملفات والموارد مثل الطابعات", "توليد الطاقة الكهربائية"], "answer": "مشاركة الملفات والموارد مثل الطابعات"}
        ]
    },
    "المجال الثاني: المكتبية (Bureautique)": {
        "معالج النصوص (Microsoft Word)": [
            {"question": "في برنامج معالج النصوص MS Word، ما هو اختصار لوحة المفاتيح المستخدم لنسخ (Copy) نص مححدد؟", "options": ["Ctrl + V", "Ctrl + X", "Ctrl + C"], "answer": "Ctrl + C"},
            {"question": "عند استخدام اختصار لوحة المفاتيح (Ctrl + Z) في برامج المكتبية، ما هي العملية التي يتم تنفيذها؟", "options": ["حفظ الملف تلقائياً", "التراجع عن آخر خطوة قام بها المستخدم", "فتح ملف جديد فارغ"], "answer": "التراجع عن آخر خطوة قام بها المستخدم"},
            {"question": "لإدراج جدول أو صورة داخل مستند Word، نتوجه إلى تبويب:", "options": ["الصفحة الرئيسية (Home)", "إدراج (Insert)", "تخطيط الصفحة (Layout)"], "answer": "إدراج (Insert)"}
        ],
        "المجدول وجداول البيانات (Microsoft Excel)": [
            {"question": "ما هو البرنامج المكتبي الأنسب لإجراء العمليات الحسابية الآلية، تنظيم الميزانيات، ورسم المخططات البيانية؟", "options": ["Microsoft Excel", "Microsoft PowerPoint", "Microsoft Word"], "answer": "Microsoft Excel"},
            {"question": "في برنامج Excel، تسمى نقطة تقاطع العمود مع السطر بـ:", "options": ["الخلية (Cell)", "المخطط", "الصيغة"], "answer": "الخلية (Cell)"}
        ],
        "العروض التقديمية (Microsoft PowerPoint)": [
            {"question": "يُستخدم برنامج PowerPoint أساساً من أجل:", "options": ["إنشاء وتصميم شرائح تفاعلية لعرض الدروس والبحوث", "تسيير قواعد البيانات الضخمة", "تثبيت أنظمة التشغيل"], "answer": "إنشاء وتصميم شرائح تفاعلية لعرض الدروس والبحوث"}
        ]
    },
    "المجال الثالث: تقنيات الويب": {
        "لغة HTML وتصميم الصفحات": [
            {"question": "في لغة HTML الأساسية لإنشاء صفحات الويب، ما هو الوسم (Tag) المستخدم لإدراج عنوان رئيسي عريض وكبير؟", "options": ["<p>", "<h1>", "<a>"], "answer": "<h1>"},
            {"question": "الوسم <p> في لغة HTML يُستخدم لبناء وإدراج عنصر مهم في الصفحة، ما هو؟", "options": ["فقرة نصية (Paragraph)", "رابط تشعبي لموقع آخر", "صورة متحركة أو ثابتة"], "answer": "فقرة نصية (Paragraph)"}
        ],
        "متصفحات الإنترنت والبحث الآمن": [
            {"question": "أي من البرامج التالية يُصنف كـ 'متصفح إنترنت' (Web Browser) يُستخدم لفتح وعرض صفحات الويب الرقمية؟", "options": ["Google Chrome", "Google Search", "Gmail"], "answer": "Google Chrome"},
            {"question": "لإرسال رسالة إلكترونية رسمية مرفقة بملف رقمي إلى الأستاذة، نستخدم خدمة:", "options": ["محرك البحث", "البريد الإلكتروني (Email)", "محرر النصوص"], "answer": "البريد الإلكتروني (Email)"}
        ]
    }
}
# --- 4. تهيئة ذاكرة الموقع (session_state) ---
if "step" not in st.session_state:
    st.session_state.step = "main"
    st.session_state.selected_field = None
    st.session_state.selected_lesson = None
    st.session_state.current_q = 0
    st.session_state.score = 0

# --- 5. الواجهة الأولى: الشاشة الرئيسية (اختيار المجال الدراسي) ---
if st.session_state.step == "main":
    st.markdown("""
        <div class="main-title">
            <h1 style="margin:0; font-size: 28px; font-weight: bold;">⚡ المنصة الرقمية لتحدي المعلوماتية ⚡</h1>
            <p style="margin:5px 0 0 0; font-size: 16px; opacity: 0.9;">مرحباً بك! اختر مجالاً دراسياً لتحدي معلوماتك وتغيير الواجهة</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: right; color: #1e3c72;'>📌 الخطوة 1: اختر المجال الدراسي المستهدف:</h3>", unsafe_allow_html=True)
    st.write("")
    
    for field_name in data.keys():
        if st.button(f"📂 {field_name}", use_container_width=True):
            st.session_state.selected_field = field_name
            st.session_state.step = "lessons"
            st.rerun()

# --- 6. الواجهة الثانية: شاشة عرض دروس المجال المختار ---
elif st.session_state.step == "lessons":
    st.markdown(f"""
        <div class="main-title">
            <h1 style="margin:0; font-size: 24px; font-weight: bold;">📖 {st.session_state.selected_field}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: right; color: #1e3c72;'>📌 الخطوة 2: اختر الدرس الذي ترغب في مراجعته الآن:</h3>", unsafe_allow_html=True)
    st.write("")
    
    lessons = data[st.session_state.selected_field]
    for lesson_name in lessons.keys():
        if st.button(f"📝 {lesson_name}", use_container_width=True):
            st.session_state.selected_lesson = lesson_name
            st.session_state.step = "quiz"
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.rerun()
            
    st.write("")
    if st.button("⬅️ العودة للمجالات الرئيسية", type="secondary", use_container_width=True):
        st.session_state.step = "main"
        st.rerun()

# --- 7. الواجهة الثالثة: شاشة التحدي التفاعلي (سؤال واحد في كل واجهة) ---
elif st.session_state.step == "quiz":
    questions_list = data[st.session_state.selected_field][st.session_state.selected_lesson]
    total_q = len(questions_list)
    q_index = st.session_state.current_q
    
    st.markdown(f"""
        <div class="main-title" style="padding: 15px;">
            <h2 style="margin:0; font-size: 20px;">✏️ تحدي: {st.session_state.selected_lesson}</h2>
            <p style="margin:5px 0 0 0; font-size: 14px;">السؤال {q_index + 1} من أصل {total_q}</p>
        </div>
    """, unsafe_allow_html=True)
    
    q_data = questions_list[q_index]
    st.markdown(f'<div class="question-box">{q_data["question"]}</div>', unsafe_allow_html=True)
    
    user_choice = st.radio("اختر الإجابة التي تراها صحيحة:", q_data["options"], key=f"quiz_q_{q_index}")
    
    st.write("---")
    
    if st.button("التالي ➡️", use_container_width=True):
        if user_choice == q_data["answer"]:
            st.session_state.score += 1
            
        if q_index + 1 < total_q:
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.session_state.step = "result"
            st.rerun()

# --- 8. الواجهة الرابعة: شاشة النتيجة والتقييم النهائي ---
elif st.session_state.step == "result":
    questions_list = data[st.session_state.selected_field][st.session_state.selected_lesson]
    total_q = len(questions_list)
    final_score = st.session_state.score
    percentage = (final_score / total_q) * 100
    
    st.markdown("""
        <div class="main-title">
            <h1 style="margin:0; font-size: 26px; font-weight: bold;">📊 لوحة النتائج والتقييم البيداغوجي</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    if percentage == 100:
        st.success(f"🏆 مستوى عبقري ومبهر! العلامة كاملة: {final_score} من {total_q} (نسبة {percentage:.0f}%)")
        st.balloons()
    elif percentage >= 70:
        st.info(f"✨ مستوى ممتاز! لقد نجحت بتفوق وأجبت على: {final_score} من {total_q} (نسبة {percentage:.0f}%)")
        st.snow()
    elif percentage >= 50:
        st.warning(f"👍 مستوى مقبول (ناجح): {final_score} من {total_q} (نسبة {percentage:.0f}%) - نقترح إعادة المحاولة!")
    else:
        st.error(f"📚 تحتاج إلى مراجعة كراسك والتركيز أكثر. النتيجة الحالية: {final_score} من {total_q} (نسبة {percentage:.0f}%)")
        
    st.write("---")
    
    if st.button("🔄 العودة إلى الواجهة الرئيسية وتجربة تحدي آخر", use_container_width=True, type="primary"):
        st.session_state.step = "main"
        st.session_state.selected_field = None
        st.session_state.selected_lesson = None
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.rerun()


