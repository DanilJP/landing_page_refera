import streamlit as st

# ==========================
# CONFIG
# ==========================
st.set_page_config(
    page_title="Refera",
    layout="wide",
    page_icon="📊"
)

HOTMART_LINK = "https://SEU_LINK_HOTMART_AQUI"

# ==========================
# STYLE
# ==========================
st.markdown("""
<style>

/* FUNDO */
body {
    background: radial-gradient(circle at top, #0f172a 0%, #020617 100%);
}

/* HERO */
.hero {
    padding: 80px 0;
}

.hero-title {
    font-size: 56px;
    font-weight: 800;
    line-height: 1.05;
    color: #f8fafc;
}

.hero-gradient {
    background: linear-gradient(90deg, #6366f1, #22c55e, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #94a3b8;
    font-size: 18px;
    margin-top: 20px;
}

/* BOTÃO */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #4f46e5);
    color: white;
    border-radius: 999px;
    height: 3.2em;
    font-weight: 600;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 40px rgba(99,102,241,0.5);
}

/* GLASS CARD */
.glass {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* GRID */
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

/* TEXTO */
.section-title {
    font-size: 36px;
    font-weight: 700;
    color: #f1f5f9;
}

.section-sub {
    color: #94a3b8;
    margin-top: 10px;
}

/* PRICE */
.price-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
    border-radius: 25px;
    padding: 50px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 30px 80px rgba(0,0,0,0.6);
}

.price {
    font-size: 48px;
    font-weight: 800;
    color: #f8fafc;
}

/* HOVER IMAGEM */
.img-hover {
    transition: 0.4s;
}
.img-hover:hover {
    transform: scale(1.04);
}

.image-card {
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 30px 80px rgba(0,0,0,0.6);
    transition: 0.4s;
}

.image-card:hover {
    transform: scale(1.02);
    box-shadow: 0 40px 100px rgba(0,0,0,0.8);
}
            
.social-proof {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
    margin-top: 40px;
    margin-bottom: 40px;
}

.avatars {
    display: flex;
}

.avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid #020617;
    margin-left: -10px;
    background-size: cover;
    background-position: center;
}

.social-text {
    color: #94a3b8;
    font-size: 14px;
}

.social-box {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 15px 25px;
    border-radius: 999px;
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

def section_title(title, subtitle=None):
    st.markdown(f"""
    <div style="margin-top:60px; margin-bottom:20px;">
        <h2 style="
            font-size:32px;
            font-weight:700;
            margin-bottom:5px;
        ">
            {title}
        </h2>
        {f'<p style="color:#aaa; font-size:16px;">{subtitle}</p>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)

# ==========================
# HERO
# ==========================
col1, col2 = st.columns([1.2,1])

with col1:
    st.title("📊 Refera")
    st.subheader("Pare de decidir no escuro em FIIs")

    st.markdown("""
    <div class="hero">

    <div class="hero-title">
    Pare de investir no escuro.<br>
    <span class="hero-gradient">Tenha clareza real</span>
    </div>

    <div class="subtitle">
    Um sistema que transforma dados e relatórios em decisões claras de risco, qualidade e estabilidade.
    </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Começar agora", use_container_width=True):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={HOTMART_LINK}">', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="img-hover">', unsafe_allow_html=True)
    st.image("fii.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==========================
# PROBLEMA
# ==========================
section_title(
    "Você não está vendo o risco real",
    "A maioria dos investidores só percebe quando já é tarde"
)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="box">

    <b>O problema não é investir.</b><br><br>

    É investir sem entender:

    - O risco real do fundo  
    - A qualidade da renda  
    - O que está deteriorando  

    <br>
    👉 E só perceber quando já caiu.

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="img-hover">', unsafe_allow_html=True)
    st.image("caindo_black.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("👉 Isso custa dinheiro.")

st.divider()

# ==========================
# SOLUÇÃO
# ==========================
section_title(
    "Clareza sobre seus FIIs em segundos",
    "Sem relatórios longos. Sem achismo."
)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    st.image("carteira.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="box">

    <b>O Refera resolve isso.</b><br><br>

    Transformando tudo em um sistema simples:

    ✅ Aprovado  
    ⚠️ Atenção  
    ❌ Deteriorando  

    <br>
    <b>Você entende em segundos o que antes levava horas.</b>

    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================
# OFERTA
# ==========================
section_title(
    "Tudo que você precisa em um só lugar",
    "Um sistema completo para analisar, entender e agir"
)

st.markdown("""
<div class="box">

<b>Você recebe acesso completo a:</b><br><br>

📊 Score Refera (qualidade + risco)  
🧠 Ranking dos FIIs  
📄 Resumo de relatórios gerenciais  
🔍 Análises individuais  
📈 2 diagnósticos mensais da sua carteira  
🧑‍🤝‍🧑 Comunidade exclusiva  

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# PREÇO (NOVA SEÇÃO)
# ==========================
section_title(
    "Comece com acesso completo",
    "Sem complicação. Sem compromisso longo."
)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("""
    <div class="section-title center-text">Comece agora</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="price-card">

    <p style="color:#94a3b8; font-size:14px;">Plano de lançamento</p>

    <p style="margin:10px 0;">
        <span style="text-decoration: line-through; color:#64748b; font-size:18px;">
            R$49,90
        </span>
    </p>

    <p class="price">
        R$19,90<span style="font-size:16px;">/mês</span>
    </p>

    <p style="color:#94a3b8;">Acesso completo à plataforma</p>

    </div>
    """, unsafe_allow_html=True)
    
st.markdown("""
<div class="center-text">
<span class="highlight">Menos de R$1 por dia para investir com mais segurança</span>
</div>
""", unsafe_allow_html=True)
st.markdown("")

if st.button("💰 Garantir acesso agora", use_container_width=True):
    st.markdown(
        f'<meta http-equiv="refresh" content="0; url={HOTMART_LINK}">',
        unsafe_allow_html=True
    )

st.markdown("👉 Oferta de lançamento para os primeiros usuários")

st.divider()

# ==========================
# DIFERENCIAL
# ==========================
st.markdown("""
<div class="section-title">Uma nova forma de analisar FIIs</div>
<div class="section-sub">Menos achismo. Mais estrutura.</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="grid">

<div class="glass">
🧠 <b>Clareza</b><br><br>
Entenda rapidamente o que está acontecendo
</div>

<div class="glass">
⚡ <b>Velocidade</b><br><br>
Análise em segundos
</div>

<div class="glass">
🛡️ <b>Segurança</b><br><br>
Reduza erros e decisões impulsivas
</div>

</div>
""", unsafe_allow_html=True)
st.divider()

#💻 SEÇÃO PRODUTO (cara de SaaS)
st.markdown("""
<div class="section-title">Tudo que você precisa</div>
<div class="section-sub">Um sistema completo para sua tomada de decisão</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass">

📊 Score Refera  
🧠 Ranking dos FIIs  
📄 Resumos gerenciais  
📈 Diagnóstico da carteira  
🧑‍🤝‍🧑 Comunidade  

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
    <div class="section-title">Visualize sua carteira</div>
    <div class="section-sub">
    Entenda risco, qualidade e concentração em um só lugar
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    st.image("carteira.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="section-title">Como funciona</div>
<div class="section-sub">Simples, rápido e direto ao ponto</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="grid">

<div class="glass">
<b>1. Análise</b><br><br>
O modelo processa dados e relatórios
</div>

<div class="glass">
<b>2. Classificação</b><br><br>
Cada FII recebe um status claro
</div>

<div class="glass">
<b>3. Decisão</b><br><br>
Você entende o cenário em segundos
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-title center-text">
Usado por investidores que querem mais controle
</div>
""", unsafe_allow_html=True)

# ==========================
# CTA FINAL
# ==========================
section_title(
    "Pare de investir no escuro",
    "Tenha clareza sobre seus FIIs hoje"
)
st.markdown("""
<div class="highlight center-text">
Pare de investir no escuro.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="center-text subtitle">
Tenha clareza sobre seus FIIs hoje.
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Entrar no Refera", use_container_width=True):
    st.markdown(
        f'<meta http-equiv="refresh" content="0; url={HOTMART_LINK}">',
        unsafe_allow_html=True
    )

st.divider()

# ==========================
# DISCLAIMER
# ==========================
st.caption("""
O Refera não realiza recomendações de investimento.
A ferramenta organiza informações para apoiar decisões.
""")