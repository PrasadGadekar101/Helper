from flask import Flask, render_template
from converter import Calculator
import PyPDF2

app = Flask(__name__)


@app.route('/')
def hello():
    a = int(input("input a:"))
    b = int(input("input b:"))
    result = Calculator.add(a, b)
    print(result)
    return render_template('gtml/home.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
