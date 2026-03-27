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

/* Botão */
.stButton>button {
    background: linear-gradient(90deg, #111, #333);
    color: white;
    border-radius: 10px;
    height: 3em;
    font-weight: 600;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #000, #444);
}

/* Card preço */
.price-card {
    background-color: #111;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    color: white;
}

.price {
    font-size: 40px;
    font-weight: bold;
}

.old-price {
    text-decoration: line-through;
    color: #aaa;
}

/* Hover imagem */
.img-hover {
    transition: 0.3s;
}
.img-hover:hover {
    transform: scale(1.05);
}
/* Texto refinado */
.subtitle {
    color: #aaa;
    font-size: 18px;
}

.section {
    margin-top: 40px;
    margin-bottom: 40px;
}

.highlight {
    font-size: 20px;
    font-weight: 600;
}

.box {
    background-color: #0e1117;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #222;
}

.center-text {
    text-align: center;
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
    <div class="subtitle">
    Pare de depender de achismo para investir em FIIs
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    O Refera transforma dados complexos em decisões claras.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    - Qualidade  
    - Risco  
    - Estabilidade  

    👉 Tudo em um único lugar
    """)

    if st.button("🚀 Acessar o Refera agora", use_container_width=True):
        st.markdown(
            f'<meta http-equiv="refresh" content="0; url={HOTMART_LINK}">',
            unsafe_allow_html=True
        )

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
    <b>A maioria dos investidores:</b><br><br>

    - Investe sem entender o risco real  
    - Descobre problemas tarde demais  
    - Se perde em relatórios complexos  
    - Toma decisões no escuro  

    <br>
    👉 <b>Isso impacta diretamente sua rentabilidade.</b>
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
    st.markdown('<div class="img-hover">', unsafe_allow_html=True)
    st.image("carteira.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="box">
    O Refera organiza tudo em um sistema claro:

    <br>

    ✅ Fundos aprovados  
    ⚠️ Fundos em alerta  
    ❌ Fundos deteriorando  

    <br>
    <b>Sem opinião. Sem ruído. Só sinal.</b>
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
    <div class="price-card">
        <p>Plano de lançamento</p>
        <p class="old-price">R$49,90/mês</p>
        <p class="price">R$19,90<span style="font-size:16px;">/mês</span></p>
        <p>Acesso completo à plataforma</p>
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
section_title(
    "Por que o Refera é diferente",
    "Você não precisa virar especialista para investir melhor"
)
col1, col2, col3, col4 = st.columns(4)

col1.markdown("🧠 Menos achismo")
col2.markdown("⚡ Decisão rápida")
col3.markdown("🛡️ Menos erro")
col4.markdown("📉 Risco antecipado")

st.divider()

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