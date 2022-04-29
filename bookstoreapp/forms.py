from django import forms
from django.forms import ModelForm
from bookstoreapp.models import Book,Orders

# class BookForm(forms.Form):
#     book_name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
#     author=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
#     copies=forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()   #base formile clean method call cheyyan aaan super().clean()
#         price=cleaned_data["price"]
#         copies=cleaned_data["copies"]
#
#         if price < 0:
#             msg="invalid price"
#             self.add_error("price",msg)
#
#         if copies < 0:
#             msg="invalid copies"
#             self.add_error("copies",msg)


class BookForm(ModelForm):
    class Meta:
        model=Book
        fields=["book_name","author","price","copies","image"]        #or ["__all__"]
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "copies":forms.NumberInput(attrs={"class":"form-control"})
        }

class OrderUpdateForm(ModelForm):
    class Meta:
        model=Orders
        fields=["status","expected_delivery_date"]
        widgets={
            "status":forms.Select(attrs={"class":"form-select"}),
            "expected_delivery_date":forms.DateInput(attrs={"type":"date"})}

