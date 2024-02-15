pfrom flask import Flask , render_template, request
import joblib

model = joblib.load('Log_Reg_model.pkl')



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/careers')
def Career():
    return render_template('careers.html')

@app.route('/alumni')
def Alumni_Reviews():
    return 'Welcome to the Alumni Reviews'

@app.route('/projectlab')
def ProjectLab():
    return 'Welcome to the ProjectLab'

@app.route('/blog')
def Blog():
    return 'Welcome to the Blog'

@app.route('/Login', methods = ['post'])
def submit():
    a = request.form.get('user_name')
    b = request.form.get('ph_no')
    c = request.form.get('password')
    print(a, b, c)
    return 'Login Success'


@app.route('/Model', methods = ['post'])
def model_predict():
    a = float(request.form.get('preg'))
    b = float(request.form.get('plas'))
    c = float(request.form.get('pres'))
    d = float(request.form.get('skin'))
    e = float(request.form.get('test'))
    f = float(request.form.get('pedi'))
    g = float(request.form.get('mass'))
    h = float(request.form.get('age'))
    re = model.predict([[a,b,c,d,e,f,g,h]])
    if re[0]==1:
        return 'Person is Diabetic'
    else:
        return 'Person is Non Diabetic'

    return 'Prediction Done'


app.run(debug=True)