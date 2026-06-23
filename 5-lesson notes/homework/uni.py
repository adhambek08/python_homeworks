universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return students, tuitions

def mean(lst):
    return sum(lst) / len(lst)

def median(lst):
    sorted_lst = sorted(lst)
    mid = len(sorted_lst) // 2
    if len(sorted_lst) % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

students, tuitions = enrollment_stats(universities)

print("*" * 31)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuitions):,}")
print()
print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,}")
print()
print(f"Tuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {median(tuitions):,}")
print("*" * 31)