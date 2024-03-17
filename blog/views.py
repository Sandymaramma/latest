from django.shortcuts import render

posts = [
  {
    'author': 'Sandy',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'March 17, 2024'
  },
  {
    'author': 'Mary',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'March 18, 2024'
  }
]


def home(request):
    context = {
      'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
