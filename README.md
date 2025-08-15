# Copiloto_IA
Proyecto de Copiloto conversacional con IA

## Funciones mínimas
- [✓] Subida de hasta 5 PDFs.
- [✓] Extracción, división y vectorización del contenido.
- [✓] Interfaz conversacional donde el usuario pueda hacer preguntas.
- [✓] Orquestación estructurada, con pasos del flujo claramente definidos y extensibles.

## Funciones adicionales

- [✓] Resumen de contenido
- [✓] Comparaciones automáticas entre documentos
- [ ] Clasificación por temas o mezcla de tópicos
- [✓] Ciberseguridad: Proteccion de datos del usuario y del servidor.

## Instrucciones para levantar el entorno
                En desarrollo

## Arquitectura del sistema
                En desarrollo, se escribirá cuando este funcional

## Explicacion de flujo conversacional
                En desarrollo, se escribirá cuando este funcional

## Mejoras futuras
- Implementación de cuentas de usuario con historial de consultas.
- Indexación incremental (para cargas frecuentes de documentos).
- Respuestas con referencias de página y citas automáticas.
- API pública con autenticación para uso externo.

## Tecnologias aplicadas 

### Frameworks de orquestación: LangChain
Permite estructurar y componer flujos conversacionales complejos integrando múltiples herramientas (vector stores, modelos, memoria, etc.) de forma modular.

### LLMs: "TynyLlama" (Modelo de Llama)
Se opta por un modelo LLM liviano y open-source que puede ejecutarse localmente sin requerir servicios externos pagos. Ideal para entornos de prueba y despliegue controlado.

### Vector store: Chroma
Base de datos vectorial ligera y eficiente, optimizada para búsquedas semánticas. Se integra de manera nativa con LangChain.

### Interfaz: Streamlit
Herramienta sencilla y eficaz, de fácil integracion con el backend de Python (tendriamos ambos basados en python)

### Backend: FastAPI
Aunque el uso de backend separado es opcional, se ha optado por FastAPI debido a su velocidad, tipado fuerte, integración nativa con Pydantic y compatibilidad con proyectos de IA. 
Esta separación permite escalar el proyecto a una web app más robusta (como React) sin necesidad de rehacer el backend.

### Contenerización: Docker + docker-compose
Además de ser un requerimiento técnico, su inclusión permite:
- Portabilidad entre entornos de desarrollo y producción.
- Aislamiento de dependencias.
- Escalabilidad mediante microservicios.

## Estructura General del proyecto
Copiloto_IA/
│
├── backend/
│ ├── main.py
│ ├── routes/
│ ├── middlewares/
│ └── ...
├── frontend/
│ └── streamlit_app.py
├── .env
├── Dockerfile
└── docker-compose.yml