from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "pera123"


class EstateForm(FlaskForm):
    lokacija = FloatField("Unesite udaljenost od centra grada u m2",validators = [DataRequired()])
    kvadratura = FloatField("Unesite kvadraturu stana",validators = [DataRequired()])
    sobnost = FloatField("Unesite broj soba",validators = [DataRequired()])
    submit = SubmitField("Submit")
    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/proveri-cenu",methods=["GET","POST"])
def proveri_cenu():
  
    form = EstateForm()
    lokacija = None
    kvadratura = None
    sobnost = None
    predvidjena_cena = None
    if form.validate_on_submit():
        lokacija = form.lokacija.data
        kvadratura = form.kvadratura.data
        sobnost = form.sobnost.data
        form.lokacija.data = ''
        form.sobnost.data = ''
    if request.method == 'POST':
        app.logger.debug(request.form)
        lokacija = request.form['lokacija']
        kvadratura = request.form['kvadratura']
        sobnost = request.form['sobnost']
        predvidjena_cena = 2.3572870790941087 + 7.031327*float(kvadratura) + 6.561546708895282*float(sobnost) + 1.456837214510932*float(lokacija)
        
        #rastojanje': 1.456837214510932e+277, 'povrsina': 7.03132733424158e+280, 'sobnost': 6.561546708895282e+276, 'w0': 2.3572870790941087e+276}
        

    return render_template("predikcije.html", lokacija = lokacija, kvadratura = kvadratura, sobnost = sobnost, form=form, predvidjena_cena = predvidjena_cena)
