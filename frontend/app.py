import streamlit as st
import requests

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Copiloto de Documentos",
    page_icon="🏙️",
    layout="wide"
)

# --- Constantes ---
BACKEND_URL = "http://backend:6060"


# --- Estado de la Sesión ---
if 'files_processed' not in st.session_state:
    st.session_state.files_processed = False
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'summaries' not in st.session_state:
    st.session_state.summaries = {}
if 'comparison' not in st.session_state:
    st.session_state.comparison = ""


# --- UI Principal ---
st.title(" Copiloto de Documentos IA")
st.markdown("Sube tus PDFs, obtén resúmenes automáticos y conversa con tus documentos.")

# --- Sección de Carga de Archivos ---
with st.sidebar:
    st.header("1. Carga tus Documentos")
    uploaded_files = st.file_uploader(
        "Selecciona hasta 5 archivos PDF",
        type="pdf",
        accept_multiple_files=True
    )

    if st.button("Procesar Archivos"):
        if uploaded_files:
            if len(uploaded_files) > 5:
                st.error("Error: No puedes subir más de 5 archivos a la vez.")
            else:
                # Preparar archivos para la API
                files_for_api = [
                    ("archivos", (file.name, file.getvalue(), file.type))
                    for file in uploaded_files
                ]
                
                with st.spinner("Procesando y analizando documentos... Esto puede tardar un momento."):
                    try:
                        response = requests.post(f"{BACKEND_URL}/upload/", files=files_for_api)
                        
                        if response.status_code == 200:
                            data = response.json()
                            st.session_state.summaries = data.get("resumenes", {})
                            st.session_state.comparison = data.get("comparacion", "")
                            st.session_state.files_processed = True
                            st.session_state.messages = [] # Reinicia el chat con nuevos archivos
                            st.success("¡Archivos procesados con éxito!")
                            st.rerun() # Refresca la UI para mostrar las pestañas
                        else:
                            st.error(f"Error del servidor: {response.status_code} - {response.text}")

                    except requests.exceptions.RequestException as e:
                        st.error(f"Error de conexión con el backend: {e}")
        else:
            st.warning("Por favor, sube al menos un archivo PDF.")

# --- Sección de Resultados y Chat ---
if st.session_state.files_processed:
    tab1, tab2 = st.tabs(["Resúmenes y Comparación", "Chat con Documentos"])

    with tab1:
        st.header("Análisis de Documentos")
        if st.session_state.summaries:
            st.subheader("Resúmenes individuales")
            for filename, summary in st.session_state.summaries.items():
                with st.expander(f"Resumen de: **{filename}**"):
                    st.write(summary)
        
        if st.session_state.comparison:
            st.subheader("Comparación entre documentos")
            st.info(st.session_state.comparison)

    with tab2:
        st.header("Conversa con tus Documentos")
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Haz una pregunta sobre el contenido de los documentos..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Pensando..."):
                    try:
                        chat_payload = {"pregunta": prompt}
                        response = requests.post(f"{BACKEND_URL}/chat/", json=chat_payload)
                        full_response = response.json().get("respuesta", "No se pudo obtener una respuesta.") if response.status_code == 200 else f"Error: {response.status_code}"
                    except requests.exceptions.RequestException as e:
                        full_response = f"Error de conexión con el backend: {e}"
                    st.markdown(full_response)
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})
else:
    st.info("Por favor, carga tus documentos en la barra lateral para comenzar.")
