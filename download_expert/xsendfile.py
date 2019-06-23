import os.path
from django.utils.encoding import smart_str
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest

serve_root = getattr(settings, 'SERVE_FILES_FROM', "")


def base_xsendfile(request):
    filename = request.GET.get('name', None)
    filetype = request.GET.get('type', None)
    path = os.path.join(serve_root, filename + '.' + filetype)
    if not os.path.exists(smart_str(path)):
        response = HttpResponseBadRequest()
        return response
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="%s"' % path
    response['X-Sendfile'] = path
    return response
