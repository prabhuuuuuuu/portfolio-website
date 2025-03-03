from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    # Sample project data (replace with real data later)
    learning_projects = [
        {"title": "Movie Recommender", "description": "Built using Python, NumPy, and Pandas."},
        {"title": "Iris Flower Species Predictor", "description": "Classifies Iris flowers into three species using ML."}
    ]

    
    hackathon_projects = [
        {"title": "PathPlex", "description": "Engineered a machine learning-driven career aptitude portal", 'github_link': 'https://github.com/prabhuuuuuuu/PathPlex1'},
        {"title": "CaseFlow", "description": "Coming soon... Work in progress."}
    ]


    innovative_projects = [
        {"title": "StudyGuard", "description": "Coming soon... Work in progress."}
    ]

    return render_template(
        "projects.html",
        learning_projects=learning_projects,
        hackathon_projects=hackathon_projects,
        innovative_projects=innovative_projects
    )

@app.route("/experiences")
def experiences():
    club_experiences = [
        {"title": "PitchAThon Volunteer", "organization": "VIT Chennai", "date": "Sep 2024", "description": "Managed events, coordinated with seniors, and learned leadership skills."},
        {"title": "AI Club Member", "organization": "VIT Chennai", "date": "Oct 2024", "description": "Collaborated on AI projects and participated in technical workshops."}
    ]

    professional_experiences = [
        {"title": "AI Hackathon Project", "organization": "Open Innovation Hackathon", "date": "Feb 2025", "description": "Developed an AI-powered aptitude test website."},
        {"title": "Data Science Workshop", "organization": "IIT Bombay TechFest", "date": "Dec 2024", "description": "Attended hands-on sessions on data science and machine learning."}
    ]

    return render_template(
        "experiences.html",
        club_experiences=club_experiences,
        professional_experiences=professional_experiences
    )

@app.route('/certificates')
def certificates():
    course_certificates = [
        # Existing certificate
        {
            'title': 'Advanced Python: Classes and Functions',
            'issuer': 'LinkedIn',
            'date': '21 November 2024',
            'image': url_for('static', filename='img/Courses/CertificateOfCompletion_Advanced Python Classes and Functions.jpg'),
            'full_image': url_for('static', filename='img/Courses/CertificateOfCompletion_Advanced Python Classes and Functions.jpg')
        },
        # Your new certificates
        {
            'title': 'Agentic AI Fundamentals: Architectures, Frameworks and Applications',
            'issuer': 'LinkedIn',
            'date': '28 January 2025',
            'image': url_for('static', filename='img/Courses/CertificateOfCompletion_Agentic AI Fundamentals Architectures Frameworks and Applications.jpg'),
            'full_image': url_for('static', filename='img/Courses/CertificateOfCompletion_Agentic AI Fundamentals Architectures Frameworks and Applications.jpg')
        },
        {
            'title': 'Introduction to Prompt Engineering for ChatGPT 4',
            'issuer': 'LinkedIn',
            'date': '1 November 2024',
            'image': url_for('static', filename='img/Courses/CertificateOfCompletion_Introduction to Prompt Engineering for Generative AI 2023.jpg'),
            'full_image': url_for('static', filename='img/Courses/CertificateOfCompletion_Introduction to Prompt Engineering for Generative AI 2023.jpg')
        },
        {
            'title': 'Learning MATLAB',
            'issuer': 'LinkedIn',
            'date': '26 November 2024',
            'image': url_for('static', filename='img/Courses/CertificateOfCompletion_Learning MATLAB.jpg'),
            'full_image': url_for('static', filename='img/Courses/CertificateOfCompletion_Learning MATLAB.jpg')
        },
        {
            'title': 'NumPy Essential Training 1: Foundations of NumPy',
            'issuer': 'LinkedIn',
            'date': '21 December 2024',
            'image': url_for('static', filename='img/Courses/CertificateOfCompletion_NumPy Essential Training 1 Foundations of NumPy.jpg'),
            'full_image': url_for('static', filename='img/Courses/CertificateOfCompletion_NumPy Essential Training 1 Foundations of NumPy.jpg')
        },
        {
            'title': 'NumPy Essential Training 2: MatPlotlib and Linear Algebra Capabilities',
            'issuer': 'LinkedIn',
            'date': '17 January 2025',
            'image': url_for('static', filename='img/Courses/CertificateOfCompletion_NumPy Essential Training 2 MatPlotlib and Linear Algebra Capabilities.jpg'),
            'full_image': url_for('static', filename='img/Courses/CertificateOfCompletion_NumPy Essential Training 2 MatPlotlib and Linear Algebra Capabilities.jpg')
        },
        {
            'title': 'Programming Foundations: Object-Oriented Design',
            'issuer': 'LinkedIn',
            'date': '25 October 2024',
            'image': url_for('static', filename='img/Courses/CertificateOfCompletion_Programming Foundations ObjectOriented Design.jpg'),
            'full_image': url_for('static', filename='img/Courses/CertificateOfCompletion_Programming Foundations ObjectOriented Design.jpg')
        },
    ]
    
    hackathon_certificates = [
        {
            'title': 'Nexathon 2025',
            'issuer': 'VIT NEXUS',
            'date': '10 - 11 Feb 2025',
            'image': url_for('static', filename='img/Participation/Nexathon feb 2025.png'),
            'full_image': url_for('static', filename='img/Participation/Nexathon feb 2025.png')
        },

        {
            'title': 'Data Science Workshop',
            'issuer': 'IIT BOMBAY Tech Fest',
            'date': '18 - 19 Dec 2024',
            'image': url_for('static', filename='img/Participation/97b6ad44-c7c0-11ef-bab3-551b3f897b3f_page-0001.jpg'),
            'full_image': url_for('static', filename='img/Participation/97b6ad44-c7c0-11ef-bab3-551b3f897b3f_page-0001.jpg')
        }
    ]
    
    return render_template('certificates.html', 
                          course_certificates=course_certificates,
                          hackathon_certificates=hackathon_certificates)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
