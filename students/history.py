from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ride
from .serializers import RideSerializer


@api_view(['GET'])
def ride_history(request):

    rides = Ride.objects.all().order_by('-created_at')

    # Date filter
    date = request.GET.get('date')

    if date:
        rides = rides.filter(created_at__date=date)

    # Status filter
    status = request.GET.get('status')

    if status:
        rides = rides.filter(status__iexact=status)

    # Driver filter
    driver = request.GET.get('driver')

    if driver:
        rides = rides.filter(driver__icontains=driver)

    # Minimum fare filter
    min_fare = request.GET.get('min_fare')

    if min_fare:
        rides = rides.filter(fare__gte=min_fare)

    # Maximum fare filter
    max_fare = request.GET.get('max_fare')

    if max_fare:
        rides = rides.filter(fare__lte=max_fare)

    serializer = RideSerializer(rides, many=True)

    return Response({
        'count': rides.count(),
        'results': serializer.data
    })