from fastapi import HTTPException, status

def secure_file(archivo):
    # 1) Segurizar que el archivo cargado sea un PDF
    if not archivo.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se permiten archivos PDF."
        )
    
    # 2) Segurizar que sea tipo PDF, leyendo el MIME type
    if archivo.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo no es un PDF válido."
        )
    
    # 3) Limitar el tamaño del archivo
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 50 MB
    archivo.file.seek(0, 2)
    fileSize = archivo.file.tell()
    archivo.file.seek(0)
    if fileSize > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo es demasiado grande. El tamaño máximo permitido es 50 MB."
        )
    
    pass