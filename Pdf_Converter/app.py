
from fileinput import filename
from flask import Flask, send_file, render_template, request, redirect
from converter import converter
from PyPDF2 import PdfFileReader
import os

from werkzeug.utils import secure_filename


def read_to_string(pdfReader_obj):
    all_in_one = ''
    for page_no in range(pdfReader_obj.getNumPages()):
        pageObj_single = pdfReader_obj.getPage(page_no)
        pageone_text_single = pageObj_single.extractText()
        all_in_one = all_in_one + pageone_text_single
    return all_in_one


def exception_handling(response_dict):
    return render_template("home.html", response_dict=response_dict)


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def hello():
    return render_template('home.html', response_dict={})


@app.route('/', methods=['POST'])
def upload_file():
    response_dict = {'starting_seat_no': False,
                     'end_seat_no': False, 'sem_no': False, 'file': False}
    uploaded_file = request.files['file']
    if request.form.get("start_seat_no"):
        starting_seat_no = int(request.form.get("start_seat_no"))
        print(starting_seat_no)
        response_dict['starting_seat_no'] = True
    if request.form.get("end_seat_no"):
        end_seat_no = int(request.form.get("end_seat_no"))
        response_dict['end_seat_no'] = True
        print(end_seat_no)
    if request.form.get("sem_no"):
        sem_no = int(request.form.get("sem_no"))
        response_dict['sem_no'] = True
        print(sem_no)
    if uploaded_file:
        response_dict['file'] = True
        print(uploaded_file.filename)

    print(response_dict)
    response = list(response_dict.values())
    if False not in response:
        uploaded_file.save(os.path.join(
            app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        file_name = (uploaded_file.filename).split('.')[0]
        uploaded_file_data = open('uploads/'+uploaded_file.filename, 'rb')
        pdfReader_obj = PdfFileReader(uploaded_file_data)
        to_single_string = read_to_string(pdfReader_obj)
        status = converter(to_single_string, starting_seat_no,
                           end_seat_no, sem_no, file_name)
        uploaded_file_data.close()
        response_dict['Successfully_Done'] = True
        response_dict['file_name'] = file_name
        file_name = file_name +'.xlsx'
        return redirect('/downloadfile/' + file_name)
        # return render_template("home copy.html", response_dict=response_dict)
    else:
        return render_template("home.html", response_dict=response_dict)


@app.route("/downloadfile/<filename>", methods=["GET", "POST"])
def get_file(filename):
    return render_template('download.html', value=filename)


@app.route("/return-files/<filename>")
def return_files_tut(filename):
    file_path = 'uploads/' + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
