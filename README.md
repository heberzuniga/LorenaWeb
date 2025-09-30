# Belleza & Bienestar — Página simple en Streamlit (con imágenes incluidas)

Esta app muestra una página estática de **esmaltes, cremas y bienestar** usando **Python + Streamlit**.
Las imágenes están incluidas en `assets/` (no se generan en runtime).

## Cómo ejecutar

```bash
# 1) (opcional) Crear entorno virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Ejecutar
streamlit run app.py
```

## Reemplazar imágenes
Coloca tus fotos en `assets/` con los mismos nombres (o ajusta las rutas en `app.py`).
