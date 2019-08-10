from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from . import permissions
from . import xsendfile


class PremiumUser(APIView):
    permission_classes = (IsAuthenticated, permissions.IsGroupUser,)
    group_name = 'Premium'

    def get(self, request):
        response = xsendfile.base_xsendfile(request)
        return response


class FreeUser(APIView):
    permission_classes = (IsAuthenticated, permissions.IsGroupUser)
    group_name = 'Free'

    def get(self, request):
        response = xsendfile.base_xsendfile(request)
        return response
