# Simple blog

* Python3
* Flask
* Pymongo
* MongoDB

I used it for my own blog. You can visit it on lancelot.xyz

Before using, you should set up some base data into mongodb
```
db.info.insert( { 'content':'post_count_abs', 'post_count_abs':0 } )
db.info.insert( { 'content':'tags', 'tags':[] } )
db.info.insert( { 'content':'topics', 'topics':[] } )
```

tags's addition and displayment will be dynamic, can't delete and no need to do so
topics will be static, if you want to add a topic, you should modify the base.html and add a topic into mongodb by yourself
But both can be choose when post a post
