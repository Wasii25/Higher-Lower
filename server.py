from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center; font-family: Faculty Glyphic;">Guess a number between 0 and 9</h1>'
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3VuNXF4aWx0eGZjbjJ5eTA0OGVzbnlrNjBuMm01N2txeTNubGZraCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/J06KLycl29d4N7dWdu/200.webp" '
            'alt="Guessing GIF" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">')

random_number = random.randint(0, 9)

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < random_number:
        return ('<h1 style="font-family: Faculty Glyphic; color: #433878;">Too low! Guess again</h1>'
                '<img src="https://media0.giphy.com/media/t9l9L8qFKJfsFn2WLm/200.webp?cid=790b76118bi33qv450vnc2znr9e67ph421n65jvxhf68jpoa&ep=v1_gifs_search&rid=200.webp&ct=g" '
                'alt="Too low GIF" style="width: 50%;">')

    elif guess > random_number:
        return ('<h1 style="font-family: Faculty Glyphic; color: #FFE1FF;">Too high! Guess again</h1>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmVuNWxnYzJ6MGVhbXYzYzVvdzVhOHpoMDlmdTA1eDU1b2tqbXZraCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d7zlVzxPEcqay0NeNw/giphy.webp" '
                'alt="Too high GIF" style="width: 50%;">')

    else:
        return ('<h1 style="font-family: Faculty Glyphic; color: #88C273;">You are right!!</h1>'
                '<img src="https://media4.giphy.com/media/xXSLvTw6fRgqJPNyHg/200.webp?cid=ecf05e47yazaw88z7v9wmv8gzehlychxizuzy9w0ng0r2kht&ep=v1_gifs_search&rid=200.webp&ct=g" '
                'alt="Correct guess GIF" style="width: 50%;">')

if __name__ == '__main__':
    app.run(debug=True)
