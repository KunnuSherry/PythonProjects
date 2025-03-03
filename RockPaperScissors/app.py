from flask import Flask, redirect, render_template, url_for, request
import random

app = Flask(__name__)

options = ['rock', 'paper', 'scissors']

compScore = 0
userScore = 0
message="Let's Start"

@app.route('/', methods=['GET','POST'])
def index():
    global compScore
    global userScore
    global message
    if(request.method=='POST'):
        compChoice = options[random.randint(0,2)]
        userChoice = request.form.get('rps')
        if(userChoice=='rock' and compChoice=='scissors' or userChoice=='paper' and compChoice=='rock' or userChoice=='scissors' and compChoice=='paper'):
            message = 'You Won !'
            userScore+=1
        else:
            message = 'You Lost :)'
            compScore+=1
    return render_template('index.html', compScore=compScore, userScore=userScore, message=message)

if __name__ == '__main__':
    app.run(debug=True)