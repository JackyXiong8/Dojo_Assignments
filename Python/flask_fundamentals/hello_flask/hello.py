from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/success')
def success():
    return render_template('index1.html')

@app.route('/fail')
def fail():
    return render_template('index2.html')

if __name__=="__main__":
    app.run(debug=True)