from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Background Remover API is running!'

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    input_data = image_file.read()
    output_data = remove(input_data)
    output_image = Image.open(io.BytesIO(output_data)).convert("RGBA")

    byte_io = io.BytesIO()
    output_image.save(byte_io, format='PNG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/png', download_name='no-bg.png')

# THIS IS IMPORTANT 👇
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Fallback to 5000 for local use
    app.run(host='0.0.0.0', port=port)
