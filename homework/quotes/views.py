from .utils import get_mongodb
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Quote


# for mongo
def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quote.find()
    # print(f"..............{type(quotes)}.............")
    quotes = Quote.objects.all()
    # for quote in quotes:
    #     print(f"..............{quote.author.fullname}.............")
    # per_page = 10
    # paginator = Paginator(list(quotes), per_page)
    # quotes_on_page = paginator.page(page)
    # print(f"..............{type(quotes_on_page)}.............")
    # return render(request, "quotes/index.html", context = {"quotes" : quotes_on_page} )
    return render(request, "quotes/index.html", context =  {"quotes": quotes} )






