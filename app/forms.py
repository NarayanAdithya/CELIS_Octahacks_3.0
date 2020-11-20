#Web Forms for Registration and Signin Here
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,RadioField,SelectField,TextAreaField
from wtforms.fields.html5 import EmailField,URLField,DateField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,URL,Length
from app.models import User,Courses
from flask_login import current_user,login_user,logout_user,login_required
class RegisterForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()],render_kw={'class':'form-control form-group'})
    email=EmailField('Email',validators=[DataRequired(),Email()],render_kw={'class':'form-control form-group'})
    password=PasswordField('Password',validators=[DataRequired()],render_kw={'class':'form-control form-group'})
    conpassword=PasswordField('Re-Enter Password',validators=[DataRequired(),EqualTo('password')],render_kw={'class':'form-control form-group'})#('values','label')
    user_role=RadioField('User Role',validators=[DataRequired()],choices=[('Student','Student'),('Instructor','Instructor')],render_kw={'class':'form-check form-check-input','style':'list-style:none;'})
    Region=SelectField('Select Region',validators=[(DataRequired())],choices=[('America','America'),('Africa','Africa'),('Asia','Asia'),('Europe','Europe')],render_kw={'class':'form-group col-md-4 form-control '})
    # remember_me=BooleanField('Keep Me Signed In')
    submit=SubmitField('Sign In',render_kw={'class':'btn btn-primary btn-pill','style':'height : 50px;'})
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please Use a Different Username.')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please Use A different Email Address')
        
class LoginForm(FlaskForm):
    email=EmailField('Email',validators=[DataRequired(),Email()],render_kw={'class':'form-control form-group'})
    password=PasswordField('Password',validators=[DataRequired()],render_kw={'class':'form-control form-group'})
    remember_me=BooleanField('Keep Me Signed In')
    submit=SubmitField('Sign In',render_kw={'class':'btn btn-primary btn-pill','style':'height : 50px;'})




