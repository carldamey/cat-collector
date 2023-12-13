from django.shortcuts import render
from .models import Cat

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html' , {
    'cats': cats,
  })

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', {
    'cat': cat
  })


# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
#   {'name': 'Bug', 'breed': 'piebald', 'description': 'pants', 'age': 2},
#   {'name': 'Pooka', 'breed': 'black', 'description': '5 dolar', 'age': 9},
# ]
