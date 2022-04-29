from django.urls import path
from customer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.CustomerHome.as_view(),name="customer"),
    path("accounts/users/add",views.SignUpView.as_view(),name="signup"),
    path("accounts/users/login",views.SignInView.as_view(),name="signin"),
    path("accounts/users/logout",views.sign_out,name="signout"),
    path("addtocart/<int:id>",views.AddToCart.as_view(),name="addtocart"),
    path("books/viewmycart",views.ViewMyCart.as_view(),name="viewmycart"),
    path("carts/item/remove/<int:id>",views.RemoveCartItem.as_view(),name="removeitem"),
    path("books/buynow/<int:id>",views.OrderCreate.as_view(),name="ordercreate"),
    path("books/myorders",views.ViewMyOrder.as_view(),name="myorders"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)