from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)   #unique kodukkunnath same name il vere varathirikkan
    author=models.CharField(max_length=50)
    price=models.PositiveIntegerField(default=50)
    copies=models.PositiveIntegerField(default=1)
    image=models.ImageField(upload_to="images",null=True)   # images ennulla folderilekk images add cheyyaan

    def __str__(self):
        return self.book_name      #default aaaytt bookname mathrem print cheyyikkan

class Cart(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)  #item ennullath oru book aaan,  Book il ninnaan edkkunnath so (Book)
                            #oru book ne delete cheythaal athinte corresponding entry avde ninn pokaan aan "on_delete=" kodukkunnath
    user=models.ForeignKey(User,on_delete=models.CASCADE)  #cart ilekk add cheytha user nte details kittaan
    options=(("incart","incart"),   #2 values varunnath select input type il options kodukkumbol varunnathil key and value set cheythathaan
             ("cancelled","cancelled"),
             ("orderplaced","orderplaced"))
    status=models.CharField(max_length=30,choices=options,default="incart")

class Orders(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.CharField(max_length=40)
    addres=models.CharField(max_length=120)
    date_order=models.DateField(auto_now_add=True)
    # orderplaced,dispatch,intransit,delivered,order_cancelled
    options=(
        ("orderplaced","orderplaced"),
        ("dispatch","dispatch"),
        ("intransit","intransit"),
        ("delivered","delivered"),
        ("order_cancelled","order_cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="orderplaced")
    expected_delivery_date=models.DateField(null=True,blank=True)


#oro new models create cheyyumbozhm migrate cheyyanm

#ORM QUERIES

# new values add cheyyan

#book=Book(book_name="oozham",author="mt",price=100,copies=10)
#book.save()

 # ella elements um print cheyyan

#books=Book.objects.all()
#books

#book_name and price mathram print cheyyaan

#for book in books
#   print(book.book_name,book.price)


#print all books whiose price under 300
#books=Book.objects.filter(price__lt=300)
#books       print cheyyaan

#print all books whiose price in range of 100 to 300
#books=Book.objects.filter(price__gt=100,price__lt=300)
#books


#books=Book.objects.filter(book_name="randalukal")
#books



#case insensitive matching  (letters upper/lowercase aano enn nokkathe out kittaan)
#books=Book.objects.filter(book_name__iexact="Randalukal")


#for deleting,updating

#fetching  a particular objects
#book=Book.objects.get(book_name="book_name")
#book.delete()

#update ORM queries
#book=Book.objects.get(id=3)
#book.price=350
#book.copies=210
#book.save()



#aavashyamulla data mathram access cheyyaan

#books=Book.objects.all().values('id','book_name')    ivide id and book_name mathram print cheyyulloo