from flask import Flask, render_template

app = Flask(__name__)

# Frontend route
@app.route('/')
def index():
    frontend_link = 'https://oss-frontend.onrender.com'
    backend_link = 'https://oss-project.onrender.com'
    return render_template('index.html', frontend_link=frontend_link, backend_link=backend_link)

if __name__ == '__main__':
    app.run()
