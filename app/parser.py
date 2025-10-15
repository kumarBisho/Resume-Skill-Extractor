import re

def extract_resume_info(text):
    # Extract name (assuming it's at the top)
    name = text.split('\n')[0].strip()
    # Extract email using regex
    email = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    email = email.group(0) if email else "Not found"
    # Extract phone number using regex
    phone = re.search(r'\+?\d{10,12}', text)
    phone = phone.group(0) if phone else "Not found"
    # Extract skills (common keywords)
    skills = []
    skill_keywords = [
        "C", "C++", "C#", "Go", "Java", "JavaScript", "MATLAB", "PHP", "Python", "R", "TypeScript",
        "Bootstrap", "CSS", "CSS3", "HTML", "HTML5", "React", "Next.js", "Tailwind CSS",
        "Django", "Express.js", "FastAPI", "Flask", "Node.js", "PHP", "Spring", "Spring Boot", "Spring MVC",
        "Microservices", "REST API", "RESTful API", "WebSockets",
        "MySQL", "PostgreSQL", "SQLite", "SQL Server",
        "MongoDB", "DynamoDB", "Redis", "Cassandra", "Elasticsearch",
        "Ansible", "AWS", "Azure", "CentOS", "CI/CD", "DevOps", "Docker", "Git", "GitHub", "GitLab", "Google Cloud Platform (GCP)", "Jenkins", "Kubernetes", "Linux", "macOS", "Terraform", "Ubuntu", "Windows",
        "Application Security", "Business Continuity", "Cloud Security", "Compliance", "Cryptography", "Cybersecurity", "Data Security", "Disaster Recovery", "Ethical Hacking", "Governance, Risk, and Compliance (GRC)", "Information Security", "Network Security", "Penetration Testing", "Risk Management",
        "Algorithms", "Artificial Intelligence (AI)", "Data Analysis", "Data Mining", "Data Structures", "Data Structures and Algorithms", "Data Visualization", "Deep Learning", "ETL", "Machine Learning (ML)", "Neural Networks", "NLP (Natural Language Processing)", "Numpy", "Pandas", "PyTorch", "Scikit-learn", "TensorFlow",
        "Big Data", "Data Lakes", "Data Warehousing", "Hadoop", "Hive", "Kafka", "Pig", "Spark",
        "AI21 Labs", "Anthropic", "Bard / Gemini", "ChatGPT", "Claude", "Cohere", "Copy.ai", "DALL·E", "DeepMind", "Hugging Face", "Jasper AI", "Kaggle", "LLaMA", "Midjourney", "Mistral", "OpenAI", "Replit", "Runway ML", "Stability AI", "Synthesia", "Tabnine", "Writesonic",
        "Excel", "Power BI", "Tableau",
        "Agile", "APIs", "Data Models", "Design Patterns", "Jira", "Object-Oriented Programming (OOPs)", "Scrum", "SOLID Principles", "System Design", "Testing / QA", "Version Control",
        "Cloud Computing", "Enterprise Architecture", "IT Infrastructure", "MCP Server", "Networking", "System Administration", "Virtualization (VMware, Hyper-V, Citrix)",
        "3D Modeling", "After Effects", "Animation", "Audio Editing", "Blender", "Copywriting", "Final Cut Pro", "Graphic Design", "Illustrator", "InDesign", "Music Production", "Photoshop", "Premiere Pro", "UI/UX Design", "Video Editing",
        "Altium", "Ansys", "ArchiCAD", "AutoCAD", "Cadence", "CATIA", "COMSOL", "Eagle", "Fusion 360", "Grasshopper", "LabVIEW", "Maya", "Multisim", "NX", "Proteus", "Revit", "Rhino", "Simulink", "SketchUp", "SolidWorks", "3ds Max", "Unity", "Unreal Engine",
        "Adaptability", "Budgeting", "Business Analysis", "Change Management", "Communication Skills", "Content Creation", "Creativity", "Critical Thinking", "Customer Service", "Digital Marketing", "Employee Relations", "Event Planning", "Financial Analysis", "Forecasting", "Human Resources", "Innovation", "Leadership", "Marketing", "Organizational Development", "Performance Management", "Presentation Skills", "Problem-Solving", "Project Management", "Public Relations", "Public Speaking", "Quality Assurance", "Recruitment", "Sales", "SEO", "Social Media Marketing", "Strategic Planning", "Supply Chain Management", "Teamwork", "Teaching / Training / Mentoring", "Time Management"
        
    ]
    skill_keywords = [kw.lower() for kw in skill_keywords]
    text_lower = text.lower()
    for keyword in skill_keywords:
        if ' ' in keyword:
            if keyword in text_lower:
                skills.append(keyword.title())
        else:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                skills.append(keyword.title())
    experience = []
    lines = text.split('\n')
    for line in lines:
        if any(word in line.lower() for word in ['company', 'experience', 'engineer', 'developer', 'intern', 'work', 'project', 'role', 'responsibilities']):
            experience.append(line.strip())
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'skills': ', '.join(skills),
        'experience': '\n'.join(experience)
    }