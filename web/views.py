from django.shortcuts import render


# 404 page not found
def page_not_found(request,exception):
    return render(request, 'error/404.html')

# 500 server_error
def server_error(request):
    return render(request, 'error/500.html')

# 400 bad request
def bad_request(request,exception):
    return render(request, 'error/400.html')