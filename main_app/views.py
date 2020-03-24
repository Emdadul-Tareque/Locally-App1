from django.http import HttpRequest
from django.shortcuts import render

from main_app.models import registration, Foods, Parlor, Tutor


def index(request: HttpRequest):
    error = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        again_password = request.POST.get('again_password')

        if not len(phone_number) == 11:
            error['phone'] = "ফোন নাম্বারটি ভুল"
        if len(name) <= 2:
            error['name'] = "নাম অবশ্যই দুই অক্ষরের বেশি হতে হবে"
        if not email:
            error['email'] = "ইমেল ফিল্ডটি পূরণ করুন"
        if len(password) <= 4:
            error['password'] = "পাসওয়ার্ড অব্যশই ৪ অক্ষরের বেশি হতে হবে"
        if password != again_password:
            error['again_password'] = "পাসওয়ার্ড একই হয়নি"

    success = request.method == "POST" and not error
    if success:
        db_id = len(registration.objects.all())
        db_id += 1
        student = registration(db_id,
                               request.POST.get('name'),
                               request.POST.get('email'),
                               request.POST.get('phone'),
                               request.POST.get('password'),
                               request.POST.get('again_password'))

        student.save()

    else:
        student = None

    return render(request, 'index.html', context={'error': error, 'ticket': student})


def sign_in(request):
    error = {}
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = registration.objects.filter(phone=phone)

        if not user:
            error = {'phone': phone}
        if user:
            user_pass = user[0].password
            if password != user_pass:
                error = {'password': password}

            else:

                return render(request, 'Food.html')

    return render(request, 'sign_in.html', context={'error': error})


def user(request):
    return render(request, 'Profile.html')



def home(request):
    return render(request, 'home.html')


def main_home(request):
    return render(request, 'main_home.html')


def food_list(request):
    foods = Foods.objects.all()

    context = {
        'foods': foods
    }
    return render(request, 'food.html', context=context)


def parlor(request):
    parlor = Parlor.objects.all()

    context = {
        'parlor': parlor
    }
    return render(request, 'parlor.html', context=context)


def tutor(request):
    tutor = Tutor.objects.all()

    context = {
        'tutor': tutor
    }
    return render(request, 'Tutor.html', context=context)
