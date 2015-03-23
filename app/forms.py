from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SelectMultipleField

# validator is a function that can be attached to a field to perform validation on the data submitted by the user
from wtforms.validators import DataRequired, Length
from app import db


class PostForm(Form):
    '''
    used in admin page to post my post
    '''
    title = StringField('title',validators=[DataRequired()])
    body = TextAreaField('body',validators=[DataRequired()])

    #tags = SelectMultipleField('tags', choices = [('C++','C++'), ('Python','Python')])
    tags = SelectMultipleField('tags', coerce = str)    # cause the choices is dynamic, so we put it in view function
    tag_addition = StringField('tag_addition')

    topics = SelectMultipleField('topics', coerce = str)    # watch out the 'str' here, don't write int!

'''
class EditForm(Form):
    nickname = StringField('nickname', validators = [DataRequired()],)
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user_record = db.users.find_one({'nickname':self.nickname.data})
        if user_record != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True
'''
