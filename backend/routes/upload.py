from fastapi import APIRouter, UploadFile, File, HTTPException, status
from typing import List
from pathlib import Path
import shutil

from backend.utils.secureFile import secureFile
from backend.services.pdfReader import readPdfContent

router = APIRouter()

# Definir carpeta para almacenar los PDF's cargados
UPLOAD_DIRECTORY = Path("uploads")
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)

@router.post("/")
async def router(archivos: List[UploadFile] = File(...)):

    # Controlar la cantidad de archivos cargados
    if len(archivos) > 5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pueden cargar más de 5 archivos a la vez."
        )

    resultados = []

    for archivo in archivos:
        secureFile(archivo)  # Aplicar medidas de seguridad en el archivo cargado
        
        archivo_path = UPLOAD_DIRECTORY / archivo.filename
        
        try:
            # Guardar el archivo subido de forma segura
            with open(archivo_path, "wb") as buffer:
                shutil.copyfileobj(archivo.file, buffer)
            
            # Procesar el PDF
            readPdfContent(archivo_path)

            resultados.append({"archivo": archivo.filename, "mensaje": "Procesado correctamente"})
        
        except Exception as e:
            resultados.append({"archivo": archivo.filename, "error": str(e)})
        finally:
            await archivo.close()
    
    return {"resultados": resultados}

