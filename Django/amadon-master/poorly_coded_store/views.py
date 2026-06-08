from django.shortcuts import get_object_or_404, redirect, render
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method != "POST":
        return redirect("/")
        
    try:
        quantity_from_form = int(request.POST.get("quantity", 0))
        product_id_from_form = int(request.POST.get("product_id", 0))
        product = get_object_or_404(Product, id=product_id_from_form) 
    except (ValueError, TypeError):
        return redirect("/")
    
    if quantity_from_form <= 0:
        return redirect("/")
    
    if quantity_from_form > product.quantity:
        print("Not enough inventory!")
        return redirect("/")
    
    total_charge = quantity_from_form * product.price
    Order.objects.create(quantity_ordered=quantity_from_form, 
    total_price=total_charge)
    product.quantity -= quantity_from_form
    product.save()
    return redirect( "/checkout")