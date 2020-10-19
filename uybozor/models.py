from django.db import models
from datetime  import date


class Viloyatlar(models.Model):
    viloyat = models.CharField(max_length=30)

    def __str__(self):
        return self.viloyat


class Tumanlar(models.Model):
    name = models.CharField(max_length=25)
    viloyat = models.ForeignKey(Viloyatlar, on_delete =  models.CASCADE)

    def __str__(self):
        return self.name


class Ann_type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ann_view(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Cond(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    viloyat = models.ForeignKey(Viloyatlar, on_delete =  models.CASCADE)
    tuman = models.ForeignKey(Tumanlar, on_delete =  models.CASCADE)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    remaining_inf = models.TextField()
    description = models.TextField()
    announce_type = models.ForeignKey(Ann_type, on_delete = models.CASCADE)
    announce_view = models.ForeignKey(Ann_view, on_delete = models.CASCADE)
    condition = models.ForeignKey(Cond, on_delete = models.CASCADE)
    img1 = models.ImageField(upload_to="pics")
    img2 = models.ImageField(upload_to="pics")
    img3 = models.ImageField(upload_to="pics")
    img4 = models.ImageField(upload_to="pics")
    img5 = models.ImageField(upload_to="pics")
    price = models.IntegerField()
    phone = models.CharField(max_length=20)
    is_paid = models.BooleanField(default=True)
    upload_date = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.address


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    user = models.CharField(max_length=30)
    description = models.TextField()
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title