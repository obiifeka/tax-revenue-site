from flask import Flask, redirect, url_for, render_template, request
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Enable CSRF protection for all routes
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
@csrf.exempt # Disable CSRF protection for this route
def home():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('home.html')
    return render_template('home.html')
