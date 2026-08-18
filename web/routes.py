from flask import Flask, request, jsonify, render_template
from app.services import Services
s = Services()

def create_app():
    app = Flask(__name__)

    # A simple example of how to do a GET method
    @app.route("/hello", methods=["GET"])
    def hello():
        return "Hello World!"

    # user inputs text via flask api
    @app.route("/id_text", methods=["POST"])
    def id_text():
        user_text = request.form.get("user_text")
        user_loc = s.rank_countries(user_text)
        return jsonify(user_loc)

    # user inputs text via flask api
    @app.route("/", methods=["GET"])
    def HTMLrender():
        return render_template("LG_html_input.html")

    return app


if __name__ == "__main__":
    myapp = create_app()
    myapp.run()
