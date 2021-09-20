from flask import Flask, render_template

tempo_app = Flask(__name__) 

@tempo_app.route("/")
def index():
  
    return 'Hola Diego Romo'


if __name__=='__main__':
 
    tempo_app.run(debug=True)
