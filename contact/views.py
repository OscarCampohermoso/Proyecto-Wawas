from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    return render(request, 'contact.html')

def registercontact(request):
    name=request.POST['txtName']
    email=request.POST['txtEmail']
    phone=request.POST['numPhone']
    message=request.POST['txtMessage']

    regcontact=Contact.objects.create(name=name, email=email, phone=phone, message=message)
    #messages.success(request, "¡Cliente registrado!")
    return redirect('/')

"""def revisar(request, ci):
    regcontact=Contact.objects.get(ci=ci)
    return render(request, ".html", {"regcontact": regcontact})"""

"""def contact(request):
    data = {
        'formContact': ContactForm()
    }
    if request.method == 'POST':
        formC = ContactForm(data=request.POST)
        if formC.is_valid():
            formC.save()
            data["message"]="Mensaje guardado"
        else:
            data["formContact"] = formC
    return render(request, 'contact.html', data)"""