import os
from flask import Flask, request, send_file, jsonify
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return "Background Remover is running!"

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

# Render-compatible port binding
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # 5000 for local, replaced by Render
    app.run(host='0.0.0.0', port=port)
