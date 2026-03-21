from django.urls import path
from blog_app.views import hello_view,emodji,pic

urlpatterns = [
    path('hello/', hello_view),
    path('emodji/', emodji),
    path('pic/', pic)
]
