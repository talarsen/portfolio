import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_googlemaps import GoogleMaps, Map, icons
import json

load_dotenv()
app = Flask(__name__)

os.getenv("API_KEY") 
educationData = [
    {
        "school_name": "Major Leauge Hacking | MLH Fellowship",
        "school_img": "/static/img/education-imgs/mlh-logo-color.png",
        "degree": "Certificate: Site Realiability Software Engineering"
    },
    {
        "school_name": "Techtonica",
        "school_img": "/static/img/education-imgs/techtonica.png",
        "degree": "Certificate: Software Engineering"
    },
    {
        "school_name": "University Massachussetts, Lowell",
        "school_img": "/static/img/education-imgs/uMassLowell.png",
        "degree": "Bachelor of Science: Information Technology"
    },
    {
        "school_name": "California State University, Chico",
        "school_img": "/static/img/education-imgs/chicoState3.jpg",
        "degree": "Bachelor of Science: Parks and Natural Resources"
    },
]


@app.route('/')
def landingPage():
    context = {
        "educationData": educationData
    }
    return render_template('landingPage.html', title="MLH Fellow", url=os.getenv("URL"), **context)

# Hobbies data
hobbyData = [
    {"imgSrc": "/static/img/logo.jpg",
    "name": "Photography", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur convallis orci nulla, id dignissim diam vulputate a. Ut ullamcorper, ex et elementum posuere, arcu ante vulputate risus, non aliquet augue metus eget enim. Sed auctor non nibh eget porttitor. Aliquam consectetur ipsum eget mi tempus tempus. "},
    {"imgSrc": "/static/img/logo.jpg", 
    "name": "Hiking", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur convallis orci nulla, id dignissim diam vulputate a. Ut ullamcorper, ex et elementum posuere, arcu ante vulputate risus, non aliquet augue metus eget enim. Sed auctor non nibh eget porttitor. Aliquam consectetur ipsum eget mi tempus tempus. "},
    {"imgSrc": "/static/img/logo.jpg", 
    "name": "Dancing", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur convallis orci nulla, id dignissim diam vulputate a. Ut ullamcorper, ex et elementum posuere, arcu ante vulputate risus, non aliquet augue metus eget enim. Sed auctor non nibh eget porttitor. Aliquam consectetur ipsum eget mi tempus tempus. "},
    {"imgSrc": "/static/img/logo.jpg", 
    "name": "Programming", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur convallis orci nulla, id dignissim diam vulputate a. Ut ullamcorper, ex et elementum posuere, arcu ante vulputate risus, non aliquet augue metus eget enim. Sed auctor non nibh eget porttitor. Aliquam consectetur ipsum eget mi tempus tempus. "}
]

@app.route('/hobbies')
def hobbiesPage():
    context={
        "hobbyData": hobbyData
    }
    return render_template('hobbies.html', title="MLH Fellow - Hobbies", url=os.getenv("URL"), **context)

#Location Data
locationData = [
    {"country": "Canada", "lat": 45.421532, "long": -75.697189},
    {"country": "Mexico", "lat": 19.432608, "long": -99.133209},
    {"country": "US", "lat": 38.9071923, "long": -77.0368707},
    {"country": "UK", "lat": 51.509865, "long": -0.118092},
    {"country": "France", "lat": 48.864716, "long": 2.349014},
    {"country": "Spain", "lat": 40.416775, "long": -3.703790},
    {"country": "Japan", "lat": 36.2048, "long": 138.2529},
    {"country": "Tunisia", "lat": 33.8869, "long": 9.5375},
    {"country": "South Korea", "lat": 35.9078, "long": 127.7669},
    {"country": "Belize", "lat": 17.1899, "long": 88.4976},
    {"country": "Guatemala", "lat": 15.7835, "long": 90.2308},
]

#Location route
@app.route('/locations/')
def mapview():
    context = {
        "locationData": locationData
    }
    return render_template('locations.html', title="MLH Fellow - Locations", url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"),  **context)

# Experience data
experienceData = [
    {"company_img": "static/img/favicon.ico",
    "company_name": "Major League Hacking",
    "job_title": "Site-Reliability Engineer | Fellow @ MLH",
    "position_type": "Fellowship",
    "date_worked": "Sep 2022 - Dec 2022", 
    "location": "United States",
    "description": [
        "Collaborated with some incredible people, amazing pod leader, and great mentor company.", 
        "Worked on a portfolio project, creating a reusable template for the future.", 
        "Used Python, Flask and Jinja, Bootstrap for styling "
        ],
    },
    {"company_img": "static/img/MLBLogo.png",
    "company_name": "Major League Baseball",
    "job_title": "Site-Reliability Engineer",
    "position_type": "Full-time",
    "date_worked": "Sep 2022 - Present", 
    "location": "New York, New York",
    "description": [
        "Collaborated with some incredible people, amazing pod leader, and great mentor company.", 
        "Worked on a portfolio project, creating a reusable template for the future.", 
        "Used Python, Flask and Jinja, Bootstrap for styling "
        ],
    },
    {"company_img": "static/img/logo-Meta.png",
    "company_name": "Meta",
    "job_title": "Production Engineer",
    "position_type": "Full-time",
    "date_worked": "Jun 2020 - Aug 2022", 
    "location": "Menlo Park, California",
    "description": [
        "Collaborated with some incredible people, amazing pod leader, and great mentor company.", 
        "Worked on a portfolio project, creating a reusable template for the future.", 
        "Used Python, Flask and Jinja, Bootstrap for styling "
        ],
    },
]

# Work Experience
@app.route('/experience')
def experiencePage():
    context={
        "experienceData": experienceData
    }
    return render_template('experience.html', title="MLH Fellow - Experience", url=os.getenv("URL"), **context)
