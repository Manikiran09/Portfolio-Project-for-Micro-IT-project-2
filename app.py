from flask import Flask, request, redirect, render_template, url_for
import string, random, json, os

app = Flask(__name__)
DB_FILE = 'database.json'

def load_urls():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_urls(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f)

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    urls = load_urls()
    short_url = None

    if request.method == 'POST':
        original_url = request.form['original_url']
        short_id = generate_short_id()

        while short_id in urls:
            short_id = generate_short_id()

        urls[short_id] = original_url
        save_urls(urls)
        short_url = request.host_url + short_id

    return render_template('index.html', short_url=short_url)

@app.route('/<short_id>')
def redirect_short_url(short_id):
    urls = load_urls()
    original_url = urls.get(short_id)
    if original_url:
        return redirect(original_url)
    return "Invalid short URL", 404

if __name__ == '__main__':
    app.run(debug=True)
