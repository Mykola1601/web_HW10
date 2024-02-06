
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("quotes.urls")),
    path('author/', include("authors.urls")),
    # path('author/<int:page>', views.main, name = "root_paginate"),
    path('users/', include("users.urls")),

]
