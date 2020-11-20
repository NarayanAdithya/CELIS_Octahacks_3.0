#Code for all Linked Routes
from app import app,forms,db,socketio,mail
from flask_socketio import emit,leave_room,join_room
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,flash,jsonify
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User,thread,post,Courses,enrolled
from app.forms import LoginForm,RegisterForm,add_course_form,RequestResetForm, ResetPasswordForm
from werkzeug.urls import url_parse
from wtforms.validators import ValidationError
from datetime import datetime
import pickle
from flask_mail import Message
from threading import Thread

#Login Part
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Email or Password',category="danger")
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc!='':
            next_page=url_for('index')
        return redirect(next_page)
    return render_template('signinpage.html',title='SignIn',form=form)

#Registration
@app.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=forms.RegisterForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,user_role=form.user_role.data,Region=form.Region.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Successfully Registered',category="success")
        msg = Message('Welcome to CELIS',
                  sender="celis.students@gmail.com",
                  recipients=[user.email])
        msg.body="Hey There, We are happy that you have decided to join our community, We look forward to working with you. If you have any issues do notify us in our contact us section"
        Thread(target=send_async_email,args=(app,msg)).start()
        print(form.password.data)
        print(form.user_role.data)
        print(form.Region.data)
        return redirect(url_for('login'))
    return render_template('signuppage.html',form=form,title='Register')


@app.route('/')
@app.route('/index')
def index():
    return render_template('celis.html',title='Home',data_footer_aos="fade-left",data_aos_footer_delay=100,data_aos_header="fade-left",data_header_aos_delay=100)


@app.route('/logout')
def logout():
    current_user.last_seen=datetime.utcnow()
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))


