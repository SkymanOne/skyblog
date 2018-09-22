from app.models import *
from app import db


def create_new_post(title, short, body, time, author):
    try:
        url = title.replace(' ', '_')
        new_post = Post(title=title, url=url, short=short, body=body,
                        time=time, author=author)
        db.session.add(new_post)
        db.session.commit()
    except:
        return False
    return new_post


def get_topic(name):
    return Topic.query.filter_by(name=name).first()


def create_or_get_topic(name):
    topic = get_topic(name)
    if topic is None:
        topic = Topic(name=name)
        db.session.add(topic)
        db.session.commit()
    return topic


def get_post(url):
    return Post.query.filter_by(url=url).first()
