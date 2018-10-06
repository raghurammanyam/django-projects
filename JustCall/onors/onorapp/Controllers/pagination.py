from rest_framework import pagination
class StandardResultsSetPagination(pagination.PageNumberPagination):
    #n = request.META.get('HTTP_PAGES')
    #page_size =
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 1000
