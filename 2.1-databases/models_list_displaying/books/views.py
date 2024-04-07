from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book
from datetime import datetime


def books_view(request):
    template = 'books/books_list.html'
    # template = 'base.html'
    # context = {}
    # return render(request, template, context)
    book_objects = Book.objects.order_by('pub_date')
    books_list = []
    for book in book_objects:
        books_list.append({
            'book_name': book.name,
            'book_author': book.author,
            'book_pub_date': book.pub_date.strftime('%Y-%m-%d')
        })
    context = {
        'books_list': books_list,
        'prev_page': '',
        'next_page': ''
    }
    return render(request, template, context)

def pub_date_view(request, pub_date):
    template = 'books/books_list.html'
    # book_objects = Book.objects.filter(pub_date=datetime.strptime(pub_date, '%Y-%m-%d'))
    book_objects = Book.objects.order_by('pub_date')
    books_list = []
    for book in book_objects:
        books_list.append({
            'book_name': book.name,
            'book_author': book.author,
            'book_pub_date': book.pub_date.strftime('%Y-%m-%d')
        })
    prev_page = ''
    next_page = ''
    for book in books_list:
        if book['book_pub_date'] == pub_date:
            book_for_show = {
                'book_name': book['book_name'],
                'book_author': book['book_author'],
                'book_pub_date': book['book_pub_date']
            }
        elif book['book_pub_date'] < pub_date:
            prev_page = book['book_pub_date']
        elif book['book_pub_date'] > pub_date and next_page == '':
            next_page = book['book_pub_date']
    context = {
        'books_list': [book_for_show],
        'prev_page': prev_page,
        'next_page': next_page,
    }
    return render(request, template, context)