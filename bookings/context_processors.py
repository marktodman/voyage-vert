from .models import Route


def get_routes(request):

    routes = Route.objects.filter(status=1).order_by('route_name')

    return {'routes': routes}