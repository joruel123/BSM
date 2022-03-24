from django.shortcuts import render, HttpResponse, redirect
from .models import Province, City, Barangay, Survey
from .forms import SurveyForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def survey(request):
    province = Province.objects.all()

    if request.method == 'POST':

        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        contact = request.POST['contact']
        age = request.POST['age']
        precinct = request.POST['precinct']
        role = request.POST['role']
        province = request.POST['province']
        city = request.POST['city']
        barangay = request.POST['barangay']


        get_province = Province.objects.get(id=province)
        get_city = City.objects.get(id=city)
        get_barangay = Barangay.objects.get(id=barangay)

        survey = Survey(
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact=contact,
            age=age,
            precinct=precinct,
            role=role,
            province=get_province,
            city=get_city,
            barangay=get_barangay
        )

        survey.save()


        return redirect('survey')

    return render(request,'user/surveyform.html', {
        'province': province
    })

def city(request):
    province = request.GET.get('province')
    try:
        city = City.objects.filter(province=province)
    except ValueError:
        city = []

    return render(request, 'user/city.html', { 'city': city })

def barangay(request):
    city = request.GET.get('city')
    try:
        barangay = Barangay.objects.filter(city=city)
    except ValueError:
        barangay = []

    return render(request, 'user/barangay.html', { 'barangay': barangay })

def list(request):

    survey = Survey.objects.all()

    province = Province.objects.all()
    city = City.objects.all()
    barangay = Barangay.objects.all()

    return render(request,'administration/list.html', {
        'survey': survey,
        'province': province,
        'city': city,
        'barangay': barangay
    })