from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import os
import rec_gan

UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = {'npz'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            savepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(savepath)
            print "Image uploaded successfully."
            return predict(savepath)
    return render_template('home.html')


@app.route('/images/<filename>')
def uploaded_file(filename):
    html_str = '''
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Flask Application</title>
      </head>
      <body>
        <h1> 3-D image reconstruction from 2.5-D images </h1>
        <p> Input Image </p>
        <img src='{}' alt="alt">
      </body>
    </html>
    '''.format(filename)

    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


def get_y(x):
    return '/Users/souravchk/Desktop/table1_2040_y.npz'


def predict(x):
    y = get_y(x)
    rec_gan.demo_3D_RecGAN.ttest_demo(x, y)
    print "predictions done and locally saved."
    rec_gan.demo_3D_RecGAN.visualize()
    print 'All plots saved as images.'
    return render_template('output.html')


if __name__ == "__main__":
    app.run(debug=True)
