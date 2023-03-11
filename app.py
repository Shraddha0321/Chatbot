from flask import Flask ,render_template,request,jsonify
from flask_cors import CORS
from chat import get_response

app=Flask(__name__)
CORS(app)

@app.route("/",methods=["GET"])

def new_func():
    return render_template("base.html")

@app.route("/predict",methods=["POST"])
def predict():
    text = request.get_json(force=True).get("message")
    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)

if __name__=="main":
 app.run(debug=True)           


