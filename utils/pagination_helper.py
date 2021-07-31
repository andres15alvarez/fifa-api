from flask import url_for
from flask import current_app


class PaginationHelper:

    def __init__(self, page_number, query, resource_for_url, key_name, schema):
        self.query = query
        self.resource_for_url = resource_for_url
        self.key_name = key_name
        self.schema = schema
        self.page_number = page_number
        self.page_size = current_app.config['PAGINATION_PAGE_SIZE']
        self.page_argument_name = current_app.config['PAGINATION_PAGE_ARGUMENT_NAME']

    def paginate_query(self):
        paginated_objects = self.query.paginate(
            self.page_number,
            per_page=self.page_size,
            error_out=False
        )
        objects = paginated_objects.items
        if paginated_objects.has_prev:
            previous_page_url = url_for(
                self.resource_for_url, 
                page=self.page_number-1, 
                _external=True
            )
        else:
            previous_page_url = None
        if paginated_objects.has_next:
            next_page_url = url_for(
                self.resource_for_url,
                page=self.page_number+1,
                _external=True
            )
        else:
            next_page_url = None
        dumped_objects = self.schema.dump(objects, many=True)
        return {
            self.key_name: dumped_objects,
            'previous': previous_page_url,
            'next': next_page_url,
            'pages': paginated_objects.pages,
            'count': paginated_objects.total
        }
