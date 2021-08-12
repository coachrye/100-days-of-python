from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '</b>'
        # print('</b>')
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h2>' \
           '<p>yo!!!</p>'

# @app.route('/hello/<name>')
# def hello_basic(name):
#     return f'Bye! Bye! Bye! {name}!'
#
# @app.route('/hello_multi/<name>/1')
# def hello_multiple(name):
#     return f'Bye! 111! {name}!'
#
# @app.route('/path_sample/<path:name>')
# def hello_path(name):
#     return f'Bye! 111! {name}!'
#
# @app.route('/hello_multi_var/<path:name>/<int:numero>')
# def hello_multiple_var(name, numero):
#     return f'Multi Var. {name} | {numero}!'


@app.route('/bye')
@make_bold
def byebyebye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
