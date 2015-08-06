from scholrroles import set_permission

class PermissionsMiddleware(object):
    def process_request(self, request):
        if hasattr(request, 'user') and not hasattr(request.user,'permissions') :
            set_permission(request.user, request)

