# utils.py
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import AzureChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
from langchain.agents import initialize_agent, Tool
import os
import pinecone
from dotenv import load_dotenv

load_dotenv()

# Configuración de las API y la inicialización de objetos
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME = os.getenv("OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME")
OPENAI_ADA_EMBEDDING_MODEL_NAME = os.getenv("OPENAI_ADA_EMBEDDING_MODEL_NAME")
OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
PINECONE_INDEX_NAME = ""
PINECONE_API_KEY = ""
OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
OPENAI_DEPLOYMENT_VERSION = os.getenv("OPENAI_DEPLOYMENT_VERSION")

pinecone.init(api_key=PINECONE_API_KEY, environment='gcp-starter')
index_name = pinecone.Index(PINECONE_INDEX_NAME)

embeddings = OpenAIEmbeddings(
    deployment=OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME,
    model=OPENAI_ADA_EMBEDDING_MODEL_NAME,
    openai_api_base=OPENAI_DEPLOYMENT_ENDPOINT,
    openai_api_type="azure",
    chunk_size=1
)

llm = AzureChatOpenAI(
    deployment_name=OPENAI_DEPLOYMENT_NAME,
    model_name=OPENAI_MODEL_NAME,
    openai_api_base=OPENAI_DEPLOYMENT_ENDPOINT,
    openai_api_version=OPENAI_DEPLOYMENT_VERSION,
    openai_api_key=OPENAI_API_KEY,
    openai_api_type="azure",
    temperature=0.3
)

# Configuración del agente conversacional y la memoria
text_field = "texto"
vectorstore = Pinecone(
    index_name, embeddings.embed_query, text_field
)

conversational_memory = ConversationBufferWindowMemory(memory_key='chat_history', k=5, return_messages=True)
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

tools = [
    Tool(
        name='Knowledge Base',
        func=qa.run,
        description=(
            'use this tool when answering general knowledge queries to get '
            'more information about the topic'
        )
    )
]

agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    memory=conversational_memory
)

def extraer_texto_relevante(evento_json):
    # Incluir detalles adicionales del evento en el texto
    texto = f"ID del Evento: {evento_json['event_id']}, " \
            f"Tipo de Evento: {evento_json['event_type']}, " \
            f"Severidad: {evento_json['severity']}, " \
            f"Timestamp: {evento_json['timestamp']}, " \
            f"Usuario: {evento_json['device']['user']}, " \
            f"ID del Dispositivo: {evento_json['device']['device_id']}, " \
            f"Nombre del Host: {evento_json['device']['hostname']}, " \
            f"Dirección IP: {evento_json['device']['ip_address']}, " \
            f"Familia de Malware: {evento_json['attack_details']['malware_family']}, " \
            f"Tácticas: {' '.join(evento_json['attack_details']['tactics'])}, " \
            f"Técnicas: {' '.join(evento_json['attack_details']['techniques'])}, " \
            f"Ruta del Archivo: {evento_json['attack_details']['file_path']}, " \
            f"Hash: {evento_json['attack_details']['hash']}, " \
            f"Puntuación del Incidente: {evento_json['incident_score']}, " \
            f"Acción Tomada: {evento_json['action_taken']}, " \
            f"Estado: {evento_json['status']}."
    return texto
