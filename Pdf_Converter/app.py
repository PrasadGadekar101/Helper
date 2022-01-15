from flask import Flask, render_template, request, redirect, url_for
from converter import converter
from PyPDF2 import PdfFileReader


def read_to_string(pdfReader_obj):
    all_in_one = ''
    for page_no in range(pdfReader_obj.getNumPages()):
        pageObj_single = pdfReader_obj.getPage(page_no)
        pageone_text_single = pageObj_single.extractText()
        all_in_one = all_in_one + pageone_text_single
    return all_in_one


app = Flask(__name__)


@app.route('/')
def hello():
    # get the file and start seat number and end seat number sem number
    # create pdfReader_obj = PyPDF2.PdfFileReader(pdfFileObj_final) object
    # call function converter and pass that object seat nos and sem no
    return render_template('home.html', info={'no_file': False})


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        starting_seat_no = int(request.form.get("start_seat_no"))
        ending_seat_no = int(request.form.get("end_seat_no"))
        sem_no = int(request.form.get("sem_no"))
        uploaded_file.save('uploads/' + uploaded_file.filename)
        uploaded_file_data = open('uploads/'+uploaded_file.filename, 'rb')
        pdfReader_obj = PdfFileReader(uploaded_file_data)
        to_single_string = read_to_string(pdfReader_obj)
        status = converter(to_single_string, starting_seat_no,
                           ending_seat_no, sem_no)
        print(status)
        return redirect(url_for('upload_file'))
    else:
        return render_template("home.html", info={'no_file': True, 'file_upload': True})


if __name__ == "__main__":
    app.run(port=8000, debug=True)
