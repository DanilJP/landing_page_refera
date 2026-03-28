import streamlit as st

st.set_page_config(page_title="Refera", layout="wide", page_icon="📊")

# ==========================
# STYLE
# ==========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

/* FUNDO */
section[data-testid="stMain"] {
    background: radial-gradient(ellipse 80% 60% at 50% -10%, #1e1b4b 0%, #0f0f1a 55%, #020617 100%);
    min-height: 100vh;
}

/* ESCONDE HEADER STREAMLIT */
header[data-testid="stHeader"] {
    background: transparent;
}

/* SCROLLBAR */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0f0f1a; }
::-webkit-scrollbar-thumb { background: #6366f1; border-radius: 4px; }

/* ────────── HERO ────────── */
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 52px;
    font-weight: 800;
    line-height: 1.05;
    color: #f8fafc;
    letter-spacing: -1.5px;
}

@media (max-width: 768px) {
    .hero-title { font-size: 34px; }
}

.hero-gradient {
    background: linear-gradient(100deg, #818cf8 0%, #34d399 50%, #38bdf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.subtitle {
    color: #94a3b8;
    font-size: 17px;
    line-height: 1.65;
    max-width: 460px;
    font-weight: 300;
}

/* ────────── BOTÃO PRINCIPAL ────────── */
.cta-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    height: 3.4em;
    border-radius: 999px;
    background: linear-gradient(90deg, #6366f1, #4f46e5);
    color: #fff !important;
    font-weight: 600;
    font-size: 15px;
    border: none;
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.2s, box-shadow 0.2s;
    letter-spacing: 0.01em;
}
.cta-btn:hover {
    transform: scale(1.03);
    box-shadow: 0 0 48px rgba(99,102,241,0.55);
}

/* ────────── DIVIDER ────────── */
hr[data-testid="stDivider"] {
    border-color: rgba(255,255,255,0.06) !important;
    margin: 48px 0 !important;
}

/* ────────── IMAGE CARD ────────── */
.image-card {
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 30px 80px rgba(0,0,0,0.6), 0 0 0 1px rgba(99,102,241,0.08);
    transition: 0.4s ease;
}
.image-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 48px 100px rgba(0,0,0,0.8), 0 0 0 1px rgba(99,102,241,0.18);
}

/* ────────── SECTION TITLES ────────── */
.section-label {
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #818cf8;
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.2);
    padding: 4px 12px;
    border-radius: 999px;
    margin-bottom: 14px;
}

.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 36px;
    font-weight: 700;
    color: #f1f5f9;
    letter-spacing: -0.8px;
    line-height: 1.15;
    margin: 0 0 8px 0;
}

.section-sub {
    color: #64748b;
    font-size: 15px;
    font-weight: 300;
    margin-top: 4px;
}

/* ────────── PROBLEMA / GLASS CARD ────────── */
.problem-card {
    background: linear-gradient(135deg, rgba(239,68,68,0.06) 0%, rgba(15,15,26,0.8) 100%);
    border-radius: 20px;
    padding: 36px;
    border: 1px solid rgba(239,68,68,0.12);
    position: relative;
    overflow: hidden;
}
.problem-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(239,68,68,0.4), transparent);
}
.problem-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 18px;
    padding: 16px 18px;
    background: rgba(239,68,68,0.04);
    border-radius: 12px;
    border: 1px solid rgba(239,68,68,0.08);
}
.problem-icon {
    font-size: 20px;
    flex-shrink: 0;
    margin-top: 2px;
}
.problem-text-title {
    font-family: 'Syne', sans-serif;
    font-weight: 600;
    font-size: 15px;
    color: #f1f5f9;
    margin-bottom: 3px;
}
.problem-text-sub {
    font-size: 13px;
    color: #64748b;
    font-weight: 300;
}
.problem-cta {
    margin-top: 24px;
    font-size: 14px;
    color: #ef4444;
    font-weight: 500;
    padding: 12px 16px;
    background: rgba(239,68,68,0.07);
    border-radius: 10px;
    border-left: 3px solid #ef4444;
}

/* ────────── SOLUÇÃO ────────── */
.solution-card {
    background: linear-gradient(135deg, rgba(99,102,241,0.07) 0%, rgba(15,15,26,0.8) 100%);
    border-radius: 20px;
    padding: 36px;
    border: 1px solid rgba(99,102,241,0.14);
    position: relative;
    overflow: hidden;
}
.solution-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,102,241,0.5), transparent);
}
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 14px 20px;
    border-radius: 14px;
    margin-bottom: 12px;
    width: 100%;
    font-family: 'Syne', sans-serif;
    font-weight: 600;
    font-size: 15px;
    transition: transform 0.2s;
}
.status-badge:hover { transform: translateX(4px); }
.status-badge.aprovado {
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.18);
    color: #4ade80;
}
.status-badge.atencao {
    background: rgba(234,179,8,0.08);
    border: 1px solid rgba(234,179,8,0.18);
    color: #facc15;
}
.status-badge.deteriorando {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.18);
    color: #f87171;
}
.status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}
.dot-green { background: #4ade80; box-shadow: 0 0 8px #4ade80; }
.dot-yellow { background: #facc15; box-shadow: 0 0 8px #facc15; }
.dot-red { background: #f87171; box-shadow: 0 0 8px #f87171; }

.solution-summary {
    margin-top: 24px;
    padding: 18px;
    background: rgba(99,102,241,0.06);
    border-radius: 12px;
    border: 1px solid rgba(99,102,241,0.12);
    color: #cbd5e1;
    font-size: 14px;
    font-weight: 300;
    line-height: 1.6;
}
.solution-summary strong {
    color: #a5b4fc;
    font-weight: 600;
}

/* ────────── COMO FUNCIONA ────────── */
.steps-wrapper {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 8px;
}
@media (max-width: 768px) {
    .steps-wrapper { grid-template-columns: 1fr; }
}
.step-card {
    background: rgba(255,255,255,0.025);
    border-radius: 18px;
    padding: 28px 24px;
    border: 1px solid rgba(255,255,255,0.06);
    position: relative;
    transition: border-color 0.3s, transform 0.3s;
}
.step-card:hover {
    border-color: rgba(99,102,241,0.3);
    transform: translateY(-4px);
}
.step-number {
    font-family: 'Syne', sans-serif;
    font-size: 42px;
    font-weight: 800;
    color: rgba(99,102,241,0.15);
    line-height: 1;
    margin-bottom: 14px;
    letter-spacing: -2px;
}
.step-title {
    font-family: 'Syne', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: #f1f5f9;
    margin-bottom: 8px;
}
.step-desc {
    font-size: 13px;
    color: #64748b;
    font-weight: 300;
    line-height: 1.6;
}

/* ────────── COMPARATIVO ────────── */
.compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 8px;
}
@media (max-width: 768px) {
    .compare-grid { grid-template-columns: 1fr; }
}
.compare-col {
    border-radius: 20px;
    padding: 28px;
    border: 1px solid;
}
.compare-col.sem {
    background: rgba(239,68,68,0.04);
    border-color: rgba(239,68,68,0.1);
}
.compare-col.com {
    background: rgba(34,197,94,0.04);
    border-color: rgba(34,197,94,0.1);
}
.compare-header {
    font-family: 'Syne', sans-serif;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 20px;
    padding-bottom: 14px;
    border-bottom: 1px solid;
}
.compare-col.sem .compare-header {
    color: #f87171;
    border-color: rgba(239,68,68,0.15);
}
.compare-col.com .compare-header {
    color: #4ade80;
    border-color: rgba(34,197,94,0.15);
}
.compare-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 14px;
    font-size: 14px;
    color: #94a3b8;
    font-weight: 300;
    line-height: 1.5;
}
.compare-item span {
    flex-shrink: 0;
    font-size: 16px;
}

/* ────────── O QUE VOCÊ RECEBE ────────── */
.deliverables-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-top: 8px;
}
@media (max-width: 900px) {
    .deliverables-grid { grid-template-columns: repeat(2, 1fr); }
}
.deliverable-card {
    background: rgba(255,255,255,0.025);
    border-radius: 16px;
    padding: 24px 18px;
    border: 1px solid rgba(255,255,255,0.06);
    text-align: center;
    transition: border-color 0.3s, transform 0.3s, background 0.3s;
}
.deliverable-card:hover {
    border-color: rgba(99,102,241,0.3);
    transform: translateY(-4px);
    background: rgba(99,102,241,0.05);
}
.deliverable-icon {
    font-size: 28px;
    margin-bottom: 12px;
}
.deliverable-title {
    font-family: 'Syne', sans-serif;
    font-size: 14px;
    font-weight: 600;
    color: #e2e8f0;
    margin-bottom: 6px;
}
.deliverable-desc {
    font-size: 12px;
    color: #475569;
    font-weight: 300;
}

/* ────────── PREÇO ────────── */
.price-wrapper {
    max-width: 460px;
    margin: 0 auto;
}
.price-card {
    background: linear-gradient(135deg, rgba(99,102,241,0.08) 0%, rgba(15,15,26,0.9) 100%);
    border-radius: 28px;
    padding: 48px 40px;
    text-align: center;
    border: 1px solid rgba(99,102,241,0.2);
    position: relative;
    overflow: hidden;
}
.price-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,102,241,0.7), transparent);
}
.price-badge {
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #818cf8;
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.2);
    padding: 5px 14px;
    border-radius: 999px;
    margin-bottom: 24px;
}
.price-old {
    font-size: 16px;
    color: #475569;
    text-decoration: line-through;
    margin-bottom: 4px;
}
.price-amount {
    font-family: 'Syne', sans-serif;
    font-size: 68px;
    font-weight: 800;
    color: #f8fafc;
    line-height: 1;
    letter-spacing: -3px;
}
.price-period {
    font-size: 18px;
    color: #64748b;
    font-weight: 300;
    margin-left: 4px;
    letter-spacing: 0;
}
.price-savings {
    display: inline-block;
    margin-top: 14px;
    font-size: 12px;
    color: #4ade80;
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.15);
    padding: 4px 12px;
    border-radius: 999px;
    font-weight: 500;
}
.price-guarantee {
    margin-top: 20px;
    font-size: 13px;
    color: #475569;
    font-weight: 300;
}

/* ────────── SOCIAL PROOF ────────── */
.social-proof {
    text-align: center;
    margin-top: 32px;
    color: #334155;
    font-size: 13px;
    font-weight: 300;
    letter-spacing: 0.03em;
}

/* ────────── DISCLAIMER ────────── */
.disclaimer {
    text-align: center;
    font-size: 12px;
    color: #334155;
    font-weight: 300;
    margin-top: 24px;
    padding: 16px;
    border-top: 1px solid rgba(255,255,255,0.04);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HERO
# ==========================
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("""
    <div class="hero-title" style="margin-bottom:20px;">
        Pare de investir<br>no escuro.<br>
        <span class="hero-gradient">Tenha clareza real.</span>
    </div>
    <div class="subtitle">
        Um sistema que transforma dados e relatórios em decisões claras de risco, qualidade e estabilidade — em segundos.
    </div>
    """, unsafe_allow_html=True)

    st.write('')

    st.markdown("""
    <a class="cta-btn" href="https://wa.me/5513981832920?text=Ol%C3%A1,%20conheci%20o%20Refera%20e%20gostaria%20de%20solicitar%20acesso%20para%20conhecer%20melhor%20a%20plataforma%20e%20suas%20an%C3%A1lises%20%F0%9F%93%8A" target="_blank">
        🚀 Quero entender melhor o Refera
    </a>
    """, unsafe_allow_html=True)

    st.markdown('<div class="social-proof">Usado por investidores que querem mais controle e menos achismo</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    st.image("fii.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==========================
# PROBLEMA + SOLUÇÃO (lado a lado)
# ==========================
col_prob, col_sol = st.columns(2, gap="large")

with col_prob:
    st.markdown("""
    <div class="section-label">O problema</div>
    <div class="section-title">Você está<br>no escuro</div>
    <div class="section-sub">O que a maioria dos investidores enfrenta</div>
    """, unsafe_allow_html=True)
    st.write('')
    st.markdown("""
    <div class="problem-card">
        <div class="problem-item">
            <div class="problem-icon">🕳️</div>
            <div>
                <div class="problem-text-title">Risco invisível</div>
                <div class="problem-text-sub">Problemas reais que você não consegue enxergar nos relatórios</div>
            </div>
        </div>
        <div class="problem-item">
            <div class="problem-icon">⏰</div>
            <div>
                <div class="problem-text-title">Descobre tarde demais</div>
                <div class="problem-text-sub">Você reage depois da queda, não antes</div>
            </div>
        </div>
        <div class="problem-item">
            <div class="problem-icon">📄</div>
            <div>
                <div class="problem-text-title">Perdido nos relatórios</div>
                <div class="problem-text-sub">Páginas e páginas sem clareza sobre o que importa</div>
            </div>
        </div>
        <div class="problem-cta">👉 E você paga por isso com prejuízo</div>
    </div>
    """, unsafe_allow_html=True)

with col_sol:
    st.markdown("""
    <div class="section-label">A solução</div>
    <div class="section-title">Clareza em<br>3 status</div>
    <div class="section-sub">O Refera transforma tudo em um sistema simples</div>
    """, unsafe_allow_html=True)
    st.write('')
    st.markdown("""
    <div class="solution-card">
        <div class="status-badge aprovado">
            <div class="status-dot dot-green"></div>
            ✅ Aprovado — seguro pra manter
        </div>
        <div class="status-badge atencao">
            <div class="status-dot dot-yellow"></div>
            ⚠️ Atenção — fique de olho
        </div>
        <div class="status-badge deteriorando">
            <div class="status-dot dot-red"></div>
            ❌ Deteriorando — hora de agir
        </div>
        <div class="solution-summary">
            <strong>Você entende em segundos.</strong> Sem precisar estudar relatório por relatório. 
            O modelo analisa, classifica e entrega o diagnóstico — você decide com clareza.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================
# COMO FUNCIONA
# ==========================
st.markdown("""
<div class="section-label">Como funciona</div>
<div class="section-title">Simples, direto e sem esforço</div>
<div class="section-sub">Três passos entre os dados brutos e a sua decisão</div>
""", unsafe_allow_html=True)
st.write('')

st.markdown("""
<div class="steps-wrapper">
    <div class="step-card">
        <div class="step-number">01</div>
        <div class="step-title">O modelo analisa</div>
        <div class="step-desc">Dados financeiros e relatórios são processados automaticamente, sem esforço da sua parte.</div>
    </div>
    <div class="step-card">
        <div class="step-number">02</div>
        <div class="step-title">Classifica os FIIs</div>
        <div class="step-desc">Cada fundo recebe um status — Aprovado, Atenção ou Deteriorando — com base em critérios reais.</div>
    </div>
    <div class="step-card">
        <div class="step-number">03</div>
        <div class="step-title">Você decide rápido</div>
        <div class="step-desc">Sem precisar estudar tudo. Você chega já com a leitura feita e decide com clareza.</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# COMPARATIVO SEM vs COM
# ==========================
st.markdown("""
<div class="section-label">Por que usar</div>
<div class="section-title">Sem clareza, você perde</div>
<div class="section-sub">Veja a diferença de investir com e sem o Refera</div>
""", unsafe_allow_html=True)
st.write('')

st.markdown("""
<div class="compare-grid">
    <div class="compare-col sem">
        <div class="compare-header">❌ Sem o Refera</div>
        <div class="compare-item"><span>🕳️</span> Risco invisível que só aparece tarde demais</div>
        <div class="compare-item"><span>😰</span> Decisões baseadas em emoção e achismo</div>
        <div class="compare-item"><span>📄</span> Horas perdidas em relatórios sem conclusão</div>
        <div class="compare-item"><span>📉</span> Carteira sem critério de qualidade</div>
        <div class="compare-item"><span>💸</span> Perda de capital por falta de clareza</div>
    </div>
    <div class="compare-col com">
        <div class="compare-header">✅ Com o Refera</div>
        <div class="compare-item"><span>🔍</span> Risco identificado antes de virar problema</div>
        <div class="compare-item"><span>🧠</span> Decisões com estrutura e critério definido</div>
        <div class="compare-item"><span>⚡</span> Diagnóstico completo em segundos</div>
        <div class="compare-item"><span>📊</span> Carteira com qualidade monitorada</div>
        <div class="compare-item"><span>🛡️</span> Patrimônio protegido com mais controle</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# O QUE VOCÊ RECEBE
# ==========================
st.markdown("""
<div class="section-label">O que você recebe</div>
<div class="section-title">Tudo que você precisa</div>
<div class="section-sub">Dentro de uma única plataforma</div>
""", unsafe_allow_html=True)
st.write('')

st.markdown("""
<div class="deliverables-grid">
    <div class="deliverable-card">
        <div class="deliverable-icon">📊</div>
        <div class="deliverable-title">Score Refera</div>
        <div class="deliverable-desc">Nota objetiva de qualidade por FII</div>
    </div>
    <div class="deliverable-card">
        <div class="deliverable-icon">🏆</div>
        <div class="deliverable-title">Ranking</div>
        <div class="deliverable-desc">Os melhores e piores classificados</div>
    </div>
    <div class="deliverable-card">
        <div class="deliverable-icon">📄</div>
        <div class="deliverable-title">Resumos</div>
        <div class="deliverable-desc">Relatórios digeridos sem enrolação</div>
    </div>
    <div class="deliverable-card">
        <div class="deliverable-icon">📈</div>
        <div class="deliverable-title">Diagnóstico</div>
        <div class="deliverable-desc">Análise completa da sua carteira</div>
    </div>
    <div class="deliverable-card">
        <div class="deliverable-icon">🧑‍🤝‍🧑</div>
        <div class="deliverable-title">Comunidade</div>
        <div class="deliverable-desc">Outros investidores com o mesmo foco</div>
    </div>
    <div class="deliverable-card">
        <div class="deliverable-icon">🚨</div>
        <div class="deliverable-title">Alertas Inteligentes</div>
        <div class="deliverable-desc">Mudanças relevantes nos FIIs em tempo real</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# VISUAL DA CARTEIRA
# ==========================
col1, col2 = st.columns([1, 1.1], gap="large")

with col1:
    st.markdown("""
    <div class="section-label">Visualização</div>
    <div class="section-title">Sua carteira em<br>um só lugar</div>
    <div class="section-sub" style="margin-top:12px;">
        Risco, qualidade e concentração centralizados. 
        Veja exatamente onde está a fragilidade — antes de se tornar um problema.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    st.image("carteira.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==========================
# PREÇO
# ==========================
st.markdown("""
<div style="text-align:center;">
    <div class="section-label">Acesso</div>
    <div class="section-title">Comece agora</div>
    <div class="section-sub">Sem risco. Cancele quando quiser.</div>
</div>
""", unsafe_allow_html=True)

st.write('')

st.markdown("""
<div class="price-wrapper">
    <div class="price-card">
        <div class="price-badge">Plano de Lançamento</div>
        <div class="price-old">De R$49,90/mês</div>
        <div>
            <span class="price-amount">R$19<span style="font-size:36px;">,90</span></span>
            <span class="price-period">/mês</span>
        </div>
        <div class="price-savings">🎉 Você economiza R$30 por mês</div>
        <div class="price-guarantee">🔒 Acesso imediato · Sem fidelidade · Cancele quando quiser</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write('')

st.markdown("""
<a class="cta-btn" href="https://wa.me/5513981832920?text=Ol%C3%A1,%20conheci%20o%20Refera%20e%20gostaria%20de%20solicitar%20acesso%20para%20avaliar%20a%20plataforma%20e%20seus%20insights%20%F0%9F%93%8A" target="_blank">
    💰 Quero acesso ao Refera
</a>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# CTA FINAL
# ==========================
st.markdown("""
<div style="text-align:center; padding: 20px 0 32px;">
    <div class="section-title">Pare de investir no escuro</div>
    <div class="section-sub" style="margin-top: 10px; font-size: 16px;">
        Tenha clareza sobre seus FIIs a partir de hoje
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<a class="cta-btn" href="https://wa.me/5513981832920?text=Ol%C3%A1,%20conheci%20o%20Refera%20e%20gostaria%20de%20solicitar%20acesso%20para%20conhecer%20melhor%20a%20plataforma%20e%20suas%20an%C3%A1lises%20%F0%9F%93%8A" target="_blank">
    🚀 Quero começar agora
</a>
""", unsafe_allow_html=True)

# ==========================
# DISCLAIMER
# ==========================
st.markdown("""
<div class="disclaimer">
    O Refera não faz recomendação de investimento. Considere buscar um consultor financeiro antes de decidir.
</div>
""", unsafe_allow_html=True)
