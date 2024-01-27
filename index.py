from flask import Flask
from routes import main_bp

app = Flask(__name__)



if __name__ == "__main__":
    app.register_blueprint(main_bp)
    app.run(debug=True)