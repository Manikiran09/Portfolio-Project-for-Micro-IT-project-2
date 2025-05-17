📌 Project 14: URL Shortener
A URL Shortener is a tool that takes a long URL and generates a short, unique alias that redirects users to the original URL. This project also persists data using a JSON file and can be extended with analytics or database support.

🚀 Features
Convert long URLs into short links

Automatically saves mappings to a database.json file

Simple web interface using HTML and CSS

Flask-based backend

Unique short URL generation

📁 Project Structure
url-shortener/
│
├── app.py                # Main Flask application
├── database.json         # Stores URL mappings (created automatically)
│
├── templates/
│   └── index.html        # Frontend HTML form
│
├── static/
│   └── style.css         # CSS styling for the form
│
└── README.md             # Project documentation


⚙️ Requirements
Install dependencies using:
pip install -r requirements.txt
🧪 How to Run the Project
python app.py
5000

🧠 How It Works
User submits a long URL.

Flask generates a random short ID (e.g., a1B2c3).

The short ID and original URL are saved in database.json.

When a user visits /a1B2c3, they are redirected to the original URL.

