# api-cv-parser-flask

This API made for parsing CV/Resume data into JSON with Flask python, main library that use is Pyresparser from [here](https://github.com/OmkarPathak/pyresparser)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Endpoints](#endpoints)
- [License](#license)


## Features

- Parsing CV data from PDF

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/your-repository.git

# Change directory
cd your-repository

# Install dependencies
pip install nltk
pip install spacy==2.3.5
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
pip install pyresparser

# nltk
python -m nltk.downloader words
python -m nltk.downloader stopwords

# Run the Flask app
python api.py
```

## Endpoints

The API exposes the following endpoint:

### Parse Resume Endpoint

- **URL:** `/parse-resumes`
- **Method:** POST
- **Description:** This endpoint allows you to upload a PDF file containing the CV/Resume data. The API will parse the data and return the extracted information in JSON format.

#### Request

- **HTTP Method:** POST
- **Content-Type:** `multipart/form-data`
- **Parameter:**
  - `resume` (File): The PDF file containing the CV/Resume data to be parsed.

#### Response

- **Status Code:** 200 OK
- **Content-Type:** `application/json`
- **Response Body:** A JSON object containing the extracted information from the CV/Resume, including fields such as name, email, phone number, education, skills, etc.


## License

The API-cv-parser-flask project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

This project uses the `pyresparser` library by OmkarPathak. You can find the library [here](https://github.com/OmkarPathak/pyresparser).



