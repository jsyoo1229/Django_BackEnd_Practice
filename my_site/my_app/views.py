from django.shortcuts import render


def example_view(request):
    return render(request, "my_app/example.html")


def variable_view(request):
    my_var = {
        "first_name": "rosaLind",
        "last_name": "franKlin",
        "some_list": [1, 2, 3],
        "user_logged_in": True,
    }

    return render(request, "my_app/variable.html", context=my_var)
