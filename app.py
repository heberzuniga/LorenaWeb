import streamlit as st
import os

st.set_page_config(page_title="Belleza & Bienestar", page_icon="💅", layout="wide")

ASSETS = "assets"
# Asegúrate de que las imágenes existan en el repositorio (incluidas en assets/)
HERO = os.path.join(ASSETS, "hero.jpg")
ESM1 = os.path.join(ASSETS, "esmaltes1.jpg")
ESM2 = os.path.join(ASSETS, "esmaltes2.jpg")
CRM1 = os.path.join(ASSETS, "cremas1.jpg")
CRM2 = os.path.join(ASSETS, "cremas2.jpg")
BNS1 = os.path.join(ASSETS, "bienestar1.jpg")
BNS2 = os.path.join(ASSETS, "bienestar2.jpg")

# ---------- Styles ----------
st.markdown(
    """
    <style>
    .title-hero { font-size: 2.2rem; font-weight: 700; margin-bottom: 0.35rem; }
    .subtitle-hero { font-size: 1.05rem; opacity: 0.9; }
    .pill { display:inline-block; padding:6px 12px; border-radius:999px; background:#f1e8ff; color:#5a2ea6; font-weight:600; margin-bottom:8px;}
    .price { font-weight:700; }
    .muted { color: #6b7280; }
    footer { text-align:center; color:#6b7280; padding:1rem 0; font-size:0.9rem; }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Hero ----------
st.image(HERO, use_container_width=True, caption=None)
st.markdown('<div class="pill">Belleza • Cuidado de la piel • Bienestar</div>', unsafe_allow_html=True)
st.markdown('<div class="title-hero">Todo para tu rutina de belleza y bienestar — simple y natural</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-hero">Esmaltes de larga duración, cremas hidratantes y accesorios para tu día a día.</div>', unsafe_allow_html=True)

st.divider()

# ---------- Tabs & products ----------
tab1, tab2, tab3, tab4 = st.tabs(["✨ Destacados", "💅 Esmaltes", "🧴 Cremas & Serums", "🧘 Bienestar"])

def product_card(image_path, title, desc, price):
    with st.container():
        st.image(image_path, use_container_width=True)
        st.markdown(f"**{title}**")
        st.markdown(f"<span class='muted'>{desc}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='price'>Bs {price:.2f}</span>", unsafe_allow_html=True)

with tab1:
    c1, c2, c3 = st.columns(3)
    with c1: product_card(ESM1, "Esmalte Ultra Shine", "Brillo intenso por 10 días.", 35.00)
    with c2: product_card(CRM1, "Crema Hidratante Diaria", "Con ácido hialurónico y vitaminas.", 55.00)
    with c3: product_card(BNS1, "Aceites Esenciales Relax", "Lavanda & manzanilla para descanso.", 40.00)

with tab2:
    st.subheader("Colección de Esmaltes")
    c1, c2, c3 = st.columns(3)
    with c1: product_card(ESM1, "Esmalte Ultra Shine", "Secado rápido, acabado espejo.", 35.00)
    with c2: product_card(ESM2, "Esmalte Gel", "Efecto gel sin lámpara.", 39.00)
    with c3: product_card(ESM1, "Top Coat Protector", "Sella el color y extiende la duración.", 29.00)

with tab3:
    st.subheader("Cremas, Serums y Cuidado Facial")
    c1, c2, c3 = st.columns(3)
    with c1: product_card(CRM1, "Crema Hidratante Diaria", "Ligera y de rápida absorción.", 55.00)
    with c2: product_card(CRM2, "Serum Nutritivo Nocturno", "Renueva tu piel mientras duermes.", 69.00)
    with c3: product_card(CRM1, "Crema Manos & Uñas", "Nutrición intensiva para manos.", 32.00)

with tab4:
    st.subheader("Bienestar en Casa")
    c1, c2, c3 = st.columns(3)
    with c1: product_card(BNS1, "Aceites Esenciales Relax", "Aromaterapia para tu descanso.", 40.00)
    with c2: product_card(BNS2, "Kit Spa en Casa", "Sales, velas y almohadilla térmica.", 89.00)
    with c3: product_card(BNS1, "Spray Ambiental", "Fragancia suave para ambientes.", 30.00)

st.divider()

# ---------- Newsletter (demo) ----------
st.subheader("📬 Novedades y promociones")
with st.form("newsletter"):
    col1, col2 = st.columns([2,1])
    with col1:
        email = st.text_input("Tu correo electrónico")
    with col2:
        interes = st.selectbox("Tu interés", ["Esmaltes", "Cremas/Skincare", "Bienestar", "Todo"])
    enviado = st.form_submit_button("Quiero suscribirme")
    if enviado:
        st.success("¡Gracias! Te llegará un mensaje con novedades (demo).")

st.caption("🖼️ Imágenes incluidas en la carpeta `assets/`. Reemplaza por tus fotos si lo deseas y usa los mismos nombres de archivo.")
st.markdown("<footer>© 2025 Belleza & Bienestar · Página demo con Streamlit</footer>", unsafe_allow_html=True)
