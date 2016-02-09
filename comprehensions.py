# tiy week 2, day 1 HW - comprehension practice
import csv


with open("dataset.csv") as csvfile:
    file_reader = csv.reader(csvfile)
    rows = [row for row in file_reader]
    headers = rows[0]
    data = rows[1:]


def get_water_temp_by_date(rows):
    return [col[-2:] for col in rows]


def convert_temp_to_float(rows):
    return [float(row[4]) for row in rows]


def convert_temps_to_f(rows):
    temps = convert_temp_to_float(rows)
    return [int(((temp * 1.8) + 32)) for temp in temps]


def date_wave_height(rows):
    return {row[5]: row[1] for row in rows}


print("Water temps by date: ")
print(get_water_temp_by_date(data))

print("Water temps to float: ")
print(convert_temp_to_float(data))

print("Water temps expressed in degrees F: ")
print(convert_temps_to_f(data))

print("Date: Wave Height: ")
print(date_wave_height(data))

sentence = "List Comprehensions are the Greatest!"


def remove_vowels(sentence):
    vowels = 'AEIOUaeiou'
    return ''.join([char if char not in vowels else '' for char in sentence])

print(remove_vowels(sentence))

dictionary = {
            'Gale': {'Homework 1': 88, 'Homework 2': 76},
            'Jordan': {'Homework 1': 92, 'Homework 2': 87},
            'Peyton': {'Homework 1': 84, 'Homework 2': 77},
            'River': {'Homework 1': 85, 'Homework 2': 91}
            }


def avg_homework(students, assignment):
    scores = [students[name][assignment] for name in students.keys()]
    return sum(scores)/len(scores)

print(avg_homework(dictionary, 'Homework 1'))
