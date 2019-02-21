from django.shortcuts import render


# Create your views here.
def posts_list(request):
    n = ["Ulug'bek", "Aziz", "Asil"]
    return render(request, 'blog/index.html', context={'names': n})