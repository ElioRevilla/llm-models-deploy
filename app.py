from flask import render_template, Flask 

from controller import subir_evento, consultar_evento

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/subir-evento', methods=['POST'])
def route_subir_evento():
    return subir_evento()

@app.route('/consultar-evento', methods=['POST'])
def route_consultar_evento():
    return consultar_evento()

if __name__ == '__main__':
    app.run(debug = True)
    
