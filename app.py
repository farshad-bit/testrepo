# from flask import Flask    # Install flask   import Flask aus flask module
# app = Flask("My firts Application")     # Create Object plan

# @app.route('/')    # Define Route
# def hello():    # Methode
#     return 'Hello World!'    # Return single code

# if __name__ == '__main__':   # add edquntischen
#     app.run(debug=True)   # Save and Run

from flask import Flask, render_template, request
app = Flask("MyfirstApplication")

@app.route('/sample')
def getSampleHTML():
    return render_template('sample.html')

@app.route('/user/<username>', methods=['GET'])
def greetUser(username):
    return render_template("result.html", username=username)

@app.route('/user', methods=['GET'])
def greetUserBasedOnReq():
    username = request.args.get("username")
    return render_template("result.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)