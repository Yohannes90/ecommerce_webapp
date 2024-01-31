from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators


class AddProducts(Form):
    name = StringField('Name', [validators.DataRequired()] )
    price = IntegerField('Price', [validators.DataRequired()] )
    discount = IntegerField('Discount', default=0 )
    stock = IntegerField('Stock', [validators.DataRequired()] )
    description = TextAreaField('Description', [validators.DataRequired()] )
    colors = TextAreaField('Colors', [validators.DataRequired()] )

    image_1 = FileField('Image_1', validators=[FileRequired(), validators.FileAllowed('jpg', 'png', 'gif', 'jpeg')], 'images only please' )
    image_2 = FileField('Image_2', validators=[FileRequired(), validators.FileAllowed('jpg', 'png', 'gif', 'jpeg')], 'images only please' )
    image_3 = FileField('Image_3', validators=[FileRequired(), validators.FileAllowed('jpg', 'png', 'gif', 'jpeg')], 'images only please' )
