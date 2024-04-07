from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book
from datetime import datetime


def books_view(request):
    template = 'books/books_list.html'
    # template = 'base.html'
    # context = {}
    # return render(request, template, context)
    book_objects = Book.objects.all()
    books_list = []
    for book in book_objects:
        books_list.append({
            'book_name': book.name,
            'book_author': book.author,
            'book_pub_date': book.pub_date.strftime('%Y-%m-%d')
        })
    context = {
        'books_list': books_list
    }
    return render(request, template, context)

def pub_date_view(request, pub_date):
    template = 'books/books_list.html'
    book_objects = Book.objects.filter(pub_date=datetime.strptime(pub_date, '%Y-%m-%d'))
    books_list = []
    for book in book_objects:
        books_list.append({
            'book_name': book.name,
            'book_author': book.author,
            'book_pub_date': book.pub_date.strftime('%Y-%m-%d')
        })
    paginator = Paginator(books_list, 1)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)
    context = {
        'books_list': books_list,
        'page': page
    }
    return render(request, template, context)