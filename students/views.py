from django.http import JsonResponse
from django.db.models import Count, Sum, Avg, Max, Min

from .models import Student


def student_aggregation(request):

    result = Student.objects.aggregate(
        total_students=Count("id"),
        total_earnings=Sum("fees_paid"),
        average_fees=Avg("fees_paid"),
        maximum_fees=Max("fees_paid"),
        minimum_fees=Min("fees_paid"),
    )

    completed_students = Student.objects.filter(
        marks__gte=40
    ).count()

    cancelled_students = Student.objects.filter(
        marks__lt=40
    ).count()

    data = {
        "total_rides": result["total_students"],
        "completed_rides": completed_students,
        "cancelled_rides": cancelled_students,
        "total_earnings": result["total_earnings"] or 0,
        "average_fare": result["average_fees"] or 0,
        "maximum_fare": result["maximum_fees"] or 0,
        "minimum_fare": result["minimum_fees"] or 0,
    }

    return JsonResponse(data)

from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum, Avg, Max, Min

from .models import Ride


def ride_list(request):

    rides = Ride.objects.all()

    # -------------------------
    # FILTERING
    # -------------------------
    status = request.GET.get("status")

    if status:
        rides = rides.filter(status=status)

    # -------------------------
    # SEARCHING
    # -------------------------
    search = request.GET.get("search")

    if search:
        rides = rides.filter(
            Q(ride_id__icontains=search)
            | Q(driver__icontains=search)
        )

    # -------------------------
    # SORTING
    # -------------------------
    sort = request.GET.get("sort", "-created_at")

    allowed_sorting = [
        "ride_id",
        "-ride_id",
        "driver",
        "-driver",
        "status",
        "-status",
        "fare",
        "-fare",
        "created_at",
        "-created_at",
    ]

    if sort in allowed_sorting:
        rides = rides.order_by(sort)
    else:
        rides = rides.order_by("-created_at")

    # -------------------------
    # PAGINATION
    # -------------------------
    page_number = request.GET.get("page", 1)

    paginator = Paginator(rides, 20)

    page_obj = paginator.get_page(page_number)

    data = []

    for ride in page_obj:
        data.append({
            "ride_id": ride.ride_id,
            "driver": ride.driver,
            "status": ride.status,
            "fare": float(ride.fare),
            "created_at": ride.created_at,
        })

    return JsonResponse({
        "page": page_obj.number,
        "total_pages": paginator.num_pages,
        "total_records": paginator.count,
        "results": data,
    })


def ride_aggregation(request):

    total_rides = Ride.objects.count()

    completed_rides = Ride.objects.filter(
        status="completed"
    ).count()

    cancelled_rides = Ride.objects.filter(
        status="cancelled"
    ).count()

    active_rides = Ride.objects.filter(
        status="active"
    ).count()

    statistics = Ride.objects.aggregate(
        total_earnings=Sum("fare"),
        average_fare=Avg("fare"),
        maximum_fare=Max("fare"),
        minimum_fare=Min("fare"),
    )

    return JsonResponse({
        "total_rides": total_rides,
        "completed_rides": completed_rides,
        "cancelled_rides": cancelled_rides,
        "active_rides": active_rides,
        "total_earnings": statistics["total_earnings"],
        "average_fare": statistics["average_fare"],
        "maximum_fare": statistics["maximum_fare"],
        "minimum_fare": statistics["minimum_fare"],
    })