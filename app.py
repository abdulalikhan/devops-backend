from routes.update import update_bp
from routes.create import create_bp
from routes.delete import delete_bp
from routes.list import list_bp
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(list_bp)

app.register_blueprint(delete_bp)

app.register_blueprint(create_bp)

app.register_blueprint(update_bp)


if __name__ == '__main__':
    app.run(debug=True)
