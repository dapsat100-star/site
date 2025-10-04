
# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="MAVIPE Space Systems — DAP ATLAS",
    page_icon="images/favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- CSS (look & feel) ----------
HIDE_DEFAULT = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
/* containers */
.block-container {padding-top: 1.6rem; max-width: 1200px;}
/* cards */
.card {border: 1px solid rgba(255,255,255,.10); border-radius: 18px; padding: 16px; background: #0f1830;}
.badge {display:inline-block; padding:6px 10px; border-radius:999px; border: 1px solid #3ad0c6; color:#3ad0c6; background: rgba(58,208,198,.15); font-size:12px;}
.lead {color:#b8c4e6;}
.kpi {font-weight:700; color:#58e8dd;}
hr {opacity:.25}
</style>
"""
st.markdown(HIDE_DEFAULT, unsafe_allow_html=True)

# ---------- HERO ----------
col1, col2 = st.columns([1.1, 0.9])
with col1:
    st.markdown('<span class="badge">Plataforma DAP ATLAS • OGMP 2.0 L5 • InSAR</span>', unsafe_allow_html=True)
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
    st.image("images/hero-dashboard.png", use_column_width=True, caption="Painel DAP ATLAS (ilustração)")

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
    st.image("images/case-petrobras.png", use_column_width=True, caption="Exemplo ilustrativo de relatório OGMP")


# ---------- CTA ----------
st.info("Quer ver um demo curto do DAP ATLAS? Agendamos uma chamada de 15 minutos e mostramos como os KPIs atendem seu caso.")
cta1, cta2 = st.columns(2)
with cta1:
    st.link_button("Agendar por e-mail", "mailto:contato@dapsat.com?subject=Demo%20DAP%20ATLAS&body=Olá%2C%20gostaria%20de%20agendar%20um%20demo%20de%2015%20min.%20%F0%9F%9A%80")  # mailto
with cta2:
    st.link_button("Falar no WhatsApp", "https://wa.me/50700000000?text=Quero%20um%20demo%20do%20DAP%20ATLAS")  # ajuste o número

st.divider()

# ---------- SOBRE ----------
st.header("Sobre a MAVIPE")
st.markdown("""<p class='lead'>Fundada por profissionais com experiência em <b>centros de operações de satélites</b> e <b>geointeligência</b> no mercado privado, unimos tecnologia espacial e análise avançada para gerar valor prático.</p>""", unsafe_allow_html=True)

# ---------- CONTATO ----------
st.header("Contato")
with st.form("contato_form"):
    colA, colB = st.columns(2)
    with colA:
        nome = st.text_input("Seu nome", placeholder="Seu nome completo")
        email = st.text_input("E-mail", placeholder="seu@email.com")
    with colB:
        empresa = st.text_input("Empresa (opcional)", placeholder="Sua empresa")
        telefone = st.text_input("WhatsApp/Telefone (opcional)", placeholder="(+55) 11 99999-9999")
    msg = st.text_area("Como podemos ajudar?", placeholder="Descreva seu desafio…"))
    enviar = st.form_submit_button("Enviar (gera e-mail)")
    if enviar:
        assunto = "Contato via site — MAVIPE"
        body = f"Nome: {nome}%0AEmail: {email}%0AEmpresa: {empresa}%0ATelefone: {telefone}%0AMensagem:%0A{msg}"
        st.markdown(f"[Clique aqui para enviar por e-mail](mailto:contato@dapsat.com?subject={assunto}&body={body})")  # mailto gerado
        st.success("Link de e-mail gerado. Clique para abrir seu cliente de e-mail.")

st.caption("© MAVIPE Space Systems · DAP ATLAS")
