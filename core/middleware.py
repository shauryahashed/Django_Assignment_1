import datetime
from django.utils.deprecation import MiddlewareMixin

class TrackUserActivityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            session_data = request.session.get('user_activity', {'count': 0, 'last_visit': datetime.datetime.now()})
            session_data['count'] += 1
            session_data['last_visit'] = datetime.datetime.now()
            request.session['user_activity'] = session_data

    def process_response(self, request, response):
        return response