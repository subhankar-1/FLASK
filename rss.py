from flask import Flask,remote_template

app=Flsk(__name__)
@app.route("/")
def home():
  return "hello" 
@app.route("/rss")
def rss():
  return remote_template("rss.html")
app.run(host='0.0.0.0',port=80,debug=True)
