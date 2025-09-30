import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

st.set_page_config(page_title="Belleza & Bienestar", page_icon="💅", layout="wide")

ASSETS = "assets"
os.makedirs(ASSETS, exist_ok=True)

# ---------- Image helpers (Pillow 10+ compatible) ----------
def _gradient(size, c1, c2):
    """
    Create a vertical gradient image from color c1 to c2.
    Works without external assets so the app runs offline.
    """
    w, h = size
    base = Image.new("RGB", size, c1)
    top = Image.new("RGB", size, c2)

    # Build a 1px-wide vertical alpha mask from 0..255 and stretch it
    mask = Image.new("L", (1, h))
    for y in range(h):
        mask.putpixel((0, y), int(255 * y / max(h - 1, 1)))
    mask = mask.resize((w, h))

    base.paste(top, (0, 0), mask)
    return base

def _text_size(draw, text, font):
    """
    Pillow >=10 removed textsize; prefer textbbox and fallback if needed.
    """
    try:
        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
        return right - left, bottom - top
    except AttributeError:
        # Pillow < 10
        return draw.textsize(text, font=font)

def _draw_label(img, text):
    """
    Draw a semi-transparent panel at the bottom with centered text.
    Compatible with Pillow 10+.
    """
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 54)
    except Exception:
        font = ImageFont.load_default()

    w, h = img.size
    tw, th = _text_size(draw, text, font)

    # Semi-transparent footer panel
    panel_h = th + 40
    panel = Image.new("RGBA", (w, panel_h), (0, 0, 0, 90))
    img = img.convert("RGBA")
    img.paste(panel, (0, h - panel_h), panel)

    # Centered white text
    draw = ImageDraw.Draw(img)
    draw.text(((w - tw) / 2, h - panel_h + 20), text, fill=(255, 255, 255, 255), font=font)
    return img.convert("RGB")

def ensure_asset(path, size, c1, c2, label):
    full = os.path.join(ASSETS, path)
    if not os.path.exists(full):
        img = _gradient(size, c1, c2)
        img = _draw_label(img, label)
        img.save(full, "JPEG", quality=92)
    return full

# Generate demo images so the app works offline (replace with your photos anytime)
HERO = ensure_asset("hero.jpg", (1800, 700), (240, 215, 245), (187, 155, 209), "Belleza & Bienestar")
ESM1 = ensure_asset("esmaltes1.jpg", (800, 600), (255, 209, 220), (255, 128, 171), "Esmaltes Ultra Shine")
ESM2 = ensure_asset("esmaltes2.jpg", (800, 600), (255, 224, 230), (255, 153, 187), "Esmaltes Gel")
CRM1 = ensure_asset("cremas1.jpg", (800, 600), (255, 239, 213), (255, 204, 153), "Crema Hidratante")
CRM2 = ensure_asset("cremas2.jpg", (800, 600), (255, 250, 240), (255, 204, 170), "Serum Nutritivo")
BNS1 = ensure_asset("bienestar1.jpg", (800, 600), (209, 245, 225), (153, 209, 187), "Aceites Esenciales")
BNS2 = ensure_asset("bienestar2.jpg", (800, 600), (222, 246, 235), (170, 214, 194), "Kit Relax")

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

st.caption("🖼️ Imágenes generadas dinámicamente en la app (sin necesidad de internet). Reemplaza por tus fotos si lo deseas: coloca archivos en la carpeta `assets/` y actualiza los nombres en el código.")
st.markdown("<footer>© 2025 Belleza & Bienestar · Página demo con Streamlit</footer>", unsafe_allow_html=True)
