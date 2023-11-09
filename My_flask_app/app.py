from flask import Flask, render_template, request
from Circle import Circle
from Triangle import Triangle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def works():
    return render_template('index.html')

@app.route('/profile')
def profile():  
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return "Contact Page. please create me an html page with dummy contact info"


@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/AreaOfCircle', methods= ['GET', 'POST'])
def AreaOfCircle():
    AreaofCircle = None
    if request.method == 'POST':
        Radius = int(request.form.get('Radius', ''))
        circle = Circle(Radius)
        AreaofCircle = circle.getArea()
    return render_template('AreaOfCircle.html', AreaofCircle = AreaofCircle)

@app.route('/AreaOfTriangle', methods= ['GET', 'POST'])
def AreaOfTriangle():
    AreaofTriangle = None
    if request.method == 'POST':
        Base = int(request.form.get('Base', ''))
        Height = int(request.form.get('Height', ''))
        triangle = Triangle(Base, Height)
        AreaofTriangle = triangle.getArea()
    return render_template('AreaOfTriangle.html', AreaofTriangle = AreaofTriangle)


if __name__ == "__main__":
    app.run(debug=True)
