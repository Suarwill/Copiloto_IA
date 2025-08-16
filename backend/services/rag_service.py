import logging
from langchain.chains import RetrievalQA, LLMChain
from langchain_core.prompts import PromptTemplate

from services.vector_store_service import get_vector_store
from services.llm_service import get_llm
from config import RETRIEVER_K

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def query_rag(query: str) -> str:

    logging.info(f"Recibida consulta: '{query}'")

    # 1. Cargar el vector store y el LLM
    vector_store = get_vector_store()
    llm = get_llm()

    # 2. Crear un retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": RETRIEVER_K})

    # 3. Crear la cadena de RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
    )

    # 4. Ejecutar la cadena y obtener la respuesta
    response = qa_chain.invoke({"query": query})
    logging.info(f"Respuesta generada para: '{query}'")
    
    return response.get("result", "No se pudo generar una respuesta.")

def generate_summary(document_text: str) -> str:

    logging.info("Generando resumen...")
    llm = get_llm()
    
    prompt_template = """
    Escribe un resumen conciso y claro del siguiente texto en un máximo de 100 palabras.
    Enfócate en las ideas y conclusiones principales.

    Texto:
    "{text}"

    Resumen:
    """
    
    prompt = PromptTemplate.from_template(prompt_template)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    response = llm_chain.invoke({"text": document_text})
    
    # El resultado puede ser un string o un dict, lo normalizamos a string.
    return response.get("text", str(response))

def generate_comparison(document_summaries: dict[str, str]) -> str:

    if len(document_summaries) < 2:
        return "Se necesitan al menos dos documentos para realizar una comparación."

    logging.info("Generando comparación entre documentos...")
    llm = get_llm()

    context = ""
    for i, (filename, summary) in enumerate(document_summaries.items()):
        context += f"Documento {i+1} ({filename}):\n{summary}\n\n"

    prompt_template = """
    A continuación se presentan resúmenes de varios documentos. 
    Realiza una comparación concisa entre ellos, destacando sus principales similitudes, diferencias y puntos clave.

    Contexto:\n{context}\nComparación:
    """
    
    prompt = PromptTemplate.from_template(prompt_template)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    response = llm_chain.invoke({"context": context})

    return response.get("text", str(response))
