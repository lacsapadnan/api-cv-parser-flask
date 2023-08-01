from flask import Flask, request, jsonify
from pyresparser import ResumeParser
import os
import tempfile

app = Flask(__name__)

# Details API Route
@app.route("/parse-resumes", methods=['POST'])
def details():
    if 'resumes' not in request.files:
        return jsonify({"error": "No resume files provided."}), 400

    resume_files = request.files.getlist('resumes')
    if len(resume_files) == 0:
        return jsonify({"error": "No resume files provided."}), 400

    parsed_resumes = []
    for resume_file in resume_files:
        # Create a temporary file to store the uploaded resume
        temp_dir = tempfile.gettempdir()
        temp_file_path = os.path.join(temp_dir, resume_file.filename)
        resume_file.save(temp_file_path)

        # Parse the resume using the temporary file path
        resume_data = ResumeParser(temp_file_path).get_extracted_data()

        # Remove the temporary file
        os.remove(temp_file_path)

        parsed_resumes.append(resume_data)

    return jsonify(parsed_resumes)

if __name__ == "__main__":
    app.run(debug=True)
