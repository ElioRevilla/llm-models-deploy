# llm-models-deploy
Por supuesto, aquí tienes el README en un formato descargable para incluirlo en tu repositorio de GitHub:

```
# Chatbot para Consulta de Eventos

Este proyecto consiste en un Chatbot desarrollado en Python utilizando Flask como interfaz, que permite a los usuarios realizar consultas sobre eventos JSON de ciberseguridad almacenados (esta parte se debe variar de acuerdo a tus datos) . El modelo de lenguaje utilizado es GPT-3.5 de OpenAI alojado en Azure. La información relevante se extrae de los archivos JSON, se vectoriza y se almacena en Pinecone para una rápida recuperación durante las consultas.

## Configuración

Para ejecutar este proyecto, necesitarás definir algunas variables de entorno en un archivo `.env`. Aquí está un ejemplo de cómo podría ser:

```
OPENAI_API_KEY=xxxxxxxxxxxxxxxx
OPENAI_DEPLOYMENT_ENDPOINT=https://openaigm12456.openai.azure.com/
OPENAI_DEPLOYMENT_VERSION=2023-09-15-preview
OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME=text_embedding
OPENAI_ADA_EMBEDDING_MODEL_NAME=text-embedding-ada-002
OPENAI_MODEL_NAME=gpt-35-turbo
OPENAI_DEPLOYMENT_NAME=xxxxxxxxxxxxxxxx
PINECONE_API_KEY=xxxxxxxxxxxxxxxx
```

Asegúrate de que tienes Python y Flask instalados en tu entorno antes de ejecutar la aplicación.

## Ejecución

Para ejecutar la aplicación, simplemente ejecuta `app.py` en tu terminal:

```
python app.py
```

Esto iniciará el servidor Flask y podrás acceder a la aplicación desde tu navegador.

## Contribución

Si deseas contribuir a este proyecto, ¡no dudes en hacerlo! Simplemente crea un fork del repositorio, realiza tus cambios y envía un pull request. ¡Estamos ansiosos por ver tus contribuciones!
```

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).