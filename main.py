from flask import Flask, request
app = Flask(__name__)


@app.route("/api/cordenadas", methods=["POST"])
def recibir_datos():
    datos = request.get_json()
    print(datos)
    return "Datos recibidos correctamente"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4141)
