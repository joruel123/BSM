from django.shortcuts import render, HttpResponse, redirect
from .models import Province, City, Barangay, Survey
from .forms import SurveyForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def survey(request):
    form = SurveyForm()

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('survey')

    return render(request,'user/surveyform.html', {
        'form': form,
    })

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