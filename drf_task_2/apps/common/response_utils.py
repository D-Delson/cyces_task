from rest_framework import status
from rest_framework.response import Response
from functools import wraps


def handle_response(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        try:
            response = view_func(*args, **kwargs)
            return handle_success(response)
        except Exception as e:
            return handle_error(e)
    return wrapper

def handle_success(response):
    response_data = {
        'message': 'successful',
        'data': response.data
    }
    return Response(response_data, status=response.status_code)

def handle_error(error):
    error_message = str(error)
    error_data = {
        'message': 'failure',
        'error': error_message
    }
    return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class ResponseUtils:

    @handle_response
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @handle_response
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @handle_response
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @handle_response
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)