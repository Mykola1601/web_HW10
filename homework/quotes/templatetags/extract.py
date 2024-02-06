
# from bson.objectid import ObjectId
from django.shortcuts import  get_object_or_404
from django import template
from ..models import Author, Tag


register = template.Library()


def get_author(id_):
    # print("........",id_)
    author = get_object_or_404(Author, id = id_)
    # print("...........", author.fullname)
    return author.fullname



def get_tags(id_):
    tags = Tag.objects.filter(quote = id_).all()
    return tags


register.filter('tags', get_tags)
register.filter('author', get_author)











