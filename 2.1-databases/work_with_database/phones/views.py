from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        phones_object = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones_object = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones_object = Phone.objects.order_by('-price')
    else:
        phones_object = Phone.objects.all()
    phones_list = []
    for phone in phones_object:
        phones_list.append({
            'name': phone.name,
            'image': phone.image,
            'slug': phone.slug,
            'price': phone.price,
            'release_date': phone.release_date,
            'lte_exists': phone.lte_exists
        })
    context = {
        'phones': phones_list
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    phone_dict = {
        'name': phone.name,
        'image': phone.image,
        'slug': phone.slug,
        'price': phone.price,
        'release_date': phone.release_date,
        'lte_exists': phone.lte_exists
    }
    context = {
        'phone': phone_dict
    }
    return render(request, template, context)
