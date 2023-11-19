from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView
from django.core.paginator import Paginator

def index(request):
    page_obj = items = Product.objects.all()

    item_name = request.GET.get("search")
    if item_name != "" and item_name is not None:
        page_obj = items.filter(name__icontains=item_name)

    paginator = Paginator(page_obj, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "snsorder/index.html", context)


class ProductListView(ListView):
    model = Product
    template_name = "snsorder/index.html"
    context_object_name = "items"
    paginate_by = 2


"""def indexItem(request, my_id):
    item = Product.objects.get(id = my_id)
    context = {
        "item": item
    }
    return render(request, "snsorder/detail.html", context)"""

class ProductDetailView(DetailView):
    model = Product
    template_name = "snsorder/detail.html"
    context_object_name = "item"

@login_required()
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["upload"]
        seller = request.user
        item = Product(
            name=name, price=price, description=description, image=image, seller=seller
        )
        item.save()
    return render(request, "snsorder/additem.html")


def update_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/snsorder/")
    context = {"item": item}
    return render(request, "snsorder/updateitem.html", context)

def delete_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("/snsorder/")
    context = {"item": item}
    return render(request, "snsorder/deleteitem.html", context)

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("snsorder:index")

