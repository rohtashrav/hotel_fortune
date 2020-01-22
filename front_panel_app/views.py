from django.shortcuts import render, HttpResponse
from backend_panel_app.models import UserRole,RoleDetails


def index(request):
    return render(request, "index.html")
def registration(request):
    role_data = UserRole.objects.all()
    if request.method == "POST":
        detail_form = RoleDetailsForm(request.POST)
        if detail_form.is_valid():
            form = detail_form.save(commit=False)
            form.role_id_id = request.POST['role']
            form.name = request.POST['name']
            form.mobile = request.POST['mobile']
            form.email = request.POST['email']
            form.password = make_password(request.POST['password'])
            form.address = request.POST['address']
            form.gender = request.POST['gender']
            token = make_password(token_generate())
            link = "127.0.0.1:8000/verify/?token={}".format(token)
            form.verify_link = token
            form.save()
            #  try:
            #      verify_link_mail(request.POST['name'], request.POST['email'], link)
            #  except:
            #     return HttpResponse("<h1>Mail not send</h1>")
            return HttpResponse("<h1>Data Save Successfully")
        else:
            return HttpResponse("<h1>Form not valid")
    return render(request, "registration.html", {'role_data': role_data})
def backend_index(request):
    return render(request, "backend_index.html")