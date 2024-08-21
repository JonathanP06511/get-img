from flask import Flask
from flasgger import Swagger
from controllers.image_controller import image_blueprint

app = Flask(__name__)
swagger = Swagger(app, template_file='swagger/image_swagger.yml') 


app.register_blueprint(image_blueprint)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=3012)
