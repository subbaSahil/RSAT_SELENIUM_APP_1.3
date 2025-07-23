from flask import Flask, request, jsonify, send_file
import os
import zipfile
from scriptGenerator import getScript
from dataDrivenScriptGenerator import getDataDrivenScript
from xmlConverter import extract_user_actions
from flask_cors import CORS
import traceback
import subprocess
from Utils.dataFormatGenerator import generate_dynamic_header_excel  # ✅ Add this import

app = Flask(__name__)
CORS(app)
 
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'tests'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
 
@app.route('/generate-script', methods=['POST'])
def run_script():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded', 'scripts': {}}), 400

    files = request.files.getlist('file')
    results = {}

    for file in files:
        filename = file.filename
        base_name = os.path.splitext(filename)[0]
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_script_path = os.path.join(OUTPUT_FOLDER, f'script_{base_name}_test.py')
        script_type = request.form.get("scriptType", "1")
        try:
            file.save(input_path)
            selenium_data = None
            extract_user_actions(input_path)  # creates output.xml
            if(script_type == "1"):
                selenium_data = getScript('output.xml')
            elif(script_type == "2"):
               selenium_data = getDataDrivenScript('output.xml',f'script_{base_name}_test_data.xlsx')
               generate_dynamic_header_excel("output.xml", output_script_path)
            with open(output_script_path, 'w', encoding='utf-8') as f:
                f.write(selenium_data)
            results[filename] = selenium_data
        except Exception as e:
            results[filename] = f"Error: {str(e)}\n{traceback.format_exc()}"

    return jsonify({
        "message": "Script(s) and Excel(s) generated successfully.",
        "scripts": results
    })
    
 
@app.route('/download-all-scripts', methods=['GET'])
def download_all_scripts():
    zip_path = "all_scripts.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in os.listdir(OUTPUT_FOLDER):
            if file.endswith(".py"):
                zipf.write(os.path.join(OUTPUT_FOLDER, file), arcname=file)
    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5010)
 
