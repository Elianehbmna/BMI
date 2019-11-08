from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Profile,User,Result
from .forms import  UpdateProfile,ResultForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def new(request):
    return render(request,'new.html')

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):
    '''
    Method that fetches a users profile page
    '''
    user=User.objects.get(pk=profile_id)
    title = User.objects.get(pk = profile_id).username
    profile = Profile.objects.filter(user = profile_id)
    results = Result.objects.filter(user = profile_id)
    return render(request,"profile.html",{"profile":profile,"title":title,"results":results})

@login_required(login_url='/accounts/login/')
def updateProfile(request):

    current_user=request.user
    if request.method =='POST':
        if Profile.objects.filter(user_id=current_user).exists():
            form = UpdateProfile(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
        else:
            form=UpdateProfile(request.POST,request.FILES)
        if form.is_valid():
          profile=form.save(commit=False)
          profile.user=current_user
          profile.save()
        return redirect('profile',current_user.id)
    else:

        if Profile.objects.filter(user_id = current_user).exists():
           form=UpdateProfile(instance =Profile.objects.get(user_id=current_user))
        else:
            form=UpdateProfile()

    return render(request,'update.html',{"form":form})



# @login_required(login_url='/accounts/login/')
# def result(request):
#     if request.method == "POST":
#         form = ResultForm(request.POST)
#         if form.is_valid():
#             height = form.cleaned_data["height"]
#             weight = form.cleaned_data["weight"]
#             bmi = (weight /(height*height))
#             return render(request, "result.html", {"form": form, "bmi": bmi})
#     else:
#         form = ResultForm()
#     return render(request, "result.html", {"form": form})
            # rating = form.save(commit=False)
            # rating.project= project
            # rating.profiles = profile
            # rating.overall_score = (rating.design+rating.usability+rating.content)/2
            # rating.save()
@login_required(login_url='/accounts/login/')
def result(request):
    results = Result.objects.all()
    current_user = request.user
    profile =Profile.objects.get(user = request.user.id)
    if request.method == 'POST':
        form = ResultForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.user_profile = profile
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            if weight <= 0 or weight > 500:
                print ('Weight cannot be less than 0 or greater than 500')
               


            elif height <= 0:
                print ('Height cannot be less than 0')
               
            else:
                post.BMI = round((weight /(height*height)))
                if post.BMI <= 18.5:
                    print ('Your weight status is Underweight')
                elif post.BMI >= 18.5 and post.BMI <= 24.9:
                    print ('Your weight status is Normal weight')
                elif post.BMI >= 25 and post.BMI <= 29.9:
                    print ('Your weight status is Overweight')
                elif post.BMI >= 30:
                    print ('Your weight status is Obese')
            post.save()
        return redirect('results')
    else:
        form = ResultForm()
    return render(request, 'bmi.html', {"form": form, "results": results})

