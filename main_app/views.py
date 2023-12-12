from django.shortcuts import render

cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Bug', 'breed': 'piebald', 'description': 'pants', 'age': 2},
  {'name': 'Pooka', 'breed': 'black', 'description': '5 dolar', 'age': 9},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  return render(request, 'cats/index.html' , {
    'cats': cats,
  })