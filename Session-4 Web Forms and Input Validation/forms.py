from flask_wtf import FlaskForm

from wtforms import (
    StringField ,
    SelectField ,
    DateField ,
    PasswordField ,
    SubmitField ,
    BooleanField

)

from wtforms.validators import (
    DataRequired ,
    length,
    Email,
    optional ,
    EqualTo
    
)

class SignupForm(FlaskForm):
    username=StringField(
        "Username" ,
        validators=[DataRequired() ,
        length(2,30)])
    
    email=StringField(
        "Email" ,
        validators=[DataRequired() ,
        Email()])
    
    gender=SelectField(
        "Gender",
        choices=["Mail","Female"],
        validators=[optional()]
    )

    dob=DateField(
        "Date Of Birth",
        validators=[optional()]
    )

    password=PasswordField(
    "Password",
    validators=[DataRequired(), length(5,25)]
    )

    confirm_password=PasswordField(
    "Confirm Password",
    validators=[DataRequired(), length(5,25),EqualTo("password")]
    )

    submit=SubmitField("Signup")


class LoginForm(FlaskForm):
    email=StringField(
        "Email" ,
        validators=[DataRequired() ,
        Email()])
    
    password=PasswordField(
    "Password",
    validators=[DataRequired(), length(5,25)]
    )

    remember_me=BooleanField("Remember Me")

    submit=SubmitField("Login")