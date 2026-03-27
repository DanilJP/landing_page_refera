import streamlit as st

st.set_page_config(page_title="Refera", layout="wide", page_icon="📊")

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
.hero-title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.05;
    color: #f8fafc;
}

@media (max-width: 768px) {
    .hero-title {
        font-size: 36px;
    }
}

.hero-gradient {
    background: linear-gradient(90deg, #6366f1, #22c55e, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #94a3b8;
    font-size: 18px;
}

/* BOTÃO */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #4f46e5);
    color: white;
    border-radius: 999px;
    height: 3.2em;
    font-weight: 600;
    border: none;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 40px rgba(99,102,241,0.5);
}

/* CARD */
.glass {
    background: rgba(255,255,255,0.025);
    backdrop-filter: blur(12px);
    border-radius: 14px;
    padding: 14px 16px;
    border: 1px solid rgba(255,255,255,0.06);
    display: inline-block;
    width: 100%;
}

/* GRID */
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-top: 20px;
}

@media (max-width: 768px) {
    .grid {
        grid-template-columns: 1fr;
    }
}

/* IMAGE */
.image-card {
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 30px 80px rgba(0,0,0,0.6);
    transition: 0.4s;
}

.image-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 40px 100px rgba(0,0,0,0.8);
}

/* TITLES */
.section-title {
    font-size: 32px;
    font-weight: 700;
    color: #f1f5f9;
    letter-spacing: -0.5px;
}

.section-sub {
    color: #94a3b8;
    font-size: 15px;
    margin-top: 6px;
}

/* PRICE */
.price-card {
    background: rgba(255,255,255,0.04);
    border-radius: 25px;
    padding: 50px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.1);
}

.price {
    font-size: 48px;
    font-weight: 800;
    color: #f8fafc;
}

/* ANIMAÇÃO */
.fade-in {
    animation: fadeInUp 0.6s ease forwards;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HERO
# ==========================
col1, col2 = st.columns([1.2,1])

with col1:
    st.markdown("""
    <div class="hero-title">
    Pare de investir no escuro.<br>
    <span class="hero-gradient">Tenha clareza real</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">
    Um sistema que transforma dados e relatórios em decisões claras de risco, qualidade e estabilidade.
    </div>
    """, unsafe_allow_html=True)

    st.write('')
    if st.button("🚀 Começar agora", use_container_width=True):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={HOTMART_LINK}">', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    st.image("fii.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================
# SOCIAL PROOF
# ==========================
st.markdown("""
<div style="text-align:center; margin-top:40px; color:#64748b;">
Usado por investidores que querem mais controle e menos achismo
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# PROBLEMA
# ==========================
st.markdown('<div class="section-title">O problema</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass">

A maioria dos investidores:

- Não entende o risco real  
- Descobre problemas tarde demais  
- Se perde em relatórios  

👉 E paga por isso com prejuízo

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# SOLUÇÃO
# ==========================
st.markdown('<div class="section-title">A solução</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass">

O Refera transforma tudo em um sistema simples:

✅ Aprovado  
⚠️ Atenção  
❌ Deteriorando  

<b>Você entende em segundos.</b>

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# COMO FUNCIONA
# ==========================
st.markdown('<div class="section-title">Como funciona</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Simples, direto e sem esforço</div>', unsafe_allow_html=True)

st.markdown("""
<div class="grid fade-in">

<div class="glass">
<b>1. O modelo analisa</b><br>
<small style="color:#94a3b8;">Dados e relatórios automaticamente</small>
</div>

<div class="glass">
<b>2. Classifica os FIIs</b><br>
<small style="color:#94a3b8;">Aprovado, atenção ou deteriorando</small>
</div>

<div class="glass">
<b>3. Você entende rápido</b><br>
<small style="color:#94a3b8;">Sem precisar estudar tudo</small>
</div>

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# POR QUE USAR
# ==========================
st.markdown('<div class="section-title">Sem isso, você está no escuro</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">A maioria dos investidores descobre tarde demais</div>', unsafe_allow_html=True)

st.markdown("""
<div class="grid fade-in">

<div class="glass">
❌ <b>Risco invisível</b><br>
<small style="color:#94a3b8;">Problemas que você não vê</small>
</div>

<div class="glass">
⚠️ <b>Decisão atrasada</b><br>
<small style="color:#94a3b8;">Você reage depois da queda</small>
</div>

<div class="glass">
💸 <b>Perda de dinheiro</b><br>
<small style="color:#94a3b8;">Por falta de clareza</small>
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="grid fade-in">

<div class="glass">
✅ <b>Clareza imediata</b><br>
<small style="color:#94a3b8;">Você entende o cenário</small>
</div>

<div class="glass">
📊 <b>Mais controle</b><br>
<small style="color:#94a3b8;">Sua carteira faz sentido</small>
</div>

<div class="glass">
🧠 <b>Decisão melhor</b><br>
<small style="color:#94a3b8;">Menos emoção, mais estrutura</small>
</div>

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# PRODUTO
# ==========================
st.markdown('<div class="section-title">O que você recebe</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass">

📊 Score Refera  
🧠 Ranking  
📄 Resumos  
📈 Diagnóstico da carteira  
🧑‍🤝‍🧑 Comunidade  

</div>
""", unsafe_allow_html=True)

# ==========================
# VISUAL
# ==========================
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">Visualize sua carteira</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Risco, qualidade e concentração em um só lugar</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    st.image("carteira.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==========================
# PREÇO
# ==========================
st.markdown('<div class="section-title center-text">Comece agora</div>', unsafe_allow_html=True)

st.markdown("""
<div class="price-card">

<p style="color:#94a3b8;">Plano de lançamento</p>

<p style="text-decoration: line-through; color:#64748b;">
R$49,90
</p>

<p class="price">R$19,90<span style="font-size:16px;">/mês</span></p>

</div>
""", unsafe_allow_html=True)

st.write('')
if st.button("💰 Garantir acesso", use_container_width=True):
    st.markdown(f'<meta http-equiv="refresh" content="0; url={HOTMART_LINK}">', unsafe_allow_html=True)

st.divider()

# ==========================
# CTA FINAL
# ==========================
st.markdown("""
<div style="text-align:center;">
<div class="section-title">Pare de investir no escuro</div>
<div class="section-sub">Tenha clareza sobre seus FIIs hoje</div>
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Entrar no Refera", use_container_width=True):
    st.markdown(f'<meta http-equiv="refresh" content="0; url={HOTMART_LINK}">', unsafe_allow_html=True)

# ==========================
# DISCLAIMER
# ==========================
st.caption("O Refera não faz recomendação de investimento.")