students = {
    1001: {
        "name": "Alice Johnson",
        "cgpa": 3.8,
        "department": "Computer Science",
        "gender": "F",
    },
    1002: {
        "name": "Bob Smith",
        "cgpa": 3.5,
        "department": "Electrical Engineering",
        "gender": "M",
    },
    1003: {
        "name": "Charlie Brown",
        "cgpa": 3.9,
        "department": "Mathematics",
        "gender": "M",
    },
    1004: {"name": "Diana Prince", "cgpa": 3.7, "department": "Physics", "gender": "F"},
    1005: {
        "name": "Evan Wright",
        "cgpa": 3.6,
        "department": "Chemistry",
        "gender": "M",
    },
    1006: {
        "name": "Fiona Gallagher",
        "cgpa": 3.85,
        "department": "Biology",
        "gender": "F",
    },
    1007: {
        "name": "George Harris",
        "cgpa": 3.4,
        "department": "Mechanical Engineering",
        "gender": "M",
    },
    1008: {
        "name": "Hannah Lee",
        "cgpa": 3.95,
        "department": "Economics",
        "gender": "F",
    },
    1009: {
        "name": "Ian Murphy",
        "cgpa": 3.75,
        "department": "Psychology",
        "gender": "M",
    },
    1010: {
        "name": "Julia Kim",
        "cgpa": 3.88,
        "department": "Business Administration",
        "gender": "F",
    },
}

print("-" * 71)

print(f"{'ID':<8} {'Name':<25} {'CGPA':<8} {'Department':<25} {'Gender'} |")
print("-" * 71)

# Print student data
for student_id, details in students.items():
    print(
        f"{student_id :<6} | {details['name']:<20} | {details['cgpa']:<5} | {details['department']:<25} | {details['gender']} |"
    )
print("-" * 71)
