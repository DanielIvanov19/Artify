from django.views.generic import TemplateView
# from orders.models import CustomerOrder

class CustomerDashboardView(TemplateView):
    template_name = 'profiles/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['orders'] = CustomerOrder.objects.filter(user=self.request.user)
        return context

