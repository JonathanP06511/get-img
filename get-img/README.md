# Image Service API

This project is an Image Service API built with Flask. It provides endpoints for retrieving image metadata and serving resized images.

## Technologies Used

- **Flask**: Micro web framework for Python that facilitates web application development.
- **Pillow (PIL)**: Python Imaging Library for image processing.
- **Blueprints**: Flask feature to organize routes and handlers.
- **Python**: Programming language used for development.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/JonathanP06511/get-img.git
    ```

2. Navigate to the project directory:
    ```bash
    cd <project directory>
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

   Ensure you have `Pillow` installed:
    ```bash
    pip install Pillow
    ```

## Usage

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. The API will be available at `http://localhost:3012`.

## Project Structure

- `app.py`: Main file where the Flask application is configured and run.
- `controllers/image_controller.py`: Defines routes for the image API.
- `services/image_service.py`: Contains logic for image processing and resizing.
- `config.py`: Configuration settings, including image directory and resize dimensions.

## Routes

- `GET /api/images`: Endpoint to get a list of image metadata.
- `GET /api/images/<image_name>`: Endpoint to retrieve and resize an image.

## Docker

To run this project in a Docker container:

1. Build the Docker image:
    ```bash
    docker build -t get-img .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 3012:3012 get-img
    ```

3. The API will be available at `http://localhost:3012` inside the Docker container.

## Documentation

API documentation is generated with Swagger and served at the `/apidocs` endpoint. Swagger allows you to view and test the API endpoints interactively.

## Notes

- Ensure that the image directory and configurations are set correctly in `config.py`.
- The images are served in JPEG format, and resizing is applied to images before serving.
