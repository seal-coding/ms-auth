from flask import Flask
from config import FlaskConfig, MysqlConfig

app = Flask("SealAuth")
app.config.from_object(FlaskConfig)

@app.route("/")
def hello():
    """docstring"""
    return "Hello World!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=FlaskConfig.PORT)
