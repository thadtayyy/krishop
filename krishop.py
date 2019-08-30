from flask import Flask, render_template, url_for, escape, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '02e9833c485b125c9266aff155a4c084'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return  f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    store = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
    
    def __repr__(self):
        return  f"Item('{self.name}', '{self.price}', '{self.store}', '{self.image_file}')"

items = [
    {
        'name': 'Water Bottle',
        'store': 'Nike',
        'price': '$12'
    },
    {
        'name': 'T-Shirt',
        'store': 'Uniqlo',
        'price': '$24'
    },
    {
        'name': 'Airpods',
        'store': 'Apple',
        'price': '$230'
    }
]
@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', items=items)

@app.route('/about')
def about():
    return render_template('about.html', title='About')  

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('hello'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'john@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('hello'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)

 