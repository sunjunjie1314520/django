from django.core.paginator import Paginator
from utils.Response import ErrorResponse, SuccessResponse


def PaginatorData(self, request, queryset, page_size):

    paginator = Paginator(queryset, page_size)
    pag_num = paginator.num_pages

    current_page_num = request.query_params.get('page', 1)
    if int(current_page_num) < 1 or int(current_page_num) > pag_num:
        return ErrorResponse(msg='页码错误')

    current_page = paginator.page(current_page_num)

    serializer = self.serializer_class(instance=current_page, many=True)

    data_list = {
        'total_number': queryset.count(),
        'page_count': pag_num,
        'current_page': int(current_page_num),
        'page_size': page_size,
        'is_next': pag_num != int(current_page_num),
        'is_prev': int(current_page_num) > 1,
        'paging': [row + 1 for row in range(pag_num)],
        'list_data': serializer.data,

    }
    return SuccessResponse(msg='列表获取成功', data=data_list)

