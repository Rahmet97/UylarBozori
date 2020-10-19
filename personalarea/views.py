from django.shortcuts import render
from uybozor.models import Announcement, Blog, Viloyatlar, Tumanlar, Ann_type, Ann_view, Cond
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.core import serializers
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.models import User


def index(request, username):
    announcement_list = Announcement.objects.filter(username=username).order_by('-is_paid', '-upload_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(announcement_list, 9)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)
    viloyat = Viloyatlar.objects.all()
    tuman = Tumanlar.objects.all()
    json_serializer = serializers.get_serializer("json")()
    tumanlar = json_serializer.serialize(Tumanlar.objects.all(), ensure_ascii=False)
    if request.method == 'POST':
        id = request.POST['delete-id']
        Announcement.objects.filter(id=id).delete()
    return render(request, "Hisob/index.html", {'username':username, 'announcements':announcements, 'viloyatlar':viloyat, 'tumanlar':tuman, 'tumanlar2':tumanlar})


def categories(request, username):
    announcement_list = Announcement.objects.all().order_by('-is_paid', '-upload_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(announcement_list, 12)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)
    
    viloyatlar = Viloyatlar.objects.all()
    json_serializer = serializers.get_serializer("json")()
    tumanlar = json_serializer.serialize(Tumanlar.objects.all(), ensure_ascii=False)
    return render(request, "Hisob/categories.html", {'username':username, 'announcements':announcements, 'viloyatlar':viloyatlar, 'tumanlar':tumanlar})


def main(request, username):
    viloyatlar = Viloyatlar.objects.all()
    json_serializer = serializers.get_serializer("json")()
    tumanlar = json_serializer.serialize(Tumanlar.objects.all(), ensure_ascii=False)
    ann_type = Ann_type.objects.all()
    ann_view = Ann_view.objects.all()
    cond = Cond.objects.all()
    user = User.objects.get(username=username)

    if request.method == 'POST':
        viloyati = request.POST['viloyat_id']
        tumani = request.POST['tuman_id']
        manzili = request.POST['address']
        phone = request.POST['phone']
        xususiyatlari = request.POST['xususiyati']
        batafsil = request.POST['batafsil']
        turi = request.POST['type_id']
        korinishi = request.POST['view_id']
        xolati = request.POST['condition_id']
        img1 = "pics/" + request.POST['img1']
        img2 = "pics/" + request.POST['img2']
        img3 = "pics/" + request.POST['img3']
        img4 = "pics/" + request.POST['img4']
        img5 = "pics/" + request.POST['img5']
        email = request.POST['email']
        narxi = request.POST['price']
        print("viloyat_id = ",viloyati)
        announcement = Announcement(viloyat_id=viloyati, tuman_id=tumani, address=manzili, email=email, remaining_inf=xususiyatlari, phone=phone,
        description=batafsil, announce_type_id=turi, announce_view_id=korinishi, condition_id=xolati, img1=img1, img2=img2, img3=img3, img4=img4, img5=img5, price=narxi, username=username)
        announcement.save()

    return render(request, "Hisob/main.html", {'user':user, 'username':username, 'viloyatlar':viloyatlar, 'tumanlar':tumanlar, 'ann_types':ann_type, 'ann_views':ann_view, 'conds':cond})


def about(request, username):
    viloyatlar = Viloyatlar.objects.all()
    json_serializer = serializers.get_serializer("json")()
    tumanlar = json_serializer.serialize(Tumanlar.objects.all(), ensure_ascii=False)
    
    return render(request, "Hisob/about.html", {'username':username, 'tumanlar':tumanlar, 'viloyatlar':viloyatlar})


def blog(request, username):
    blog_list = Blog.objects.all().order_by('-upload_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 9)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    viloyatlar = Viloyatlar.objects.all()
    json_serializer = serializers.get_serializer("json")()
    tumanlar = json_serializer.serialize(Tumanlar.objects.all(), ensure_ascii=False)
    return render(request, "Hisob/blog.html", {'username':username, 'blogs':blogs, 'viloyatlar':viloyatlar, 'tumanlar':tumanlar})


def contact(request, username):
    viloyatlar = Viloyatlar.objects.all()
    json_serializer = serializers.get_serializer("json")()
    tumanlar = json_serializer.serialize(Tumanlar.objects.all(), ensure_ascii=False)

    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        message = request.POST['message']
        msg = f_name + " " + l_name + '\n' + email + '\n' + message
        send_mail(
            'Yangi habar',
            msg,
            'testingemail286@gmail.com',
            ['uylarbozori@gmail.com'],
            fail_silently=False,
        )
    return render(request, "Hisob/contact.html", {'username':username, 'viloyatlar':viloyatlar, 'tumanlar':tumanlar})


def single_list(request, username, id):
    announcement = Announcement.objects.filter(id=id)
    announcements2 = Announcement.objects.all().order_by('-is_paid', '-upload_date')[:4]
    viloyatlar = Viloyatlar.objects.all()
    json_serializer = serializers.get_serializer("json")()
    tumanlar = json_serializer.serialize(Tumanlar.objects.all(), ensure_ascii=False)

    user = User.objects.get(username=username)

    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        message = request.POST['question']
        msg = f_name + " " + l_name + '\n' + message
        send_mail(
            'Yangi habar',
            msg,
            'testingemail286@gmail.com',
            [email],
            fail_silently=False,
        )

    return render(request, "Hisob/single-list.html", {'user':user, 'username':username, 'announcements':announcement, 'announcements2':announcements2, 'viloyatlar':viloyatlar, 'tumanlar':tumanlar})


def search(request, username):
    if request.method == 'GET':
        viloyat_id = request.GET.get('viloyat_id')
        tuman_id = request.GET.get('tuman_id')
        keyValue = request.GET.get('keyvalue')
        query = Q(address__icontains=keyValue) | Q(remaining_inf__icontains=keyValue) | Q(viloyat_id=viloyat_id) | Q(tuman_id=tuman_id) # | Q(announce_type__icontains=keyValue) | Q(announce_view__icontains=keyValue) | Q(condition__icontains=keyValue)
        result_list = Announcement.objects.filter(query).order_by('-is_paid', '-upload_date')
        page = request.GET.get('page', 1)
        paginator = Paginator(result_list, 9)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)
        return render(request, "Hisob/search.html", {'results':results, 'username':username})
    else:
        return render(request, "Hisob/search.html", {'username':username})