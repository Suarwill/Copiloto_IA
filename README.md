# Copiloto_IA
Proyecto de Copiloto conversacional con IA

Este readme debe incluir:

Instrucciones para levantar el entorno (docker-compose up)
Arquitectura del sistema
Justificación de elecciones técnicas
Explicación del flujo conversacional
Limitaciones actuales y mejoras futuras (roadmap)

## Funciones mínimas
- [ ] Subida de hasta 5 PDFs.
- [ ] Extracción, división y vectorización del contenido.
- [ ] Interfaz conversacional donde el usuario pueda hacer preguntas.
- [ ] Orquestación estructurada, con pasos del flujo claramente definidos y extensibles.

## Funciones adicionales

- [ ] Resumen de contenido
- [ ] Comparaciones automáticas entre documentos
- [ ] Clasificación por temas o mezcla de tópicos
- [ ] Ciberseguridad: Proteccion de datos del usuario y del servidor.

## Tecnologias aplicadas 
            --------------> Justificadas
            
- Frameworks de orquestación: LangChain, LlamaIndex, CrewAI, etc.

- LLMs: OpenAI, Claude, Mistral, Llama, HuggingFace, etc.

- Vector store: Chroma, Qdrant, Weaviate...

### Interfaz: Streamlit
Rapido y de fácil integracion con el backend de Python (tendriamos ambos basados en python)

### Backend: FastAPI
A pesar de ser un opcional, preferí realizarlo separado del frontend para hacer el proyecto escalable, en caso de querer tener un control total en el diseño y funcionalidades del frontend, sería mas sencilla su migracion a una WebApp como React ejemplo.
El usar FastAPI como backend es por su practicidad en este proyecto, ya que se integra muy bien con modelos de IA como OpenAI.

### Contenerización: Docker + docker-compose
Siendo de por si un requisito solicitado, igualmente es justificable por razones solidas como Portabilidad, Aislamiento y fácil despliegue.
Además de la facilidad que otorga para implementar microsevicios.