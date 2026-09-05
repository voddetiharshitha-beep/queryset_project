from .models import Ride


def show_query_plan():

    print("\n========== STATUS QUERY ==========")

    query = Ride.objects.filter(
        status="completed"
    )

    print(query.explain())

    print("\n========== DRIVER QUERY ==========")

    query = Ride.objects.filter(
        driver="Ravi"
    )

    print(query.explain())

    print("\n========== CREATED_AT QUERY ==========")

    query = Ride.objects.filter(
        created_at__gte="2026-01-01"
    )

    print(query.explain())

    print("\n========== RIDE_ID QUERY ==========")

    query = Ride.objects.filter(
        ride_id="RIDE001"
    )

    print(query.explain())

    print("\n========== DRIVER_USER QUERY ==========")

    query = Ride.objects.filter(
        driver_user__username="Ravi"
    )

    print(query.explain())