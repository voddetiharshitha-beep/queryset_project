from django.http import JsonResponse
from django.db import connection
from .models import Ride


def optimized_rides(request):

    start_queries = len(connection.queries)

    rides = Ride.objects.select_related(
        "driver_user"
    ).all()

    data = []

    for ride in rides:

        driver_name = None

        if ride.driver_user:
            driver_name = ride.driver_user.username

        data.append({
            "ride_id": ride.ride_id,
            "driver": ride.driver,
            "driver_user": driver_name,
            "status": ride.status,
            "fare": float(ride.fare),
        })

    total_queries = len(connection.queries) - start_queries

    return JsonResponse({
        "query_count": total_queries,
        "count": len(data),
        "rides": data,
    })