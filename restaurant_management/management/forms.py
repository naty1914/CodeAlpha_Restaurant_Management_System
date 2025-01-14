""" A module that contains Forms for the management app """
from django import forms
from .models import Reservation, Table

class ReservationForm(forms.ModelForm):
    """ Form for Reservation """
    class Meta:
        """ Meta class for ReservationForm """
        model = Reservation
        fields = ['table', 'reservation_name', 'reservation_phone', 'reservation_date']

    def __init__(self, *args, **kwargs):
        """ Initialize the ReservationForm """
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(status='available')