# Resume Analyzer

Resume Analyzer is a project designed to analyze resumes, extract key information, and generate insights using AI models.

## Installation

To get started with Resume Analyzer, follow these steps:

### Backend Setup

1. **Clone the repository:**
   ```bash
   https://github.com/Devakesavan/Resume-Analyser
   cd Resume-Analyzer
2. **Set up the backend:**
 Navigate to the backend directory:
   ```bash
   cd backend
   
 Create and activate a virtual environment (optional but recommended):
   ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
 Install dependencies,Apply database migrations (if any) and start server:
  ```bash
pip install django==3.2.8
pip install PyMuPDF==1.19.3
pip install google==3.0.0

python manage.py migrate
python manage.py runserver
```
3. FRONTEND SETUP
   Set up the frontend (if applicable):
   ```bash
   cd ../api
   npm install  # or `yarn install` if using Yarn
   npm start  # or `yarn start` if using Yarn
    ```

## Usage

**Access the application:**

Open your web browser and go to [http://localhost:8000](http://localhost:8000) (or the appropriate URL where your Django server is running).

**Upload a resume:**

- Click on the upload button to select a resume file (PDF format is supported).

**Generate insights:**

Once the resume is uploaded, the application will analyze it, extract key information, and provide insights using AI models integrated into the system.

**View results:**

Review the generated text, extracted name, experience, and education details presented on the screen.

### Collaborators

- **[Abishekmrgstar](https://github.com/Abishekmrgstar)**
- **[PriyaDharshini22-2005](https://github.com/PriyaDharshini22-2005)**
- **[Dhatchayani2006](https://github.com/Dhatchayani2006)**
- **[karthikeyan261222](https://github.com/karthikeyan261222)**

## License

This project is licensed under the MIT License.See the [LICENSE](https://github.com/Abishekmrgstar/Resume-analyzer/blame/main/LICENSE) file for details.

## Support

For support, please [contact the project maintainers](devanadhan.16102005@gmail.com).




   
