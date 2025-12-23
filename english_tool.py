import streamlit as st

# --- 页面配置 ---
st.set_page_config(page_title="英语教学规划生成器专业版", layout="centered")

# ==========================================
# 左侧侧边栏：档案录入
# ==========================================
st.sidebar.markdown("### 学生档案录入")

# 1. 年龄
st.sidebar.markdown("**1. 年龄阶段**")
age = st.sidebar.number_input("填写年龄 (周岁)", min_value=2, max_value=15, value=6, step=1, label_visibility="collapsed")
brain_stage = "处于右脑感官期" if age < 7 else "处于左脑逻辑期"
st.sidebar.caption(f"当前设定: {age} 岁 | {brain_stage}")
st.sidebar.divider()

# 2. 学段
st.sidebar.markdown("**2. 就读学段**")
school_stage = st.sidebar.radio(
    "就读学段",
    ("幼儿园 (时间充裕)", "小学 (时间碎片化)"),
    label_visibility="collapsed"
)
st.sidebar.divider()

# 3. 现状
st.sidebar.markdown("**3. 英语现状**")
history_options = {
    "zero": "1) 零基础 (完全无接触)",
    "basic_home": "2) 家庭启蒙 (只知皮毛)",
    "intl_silent": "3) 国际园 (听懂但不说)",
    "primary_struggle": "4) 校内掉队 (排斥/吃力)",
    "ket_pass": "5) 优等生 (KET已过)",
    "toefl_jr": "6) 学术转型 (冲小托福)"
}
background_key = st.sidebar.selectbox(
    "英语学习现状",
    options=list(history_options.keys()),
    format_func=lambda x: history_options[x],
    label_visibility="collapsed"
)
st.sidebar.divider()

# 生成按钮
generate_btn = st.sidebar.button("生成定制方案", type="primary")

# ==========================================
# 核心逻辑区 (纯中文处理)
# ==========================================

def get_analysis_pure_cn(bg_key):
    if bg_key == "zero": return "听音辨义能力缺失", "母语式浸润法：首要任务是建立声音与图像的直接反射，严禁让孩子背诵字母或拼写。"
    if bg_key == "basic_home": return "知识点碎片化", "体系化重构：目前的英语知识是孤立的，需通过分级阅读将单词串联成有意义的句子。"
    if bg_key == "intl_silent": return "语言沉默期", "强制性输出策略：孩子听力已溢出，需利用复述练习逼孩子开口说整句，打通口语通道。"
    if bg_key == "primary_struggle": return "防御性排斥心理", "降维打击策略：暂时脱离校内高压评价体系，用简单的自然拼读规则重塑自信。"
    if bg_key == "ket_pass": return "中级化石化现象", "精准度训练：重点攻克长难句的语法拆解，解决凭语感蒙题的问题，提升学术严谨度。"
    if bg_key == "toefl_jr": return "学术认知缺口", "学术英语转型：生活类英语已饱和，必须引入科普、历史等非虚构类阅读材料。"
    return "常规发展", "按部就班推进。"

def get_schedule_pure_cn(stage, bg_key):
    is_kindy = "幼儿园" in stage
    if is_kindy:
        time = "45-60 分钟 / 天"
        focus = "兴趣激发 & 听力输入"
        weekdays = ["晨间: 英文儿歌磨耳朵 (15分钟)", "放学: 亲子绘本共读 (20分钟)", "晚间: 睡前故事音频 (10分钟)"]
        weekend = ["生活实践: 超市/公园实物指认", "家庭游戏: 听指令做动作"]
    else:
        time = "15-20 分钟 / 天"
        focus = "效率优先 & 解决痛点"
        weekdays = ["核心任务 (15分钟)", "错题速览 (5分钟)"]
        if bg_key == "primary_struggle": weekdays = ["专项: 自然拼读卡片 (10分钟)", "校内: 课文跟读 (10分钟)"]
        if bg_key == "ket_pass": weekdays = ["精读: 长难句分析 (15分钟)", "语法: 专项刷题 (10分钟)"]
        weekend = ["影视: 原版电影/纪录片", "阅读: 章节书自由阅读"]
    return time, focus, weekdays, weekend

def get_action_kit_pure_cn(bg_key):
    if bg_key == "intl_silent": return "破冰话术：装傻游戏", "家长故意指鹿为马（比如指着苹果说是香蕉），利用孩子的纠错本能诱导其开口。"
    if bg_key == "primary_struggle": return "心理建设：三明治反馈法", "第一步先肯定具体的优点，第二步提出微小的修正建议，第三步再次鼓励。严禁直接批评。"
    if bg_key == "ket_pass": return "学术工具：长难句拆解法", "三步走：1.圈出动词；2.括号括掉修饰语（砍枝叶）；3.提取主谓宾（抓主干）。"
    if bg_key == "zero": return "全身反应互动法", "家长发出口令（如摸鼻子），自己先做示范，让孩子模仿动作，不强制孩子开口。"
    return "通用技巧：图片环游", "在读文字前，先引导孩子看图猜故事，通过提问激发好奇心，降低阅读畏难情绪。"

def get_resources_pure_cn(bg_key):
    # 书名和APP名称保留英文原名，方便家长搜索，但移除括号内的英文说明
    books = []
    apps = []
    if bg_key == "zero":
        books = ["《Brown Bear, Brown Bear》", "《The Very Hungry Caterpillar》"]
        apps = ["Super Simple Songs", "Starfall"]
    elif bg_key == "basic_home":
        books = ["《Oxford Reading Tree》 (牛津树)", "《I Can Read》 Biscuit系列"]
        apps = ["Khan Kids", "伴鱼绘本"]
    elif bg_key == "intl_silent":
        books = ["《Elephant & Piggie》", "《Don't Let the Pigeon Drive the Bus》"]
        apps = ["英语趣配音", "Talk to Me in English"]
    elif bg_key == "primary_struggle":
        books = ["《Phonics Kids》", "《Dog Man》"]
        apps = ["多邻国", "小学英语同步点读"]
    elif bg_key == "ket_pass":
        books = ["《English Grammar in Use》", "《Great Writing 1》"]
        apps = ["Quizlet", "Newsela"]
    elif bg_key == "toefl_jr":
        books = ["《Reading Explorer》", "《Wonder》"]
        apps = ["TED / TED-Ed", "Achieve3000"]
    return books, apps

# ==========================================
# 右侧主界面：仪表盘
# ==========================================

st.title("英语阶段性教学规划书")
# 这里换成了高大上的中文理论背书
st.markdown("基于认知语言学与支架式教学理论的深度定制方案")
st.markdown("---")

if generate_btn:
    # 获取数据
    problem, solution = get_analysis_pure_cn(background_key)
    time_cost, core_focus, w_plan, we_plan = get_schedule_pure_cn(school_stage, background_key)
    kit_title, kit_content = get_action_kit_pure_cn(background_key)
    book_list, app_list = get_resources_pure_cn(background_key)
    
    # 1. 诊断
    st.subheader("第一部分：深度诊断")
    c1, c2 = st.columns([1,2])
    with c1: st.markdown(f"**核心症结**\n\n{problem}") # 去掉斜体，更稳重
    with c2: st.markdown(f"**教学策略**\n\n{solution}")
    st.markdown(" ")

    # 2. 计划
    st.subheader("第二部分：本周执行计划")
    m1, m2 = st.columns(2)
    m1.metric("每日时间预算", time_cost)
    m2.metric("阶段核心指标", core_focus)
    st.markdown(" ")
    
    t1, t2 = st.tabs(["平日计划 (周一至周五)", "周末计划 (周六日)"])
    with t1: 
        for i in w_plan: st.markdown(f"• {i}")
    with t2: 
        for i in we_plan: st.markdown(f"• {i}")
    st.markdown(" ")

    # 3. 资源
    st.subheader("第三部分：推荐资源配置")
    rc1, rc2 = st.columns(2)
    with rc1:
        st.markdown("**推荐书单**") 
        for b in book_list: st.markdown(f"• {b}")
    with rc2:
        st.markdown("**推荐APP/视频**")
        for a in app_list: st.markdown(f"• {a}")

    # 4. 锦囊
    st.markdown(" ")
    st.subheader("第四部分：家校配合实操锦囊")
    # 使用 markdown 引用块代替彩色框，更像文档
    st.markdown(f"> **{kit_title}**\n\n{kit_content}")

else:
    # 初始空状态
    st.markdown("""
    <div style="text-align: center; color: #888; padding: 50px;">
        <p>请在左侧录入学生档案</p>
        <p>点击按钮生成方案</p>
    </div>
    """, unsafe_allow_html=True)
