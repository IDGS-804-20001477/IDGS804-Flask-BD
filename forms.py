from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField

from wtforms import validators

class UserForm(Form):
    id=IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre=StringField('Nombre', [validators.DataRequired(message='valor no valido')])
    apaterno=StringField('Apellido Paterno', [validators.DataRequired(message='valor no valido')])
    email=EmailField('correo', [validators.DataRequired(message='valor no valido'),
        validators.Email(message='ingresa un correo valido')])
