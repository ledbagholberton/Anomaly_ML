from flask import Flask
from flask import render_template, request, url_for, make_response
from werkzeug.utils import secure_filename
import os
from analyze_image import analyze_image
from delete_files import delete_files

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/status')
def status():
    """ check status """
    return 'OK'

@app.route('/')
def index(name=None):
    """ render index.html """
    frame = url_for('static', filename=f'frame.jpg')
    return render_template('index.html',
                            name=name,
                            path_upload_image=frame,
                            path_output_image=frame,
                            label="Result")

@app.route('/detection', methods=['POST'])
def detection(name=None):
    """ render result fo the model """
    delete_files()
    file = request.files['file']
    type_dataset = request.form['type_datasets']
    file_name = secure_filename(file.filename)
    new_path_image = os.path.join(app.root_path, 'static', 'images', file_name)
    file.save(new_path_image)
    path_upload_image = url_for('static', filename=f'images/{file_name}')
    label = analyze_image(path_image=f'static/images/{file_name}',
                          name_img=file_name,
                          type_dataset=type_dataset)
    path_output_image = url_for('static', filename=f'images/output_{file_name}')
    response = make_response(render_template('index.html',
                            name='',
                            path_upload_image=path_upload_image,
                            path_output_image=path_output_image,
                            label=label))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')