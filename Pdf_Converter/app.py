from flask import Flask, render_template
from converter import converter
import PyPDF2

app = Flask(__name__)


@app.route('/')
def hello():
# get the file and start seat number and end seat number sem number
# create pdfReader_obj = PyPDF2.PdfFileReader(pdfFileObj_final) object
# call function converter and pass that object seat nos and sem no 
    return render_template('gtml/home.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)

