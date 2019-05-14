from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ims.model_delete import m_account
from django.views.decorators.csrf import  csrf_exempt
from django import forms
from ims.models import *
import json
# Create your views here.

m = m_account()
class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    
def index(request):
    hell0 = request.GET.get("hell0",default=None)
    context = {}
    context["hello"] = hell0
    # request.session['a']='a'
    return render(request, 'hello.html', context)

@csrf_exempt
def login_delete(request):
    """
    GET request return login page
    POST request return 
    """
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        data = UserForm(request.POST)
        if data.is_valid():
            username = data.cleaned_data['username']
            password = data.cleaned_data['password']
            if m.login(username,password):
                word = "success!"
            else:
                word = "faild!"

            context = {}
            context["hello"] = "hello world!\n{0}\nusername: {1}\n password: {2}".format(word, username, password)
            return render(request, 'hello.html', context)
        else:
            return HttpResponse("error: username:None or password:None!")

def check(request):
    pass

@csrf_exempt
def ims_delete(request):
    print(request.session.get('username',default=None),"session")
    if request.session.get('username',default=None) == None:
        if request.method == 'GET':
            return render(request, 'login.html')
        if request.method == 'POST':
            data = UserForm(request.POST)
            if data.is_valid():
                username = data.cleaned_data['username']
                password = data.cleaned_data['password']
                if m.login(username,password):
                    request.session['username'] = username
                    word = "success!"
                else:
                    word = "faild!"

                context = {}
                context["hello"] = "hello world!\n{0}\nusername: {1}\n password: {2}".format(word, request.session.get("username"), password)
                return render(request, 'hello.html', context)
            else:
                return HttpResponse("error: username:None or password:None!")

    else:
        return HttpResponse("""
            <h1>IMS Index Page!!!</h1>
            <br>
            <h2>hello {username} !</h2>
            <a href="../logout">logout</a>
            """.format(username=request.session.get('username')))

@csrf_exempt
def ims(request):
    print("GET IMS")
    if request.session.get("username", default=None) == None:
        #Not logged in
        print("RUN login")
        return login(request)
    else:
        #logged in
        print("RUN ims_app")
        return ims_app(request)
        

# @csrf_exempt
def login(request):
    if request.method == "POST":
        #POST Request
        data = UserForm(request.POST)
        if data.is_valid():
            #Get value is not empty
            username = data.cleaned_data['username']
            password = data.cleaned_data['password']
            if m.login(username, password):
                #login success
                request.session['username'] = username
                return HttpResponseRedirect("../ims/")
        context = {}
        context["value"] = "false"
        return render(request, 'login.html', context)
    else:
        #GET Request
        return render(request, 'login.html')

def test_ims_app(request):
    return HttpResponse("""
            <h1>IMS Index Page!!!</h1>
            <br>
            <h2>hello {username} !</h2>
            <a href="../logout">logout</a>
            """.format(username=request.session.get('username')))

def logout(request):
    if request.session.get("username", default=None) != None:
        del request.session['username']
    print("logout!")
    return HttpResponseRedirect("../ims/")

def img(request):
    im1 = open("./static/img/background.jpg", 'rb').read()
    im2 = open("./static/img/background.png", 'rb').read()
    im_error = open("./static/img/robot.png", 'rb').read()
    if request.GET["no"] == "1":
        return HttpResponse(im1, content_type='img/jpg')
    elif request.GET.get("no") == "2":
        return HttpResponse(im2, content_type='img/png')
    return HttpResponse(im_error, content_type='img/png')
    
def ims_app(request):
    return render(request, 'ims_app.html')

def api(request):
    success = json.dumps({"value":"true"})
    faild = json.dumps({"value":"false"})

    try:
        method = request.GET.get("method")
        values = json.loads(request.GET.get("values"))
        m_tpye = request.GET.get("type")
        # print(method, values, m_tpye)
        if method == "update":
            if m_tpye == "collage":
                if m_collage(values['collage_no'], values['collage_name'], values['dean'], values['tel'], values['address']).update_collage():
                    data = success
                else:
                    data = faild
        elif method == "del":
            if m_tpye == "collage":
                if m_collage(values['collage_no'], values['collage_name'], values['dean'], values['tel'], values['address']).del_collage():
                    data = success
                else:
                    data = faild
        elif method == 'insert':
            pass
        else:
            data = faild
        # data = success
    except:
        data = faild
        


    return HttpResponse(data, content_type='application/json')

def table(request):
    context = {}
    if request.GET.get("table", default=None) == 'collage':
        data = m_collage.req2list(m_collage.list_all())
        context["data"] = json.dumps(data)
        return render(request, 'table_collage.html', context)
        
    if request.GET.get("table", default=None) == 'department':
        data = m_department.req2list(m_department.list_all())
        context["data"] = json.dumps(data)
        return render(request, 'table_department.html', context)

    if request.GET.get("table", default=None) == 'class':
        data = m_class.req2list(m_class.list_all())
        context["data"] = json.dumps(data)
        return render(request, 'table_class.html', context)

    if request.GET.get("table", default=None) == 'tro':
        data = m_tro.req2list(m_tro.list_all())
        context["data"] = json.dumps(data)
        return render(request, 'table_tro.html', context)

    if request.GET.get("table", default=None) == 'student':
        data = m_student.req2list(m_student.list_all())
        context["data"] = json.dumps(data)
        return render(request, 'table_student.html', context)

    if request.GET.get("table", default=None) == 'teacher':
        data = m_teacher.req2list(m_teacher.list_all())
        context["data"] = json.dumps(data)
        return render(request, 'table_teacher.html', context)

    return HttpResponse("<h1>404 ERROR</h1>")

