from flask import Flask, render_template, request, redirect, url_for, session
import requests
import json
app = Flask(__name__)
app.secret_key='a'



@app.route('/')
def home():
  return render_template('main.html')


  

@app.route('/predict',methods=["POST", "GET"])
def login():
  
    str=request.form['news']
    print(str)
    print("sdf")

    url = "https://fake-news-detection1.p.rapidapi.com/"

    querystring = {"text":str}

    payload = {
    "key1": "value",
    "key2": "value"
    }
    headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "be7fd5b032msh2de06b9e53f0850p1ce4b9jsna154c022de5a",
    "X-RapidAPI-Host": "fake-news-detection1.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    print(response.text)
    dict=json.loads(response.text)
    print(dict)
    return dict["prediction"]

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')

