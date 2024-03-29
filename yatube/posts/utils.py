from django.core.paginator import Paginator


def paginate_page(request, post_list):
    POSTS_PER_PAGE = 10
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
