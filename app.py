from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('open.html')  # Ensure 'index.html' is in 'templates/' folder

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render uses port 10000