from django.urls import path
from bookstoreapp import views


urlpatterns=[
    path("home",views.home,name="home"),
    path("addbook/",views.BookCreateView.as_view(),name="bookadd"),
    path("list/",views.BookList.as_view(),name="listbook"),
    path("delete/<int:id>",views.BookRemove.as_view(),name="remove"),
    path("change/<int:id>",views.BookUpdate.as_view(),name="editbook"),
    path("view/<int:id>",views.BookDetail.as_view(),name="viewbook"),
    path("customerorders",views.CustomerOrders.as_view(),name="customerorders"),
    path("orders/change/<int:id>",views.OrderUpdateView.as_view(),name="orderchange"),
    path("find",views.BookSearchView.as_view(),name="findbook")

]



#python manage.py createsuperuser               oru admin ne create cheyyan