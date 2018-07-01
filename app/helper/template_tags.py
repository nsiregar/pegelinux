from app import app
from app.models.comment import Comment


def get_children_comments(comment):
    comments = Comment.query.filter_by(parent_id=comment.id)
    return comments


app.jinja_env.globals.update(get_children_comments=get_children_comments)
