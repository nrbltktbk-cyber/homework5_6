from django.shortcuts import render, get_object_or_404
from books.models import Books
from django.core.paginator import Paginator
from django.db.models import F #модуль для просмотров
from django.views import generic

# поиск
class SearchView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_key'
    model = Books
    
    def get_queryset(self):
        return self.model.objects.filter(name_book__icontains=self.request.GET.get('s'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context
    
# def search_view(request):
#     query = request.GET.get('s', '')
    
#     if query:
#         book = Books.objects.filter(name_book__icontains=query)
#     else:
#         book = Books.objects.none()

#     return render(
#         request,
#         'book_list.html',
#         {'book': book}
#     )


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_key'
    model = Books
    paginate_by = 2
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_key'] = context['page_obj']   
        return context

# def book_list_view(req):
#     if req.method == 'GET':
#         #book - это значение
#         book = Books.objects.all().order_by('-id')
        
#         paginator = Paginator(book, 2)
#         page = req.GET.get('page')
#         page_obj = paginator.get_page(page)
        
#     return render(
#             req,
#             #books_key - это ключ который будет передан на html шаблон для запросв
#             'book_list.html',
#             {
#                 'book_key': page_obj,
#             }
#         )
class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id_key'
    pk_url_kwarg = 'id'
    model = Books

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        request = self.request
        views_book = request.session.get('viewed_book', [])

        if obj.pk not in views_book:
            Books.objects.filter(pk=obj.pk).update(
                views = F("views")+1)
            views_book.append(obj.pk)
            request.session['views_book'] = views_book
            obj.refresh_from_db()
        return obj
    
        
        
  
# def book_detail_view(req, id):
#     if req.method == 'GET':
#         book_id = get_object_or_404(Books, id=id)
#         views_book = req.session.get('viewed_book', [])
        
#         if id not in views_book:
#             #увеличиваем количество просмотров
#             book_id.views = F('views') + 1
#             book_id.save()
#             book_id.refresh_from_db()
            
#             views_book.append(id)
#             req.session['viewed_book'] = views_book
            
#     return render(
#             req,
#             'book_detail.html',
#             {
#                 'book_id_key': book_id,
#             }
#     )