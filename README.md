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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
