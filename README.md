# Resume Analysis Web Application

This project is a web application for uploading and analyzing resume files. It consists of a Django backend that processes the uploaded files and a React frontend that interacts with the user.

## Features

- Upload resume files in various formats (currently supports PDF).
- Extract and display resume text.
- Integrate with Google Generative AI to generate additional content based on the resume.

## Technologies Used

- **Backend:** Django, fitz (PyMuPDF), Google Generative AI
- **Frontend:** React, Axios
- **API Integration:** Google Generative AI

  ### Resume Analysis App Packages Documentation

This document provides a comprehensive list of packages used in the Resume Analysis App, including both backend and frontend components.

#### Backend Packages

1. **Django**
   - **Version**: 3.2 or higher
   - **Description**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
   - **Installation**: `pip install django`

2. **PyMuPDF (fitz)**
   - **Version**: 1.18.19 or higher
   - **Description**: PyMuPDF is a Python binding for MuPDF, which is a lightweight PDF and XPS viewer.
   - **Installation**: `pip install pymupdf`

3. **Google Generative AI**
   - **Version**: 1.0.0 or higher
   - **Description**: A library for interacting with Google Generative AI services.
   - **Installation**: `pip install google-generativeai`

4. **Setuptools**
   - **Version**: Latest
   - **Description**: Easily download, build, install, upgrade, and uninstall Python packages.
   - **Installation**: `pip install setuptools`

5. **Twine**
   - **Version**: Latest
   - **Description**: Utility for publishing Python packages on PyPI.
   - **Installation**: `pip install twine`

#### Frontend Packages

1. **React**
   - **Version**: 17.0.2 or higher
   - **Description**: A JavaScript library for building user interfaces.
   - **Installation**: `npm install react`

2. **React DOM**
   - **Version**: 17.0.2 or higher
   - **Description**: This package serves as the entry point to the DOM and server renderers for React.
   - **Installation**: `npm install react-dom`

3. **React Scripts**
   - **Version**: 4.0.3 or higher
   - **Description**: This package includes scripts and configuration used by Create React App.
   - **Installation**: `npm install react-scripts`

4. **Axios**
   - **Version**: 0.21.1 or higher
   - **Description**: Promise-based HTTP client for the browser and node.js.
   - **Installation**: `npm install axios`

5. **Node Package Manager (npm)**
   - **Version**: Latest
   - **Description**: A package manager for JavaScript, included with Node.js installation.
   - **Installation**: Comes with Node.js

6. **Yarn**
   - **Version**: Latest
   - **Description**: Fast, reliable, and secure dependency management.
   - **Installation**: `npm install -g yarn`


### Backend Setup Instructions

1. **Install Python Packages**

   ```sh
   pip install -r requirements.txt


```cd backend
python manage.py runserver
cd frontend
npm install
npm start
```




## Setup and Installation

### Prerequisites

- Python 3.x
- Node.js
- npm or yarn

### Backend Setup

1. **Clone the repository:**
    bash
    git clone https://github.com/yourusername/resume-analysis-app.git
    cd resume-analysis-app
    

2. **Create and activate a virtual environment:**
    bash
    python -m venv env
    source env/bin/activate  # On Windows, use env\Scripts\activate
    

3. **Install backend dependencies:**
    bash
    pip install -r requirements.txt
    

4. **Add your Google Generative AI API key:**
    - Create a file named `constant.py` in the backend directory.
    - Add your API key to this file:
        python
        API_KEY = 'your_api_key_here'
        

5. **Run database migrations:**
    bash
    python manage.py migrate
    

6. **Run the Django server:**
    bash
    python manage.py runserver
    

### Frontend Setup

1. **Navigate to the frontend directory:**
    bash
    cd frontend
    

2. **Install frontend dependencies:**
    bash
    npm install  # Or yarn install if you use yarn
    

3. **Run the React development server:**
    bash
    npm start  # Or yarn start
    

### Accessing the Application

- Open your web browser and go to `http://127.0.0.1:3000` to access the React frontend.
- The React app will make requests to the Django backend running at `http://127.0.0.1:8000`.


## API Endpoints

- **`POST /upload_file/`**: Endpoint to upload and analyze a resume file.

## Code Explanation

### Backend

- **`views.py`**:
    - The `index` function renders the main HTML page.
    - The `upload_file` function handles file uploads, processes the resume text, and interacts with the Google Generative AI API.

- **`constant.py`**:
    - Contains the Google Generative AI API key.

- **`parse_resume_text`**:
    - A helper function to parse the resume text and extract information like name, experience, and education.

### Frontend

- **`App.js`**:
    - Main React component that renders the file upload form and handles the submission.

- **`services/api.js`**:
    - Contains functions to interact with the backend API using Axios.

## Running Locally

1. Ensure the backend server is running:
    bash
    python manage.py runserver
    

2. Ensure the frontend development server is running:
    bash
    npm start  # Or yarn start
    

3. Open your browser and navigate to `http://127.0.0.1:3000`.

## Contributors ✨

Thanks go to these wonderful people :

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Abishekmrgstar/"><img src="https://avatars.githubusercontent.com/u/username1?v=4" width="100px;" alt=""/><br /><sub><b>Username1</b></sub></a><br /><a href="https://github.com/Abishekmrgstar/" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Abishekmrgstar/"><img src="https://avatars.githubusercontent.com/u/username2?v=4" width="100px;" alt=""/><br /><sub><b>Username2</b></sub></a><br /><a href="https://github.com/Abishekmrgstar/" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Abishekmrgstar/"><img src="https://avatars.githubusercontent.com/u/username3?v=4" width="100px;" alt=""/><br /><sub><b>Username3</b></sub></a><br /><a href="https://github.com/Abishekmrgstar/" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->



## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Devakesavan/Resume-Analyser/commit/339b80c30d36134b6ef9e3270f448aea0d301d55) file for details.
