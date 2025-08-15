# test_script.py
"""
Test script for Project 6 classes
"""

from interval import Interval
from scheduling import Event
import matplotlib.pyplot as plt
from scheduling import Schedule
from scheduling import Course


# Test class Interval
i1= Interval(3, 9)  # Instantiate an Interval with endpoints 3 and 9
assert i1.left==3, f"Expected 3 but got {i1.left}"
a2= i1.overlap(Interval(5, 15))  #  Expect Interval with endpoints 5 and 9
assert isinstance(a2, Interval), "Expected a2 to be an Interval instance"
L= a2.left; r= a2.right
assert L==5 and r==9, f"Expected endpoints 5, 9 but got {L}, {r}"
w= a2.get_width()
assert w==4, f"Expected width 4 but got {w}"
print('---- Done testing class Interval')


# Test class Event
e1 = Event(3 , 20 , 10 , .5 , 4);
# An Event with id 4 , importance .5 , and duration 10.
# It 's available for scheduling in the interval [3 ,20].
assert e1.available.right==20, f"Expected 20 but got {e1.available.right}"
assert e1.available.get_width()==17, f"Expected 17 but got {e1.available.get_width}"
e1.set_scheduled_time(5)
assert e1.scheduled_time==5, f"Expected 5 but got {e1.scheduled_time}"
fig, ax = plt.subplots(figsize =(10 , 6)) # Set up figure . ax is the axes .
e1.draw(ax) # Should see white box with left edge at x =3
# and colored box with left edge at x =5
plt.savefig("test_event.png") # Use this if you want to save figure file
plt.show()


# Test class Schedule
# Instantiate more Events and one Schedule
e2 = Event(0, 30, 8, 0.3, 1)
e3 = Event(8, 25, 6, 0.0, 5)
s = Schedule(0, 40, 'Test Schedule')

# Assert initial values
assert s.event_list == [], f"Expected event_list to be empty, but got {s.event_list}"
assert s.window.left == 0, f"Expected window.left to be 0, but got {s.window.left}"
assert s.window.right == 40, f"Expected window.right to be 40, but got {s.window.right}"

# Add events to the schedule
s.add_event(e2)
s.add_event(e3)

# Add duplicates
s.add_event(e2)
assert len(s.event_list) == 3, f"Expected 3 events in event_list, but got {len(s.event_list)}"
assert s.event_list.count(e2) == 2, f"Expected 2 instances of e2 in event_list, but got {s.event_list.count(e2)}"

s.add_event(e3)
assert len(s.event_list) == 4, f"Expected 4 events in event_list, but got {len(s.event_list)}"
assert s.event_list.count(e3) == 2, f"Expected 2 instances of e3 in event_list, but got {s.event_list.count(e3)}"

# Test other methods (schedule_events)
s.schedule_events()
assert e2.scheduled_time is not None, "e2 should be scheduled but it wasn't"
assert e3.scheduled_time is not None, "e3 should be scheduled but it wasn't"

print("All tests passed!")


 

# Test class Course

# Test Course Initialization
c1 = Course(8, 25, 6, 0.5, 6, 'CS1000')
assert c1.course_name == 'CS1000'
assert c1.get_id() == 6
assert c1.available.left == 8
assert c1.available.right == 25

# Test Course draw method
fig, ax = plt.subplots(figsize=(10, 6))
c1.draw(ax)  # Should show the course name in the center of the unfilled box
plt.savefig("test_course1.png")  # Save the figure

# Schedule the course and redraw
c1.set_scheduled_time(9)
fig, ax = plt.subplots(figsize=(10, 6))
c1.draw(ax)  # Should show the course name in the center of the filled box
plt.savefig("test_course2.png")  # Save the figure

# Test Course string representation
print(c1)






