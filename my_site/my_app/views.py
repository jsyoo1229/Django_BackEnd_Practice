from django.shortcuts import render

def example_view(request):
    return render(request, 'my_app/example.html')
