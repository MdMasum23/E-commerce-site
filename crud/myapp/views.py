from django.shortcuts import render, get_object_or_404, redirect
from .models import Item  # Make sure Item model exists in models.py

# Create
def create_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Item.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request, 'create_item.html')

# Read
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item_detail.html', {'item': item})

# Update
def update_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        return redirect('item_list')
    return render(request, 'update_item.html', {'item': item})

# Delete
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('item_list')
