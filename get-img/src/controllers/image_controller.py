from flask import Blueprint, jsonify, send_file
from services.image_service import resize_image, get_image_path
import os

image_blueprint = Blueprint('image_blueprint', __name__)

@image_blueprint.route('/api/images', methods=['GET'])
def get_images():
    images = [
        {"name": "imagen1.jpg", "url": "http://localhost:3012/api/images/1.jpg"},
        {"name": "imagen2.jpg", "url": "http://localhost:3012/api/images/2.jpg"},
        {"name": "imagen3.jpg", "url": "http://localhost:3012/api/images/3.jpeg"}
    ]
    return jsonify(images)

@image_blueprint.route('/api/images/<image_name>', methods=['GET'])
def get_image(image_name):
    image_path = get_image_path(image_name)
    if not os.path.exists(image_path):
        return "Image not found", 404

    resized_image = resize_image(image_path)
    return send_file(resized_image, mimetype='image/jpeg')
