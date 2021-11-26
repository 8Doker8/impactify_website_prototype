from bottle import route, run, static_file

@route('/')
def root():
  return static_file('index.html', './')
@route('/')
def css():
  return static_file('style.css', './')

run(host='0.0.0.0', port=8080)
