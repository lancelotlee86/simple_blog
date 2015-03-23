from flask import render_template,flash,redirect,session,url_for,request,g
from app import app,db    # db and posts are defined in __init__.py
from .forms import PostForm    # actually from the form.py file
from .models import Post, Info
from datetime import datetime
from .auth import requires_auth


@app.route('/')
@app.route('/index')
def index():
    '''
    the home page
    show all posts sort by time
    '''
    posts = Post.get_all_posts()
    return render_template('index.html',
        title = 'Lancelot\'s Blog',
        posts = posts
        )

@app.route('/topic/<topic>')
def topic(topic):
    '''
    return posts by topic given
    /topic/programming means that all posts with topic "programming"
    '''
    posts = Post.get_posts_by_topic(topic)
    return render_template('topic.html',
        posts = posts)

@app.route('/post/<post_id>')   # note that variable post_id is not int actually.
def post(post_id):
    '''
    get post by url.
    '/post/12' means the post with id 12
    '''
    Post.views_add_one(int(post_id))
    post = Post.get_post_by_id(int(post_id))
    return render_template('post.html',
        post = post)

@app.route('/tag/<tag>')
def tag(tag):
    '''
    get posts by tag given
    /tag/python means all posts with tag python
    '''
    posts = Post.get_posts_by_tag(tag)
    return render_template('tag.html',
        posts = posts,
        tag = tag)

@app.route('/about_me')
def about_me():
    '''
    show the about_me page
    '''
    return render_template('about_me.html')

@app.route('/message_board')
def message_board():
    '''
    show the message_board page
    '''
    return render_template('message_board.html')

@app.route('/admin', methods=['GET','POST'])
@requires_auth
def admin():
    '''
    turn to admin page
    add post, delete post, etc..
    '''
    form = PostForm()

    # change tags list into orderd pair list
    tags = Info.get_all_tags()
    tags_pair = []
    for tag in tags:
        tags_pair.append( (tag,tag) )
    form.tags.choices = tags_pair

    # change topics list into orderd pair list
    topics = Info.get_all_topics()
    topics_pair = []
    for topic in topics:
        topics_pair.append( (topic,topic) )
    form.topics.choices = topics_pair

    if form.validate_on_submit():
        if form.tag_addition.data != '':
            tags = form.tags.data + [form.tag_addition.data]
        else:
            tags = form.tags.data

        post_record = {
            'id' : Info.get_new_post_id(),
            'tags' : tags,
            'topics' : form.topics.data,
            'timestamp' : datetime.utcnow(),
            'views' : 0,
            'title' : form.title.data,
            'body' : form.body.data
        }
        Post.insert_post(post_record)

        if form.tag_addition.data is not None:
            '''
            if we have a tag_addition, we need add this tag to db.info
            '''
            Info.add_new_tag(form.tag_addition.data)
        flash('Your post is now live!')
        return redirect(url_for('admin'))

    return render_template('admin.html',
        form = form)
