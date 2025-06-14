from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Background Remover API is running!"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    input_image = file.read()
    output_image = remove(input_image)
    return send_file(BytesIO(output_image), mimetype='image/png', as_attachment=False)

if __name__ == '__main__':
    app.run()
