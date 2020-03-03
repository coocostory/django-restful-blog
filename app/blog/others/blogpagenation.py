from rest_framework.pagination import PageNumberPagination


class BlogPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 128
