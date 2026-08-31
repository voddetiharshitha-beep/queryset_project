from django.db.models import Q, F, Avg, Max, Min, Sum
from students.models import Student


# --------------------------------------------------
# 1. filter() is used to retrieve records that match certain conditions.
# --------------------------------------------------

print("\n1. FILTER")

students = Student.objects.filter(course="Django")

for student in students:
    print(student.name)


# --------------------------------------------------
# 2. exclude()return everything except the records that match certain conditions.
# --------------------------------------------------

print("\n2. EXCLUDE")

students = Student.objects.exclude(course="Django")

for student in students:
    print(student.name)


# --------------------------------------------------
# 3. Q() is used to create complex queries with OR conditions.
# --------------------------------------------------

print("\n3. Q")

students = Student.objects.filter(
    Q(course="Django") | Q(course="Python")
)

for student in students:
    print(student.name, student.course)


# --------------------------------------------------
# 4. F() is used to reference the value of a model field in a query.
#    It allows you to compare the values of two fields in the same model.
# --------------------------------------------------

print("\n4. F")

students = Student.objects.filter(
    fees_paid=F("fees_total")
)

for student in students:
    print(student.name, "Fees fully paid")


# --------------------------------------------------
# 5. annotate() is used to add additional data to each object in a queryset based on an aggregate function.
#    It allows you to calculate values based on the fields of the model and include them in
# --------------------------------------------------

print("\n5. ANNOTATE")

students = Student.objects.annotate(
    remaining_fees=F("fees_total") - F("fees_paid")
)

for student in students:
    print(
        student.name,
        "Remaining fees:",
        student.remaining_fees
    )


# --------------------------------------------------
# 6. aggregate() is used to perform calculations on a queryset and return a single value.
#    It allows you to calculate values based on the fields of the model and return a single
# --------------------------------------------------

print("\n6. AGGREGATE")

result = Student.objects.aggregate(
    average_marks=Avg("marks"),
    highest_marks=Max("marks"),
    lowest_marks=Min("marks"),
    total_marks=Sum("marks"),
)

print(result)


# --------------------------------------------------
# 7. values() is used to return a queryset of dictionaries instead of model instances.
#    Each dictionary contains the specified fields and their values for each object in the queryset.
# --------------------------------------------------

print("\n7. VALUES")

students = Student.objects.values(
    "name",
    "course",
    "marks"
)

for student in students:
    print(student)


# --------------------------------------------------
# 8. values_list() is similar to values(), but it returns a queryset of tuples instead of dictionaries.
#    Each tuple contains the specified fields and their values for each object in the queryset.
# --------------------------------------------------

print("\n8. VALUES_LIST")

students = Student.objects.values_list(
    "name",
    "marks"
)

for student in students:
    print(student)


# --------------------------------------------------
# 9. exists() is used to check if a queryset contains any records.
#    It returns True if the queryset contains at least one record, and False otherwise.
# --------------------------------------------------

print("\n9. EXISTS")

student_exists = Student.objects.filter(
    name="Harsha"
).exists()

print("Harsha exists:", student_exists)


# --------------------------------------------------
# 10. distinct()
# --------------------------------------------------

print("\n10. DISTINCT")

cities = Student.objects.values_list(
    "city",
    flat=True
).distinct()

for city in cities:
    print(city)