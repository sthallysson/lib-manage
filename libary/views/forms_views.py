from django.shortcuts import render, redirect, get_object_or_404
from libary.models import Collection
from django.urls import reverse
from libary.forms import BookForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='libary:login')
def create(request):
    form_action = reverse('libary:create')
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        context = {'form': form,
                   'form_action': form_action
                   }

        if form.is_valid():
            book = form.save()
            return redirect('libary:update', book_id=book.pk)

        return render(request, 'libary/create.html', context)

    context = {'form': BookForm(),
               'form_action': form_action
               }
    return render(request, 'libary/create.html', context)


@login_required(login_url='libary:login')
def update(request, book_id):
    book = get_object_or_404(Collection, pk=book_id)
    form_action = reverse('libary:update', args=(book_id,))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        context = {'form': form,
                   'form_action': form_action
                   }

        if form.is_valid():
            book = form.save()
            return redirect('libary:update', book_id=book.pk)

        return render(request, 'libary/create.html', context)

    context = {'form': BookForm(instance=book),
               'form_action': form_action
               }
    return render(request, 'libary/create.html', context)


@login_required(login_url='libary:login')
def delete(request, book_id):
    book = get_object_or_404(Collection, pk=book_id)
    book.delete()

    return redirect('libary:index')
