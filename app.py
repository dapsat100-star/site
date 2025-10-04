
# -*- coding: utf-8 -*-
import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="MAVIPE Space Systems — DAP ATLAS",
    page_icon="favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

CSS = """
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 0.6rem; max-width: 1200px;}
.card {border: 1px solid rgba(255,255,255,.10); border-radius: 18px; padding: 16px; background: #0f1830;}
.badge {display:inline-block; padding:6px 10px; border-radius:999px; border: 1px solid #3ad0c6; color:#3ad0c6; background: rgba(58,208,198,.15); font-size:12px;}
.lead {color:#b8c4e6;}
.kpi {font-weight:700; color:#58e8dd;}
hr {opacity:.25}
.topbar {display:flex; align-items:center; gap:14px; margin-bottom: 8px;}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------- TOP BAR (LOGO + NOME) ----------
col_logo, col_title = st.columns([0.18, 0.82])
with col_logo:
    st.image("logo-mavipe.png", width=120)
with col_title:
    st.markdown("### MAVIPE Space Systems · DAP ATLAS")

st.markdown('<span class="badge">Plataforma DAP ATLAS • OGMP 2.0 L5 • InSAR</span>', unsafe_allow_html=True)

# ---------- HERO ----------
col1, col2 = st.columns([1.1, 0.9])
with col1:
    st.title("Geointeligência prática para decisões rápidas.")
    st.markdown("""<p class='lead'>
    Integramos <b>IA</b>, <b>imagens de satélite</b> (ópticas e SAR) e dados operacionais para entregar
    <b>insights acionáveis</b> em monitoramento ambiental, emissões de metano e integridade de ativos.
    </p>""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class='card'><h4>OGMP 2.0 L5</h4><div class='kpi'>Medição baseada em detecção</div>
        <small>Fluxo kg/h • Incerteza • Q/C</small></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='card'><h4>InSAR</h4><div class='kpi'>Milímetros/mês</div>
        <small>Deformação • Estabilidade</small></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='card'><h4>GeoINT</h4><div class='kpi'>Alertas proativos</div>
        <small>Dashboards • Relatórios PDF</small></div>""", unsafe_allow_html=True)

with col2:
    st.image("hero-dashboard.png", use_column_width=True, caption="Painel DAP ATLAS (ilustração)")

st.divider()

# ---------- SOLUÇÕES ----------
st.header("Soluções")
st.markdown("""<p class='lead'>Portfólio completo para <b>ambiente</b>, <b>óleo & gás</b> e <b>defesa & segurança</b>.</p>""", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""<div class='card'><b>Metano (CH₄)</b><h4>Monitoramento OGMP 2.0 Nível 5</h4>
    <p>Medições por fonte emissora, séries temporais, vento e estabilidade atmosférica. Relatórios PDF georreferenciados com faixas de incerteza e indicador de qualidade.</p></div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class='card'><b>InSAR</b><h4>Integridade de ativos</h4>
    <p>Deformação do terreno e estruturas (mm/mês), mapas de risco e recomendações operacionais. Integração com RCM/TerraSAR‑X/COSMO‑SkyMed.</p></div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""<div class='card'><b>GeoINT</b><h4>Inteligência operacional</h4>
    <p>Camadas contextuais, alertas e dashboards. Exportações em PDF e dados para integrações (API/CSV) na plataforma DAP ATLAS.</p></div>""", unsafe_allow_html=True)

st.divider()

# ---------- CASE ----------
st.header("Case em execução — Petrobras")
cl, cr = st.columns([1.1, 0.9])
with cl:
    st.markdown("""<p class='lead'>Projeto de <b>monitoramento de metano</b> com entregas em conformidade com <b>OGMP 2.0</b> e integração de camadas operacionais no DAP ATLAS.</p>""", unsafe_allow_html=True)
    st.markdown("""
    - Detecção por fonte e cálculo de fluxo (kg/h) com incerteza.  
    - Relatórios PDF com pluma, vento (direção/velocidade) e Q/C.  
    - Histórico e ranking de superemissores, priorização de manutenção.
    """)
with cr:
    st.image("case-petrobras.png", use_column_width=True, caption="Exemplo ilustrativo de relatório OGMP")

# ---------- CTA ----------
st.info("Quer ver um demo curto do DAP ATLAS? Agendamos uma chamada de 15 minutos e mostramos como os KPIs atendem seu caso.")
colA, colB = st.columns(2)
if colA.button("Agendar por e-mail"):
    assunto = "Demo DAP ATLAS"
    corpo = "Olá, gostaria de agendar um demo de 15 min."
    link = f"mailto:contato@dapsat.com?subject={quote(assunto)}&body={quote(corpo)}"
    st.markdown(f"[Clique para abrir seu e-mail]({link})")
if colB.button("Falar no WhatsApp"):
    numero = "50700000000"  # ajuste seu número com DDI
    texto = "Quero um demo do DAP ATLAS"
    st.markdown(f"[Abrir WhatsApp](https://wa.me/{numero}?text={quote(texto)})")

st.divider()

# ---------- SOBRE ----------
st.header("Sobre a MAVIPE")
st.markdown("""<p class='lead'>Fundada por profissionais com experiência em <b>centros de operações de satélites</b> e <b>geointeligência</b> no mercado privado, unimos tecnologia espacial e análise avançada para gerar valor prático.</p>""", unsafe_allow_html=True)

# ---------- CONTATO ----------
st.header("Contato")
with st.form("contato_form"):
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Seu nome", placeholder="Seu nome completo")
        email = st.text_input("E-mail", placeholder="seu@email.com")
    with col2:
        empresa = st.text_input("Empresa (opcional)", placeholder="Sua empresa")
        telefone = st.text_input("WhatsApp/Telefone (opcional)", placeholder="(+55) 11 99999-9999")
    msg = st.text_area("Como podemos ajudar?", placeholder="Descreva seu desafio…")
    enviar = st.form_submit_button("Gerar e-mail")
    if enviar:
        assunto = "Contato via site — MAVIPE"
        body = f"Nome: {nome}\nEmail: {email}\nEmpresa: {empresa}\nTelefone: {telefone}\nMensagem:\n{msg}"
        link = f"mailto:contato@dapsat.com?subject={quote(assunto)}&body={quote(body)}"
        st.success("Link de e-mail gerado abaixo:")
        st.markdown(f"[Enviar e-mail]({link})")

st.caption("© MAVIPE Space Systems · DAP ATLAS")
