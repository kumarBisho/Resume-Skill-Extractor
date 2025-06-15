# Resume Skill Extractor

A web-based application that extracts structured information from PDF resumes using Python and machine learning techniques.

## Features

- Extracts key information from PDF resumes:
  - Name
  - Email
  - Phone number
  - Skills
  - Work experience
- Web-based interface
- Database storage
- Search functionality by skills
- Docker support for easy deployment

## Tech Stack

- Backend: Python, Flask
- Database: SQLite
- PDF Processing: pdfplumber
- Frontend: HTML, Bootstrap
- Containerization: Docker

## Installation

### Prerequisites

- Python 3.11+
- Docker (optional)

### Using Docker (Recommended)

```bash
# Build the Docker image
docker build -t resume-parser .

# Run the container
docker run -it --rm -p 5000:5000 resume-parser
```

Access the application at: `http://localhost:5000`

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/kumarBisho/Resume-Skill-Extractor.git
cd Resume-Skill-Extractor
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python resume_parser.py
```

Access the application at: `http://localhost:5000`

## Usage

1. Upload a PDF resume using the file upload button
2. The system will automatically extract:
   - Basic information (name, email, phone)
   - Skills from predefined categories
   - Work experience
3. Use the search functionality to find resumes based on specific skills

## Skill Categories

The system currently supports extracting skills from the following categories:
- Programming languages
- Web development
- Databases
- Cloud technologies
- Tools
- Machine Learning/Artificial Intelligence
- Data Structures and Algorithms

## Project Structure

```
.
├── resume_parser.py         # Main application file
├── templates/               # HTML templates
│   └── index.html          # Main web interface
├── static/                  # Static files (CSS, JS)
├── uploads/                 # Directory for uploaded resumes
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the developers of pdfplumber and Flask for their excellent libraries
- Special thanks to the open-source community for their contributions
