from app import db
from datetime import datetime


class Post():
    '''
    post contains: title,body,tags,views,comments
    '''
    def __init__(self):
        pass

    @staticmethod
    def insert_post(post_record):
        '''
        used only for admin
        '''
        db.posts.insert(post_record)

    @staticmethod
    def get_all_posts():
        '''
        return all posts
        used in index
        It posts returned should sorted by time, I haven't code it yet
        '''
        return db.posts.find()

    @staticmethod
    def get_post_by_id(post_id):
        '''
        return a dic
        return the post by id provided
        used in post page
        '''
        return db.posts.find_one({'id':post_id})

    @staticmethod
    def get_posts_by_tag(tag):
        '''
        return a cursor
        return all posts with the tag provided
        '''
        return db.posts.find({'tags':tag})

    @staticmethod
    def get_posts_by_topic(topic):
        '''
        return all posts by the topic given
        used in particular topic given
        '''
        return db.posts.find({'topic':topic})

    @staticmethod
    def get_posts_count():
        '''
        return the number of posts
        '''
        return db.posts.count()

    @staticmethod
    def views_add_one(post_id):
        '''
        add one views times to a particular post by given id
        '''
        db.posts.update({'id':post_id},{'$inc':{'views':1}})
        return True
'''
    @staticmethod
    def get_posts_by_user(email):
        posts_list = []
        posts = db.posts.find({'author.email':email})
        for post in posts:
            posts_list.append(post)
        return posts_list

    @staticmethod
    def get_posts_by_followed(user):
        posts = []
        for user_followed in user.followed: # user_followed is exactly the email, so pass it to get_posts_by_user()
            posts_by_user = Post.get_posts_by_user(user_followed)
            for posts_col in posts_by_user:
                posts.append(posts_col)
            #posts.append(Post.get_posts_by_user(user_followed))
        return posts
'''
