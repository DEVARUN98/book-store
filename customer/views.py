from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from bookstoreapp.models import Book,Cart,Orders
from django.views.generic import TemplateView,ListView
from django.contrib import messages
from bookstoreapp.decorators import signin_required
from django.utils.decorators import method_decorator
from django.db.models import Sum

@method_decorator(signin_required,name="dispatch")
class CustomerHome(TemplateView):
    def get(self,request,*args,**kwargs):
        books = Book.objects.all()
        context = {"books": books}
        return render(request, "c_home.html", context)


# def customer_home(request):        #customer nte home page ilekk books il ulla ellaa datasum kondvaraan
#     books=Book.objects.all()
#     context={"books":books}
#     return render(request,"c_home.html",context)

class SignUpView(TemplateView):
    def get(self,request,*args,**kwargs):
        form = forms.UserRegistrationForm()
        context = {"form": form}
        return render(request, "userregistration.html", context)

    def post(self,request):
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User has been created")
        return redirect("signin")

# def sign_up(request):
#     form=forms.UserRegistrationForm()
#     context={"form":form}
#     if request.method=="POST":
#         form=forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("User has been created")
#             return redirect("signin")
#     return render(request,"userregistration.html",context)

class SignInView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("customer")
            else:
                return render(request, "login.html", {"form":form})

# def sign_in(request):
#     form=forms.LoginForm()
#     if request.method=="POST":
#         context={"form":form}
#         form=forms.LoginForm(request.POST)
#         if form.is_valid():
    #         username=form.cleaned_data["username"]
    #         password=form.cleaned_data["password"]
    #                  #authenticate use cheyyunnath avde same name il oru user indo illeyo ennariyaan
    #         user=authenticate(request,username=username,password=password)    #ullil ulla values pass cheyyaan
    #         if user:
    #             login(request,user)    #user nte session start aaayi
    #             return redirect("customer")
    #         else:
    #             return render(request,"login.html",context)
    #
    #
    # return render(request,"login.html",{"form":form})

def sign_out(request):
    logout(request)
    return redirect("signin")

@method_decorator(signin_required,name="dispatch")
class AddToCart(TemplateView):
    model=Cart
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=Book.objects.get(id=id)
        cart=Cart.objects.create(item=book,user=request.user)
        cart.save()
        print("Item added to cart")
        return redirect("customer")

@method_decorator(signin_required,name="dispatch")
class ViewMyCart(ListView):
    model=Cart
    template_name = "mycartitem.html"
    context = {}
    def get(self, request, *args, **kwargs):
        items=self.model.objects.filter(user=request.user,status="incart")
        self.context["items"]=items
        total=Cart.objects.filter(user=request.user,status="incart").aggregate(Sum("item__price"))
        self.context["total"]=total['item__price__sum']
        print(total)
        return render(request,self.template_name,self.context)

@method_decorator(signin_required,name="dispatch")
class RemoveCartItem(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        cart=self.model.objects.get(id=id)
        cart.status="cancelled"
        cart.save()
        print("removed")
        messages.success(request,"Item has been removed from cart")
        return redirect("customer")

@method_decorator(signin_required,name="dispatch")
class OrderCreate(TemplateView):
    model=Orders
    form_class=forms.OrderForm   #just oru name
    template_name = "ordercreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        cart_id=kwargs["id"]
        cart_item=Cart.objects.get(id=cart_id)
        form=self.form_class(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            user=request.user.username     #user charfield aaayathond username venam
            item=cart_item.item
            order=self.model.objects.create(
                item=item,
                user=user,
                addres=address
            )
            order.save()
            cart_item.status="orderplaced"
            cart_item.save()
            messages.success((request,"Your order has been placed"))
            return redirect("customer")

@method_decorator(signin_required,name="dispatch")
class ViewMyOrder(ListView):
    model=Orders
    template_name = "myorders.html"
    #ivde vare ulla code use cheythaal ellaa users order cheytha orders um kaanikkum
    #default  context_object_name   object_list aaan.

    context_object_name = "orders"
    # queryset=Orders.objects.all()       default django listview queryset .aaa behaviour change cheyyaan aan get_queryset ne override cheythu
    def get_queryset(self):
        queryset=super().get_queryset()    #get_queryset enna model ne override cheythu
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset







