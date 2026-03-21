from django.shortcuts import get_object_or_404, render, redirect
from orders.forms import OrderForm
from orders.models import OrderBook
from django.views import generic

#creat_order

class CreateOrderView(generic.CreateView):
    template_name = 'create_order.html'
    form_class = OrderForm
    success_url = '/order_list/'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)




# def create_order_view(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/order_list')
#     else:
#         form = OrderForm()
#     return render(
#         request,
#         'create_order.html',
#          {'form': form}
#  )
    
#read
class OrderListView(generic.ListView):
    template_name = 'order_list.html'
    model = OrderBook
    context_object_name = 'order'
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    

# def order_list_view(request):
#     if request.method == 'GET':
#         order = OrderBook.objects.all().order_by('-id')
#         return render(
#             request,
#             'order_list.html',
#             {'order': order}
#         )
        



#update order
class UpdateOrderView(generic.UpdateView):
    template_name = 'update_order.html'
    form_class = OrderForm
    model = OrderBook
    success_url = '/order_list/'
    
    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=order_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateOrderView, self).form_valid(form=form)

# def update_order_view(request, id):
#     order_id = get_object_or_404(OrderBook, id=id)
#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/order_list/')
#     else:
#         form = OrderForm(instance=order_id)
    
#     return render(
#         request,
#         'update_order.html',
#         {
#             'form': form,
#             'order_id': order_id
#         }
#     )

#delete есть два способа 
class DeleteOrderView(generic.View):
    def get(self, request, id):
        order_id = get_object_or_404(OrderBook, id=id)
        order_id.delete()
        return redirect('/order_list/')
    
    
# def delete_order_view(request, id):
#     order_id = get_object_or_404(OrderBook, id=id)
#     order_id.delete()
#     return redirect('/order_list/')