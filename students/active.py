from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ride
from .serializers import RideSerializer


@api_view(['GET'])
def active_rides(request):

    rides = Ride.objects.filter(
        status__iexact='active'
    ).order_by('-created_at')

    date = request.GET.get('date')

    if date:
        rides = rides.filter(created_at__date=date)

    status = request.GET.get('status')

    if status:
        rides = rides.filter(status__iexact=status)

    driver = request.GET.get('driver')

    if driver:
        rides = rides.filter(driver__icontains=driver)

    min_fare = request.GET.get('min_fare')

    if min_fare:
        rides = rides.filter(fare__gte=min_fare)

    max_fare = request.GET.get('max_fare')

    if max_fare:
        rides = rides.filter(fare__lte=max_fare)

    serializer = RideSerializer(rides, many=True)

    return Response({
        'count': rides.count(),
        'results': serializer.data
    })