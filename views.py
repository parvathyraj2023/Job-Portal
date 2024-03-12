from django.shortcuts import render,redirect
from backend.models import categorydb,jobdb,blogdb,countrydb
from frontend.models import applicationdb,contactdb,jobpostdb,signindb
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def homepage(request):
    data = categorydb.objects.all()
    return render(request,"home.html",{'data':data})

def categorypage(request):
    cat=categorydb.objects.all()
    return render(request,"Category.html",{'cat':cat})

def joblisting(request,job_name):
    data=jobdb.objects.filter(Category=job_name)
    return render(request,"JobListing.html",{'data':data})

def jobdetails(request,jobid):
    data = jobdb.objects.get(id=jobid)
    return render(request,"JobDetails.html",{'data':data})

def alljobs(request):
    job=jobdb.objects.all()
    return render(request,"Alljobs.html",{'job':job})

def aboutpage(request):
    return render(request,"About.html")

def aboutpagetwo(request):
    return render(request,"About2.html")

def servicepage(request):
    return render(request,"Services.html")

def saveapplication(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ti = request.POST.get('title')
        co = request.POST.get('company')
        we = request.POST.get('website')
        fi = request.POST.get('file')
        cov = request.POST.get('coverletter')
        obj = applicationdb(Name=na,Email=em,Title=ti,Company=co,Website=we,File=fi,Coverletter=cov)
        obj.save()
        return redirect(jobapplicationsubmission)

def contactpage(request):
    return render(request,"Contact.html")

def savecontact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        su = request.POST.get('subject')
        me = request.POST.get('message')
        obj = contactdb(Name=na,Email=em,Subject=su,Message=me)
        obj.save()
        messages.success(request, "Query Submitted")
        return redirect(contactpage)

def jobpostpage(request):
    return render(request,"PostJob.html")
def savepostjob(request):
    if request.method == "POST":
        ti = request.POST.get('title')
        loc = request.POST.get('location')
        ty = request.POST.get('type')
        jde = request.POST.get('jdescription')
        re = request.POST.get('responsibility')
        qa = request.POST.get('qualification')
        sa = request.POST.get('salary')
        na = request.POST.get('name')
        ta = request.POST.get('tagline')
        cde = request.POST.get('cdescription')
        pr = request.POST.get('project')
        we = request.POST.get('website')
        em = request.POST.get('email')
        nu = request.POST.get('number')
        us = request.POST.get('username')
        lo = request.FILES['logo']
        obj = jobpostdb(Title=ti,Location=loc,Type=ty,JDescription=jde,Responsibility=re,Qualification=qa,Salary=sa,
                        Name=na,Tagline=ta,CDescription=cde,Project=pr,Website=we,Email=em,Number=nu,Username=us,Logo=lo)
        obj.save()
        messages.success(request, "Job Posted")
        return redirect(submissionpage)

def signinpage(request):
    return render(request,"SigninPage.html")

def loginpage(request):
    return render(request,"LoginPage.html")

def savesignin(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        us = request.POST.get('username')
        pa = request.POST.get('password')
        cpa = request.POST.get('cpassword')
        obj = signindb(Name=na,Email=em,Username=us,Password=pa,CPassword=cpa)
        obj.save()
        return redirect(signinpage)

def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if signindb.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username']=un
            request.session['Password']=pwd
            messages.success(request, f"Welcome {un}")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid username or password")
            return redirect(loginpage)
    return redirect(loginpage)

def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(userlogin)

def blogpage(request):
    blog = blogdb.objects.all()
    return render(request,"Blog.html",{'blog':blog})

def blogcontent(request,blogid):
    data=blogdb.objects.get(id=blogid)
    return render(request,"BlogContent.html",{'data':data})

def payment(request):
    if request.method=='POST':
        amount=50000
        order_currency='INR'
        client=razorpay.Client(
            auth=('rzp_test_l0gvMNxaGk6jog','EQTnIomRbY2viyDYsalbdnqe'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,"payment.html")

def gpay(request):
    return render(request,"Gpay.html")

@csrf_exempt
def success(request):
    return render(request,"success.html")

def submissionpage(request):
    return render(request,"submission.html")

def jobapplicationsubmission(request):
    return render(request,"JobApplicationSubmission.html")

def locationsearch(request):
    cat = countrydb.objects.all()
    return render(request,"LocationSearch.html",{'cat':cat})

def abc(request):
    cat = categorydb.objects.all()
    return render(request,"abc.html",{'cat':cat})
def searchjoblisting(request,job_name):
    data=jobdb.objects.filter(Country=job_name)
    return render(request,"SearchJobListing.html",{'data':data})