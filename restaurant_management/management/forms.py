from django import forms
from .models import Reservation, Table

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'reservation_name', 'reservation_phone', 'reservation_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(status='available')