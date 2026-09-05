import random
from decimal import Decimal

from django.contrib.auth.models import User

from .models import Ride


def create_rides(total=5000):

    # Get existing users
    users = list(User.objects.all())

    # Create sample users if none exist
    if not users:
        print("No users found. Creating sample users...")

        for i in range(10):
            user = User.objects.create_user(
                username=f"driver{i + 1}",
                password="test12345"
            )
            users.append(user)

        print("10 sample users created.")

    statuses = [
        "completed",
        "cancelled",
        "active",
    ]

    rides = []

    # Start after existing records
    existing_count = Ride.objects.count()

    for i in range(total):

        driver_user = random.choice(users)

        ride = Ride(
            ride_id=f"RIDE-{existing_count + i + 1}",
            driver=driver_user.username,
            driver_user=driver_user,
            status=random.choice(statuses),
            fare=Decimal(random.randint(100, 2000)),
        )

        rides.append(ride)

    # Insert records efficiently
    Ride.objects.bulk_create(
        rides,
        batch_size=500
    )

    print(f"{total} rides created successfully!")