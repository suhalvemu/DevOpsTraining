from flask import Flask 
app = Flask(__name__)

@app.route('/') 
def hello():     
       print("hey new code is added")
       return "welcome to the flask tutorials. Hello Zaria "
if __name__ == "__main__":
     app.run(host ='0.0.0.0', port = 5001, debug = True) 