from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .forms import CanvasOrderForm, AccessoriesOrderForm, TShirtOrderForm
from .models import CustomerOrder
#from .forms import TShirtOrderForm # TODO: do the form

class TShirtOrderView(CreateView, LoginRequiredMixin):
    model = CustomerOrder
    form_class = TShirtOrderForm
    template_name = 'orders/tshirt_order_template.html'
    success_url = reverse_lazy('dashboard')


class AccessoriesOrderView(CreateView, LoginRequiredMixin):
    model = CustomerOrder
    form_class = AccessoriesOrderForm
    template_name = 'orders/accessories_order_template.html'
    success_url = reverse_lazy('dashboard')


class CanvasOrderView(CreateView, LoginRequiredMixin):
    model = CustomerOrder
    form_class = CanvasOrderForm
    template_name = 'orders/canvas_order_template.html'
    success_url = reverse_lazy('dashboard')


class MyOrdersView(ListView, LoginRequiredMixin):
    model = CustomerOrder
    template_name = 'orders/my_orders_template.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return CustomerOrder.objects.filter(user=self.request.user)



