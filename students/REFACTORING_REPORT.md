## Before Refactoring

```python
from django.contrib.auth.models import User
from .models import Ride

def get_ride_details():
    rides = Ride.objects.all()

    for ride in rides:
        driver = User.objects.get(
            username=ride.driver
        )

        print(
            ride.ride_id,
            driver.username,
            ride.status
        )

    total_rides = Ride.objects.count()

    completed_rides = Ride.objects.filter(
        status="completed"
    ).count()

    total_again = Ride.objects.count()

    return {
        "total": total_rides,
        "completed": completed_rides,
        "total_again": total_again,
    }
    
### Step 4 — Save

Press:

```text
Ctrl + S