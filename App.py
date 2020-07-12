from flask import Flask

app = Flask(__name__)

# Importamos el controlador de las rutas
from Controller import *

# Inicializamos el servidor
if __name__ == '__main__':
    app.run(debug=True)