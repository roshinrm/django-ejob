from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateApplicantForm, ApplicationForm


def applicant_register(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateApplicantForm()
        if request.method == 'POST':
            form = CreateApplicantForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                Applicant.objects.create(user=user, name=username)
                return redirect('applicant-login')

        context = {'form': form}
        return render(request, 'applicant_register.html', context)


def applicant_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        return render(request, 'applicant_login.html')


def applicant_logout(request):
    logout(request)
    return redirect('applicant-login')


def home(request):
    jobs = Jobs.objects.all().order_by('-id')
    totaljobs = jobs.count()
    companies = Companies.objects.all()
    totalcompanies = companies.count()
    applicants = Applicant.objects.all()
    totalapplicants = applicants.count()

    context = {
        'jobs': jobs,
        "totaljobs": totaljobs,
        "totalcompanies": totalcompanies,
        "totalapplicants": totalapplicants
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


@login_required(login_url='applicant-login')
def jobsview(request, pk):
    job = Jobs.objects.get(id=pk)
    applicant = Applicant.objects.get(user=request.user)

    form = ApplicationForm(initial={
        "applicant": applicant,
        "jobs": job
    })
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'job': job,
        'form': form,
    }
    return render(request, 'jobs.html', context)


def companies(request):
    companies = Companies.objects.all()
    context = {"companies": companies}
    return render(request, 'companies.html', context)


@login_required(login_url='applicant-login')
def companiesDetailview(request, pk):
    companies = Companies.objects.get(id=pk)
    jobs = companies.jobs_set.all()
    context = {
        "companies": companies,
        "jobs": jobs
    }
    return render(request, 'companies_detail.html', context)
