from django.shortcuts import render
from .models import Announcement, Blog, Tumanlar, Viloyatlar, Ann_type, Ann_view, Cond
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.core import serializers
from django.db.models import Q, Count
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    announcements1 = Announcement.objects.all().order_by('-is_paid', '-upload_date')[:4]
    announcements2 = Announcement.objects.all().order_by('-is_paid', '-upload_date')[:6]
    
    json_serializer = serializers.get_serializer("json")()
    tumanlar = json_serializer.serialize(Tumanlar.objects.all(), ensure_ascii=False)
    viloyat = Viloyatlar.objects.all()
    tuman = Tumanlar.objects.all()
    
    announcement_type = Ann_type.objects.all()
    announcement_view = Ann_view.objects.all()
    condition = Cond.objects.all()

    return render(request, "index.html", {
        'announcements1':announcements1,
        'announcements2':announcements2,
        'viloyatlar':viloyat,
        'tumanlar':tuman,
        'tumanlar2':tumanlar,
        'ann_types':announcement_type,
        'ann_views':announcement_view,
        'conds':condition
    })


def about(request):
    viloyatlar = Viloyatlar.objects.all()
    json_serializer = serializers.get_serializer("json")()
    tumanlar = json_serializer.serialize(Tumanlar.objects.all(), ensure_ascii=False)
    return render(request, "about.html",{'viloyatlar':viloyatlar, 'tumanlar':tumanlar})


def categories(request):
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
    return render(request, "categories.html", {'announcements':announcements, 'viloyatlar':viloyatlar, 'tumanlar':tumanlar})


def contact(request):
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
    return render(request, "contact.html", {'viloyatlar':viloyatlar, 'tumanlar':tumanlar})


def blog(request):
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
    return render(request, "blog.html", {'blogs':blogs, 'viloyatlar':viloyatlar, 'tumanlar':tumanlar})


def search(request):
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
        return render(request, "search.html", {'results':results})
    else:
        return render(request, "search.html")