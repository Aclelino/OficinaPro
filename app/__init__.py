from flask import Flask,render_template,request

def create_flask():

    app = Flask(__name__)
    @app.route("/home")

    def inicio():
        return render_template("auth/home.html")

    @app.route('/')

    def login():

        user = request.form.get("usuario")
        passw = request.form.get("senha")
        
        return render_template('auth/login.html')


    return app