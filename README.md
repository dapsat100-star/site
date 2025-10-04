
# MAVIPE / DAP ATLAS — Site em Streamlit

Este repositório contém um site institucional simples feito em Streamlit (Python), pronto para deploy na Streamlit Community Cloud.

## Como publicar

1. Crie um repositório no GitHub (por ex. `mavipe-site-streamlit`).
2. Envie estes arquivos:
   - `app.py`
   - `requirements.txt`
   - `.streamlit/config.toml`
   - pasta `images/` (substitua pelos seus logos/imagens)
3. Vá em https://share.streamlit.io (Community Cloud) → **New app** → selecione o repositório → `app.py`.
4. Clique em **Deploy**.

## Onde trocar textos e imagens
- Textos principais estão no `app.py` (HERO, Soluções, Case, Sobre, Contato).
- Imagens ficam em `images/`:
  - `logo-mavipe.png`
  - `hero-dashboard.png`
  - `case-petrobras.png`
  - `favicon.png`

Substitua os placeholders mantendo os mesmos nomes.

## Dicas
- Para formulário de contato com backend, use serviços como FormSubmit, EmailJS ou crie um endpoint (FastAPI) e faça `requests.post()`.
- Para domínios customizados, a versão paga do Streamlit Cloud ou um proxy (Cloudflare) pode ajudar a apontar o domínio.

© MAVIPE Space Systems · DAP ATLAS
