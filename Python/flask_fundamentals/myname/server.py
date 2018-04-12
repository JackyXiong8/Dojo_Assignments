from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def finished():    
    print('Data retrieved')

    name = request.form['first_name']
    last_name = request.form['last_name']

    return redirect('/')


app.run(debug=True) 