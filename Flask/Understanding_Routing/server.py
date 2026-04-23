from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello World!!"

@app.route('/Champion')
def champion():
  return "Champion!!"

@app.route('/say/<name>')
def say(name):
  return f"Hello {name}!!"

@app.route('/repeat/<times>/<word>')
def repeat(times, word):
  return f"{word} " * int(times)


if __name__ == '__main__':
  app.run(debug=True)