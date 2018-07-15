from expects.matchers import Matcher

class _have_http_status_ok:

    def _match(self, request):
        return request.status_code == 200, []

have_http_status_ok = _have_http_status_ok()

__all__ = ['have_http_status_ok']
