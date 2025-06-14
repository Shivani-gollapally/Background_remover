from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from io import BytesIO
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Background Remover API is running!'

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    input_image = request.files['image'].read()
    output_image = remove(input_image)

    return send_file(BytesIO(output_image), mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT provided by Render, fallback to 5000
    app.run(host='0.0.0.0', port=port)
