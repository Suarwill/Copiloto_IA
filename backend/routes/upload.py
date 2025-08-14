from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pathlib import Path
import shutil

from backend.services.secureFile import secureFile
from backend.services.pdfReader import readPdfContent

router = APIRouter()

# Definir carpeta para almacenar los PDF's cargados
UPLOAD_DIRECTORY = Path("uploads")
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)

@router.post("/")
async def router(archivo: UploadFile = File(...)):

    secureFile(archivo)  # Aplicar medidas de seguridad en el archivo cargado
    
    archivo_path = UPLOAD_DIRECTORY / archivo.filename
    
    try:
        # Guardar el archivo subido de forma segura
        with open(archivo_path, "wb") as buffer:
            shutil.copyfileobj(archivo.file, buffer)
        
        # Llamar a la función del servicio para procesar el PDF
        readPdfContent(archivo_path)

        return {"archivo": archivo.filename, "mensaje": "PDF subido y procesado correctamente"}
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocurrió un error al subir el archivo: {str(e)}"
        )
    finally:
        await archivo.close()

