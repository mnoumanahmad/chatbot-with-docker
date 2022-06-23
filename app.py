from flask import Flask, render_template, jsonify, request
import processor
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
app = Flask(__name__)
from auth_module import validate_user
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'
@auth.verify_password
def verify_password(username, password):
    if validate_user(username, password):
        return  True
    return False

@app.route('/', methods=["GET", "POST"])
@auth.login_required
def index():
    return render_template('index.html', **locals())



@app.route('/chatbot', methods=["GET", "POST"])
#@auth.login_required
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
