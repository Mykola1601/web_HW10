from django.shortcuts import render
from quotes.models import Tag,Quote


def main(request, tag=""):
    tag = Tag.objects.get(name=tag)
    # Знайти всі цитати, пов'язані з цим тегом
    quotes = Quote.objects.filter(tags=tag)
    return render(request, "tags/tags.html", context = {'quotes': quotes, "tags":tag})

