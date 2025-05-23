from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Tag
from .forms import CategoryForm, TagForm

# Category Views
def category_list(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {"categories": categories})

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "category_form.html", {"form": form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)
    return render(request, "category_form.html", {"form": form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    return render(request, "category_confirm_delete.html", {"category": category})

# Tag Views
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "tag_list.html", {"tags": tags})

def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
    else:
        form = TagForm()
    return render(request, "tag_form.html", {"form": form})

def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
    else:
        form = TagForm(instance=tag)
    return render(request, "tag_form.html", {"form": form})

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        return redirect("tag_list")
    return render(request, "tag_confirm_delete.html", {"tag": tag})