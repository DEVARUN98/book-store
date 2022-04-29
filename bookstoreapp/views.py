from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from bookstoreapp.forms import BookForm,OrderUpdateForm
from bookstoreapp.models import Book,Orders
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,TemplateView
from .filters import BookFilter

def home(request):
    return render(request,"home.html")

class BookCreateView(CreateView):
    model = Book
    form_class=BookForm
    template_name = "book_add.html"
    success_url = reverse_lazy("listbook")


# def add_book(request):   #parameter "request"  aaan
#     if request.method=="GET":
#         form=BookForm(initial={"price":0,"copies":0}) #initial kodukkunnath default value set cheyyaan vendi aan
#                 # top il import cheythath form aanenkil form.bookform()
#         context={}
#         context["form"]=form    #context dictionary aaayathond square bracket
#         return render(request,"book_add.html",context)
#
#     if request.method=="POST":
#         form=BookForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             # b_name=form.cleaned_data["book_name"]
#             # author=form.cleaned_data["author"]
#             # price=form.cleaned_data["price"]
#             # copies=form.cleaned_data["copies"]
#             # books=Book.objects.create(book_name=b_name,author=author,price=price,copies=copies)    #models il ulla same name kodukkanam
#             # books.save()
#             print("book saved")
#            # print(b_name,authr,price,copies)
#             return redirect("bookadd")   #return redirect("urlpatterns il kodutha name").same view ilekk thanne varum then GET work cheyyum
#         else:
#             return render(request,"book_add.html",{'form':form})


class BookList(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"


# def list_book(request):
#     books=Book.objects.all()
#     context={}
#     context["books"]=books
#     return render(request,"book_list.html",context)

class BookRemove(DeleteView):
    model = Book
    template_name = "removebook.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listbook")

# def remove_book(request,id):
#     books=Book.objects.get(id=id)
#     books.delete()
#     return redirect("listbook")

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book_edit.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listbook")

# def update_book(request,id):
#     books=Book.objects.get(id=id)
#     if request.method=="GET":
#         form=BookForm(instance=books)
#         # form=BookForm(initial={
#         #     "book_name":books.book_name,     #form ile same name
#         #     "author":books.author,
#         #     "copies":books.copies,
#         #     "price":books.price
#         # })
#         context={}
#         context["form"]=form
#         return render(request,"book_edit.html",context)
#
#     if request.method=="POST":
#         form=BookForm(request.POST,instance=books)
#         if form.is_valid():
#             form.save()
#             # books.book_name=form.cleaned_data["book_name"]
#             # books.author=form.cleaned_data["author"]
#             # books.price=form.cleaned_data["price"]
#             # books.copies=form.cleaned_data["copies"]
#             books.save()
#             return redirect("listbook")

class BookDetail(DetailView):
    model = Book
    template_name = "book_details.html"
    context_object_name = "books"
    pk_url_kwarg='id'

# def book_details(request,id):
#     books=Book.objects.get(id=id)
#     context={}
#     context["books"]=books
#     return render(request,"book_details.html",context)

class CustomerOrders(ListView):
    model = Orders
    template_name = "customer_orders.html"
    context_object_name = "orders"
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        neworders=Orders.objects.filter(status="orderplaced")
        context["neworders"]=neworders
        context["neworders_count"]=neworders.count()
        return context

        d_orders=Orders.objects.filter(status="delivered")
        context["d_orders"]=d_orders
        context["d_order_count"]=d_orders.count()
        return context

class OrderUpdateView(UpdateView):
    model = Orders
    template_name = "orderchange.html"
    pk_url_kwarg = 'id'
    form_class = OrderUpdateForm
    success_url = reverse_lazy("customerorders")


class BookSearchView(TemplateView):
    template_name="books.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        f=BookFilter(self.request.GET,queryset=Book.objects.all())
        context["filter"]=f
        return context









# Create your views here.
