from .models import Route


# Get a route information to use in multiple templates
def get_routes(request):

    routes = Route.objects.filter(status=1).order_by('route_name')

    return {'routes': routes}
