from fastapi import APIRouter, UploadFile, File, HTTPException, status
from typing import List
from pathlib import Path
import logging
import shutil

from backend.utils.secure_file import secure_file
from backend.services.vector_store_service import procesar_guardar_pdf
from backend.services.rag_service import generate_summary, generate_comparison

router = APIRouter()

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Definir carpeta para almacenar los PDF's cargados
UPLOAD_DIRECTORY = Path("uploads")
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)

@router.post("/")
async def upload_files(archivos: List[UploadFile] = File(...)):

    # Controlar la cantidad de archivos cargados
    if len(archivos) > 5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pueden cargar más de 5 archivos a la vez."
        )

    processing_results = []
    document_texts = {}

    for archivo in archivos:
        try:
            secure_file(archivo)  # Aplicar medidas de seguridad en el archivo cargado
            
            archivo_path = UPLOAD_DIRECTORY / archivo.filename
            
            # Guardar el archivo subido de forma segura
            with open(archivo_path, "wb") as buffer:
                shutil.copyfileobj(archivo.file, buffer)

            # Procesar, almacenar en BD vectorial y obtener el texto completo
            full_text = procesar_guardar_pdf(archivo_path)
            document_texts[archivo.filename] = full_text

            processing_results.append({"archivo": archivo.filename, "mensaje": "Archivo procesado y vectorizado correctamente."})
        except Exception as e:
            logging.error(f"Error inesperado al procesar {archivo.filename}: {e}", exc_info=True)
            processing_results.append({"archivo": archivo.filename, "error": "Ocurrió un error inesperado durante el procesamiento."})
        finally:
            await archivo.close()
    
    # Generar resúmenes y comparación si el procesamiento fue exitoso
    summaries = {}
    comparison = ""
    if document_texts:
        try:
            for filename, text in document_texts.items():
                summaries[filename] = generate_summary(text)
            
            if len(summaries) > 1:
                comparison = generate_comparison(summaries)
        except Exception as e:
            logging.error(f"Error al generar resumen o comparación: {e}", exc_info=True)
            # Devolver los resultados del procesamiento con una advertencia
            return {"resultados_procesamiento": processing_results, "advertencia": "Error al generar análisis con IA."}

    return {"resultados_procesamiento": processing_results, "resumenes": summaries, "comparacion": comparison}
