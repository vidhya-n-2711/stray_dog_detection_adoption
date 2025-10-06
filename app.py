import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from models import db, Dog
from detection.detect import detect_dogs, init_model
from recommender.recommend import recommend_dogs
from sqlalchemy.exc import OperationalError

UPLOAD_FOLDER = os.path.join('static', 'images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev_secret'

db.init_app(app)
with app.app_context():
    try:
        db.create_all()
    except OperationalError:
        pass

init_model()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    recent = Dog.query.order_by(Dog.detected_at.desc()).limit(6).all()
    return render_template('index.html', recent=recent)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file.save(save_path)

            out_path = os.path.join(app.config['UPLOAD_FOLDER'], 'annot_' + filename)
            count = detect_dogs(save_path, output_path=out_path)

            dog = Dog(
                image_path=out_path,
                count=count,
                location=request.form.get('location', ''),
                health=request.form.get('health','Unknown'),
                age=request.form.get('age','Unknown'),
                size=request.form.get('size','Unknown')
            )
            db.session.add(dog)
            db.session.commit()

            flash(f'Detected {count} dog(s). Saved and registered.')
            return redirect(url_for('index'))
    return render_template('upload.html')

@app.route('/adopt', methods=['GET','POST'])
def adopt():
    recommended = []
    if request.method == 'POST':
        prefs = {
            'size': request.form.get('size'),
            'age': request.form.get('age'),
            'health': request.form.get('health')
        }
        recommended = recommend_dogs(db.session, prefs, limit=10)
    return render_template('adopt.html', recommended=recommended)

@app.route('/dog/<int:dog_id>/mark_adopted')
def mark_adopted(dog_id):
    dog = Dog.query.get_or_404(dog_id)
    dog.adopted = True
    db.session.commit()
    flash('Dog marked as adopted')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

