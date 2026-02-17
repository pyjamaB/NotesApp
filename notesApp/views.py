from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Note


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("all_notes")
    else:
        form = UserCreationForm()
    return render(request, "users/registration.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("all_notes")
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("all_notes")

@login_required
def all_notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, "notesApp/all_notes.html", {"notes":notes})

@login_required
def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        Note.objects.create(user=request.user, title=title, text=text)
        return redirect("all_notes")
    return render(request, "notesApp/note_form.html")

@login_required
def show_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, "notesApp/show_note.html", {"note": note})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        note.title = request.POST.get("title")
        note.text = request.POST.get("text")
        note.save()
        return redirect("all_notes")
    return render(request, "notesApp/note_form.html", {"note": note})

@login_required
def search_notes(request):
    query = request.GET.get("q", "")
    results = Note.objects.filter(user=request.user
    ).filter(Q(title__icontains=query) | Q(text__icontains=query))
    return render(request, "notesApp/search_notes.html", {"results": results, "query": query})
