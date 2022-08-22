from flask import Flask, render_template
from controllers.session_controller import session_blueprint
from controllers.student_controller import student_blueprint

app = Flask(__name__)

app.register_blueprint(session_blueprint)
app.register_blueprint(student_blueprint)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run