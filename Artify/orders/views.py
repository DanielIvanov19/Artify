from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import CustomerOrder
#from .forms import TShirtOrderForm # TODO: do the form

class TShirtOrderView(CreateView):
    model = CustomerOrder
    # form_class = TShirtOrderForm # TODO
    template_name = 'orders/tshirt_order_form.html'
    success_url = reverse_lazy('dashboard')


class AccessoriesOrderView(CreateView):
    model = CustomerOrder
    # form_class = AccessoriesOrderForm
    template_name = 'orders/accessories_order_form.html'
    success_url = reverse_lazy('dashboard')


class CanvasOrderView(CreateView):
    model = CustomerOrder
    # form_class = CanvasOrderForm
    template_name = 'orders/canvas_order_form.html'
    success_url = reverse_lazy('dashboard')


class MyOrdersView(ListView):
    model = CustomerOrder
    template_name = 'orders/my_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return CustomerOrder.objects.filter(user=self.request.user)



