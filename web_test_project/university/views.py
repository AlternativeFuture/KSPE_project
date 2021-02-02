from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import University
from .forms import UniversityForm


@login_required
def all_universities(request):
    university = University.objects.all()
    return render(request, "all_universities.html",
                  {"university": university})


@login_required
def get_universities_data(request, id):
    university = University.objects.get(id=id)
    return render(request, 'university_data.html', {'university': university})


@login_required
def create_university(request):
    if request.method == "POST":
        form = UniversityForm(request.POST)
        if form.is_valid():
            # if len(form.cleaned_data["subject"].split()) < 2:
            #     return HttpResponse("You must provide min 2 subject")
            print(form.cleaned_data["subject"])
            car_obj = form.save()
            car_obj.save()
            return HttpResponseRedirect('/')
    else:
        form = UniversityForm()
    return render(request, "create_university.html", {"form": form})


@login_required
def del_university(request, id):
    university = University.objects.get(id=id)
    university.delete()
    return HttpResponseRedirect('/')

