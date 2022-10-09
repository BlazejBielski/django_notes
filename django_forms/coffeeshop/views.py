from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.template import loader

from coffeeshop.forms import NameForm, UserForm


def home(request):
    return render(request, 'coffeeshop/home.html')


def thanks(request):
    return render(request, 'coffeeshop/thanks.html')


# def signup(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, f'it work properly!, {form.cleaned_data.get("name")}')
#             return HttpResponseRedirect('coffeeshop/thanks.html')
#     else:
#         form = NameForm()
#
#     template = loader.get_template('coffeeshop/signup.html')
#     context = {'form': form}
#     return HttpResponse(template.render(context, request))

def signup(request):
    form = UserForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "It works better")
            return redirect(reverse('coffeeshop:thanks'))

    return render(request, 'coffeeshop/signup.html', {'form': form})

def details(request):
    form = UserDetailForm(request.POST)
    if form.is_valid():
        user = form.save()
        form.save()
        return redirect(reverse('coffeeshop:thanks'))
    else:
        form = UserDetailForm(initial={'username': request.user.username, 'email': request.user.email})

    return render(request, 'coffeeshop/signup.html', {'form': form})
