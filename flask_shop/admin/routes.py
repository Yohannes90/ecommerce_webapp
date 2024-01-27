from flask import flash, redirect, render_template, request, session, url_for
from flask_shop import app, db, bcrypt
from .models import User
# from flask_shop.products.models import Brand, Catagory
from .forms import RegistrationForm, LoginForm



@app.route('/admin')
def admin():
    if 'email' not in session:
        flash("Please login first!", "danger")
        return redirect(url_for('login'))
    # products = AddProduct.query.all()
    return render_template('admin/index.html', title="Admin Page, products=products")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        # db.session.commit()
        flash('Your account have been successfully created', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="Registeration Page")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash('You have successfully logged in to your account', 'success')
        else:
            flash('Wrong user email or password! Please try again.', 'danger')
        return redirect(request.args.get('next') or url_for('admin'))

    return render_template('admin/login.html', form=form, title="Login Page")
