""" A module that contains Views for the management app """
from django.shortcuts import render, HttpResponse
from .models import MenuItem, Order, Table, Reservation, Inventory
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def home(request):
    """ Home view """
    return render(request, 'management/home.html')
def menu_items(request):
    """ Menu items view """
    menu_items = MenuItem.objects.all()
    return render(request, 'management/menu_items.html', {'menu_items': menu_items})
@login_required(login_url='/admin/login/')
def orders(request):
    """ Orders view """
    if not request.user.is_staff:
        raise PermissionDenied
    orders = Order.objects.all()
    return render(request, 'management/orders.html', {'orders': orders})

@login_required(login_url='/admin/login/')
def tables(request):
    """ Tables view """
    if not request.user.is_staff:
        raise PermissionDenied
    tables = Table.objects.all()
    return render(request, 'management/tables.html', {'tables': tables})

@login_required(login_url='/admin/login/')
def reservations(request):
    """ Reservations view """
    if not request.user.is_staff:
        raise PermissionDenied
    reservations = Reservation.objects.all()
    return render(request, 'management/reservations.html', {'reservations': reservations})

@login_required(login_url='/admin/login/')
def inventory(request):
    """ Inventory view """
    if not request.user.is_staff:
        raise PermissionDenied
    inventory = Inventory.objects.all()
  
    return render(request, 'management/inventory.html', {'inventory': inventory})

@login_required(login_url='/admin/login/')
def sales_report(request):
    """ Sales report view """
    if not request.user.is_staff:
        raise PermissionDenied
    sales_data = Order.objects.values('menu_item__name').annotate(total_quantity=Sum('quantity'), total_sales=Sum('quantity') * Sum('menu_item__price'))
    return render(request, 'management/sales_report.html', {'sales_data': sales_data})
