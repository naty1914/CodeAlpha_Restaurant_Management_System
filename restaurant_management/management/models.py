""" A module that contains Models for the management app """
from django.db import models
from django.core.exceptions import ValidationError

class MenuItem(models.Model):
    """ Model for Menu Item """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    
    def __str__(self): 
       """ String representation of Menu Item """
       return  f"{self.name} - ${self.price}"

class Order(models.Model):
    """ Model for Order """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       """ String representation of Order """
       return  f"{self.menu_item.name} - {self.quantity} - {self.order_date}"
    def menu_item_price(self):
        """ Get the price of the menu item """
        return self.menu_item.price
    def menu_item_name(self):
        """ Get the name of the menu item """
        return self.menu_item.name
    
class Table(models.Model):
    """ Model for Table """
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
    ]
    table_number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    
    def __str__(self):
             """ String representation of Table """
             return f"Table {self.table_number} - Seats: {self.seats} - Status: {self.status}"
    
  
class Inventory(models.Model):
    """ Model for Inventory """
    item_name = models.CharField(max_length=255)
    item_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    
    def __str__(self):
        """ String representation of Inventory """
        return  f"{self.item_name} - {self.item_quantity} - ${self.price}"
    def total_price(self):
        """ Get the total price of the inventory item """
        return  self.item_quantity * self.price
class Reservation(models.Model):
    """ Model for Reservation """
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_name = models.CharField(max_length=255)
    reservation_phone = models.CharField(max_length=255)
    reservation_date = models.DateTimeField()
    
    def __str__(self):
            """ String representation of Reservation """
            return f"Table {self.table.table_number} - {self.reservation_name} - {self.reservation_date}"
    def save(self, *args, **kwargs):
        """ Save method for Reservation """
        self.table.status = 'reserved'
        self.table.save()
        super().save(*args, **kwargs)

        
    def delete(self, *args, **kwargs):
        """ Delete method for Reservation """
        super().delete(*args, **kwargs)
        if not Reservation.objects.filter(table=self.table).exists():
            self.table.status = 'available'
            self.table.save()
    @staticmethod
    def get_reserved_tables():
        """ Get reserved tables """
        return Table.objects.filter(status='reserved')