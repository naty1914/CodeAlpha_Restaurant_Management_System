""" Test module for management app """
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.contrib.auth.models import User
from .models import MenuItem, Order, Table, Reservation, Inventory
from django.utils import timezone

class LoginTestCase(TestCase):
    """ Test class for login view """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_page(self):
        """ Test login page """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/login.html')

    def test_login(self):
        """ Test login view """
        response = self.client.post(reverse('login') + '?next=' + reverse('home'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('home'))

    def test_logout(self):
        """ Test logout view """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))

class MenuItemsViewTestCase(TestCase):
    """ Test class for menu items view """
    def setUp(self):
        """ Create test data """
        self.menu_item = MenuItem.objects.create(name='Test Item', price=10.00, description='Test Description')

    def test_menu_items_view(self):
        """ Test menu items view """
        response = self.client.get(reverse('menu_items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/menu_items.html')
        self.assertContains(response, 'Test Item')

class OrdersViewTestCase(TestCase):
    """ Test class for orders view """
    def setUp(self):
        """ Create test data """
        self.user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
        self.menu_item = MenuItem.objects.create(name='Test Item', price=10.00, description='Test Description')
        self.order = Order.objects.create(menu_item=self.menu_item, quantity=2)

    def test_orders_view(self):
        """ Test orders view """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/orders.html')
        self.assertContains(response, 'Test Item')


class ReservationsViewTestCase(TestCase):
    """ Test class for reservations view """
    def setUp(self):
        """ Create test data """
        self.user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
        self.table = Table.objects.create(table_number=1, seats=4, status='available')
        self.reservation = Reservation.objects.create(
            table=self.table,
            reservation_name='Test Reservation',
            reservation_phone='1234567890',
            reservation_date=timezone.make_aware(timezone.datetime(2023, 10, 10, 18, 0))
        )

    def test_reservations_view(self):
        """ Test reservations view """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/reservations.html')