from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App! Go to /htop for system info."

@app.route('/htop')
def htop():
    try:
        # Simplified system information
        full_name = "R Bhargava Rayudu"
        username = "Bhargavarayudu18u"
        server_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')

        response = f"""
        <h1>System Info</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        """
        return response

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
