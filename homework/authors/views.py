from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from quotes.models import Quote, Author

# for mongo
from quotes.utils import get_mongodb
def main(request, author=""):
    # db = get_mongodb()
    # a = db.author.find_one({"fullname":author}) 
    a = get_object_or_404(Author, fullname=author)
    return render(request, "authors/authors.html", context = vars(a))
    
