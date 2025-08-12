from django.shortcuts import render

def home(request):
    return render(request, 'abode/home.html')

def handler500(req):
    """Custom 500 error page view"""
    return render(req, 'abode/500.html', status=500)

# Custom 404 error handler
def handler404(request, exception):
    return render(request, 'abode/404.html', status=404)