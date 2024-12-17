
from django.urls import path
from book_review.views import index, about, contact, book_detail

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'), 
    path('contact/', contact, name='contact'),
    path('book/detail/<int:bid>/', book_detail, name='book_detail')
]
