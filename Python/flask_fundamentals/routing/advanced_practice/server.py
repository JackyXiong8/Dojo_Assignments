# from flask import Flask, render_template, request, redirect
# app = Flask(__name__)
# @app.route('/users/<username>')
# def show_user_profile(username):
#     print(username)
#     return render_template("user.html")
# if __name__=="__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return render_template("user.html")

   
    
if __name__=="__main__":
    app.run(debug=True)
