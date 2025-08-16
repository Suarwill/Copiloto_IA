import logging
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.embeddings import Embeddings

from config import (
    VECTOR_STORE_PATH,
    EMBEDDING_MODEL_NAME,
    EMBEDDING_DEVICE,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_embeddings() -> Embeddings:
    # Iniciando embeddings
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={'device': EMBEDDING_DEVICE}
        )

def get_vector_store() -> Chroma:
    # Iniciando vector store
    embeddings = get_embeddings()
    return Chroma(
        persist_directory=VECTOR_STORE_PATH, 
        embedding_function=embeddings
        )

def procesar_guardar_pdf(pdf_path: Path | str) -> str:
    
    pdf_path = Path(pdf_path)
    logging.info(f"Iniciando procesamiento con LangChain para: {pdf_path.name}")

    try:
        loader = PyPDFLoader(str(pdf_path))
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        chunks = text_splitter.split_documents(documents)

        vector_store = get_vector_store()
        vector_store.add_documents(documents=chunks)
        logging.info(f"'{pdf_path.name}' ha sido procesado y almacenado en el vector store.")

        # Unir el contenido de todas las páginas para devolver el texto completo
        full_text = "\n".join([doc.page_content for doc in documents])
        return full_text
        
    except Exception as e:
        logging.error(f"Error al procesar {pdf_path.name} con LangChain: {e}", exc_info=True)
        raise
