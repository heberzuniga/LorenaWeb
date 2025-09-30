# lorenaweb — Belleza & Bienestar (Streamlit)
Estructura lista para subir a un repo o a Streamlit Cloud.

## Estructura
```
lorenaweb/
  app.py
  assets/
    hero.jpg
    esmaltes1.jpg
    esmaltes2.jpg
    cremas1.jpg
    cremas2.jpg
    bienestar1.jpg
    bienestar2.jpg
  requirements.txt
```

## Ejecutar local
```bash
pip install -r lorenaweb/requirements.txt
streamlit run lorenaweb/app.py
```

## Streamlit Cloud
1. Sube esta carpeta a un repositorio de GitHub.
2. Crea una app en Streamlit Community Cloud.
3. En "Main file path" indica: `lorenaweb/app.py`.
