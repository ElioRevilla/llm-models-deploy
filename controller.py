from flask import request, jsonify
from utils import extraer_texto_relevante, embeddings, index_name, agent

def subir_evento():
    evento_json = request.json
    texto_relevante = extraer_texto_relevante(evento_json)
    vector_evento = embeddings.embed_documents([texto_relevante])[0]
    metadata = {"texto": texto_relevante}
    evento_id = evento_json['event_id']
    id_vector_pair = [(evento_id, vector_evento, metadata)]
    index_name.upsert(vectors=id_vector_pair)
    return jsonify({"mensaje": "Evento subido con éxito", "id": evento_id}), 200


def consultar_evento():
    consulta_json = request.json
    query_text = consulta_json['consulta']  
    prompt_modificado = f"Responde en español y solo basado en la data almacenada: {query_text}"
      
    respuesta = agent(prompt_modificado)
    output = respuesta['output']
    return jsonify({"respuesta": output}), 200