import re
import json

def parse_resume(resume_text):
    # Dummy data extraction logic; in practice, you would use NLP techniques to extract this information
    resume_data = {
        "name": "Vaibhavi Pathak",
        "contact_information": {
            "email": "vaibhavi@example.com",
            "phone": "123-456-7890",
            "address": "1234 Main St, Bengaluru, India"
        },
        "summary": "A dedicated AI enthusiast with experience in machine learning and software development.",
        "experience": [
            {
                "job_title": "AI Intern",
                "company": "Pitibit.ai",
                "location": "Bengaluru",
                "start_date": "September 2024",
                "end_date": "December 2024",
                "responsibilities": [
                    "Developed AI models for various applications",
                    "Collaborated with a team of AI researchers"
                ]
            }
        ],
        "education": [
            {
                "degree": "BTech in Computer Science",
                "institution": "ABC University",
                "location": "Bengaluru",
                "graduation_date": "2025"
            }
        ],
        "skills": ["Python", "Machine Learning", "NLP", "TensorFlow", "PyTorch"],
        "certifications": ["Certified Machine Learning Specialist"],
        "projects": [
            {
                "project_name": "E-commerce website",
                "description": "A project to create an ecommerce website using React, Node.js, and Express.",
                "technologies": ["React", "Node.js", "Express"]
            }
        ]
    }
    
    return resume_data

# Example resume text
resume_text = """
Vaibhavi Pathak
vaibhavi@example.com
123-456-7890
1234 Main St, Bengaluru, India

Summary:
A dedicated AI enthusiast with experience in machine learning and software development.

Experience:
AI Intern at Pitibit.ai, Bengaluru (September 2024 - December 2024)
- Developed AI models for various applications
- Collaborated with a team of AI researchers

Education:
BTech in Computer Science from ABC University, Bengaluru (2025)

Skills:
Python, Machine Learning, NLP, TensorFlow, PyTorch

Certifications:
Certified Machine Learning Specialist

Projects:
e-commerce website - A project to create an ecommerce website using React, Node.js, and Express.
Technologies: React, Node.js, Express
"""

parsed_resume = parse_resume(resume_text)
print(json.dumps(parsed_resume, indent=4))
