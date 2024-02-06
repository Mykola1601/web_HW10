from ..utils import get_mongodb
from django.shortcuts import render, get_object_or_404

from bson.objectid import ObjectId
from django import template
from ..models import Author, Tag


register = template.Library()


# def get_author(id_):
#     db = get_mongodb()
#     author = db.author.find_one({"_id":ObjectId(id_)  })
#     # author = Author.objects.all({"_id":ObjectId(id_)  })
#     return author["fullname"]

def get_author(id_):
    print("........",id_)
    author = get_object_or_404(Author, id = id_)
    print("...........", author.fullname)
    return author.fullname



def get_tags(id_):
    # print("...tag id ......",id_)
    tags = Tag.objects.filter(quote = id_).all()
    # for t in tags:
    #     print("...........", t.name)
    return tags


register.filter('tags', get_tags)
register.filter('author', get_author)


            # <small class="author" itemprop="author">
            #   {{quote.quote.author|author}}
            # </small>
            # <a href="/author/{{quote.quote.author|author}}">(about)</a>
            # <!-- <a href="/author/{{quote.quote.author|author}}">(about)</a>  -->
  

    # <!-- <div class="tags">
    #     Tags:
    #      {%for tag in quote.tags%}
    #     <a class="tag" href="/tag/{{tag}}">{{tag}}</a>
    #     {%endfor%}
    #   </div>










