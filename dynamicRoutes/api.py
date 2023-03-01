from django.http import HttpResponse

def Employee(request):
    return HttpResponse("Welcome to Marolix")

def EmployeeDetails(request,DevId = None):
    if DevId == 1:
        return HttpResponse("Harsha")
    else:
        return HttpResponse("David")

