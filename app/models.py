from app import db
from datetime import datetime


class Post():
    '''
    post contains: title, body, topic, tags, views, comments
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
        return db.posts.find_one( {'id':post_id} )

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
        return db.posts.find({'topics':topic})

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


class Info():
    '''
    Info contains:
        the number of the posts that I ever post (will used for post_id)
        list of topics
        list of tags
    '''
    def __init__(self):
        pass

    @staticmethod
    def get_new_post_id():
        '''
        when post a new post, we use it to get a absulote number of the new post
        and refresh the infomation of abs count
        '''
        db.info.update( { 'content':'post_count_abs' }, { "$inc" : { 'post_count_abs' : 1 } } )
        return db.info.find_one( { 'content':'post_count_abs' } )['post_count_abs']   # return a num

    @staticmethod
    def add_new_tag(tag):
        '''
        add new tag to tags list
        '''
        db.info.update( {'content':'tags'}, { "$addToSet" : { 'tags' : tag } } )

    @staticmethod
    def get_all_tags():
        '''
        get all tags from mongodb
        return a list of tags: [ 'tag1', 'tag2', ... ]
        '''
        list_of_tags = db.info.find_one( { 'content':'tags' } )['tags']
        return list_of_tags

    @staticmethod
    def add_new_topic(topic):
        '''
        add new topic to topics list
        '''
        db.info.update( {'content':'topics'}, { "$addToSet" : { 'topics' : topic } } )

    @staticmethod
    def get_all_topics():
        '''
        get all topics from mongodb
        return a list of topics: [ 'topic1', 'topic2', ... ]
        '''
        list_of_topics = db.info.find_one( { 'content':'topics' } )['topics']
        return list_of_topics
