from django.shortcuts import render


def page_not_found(request, *args, **argv):
    return render(request, 'core/404.html', {'path': request.path}, status=404)


def csrf_failure(request, *args, **argv):
    return render(request, 'core/403csrf.html')


def page_500(request, *args, **argv):
    return render(request, 'core/500.html', {'path': request.path}, status=500)


def page_403(request, *args, **argv):
    return render(request, 'core/403.html', {'path': request.path}, status=403)
