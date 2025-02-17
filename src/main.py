from flask import Flask, request, jsonify
from ocr import cleaned_text
from nlp import summary, answer

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_endpoint():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    

