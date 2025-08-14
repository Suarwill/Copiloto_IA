from fastapi import HTTPException, status

def secureFile(file):
    #Segurizar que el archivo cargado sea un PDF
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se permiten archivos PDF."
        )
    
    return