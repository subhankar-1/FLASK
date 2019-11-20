from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def home():
  return "hello" 
@app.route("/rss")
def rss():
  return render_template("rss.php")
app.run(host='0.0.0.0',port=80,debug=True)
