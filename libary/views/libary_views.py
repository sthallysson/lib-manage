from django.shortcuts import render, get_object_or_404, redirect
from libary.models import Collection
from django.db.models import Q
from django.contrib.auth.models import User


def index(request):
    collection = Collection.objects.all()
    context = {'collection': collection}
    return render(request, 'libary/index.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('libary:index')

    collection = Collection.objects.all().filter(Q(title__icontains=search_value))
    context = {'collection': collection}
    return render(request, 'libary/index.html', context)


def book(request, book_id):
    single_book = get_object_or_404(Collection, pk=book_id)
    context = {'book': single_book}
    return render(request, 'libary/book.html', context)


def user_read(request):
    users = User.objects.all()
    return render(request, 'libary/users.html', {'users': users})
