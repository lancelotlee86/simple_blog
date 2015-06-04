from flask import render_template,flash,redirect,session,url_for,request,g
from app import app,db    # db and posts are defined in __init__.py
from .forms import PostForm, MessageForm    # actually from the form.py file
from .models import Post, Info, Message
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
    form = MessageForm()
    messages = Message.get_all_messages()

    return render_template('message_board.html',
        form = form,
        messages = messages)

@app.route('/message_board', methods=["POST"])
def save_message():
    '''
    save the message the user submit
    '''
    form = MessageForm()
    # print(form.visitor.data) form的信息还是可以访问的
    # print(form.message.data)
    # print(request.form['visitor']) 可以这么访问post的数据
    message_record = {
        'visitor' : form.visitor.data,
        'message' : form.message.data,
        'timestamp' : datetime.utcnow()
    }
    Message.insert_message(message_record)
    flash('Your message is now live!')
    return redirect(url_for('message_board'))

@app.route('/admin')
@requires_auth
def admin():
    '''
    turn to admin page
    delete post
    '''
    form = PostForm()
    posts = Post.get_all_posts()

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

    return render_template('admin.html',
        form = form,
        posts = posts)

@app.route('/admin', methods=["POST"])
@requires_auth
def submit_post():
    '''
    only for post a post in the web-form
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
        if form.topic_addition.data != '':
            topics = form.topics.data + [form.topic_addition.data]
        else:
            topics = form.topics.data
        post_record = {
            'id' : Info.get_new_post_id(),
            'tags' : tags,
            'topics' : topics,
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
        if form.topic_addition.data is not None:
            '''
            if we have a topic_addition, we need add this topic to db.info
            '''
            Info.add_new_topic(form.topic_addition.data)

        flash('Your post is now live!')
        return redirect(url_for('admin'))


"""
@app.route('/admin', methods=['GET','POST'])
@requires_auth
def admin():
    '''
    turn to admin page
    add post, delete post, etc..
    '''

    form = PostForm()
    form.title.data = 'avcc'    #test
    form.tags.data = ['programming']    #test
    posts = Post.get_all_posts()

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
    print('d')

    if form.validate_on_submit():
        print('a')
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
        print('b')
        Post.insert_post(post_record)

        if form.tag_addition.data is not None:
            '''
            if we have a tag_addition, we need add this tag to db.info
            '''
            Info.add_new_tag(form.tag_addition.data)
        flash('Your post is now live!')
        print('c')
        return redirect(url_for('admin'))
    print('e')
    return render_template('admin.html',
        form = form,
        posts = posts)
"""

@app.route('/post/<post_id>/remove')
def post_remove(post_id):
    '''
    remove a post by the given id
    '''
    Post.remove_post_by_id(int(post_id))
    flash('Your post have been removed!')
    return redirect(url_for('admin'))

@app.route('/post/<post_id>/edit')
def post_edit(post_id):
    '''
    edit a post by the given id
    '''
    form = PostForm()
    post = Post.get_post_by_id(int(post_id))
    '''
    the following codes need rebuild
    '''
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

    form.body.data = post['body']

    return render_template('edit.html',
        form = form,
        post = post)

@app.route('/post/<post_id>/edit', methods=['POST'])
def update_post_edit(post_id):
    '''
    edit a post by the given id
    '''
    form = PostForm()
    post = Post.get_post_by_id(int(post_id))
    '''
    the following codes need rebuild
    '''
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

    form.body.data = post['body']

    if form.validate_on_submit():
        if form.tag_addition.data != '':
            tags = form.tags.data + [form.tag_addition.data]
        else:
            tags = form.tags.data
        if form.topic_addition.data != '':
            topics = form.topics.data + [form.topic_addition.data]
        else:
            topics = form.topics.data
        new_post_record = {
            'id' : int(post_id),
            'tags' : tags,
            'topics' : topics,
            'last_edit_time' : datetime.utcnow(),
            'title' : form.title.data,
            'body' : form.body.data}
        Post.update_post(new_post_record)
        return redirect(url_for('post',post_id = post['id']))
