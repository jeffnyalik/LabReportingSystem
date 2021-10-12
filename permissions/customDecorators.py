from functools import wraps
from rest_framework.response import Response

# def staff_only(function):
#     @wraps(function)

#     def wrap(request,  *args, **kwargs):
#         if request.user.is_authenticated and request.user_type.is_fac_staff:
#             return function(request, *args, **kwargs)
#         else:
#             return Response({'error': 'error'})
    
#     return wrap