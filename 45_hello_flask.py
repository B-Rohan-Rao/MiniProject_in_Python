from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        text = function()
        return f"<b>{text}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        text = function()
        return f"<em>{text}</em>"

    return wrapper


def make_underline(function):
    def wrapper():
        text = function()
        return f"<u>{text}</u>"

    return wrapper


@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World</h1>'
            '<image src="https://media.giphy.com/media/brRWBSKoc9ueI/giphy.gif?cid'
            '=ecf05e47jd24o1800s9vw8ksz0yynoez3duttsua9ax75e51&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=700 >')


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye"


# Creating variable path using th '<>' brackets
# @app.route('/<name>')
# def greet(name):
#     return f"Hello {name}"


# Changing the path into pre-specified data types
@app.route('/<path:fullname>/<int:number>')
def greet(fullname, number):
    return f'Hello {fullname}! You are {number} years old'


if __name__ == '__main__':
    # Run the app in debug mode for auto reload.
    app.run(debug=True)
