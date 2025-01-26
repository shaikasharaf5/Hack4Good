Diet Recommendation System

This is a diet recommendation system that uses the USDA API to provide personalized diet recommendations. The application is built with Python and can be accessed via a web interface hosted on http://localhost:5000.

Features

Personalized diet recommendations based on user inputs.

Integration with the USDA API for nutritional data.

Easy-to-use web interface.

Prerequisites

Before running the application, ensure you have the following installed:

Python 3.7 or higher

Flask (Python web framework)

An active USDA API key

Installation

Clone the repository:

git clone <https://github.com/shaikasharaf5/TasteMate.git >


Install required Python packages:

pip install -r requirements.txt

Set up your USDA API key:

Create a .env file in the project root.

Add the following line to the .env file:

USDA_API_KEY=<your_api_key>

Usage

Launch the application:

python USDA.py

Open your browser and go to:

http://localhost:5000

Follow the instructions on the web interface to get personalized diet recommendations.

File Structure

project-folder/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates for the web interface
├── static/              # Static assets (CSS, JS, images)
├── .env                 # Environment variables (not included in the repository)
└── README.md            # Project documentation

API Integration

This project integrates with the USDA API to fetch nutritional data. For more information about the USDA API, visit their official documentation.

Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

Acknowledgments

USDA API for providing nutritional data.

Flask for the web framework.

