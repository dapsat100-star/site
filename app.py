# app.py  — Landing com navbar + hero full-screen (estilo do print)
# Coloque no MESMO diretório: app.py, logo-mavipe.png e hero.jpg
import streamlit as st
from urllib.parse import quote

st.set_page_config(page_title="DAP Space Systems", page_icon="logo-mavipe.png", layout="wide")

# ================== CSS ==================
st.markdown("""
<style>
/* Reset básico */
html, body, [data-testid="stAppViewContainer"] { height: 100%; background:#0b1221; }
#MainMenu, header, footer {visibility: hidden;}
.block-container { padding: 0 !important; max-width: 100% !important; }

/* Navbar */
.navbar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  display: flex; align-items: center; justify-content: space-between;
  padding: 14px 36px;
  background: rgba(8, 16, 33, .35);
  backdrop-filter: saturate(160%) blur(10px);
  border-bottom: 1px solid rgba(255,255,255,.08);
}
.nav-left {display:flex; align-items:center; gap:14px;}
.nav-left img {height: 44px; width:auto;}
.nav-left .brand {line-height:1; color:#e6eefc; font-weight:700; letter-spacing:.5px;}
.nav-right {display:flex; align-items:center; gap:28px;}
.nav-link {color:#d6def5; text-decoration:none; font-weight:500;}
.nav-link:hover{opacity:.9}
.cta {
  background: #34d399; color:#05131a; font-weight:700;
  padding:10px 16px; border-radius:12px; text-decoration:none;
}
.cta:hover { filter:brightness(1.05); }

/* HERO */
.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; align-items: center; padding: 0 8vw;
  color: #e8eefc; overflow: hidden;
}
.hero:before{
  content:""; position:absolute; inset:0;
  background: url('hero.jpg') center/cover no-repeat fixed;
  filter: brightness(.6);
}
.hero:after{
  content:""; position:absolute; inset:0;
  background: radial-gradient(80% 60% at 30% 30%, rgba(20,30,55,.0) 0%, rgba(8,16,33,.55) 70%, rgba(8,16,33,.85) 100%);
}
.hero-content{ position:relative; max-width: 1000px; }
.kicker{ color:#cfe7ff; opacity:.9; font-weight:600; margin-bottom:10px; }
h1.hero-title{
  font-size: clamp(36px, 6vw, 64px);
  line-height: 1.05; margin: 0 0 12px 0;
}
.highlight{ color:#34d399; }  /* cor do “Ocean Framework™” */
.hero-sub{ font-size: clamp(16px, 2.2vw, 20px); color:#b9c6e6; max-width: 70ch; }
.hero-actions{ margin-top: 22px; display:flex; gap:14px; flex-wrap:wrap; }
.btn {
  display:inline-block; padding:12px 18px; border-radius:12px; text-decoration:none; font-weight:700;
  border:1px solid rgba(255,255,255,.18); color:#e6eefc; background: rgba(255,255,255,.06);
}
.btn:hover{ background: rgba(255,255,255,.12); }
@media (max-width: 820px){
  .nav-right{gap:16px}
  .navbar{padding:12px 18px}
}
</style>
""", unsafe_allow_html=True)

# ================== NAVBAR ==================
st.markdown("""
<div class="navbar">
  <div class="nav-left">
    <img src="logo-mavipe.png" alt="logo"/>
    <div class="brand">DAP SPACE SYSTEMS</div>
  </div>
  <div class="nav-right">
    <a class="nav-link" href="#company">Company</a>
    <a class="nav-link" href="#solution">Solution</a>
    <a class="nav-link" href="#industries">Industries</a>
    <a class="cta" href="#contact">Contact Sales</a>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""<div class="hero">
  <div class="hero-content">
    <div class="kicker">Maritime & Ground Domain Awareness</div>
    <h1 class="hero-title">Maritime Domain Awareness<br>Made Accessible by<br>
      <span class="highlight">DAP Ocean Framework™</span>
    </h1>
    <div class="hero-sub">
      Multi-sensor data fusion (SAR, optical, AIS, RF, weather) into one actionable framework.
      DAP Ocean Framework™ delivers detections, tracks and alerts you can trust.
    </div>
    <div class="hero-actions">
      <a class="cta" href="#contact">Contact Sales</a>
      <a class="btn" href="#solution">Explore Solution</a>
      <a class="btn" href="#industries">Use Cases</a>
    </div>
  </div>
</div>""", unsafe_allow_html=True)

# ================== SEÇÕES PLACEHOLDER ==================
st.markdown('<div id="company"></div>', unsafe_allow_html=True)
st.header("Company")
st.write("Breve descrição institucional, missão, equipe, certificações…")

st.markdown('<div id="solution"></div>', unsafe_allow_html=True)
st.header("Solution")
st.write("""
**DAP Ocean Framework™**: ingestão de dados (AIS, SAR/óptico, RF), normalização, fusão, 
analytics (deteção de embarcações, rotas anômalas), scoring de risco e APIs/UX.
""")

st.markdown('<div id="industries"></div>', unsafe_allow_html=True)
st.header("Industries / Use Cases")
st.write("- Port security • Oil & Gas offshore • IUU fishing • SAR operations • Border/coast guard.")

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.header("Contact Sales")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name")
    email = st.text_input("Work email")
with col2:
    org = st.text_input("Organization")
    phone = st.text_input("Phone/WhatsApp (optional)")
msg = st.text_area("What challenge are you trying to solve?")
if st.button("Send email"):
    subject = "DAP Ocean Framework — Contact"
    body = f"Name: {name}\\nEmail: {email}\\nOrg: {org}\\nPhone: {phone}\\nMessage:\\n{msg}"
    st.success("Click the link below to open your email client:")
    st.markdown(f"[Compose email](mailto:contato@dapsat.com?subject={quote(subject)}&body={quote(body)})")

st.caption("© DAP Space Systems · DAP Ocean Framework™")
