from django import template
from core.models import *

register=template.Library()


def slugify(value):
    value=value.split()
    return "-".join(value)

def joint(value1,value2,value3):
    return value2+value1+value3
# @register.filter
# def like(value):
#     post=Post.objects.first()
#     print(post)
#     return post.likes.count()


register.filter('slugify',slugify)
register.filter('joint',joint)
