from pyzbar import pyzbar
from flask import Flask, request, jsonify
import io
import base64
import PIL.Image as Image


def decodificar_imagen_qr(datos_base64):
    code_string = ("'" + (str(datos_base64).split(",")
                   [1])).translate({ord('"'): None})
    img = Image.open(io.BytesIO(base64.b64decode(code_string)))
    codes = pyzbar.decode(img)

    data = str(codes[0].data.decode('utf-8'))
    text = data.split("?")[1]
    rut = (text.split("&")[0]).split("=")[1]
    serial = (text.split("&")[2]).split("=")[1]

    data_decodificada = {
        'rut': rut,
        'serial': serial,
    }

    return data_decodificada


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return {'mensaje': 'Lector QR - OK'}

    @app.route('/recibir-imagen', methods=['POST'])
    def recibir_imagen():

        body_json = request.get_json()

        decodificado = decodificar_imagen_qr(body_json['imagen'])

        respuesta = {
            'mensaje': 'Imagen recibida',
            'decodificado': decodificado,
        }

        return respuesta

    return app
