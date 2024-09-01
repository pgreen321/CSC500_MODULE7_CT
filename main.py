# Create a program that lets the user enter a course number, and then it should display the course's room number,
# instructor, and meeting time.

# Create dictionary with room numbers
room_number = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

# Create dictionary with instructors
instructor = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

# Create dictionary with meeting times
meeting_time = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# The program should let the user enter a course number, and then it should display the course's room number,
# instructor, and meeting time.

course = str(input('Enter a course number: ').upper())

try:
    room = room_number[course]
    name = instructor[course]
    time = meeting_time[course]
    print('Course Number: {}, Room Number: {}, Instructor: {}, Meeting Time: {}'.format(course, room, name, time))
except KeyError:
    print('Course number not found')

