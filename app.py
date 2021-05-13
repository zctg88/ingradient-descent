#import libraries
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

# import libraries for model
from fastai.vision.all import *
from fastai.vision.widgets import *

# -------------------------------- Model Code -------------------------------------

path = Path()
vocab_1M_v1 = []
vocab_1M_v3 = []
vocab_1M_v4 = []
vocab_5k = []

def get_x(r): 
    # f = r['image']
    # return (data_path/f[0]/f[1]/f[2]/f[3]/f)
    return 0

def get_y(r): return r['labels']

def splitter(df):
    train = df.index[df['train']].tolist()
    valid = df.index[~df['train']].tolist()
    return train,valid

# Grab Recipe1M v1 vocab from file
with open('static/vocab/vocab_r1M_v1.txt') as f:
    for line in f:
        vocab_1M_v1.append(line.strip())

# Grab Recipe1M v3 vocab from file
with open('static/vocab/vocab_r1M_v3.txt') as f:
    for line in f:
        vocab_1M_v3.append(line.strip())

# Grab Recipe1M v4 vocab from file
with open('static/vocab/vocab_r1M_v4.txt') as f:
    for line in f:
        vocab_1M_v4.append(line.strip())

# Grab Recipe1M vocab from file
with open('static/vocab/vocab_r5k.txt') as f:
    for line in f:
        vocab_5k.append(line.strip())

# Method to get list of top predicted ingredients
def predict_ingredients(model, vocab, img_path):
    print(img_path)
    img = PILImage.create(img_path)
    preds = model.predict(img)
    preds_list = preds[-1].tolist()
    pred_idxs = [preds_list.index(elem) for elem in preds_list if(elem > 0.2)]
    pred_list = []
    for idx in pred_idxs:
        pred_list.append(vocab[idx])
    return pred_list

# Load model
model_1M_v1 = load_learner('static/models/r1m_v1.pkl')
model_1M_v3 = load_learner('static/models/r1m_v3.pkl')
model_1M_v4 = load_learner('static/models/r1m_v4.pkl')
model_5k = load_learner('static/models/r5k_v1.pkl')

# ---------------------------------------------------------------------------------

# Define folder to place uploaded images
UPLOAD_FOLDER = 'static/uploads/'

#Initialize the flask App
app = Flask(__name__)

# App configurations
app.secret_key = "secret key"   # change this later
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Define allowed extensions for uploaded files
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    """ 
    Return true if file is valid (contains a "." and has allowed extension); 
    false otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
# Define main page
@app.route('/')
def upload_form():
    return render_template('index.html')

# Define main page after file is uploaded
@app.route('/', methods=['POST'])
def upload_image():
    # If there is no 'file' key in the request.files dictionary
    if 'file' not in request.files:
        # flash('No file key')
        return redirect(request.url)

    # Get the file
    file = request.files['file']

    # If the file is empty
    if file.filename == '':
        # flash("No image uploaded!")
        return redirect(request.url)

    # If the file is present and valid
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Send predictions to host
        flash(predict_ingredients(model_1M_v1, vocab_1M_v1, file), 'Recipe1M+ v1')
        flash(predict_ingredients(model_5k, vocab_5k, file), 'Recipes5k')
        flash(predict_ingredients(model_1M_v3, vocab_1M_v3, file), 'Recipe1M+ v3')
        flash(predict_ingredients(model_1M_v4, vocab_1M_v4, file), 'Recipe1M+ v4')
        return render_template('index.html', filename=filename)

    # If file type isn't allowed
    else:
        # flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run(debug=True)