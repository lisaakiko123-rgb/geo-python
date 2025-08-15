# scheduling.py
# Project 6 Part A
#   Classes Event, Course (subclass of Event), Schedule
#   Function create_schedule

import numpy as np
import matplotlib.pyplot as plt
from interval import Interval


# Event Class
class Event:
    """
    An instance represents an event to be scheduled.
    
    Instance attributes:
        _id: (int) the id of the event
        duration: (int) the duration of the event
        importance: (float) the importance of the event; lower is less important
        available: (Interval) the time window within which the event can be scheduled
        scheduled_time: (int or None) the time at which the event is scheduled  
                        to start.  None if the event cannot be scheduled.
    """

    def __init__(self, start, end, duration, importance, event_id):
        '''
        Initializes an instance of Event.  Attribute scheduled_time should be
        initialized to None.
       
        Parameters:
        start: (int) the earliest time at which the event can be scheduled to start
        end: (int) the latest time at which the event can be scheduled to end
        duration: (int) the duration of the event
        importance: (float) the importance of the event
        event_id: (int) the id of the event
        '''
        # TODO: implement me
        self._id = event_id
        self.duration = duration
        self.importance = importance
        self.available = Interval(start, end)
        self.scheduled_time = None



    def get_id(self):
        '''
        Returns (int) the id of the event
        '''
        # TODO: implement me
        return int(self._id)



    def earliest_time(self, possible_interval):
        '''
        Returns (numeric) the earliest time this event can be scheduled to
        start in possible_interval.  If this event cannot be scheduled in
        possible_interval, return np.inf .
        
        Parameter possible_interval: instance of Interval
        '''
        # TODO: implement me
        #Find the overlap btwn the available interval and the possible interval
        overlap_time = self.available.overlap(possible_interval)
        #if there is no overlap or the overlapping time is too small
        if overlap_time is None or overlap_time.get_width() < self.duration:
            return np.inf
        else:
            return overlap_time.left


    def set_scheduled_time(self, t):
        '''
        Sets the time that this event is scheduled for to t (int).
        '''
        # TODO: implement me
        self.scheduled_time = t



    def unschedule(self):
        '''
        Unschedules this event (sets scheduled_time to None)
        '''
        # TODO: implement me
        self.scheduled_time = None



    def draw(self, ax):
        '''
        Draws the event.  Up to two rectangles are drawn for the event.
        First, an unfilled (white) rectangle is drawn with black border,
        representing the available interval of this event.  If the event is
        scheduled, then the time period during which the event is scheduled is
        drawn as a colored rectangle with opagueness representing the  
        importance of the event.  Both rectangles are vertically centered  
        around the id of the event.
        
        Parameter ax: the matplotlib axes on which to draw the event
        '''
        # TODO: implement me
        #Draw the unfilled rectangle for the available interval
        ax.barh(self.get_id(), self.available.get_width(), left=self.available.left, edgecolor='black', fill=False)
        if self.scheduled_time is not None:
            ax.barh(self.get_id(), self.duration, left=self.scheduled_time, edgecolor="black", color='magenta', alpha=self.importance)
        # Adjust axes limits to ensure visibility
        # ax.set_xlim(0, max(self.available.right + 5, 25))
        # ax.set_ylim(self._id - 1, self._id + 1)
        
    
    def __str__(self):
        '''
        Returns (str) a string representation of this event that includes the
        event's ID, importance, duration, and if it is scheduled, the 
        scheduled start and end time.
        '''
        # TODO: implement me
        event_info = f"Event ID={self._id}, Importance={self.importance:.4f}, Duration={self.duration}"
        #Add scheduleing details if the event isn't scheduled
        if self.scheduled_time is not None:
            end_time = self.scheduled_time + self.duration
            event_info += f"\nScheduled for time {self.scheduled_time} to {end_time}"
        else:
            event_info += "\nNot scheduled"
        return event_info


# Course Class (inherits from Event)
# TODO: implement this class as specified in the project description.
#       Include appropriate docstrings for the class and methods.



# Schedule Class
class Schedule:
    """
    An instance has these attributes:
        sname: (str) the name of the schedule
        window: (Interval) the time window in which events can be scheduled 
        event_list: (list of Event instances) the list of events for scheduling.
                    Some events may not get scheduled.
    """
    def __init__(self, start, end, name):
        '''
        Initializes an instance of Schedule.  
        Initialize attribute event_list as [] .

        Parameters:
        start: (int) the start time of the schedule (left end of `window` interval)
        end: (int) the end time of the schedule (right end of `window` interval)
        name: (str) the name of the schedule
        '''
        pass  # TODO: implement me
        self.sname = str(name)
        self.window = Interval(start, end)
        self.event_list = []

        

    def add_event(self, event):
        '''
        Adds (appends) the event to this schedule's event_list.  Returns None.

        Parameter event: (Event) the event to append to this schedule's event_list
        '''
        pass  # TODO: implement me
        self.event_list.append(event)

        

    def schedule_events(self):
        '''
        Schedule events from this schedule's event_list in this schedule's window. 
         
        First unschedules all events.
        Then use the heuristic given on the project description.
         
        Returns None
        '''
        pass  # TODO: implement me
        #unschedule all events
        for event in self.event_list:
            event.unschedule()
        
        #define the remaining window
        remaining_window = Interval(self.window.left, self.window.right)
        
        #schedule events using the heuristic
        has_events_to_schedule = True #Flag to control
        while has_events_to_schedule:
            #Find the earliest unschduled event that can fit
            best_event = None
            best_start_time = None
            best_ratio = float('-inf') #To maximize importance/duration
            
            for event in self.event_list:
                if event.scheduled_time is None: #Only consider unscheduled events
                    start_time = event.earliest_time(remaining_window)
                    if start_time != np.inf: #check if it can fit in the remaining window
                        ratio = event.importance/event.duration
                        if (best_event is None or start_time<best_start_time or (start_time== best_start_time and ratio>best_ratio)):
                            best_event = event
                            best_start_time = start_time
                            best_ratio = ratio
            
            #check if there is an event to schedule
            has_events_to_schedule =  best_event is not None
            if has_events_to_schedule:
                #schedule the chosen event
                best_event.set_scheduled_time(best_start_time)
                #update the remaining window
                remaining_window.left = best_start_time + best_event.duration
            
            

    

    def draw(self):
        '''
        Draws the schedule including all the events.  Scheduled events and 
        their time are indicated using color.  Unscheduled events are shown as
        unfilled rectangles.  See example figure on the project description.
        Save the figure to file.

        Parameter ax: the matplotlib axes on which to draw the event
        '''
        # Get the maximum event ID
        # Set figure window size, axis limits, y tickmarks
        max_id = self.event_list[-1].get_id()
        fig, ax = plt.subplots(figsize=(10, max(6,max_id/3)))
        ax.set_xlim(self.window.left, self.window.right)
        ax.set_yticks(range(max_id + 1))
            
        # Add title and labels
        ax.set_title(self.sname)
        ax.set_xlabel("Time")
        ax.set_ylabel("Event ID")
            
        # Draw each event
        for event in self.event_list:
            event.draw(ax)
        
        # Save the figure to a file
        plt.savefig("schedule_output.png")  # Save the figure as a PNG file
        plt.show()


    def print_selection(self, select='all'):
        '''
        Prints a selection of the events in this schedule's event_list.
        
        Parameter select: (str) indicates which events to print. The 3 
            possible values are
            'all' (default):  print all events
            'scheduled':  print all the scheduled events only
            'unscheduled':  print all the unscheduled events only
        '''
        pass  # TODO: implement me
        # Ensure select is valid; if not, do nothing
        if select not in ['all', 'scheduled', 'unscheduled']:
            print("Invalid selection. Choose 'all', 'scheduled', or 'unscheduled'.")
            return  # Exit the method without doing anything
        
        # Iterate through the event list and print based on the selection
        for event in self.event_list:
            if select == 'all':
                print(event)  # Print all events
            elif select == 'scheduled' and event.scheduled_time is not None:
                print(event)  # Print only scheduled events
            elif select == 'unscheduled' and event.scheduled_time is None:
                print(event)  # Print only unscheduled events
        


 
# Function to Create Schedule
def create_schedule(file_path, start, end, name):
    '''
    Returns a Schedule instance based on the data in the text file file_path.
    
    Instantiate a Schedule, read data to instantiate Events (and Courses) to
    add to the schedule, schedule the events, and draw and return the schedule.

    Parameters:
    file_path: (str) The path of the file
    name: (str) The name of the schedule
    start: (int) the start time of the schedule
    end: (int) the end time of the schedule
    '''
    s = Schedule(start, end, name)
    with open(file_path, 'r') as fileobj:
        lines= fileobj.readlines()  # lines is a list of strings,
                                    # each string is one line from the file
        
    # TODO 1. Instantiate Events (and/or Courses) and add them to Schedule s.
    #         (hint:  oneline.strip().split(",")  where oneline is one string
    #          is helpful for parsing the string with comma-separated parts)
    #      2. Schedule the events (hint: just call the relevant method!)
    #      3. Draw the schedule (hint: just call the relevant method!)
    #      4. Return the schedule
    for line in lines:
        line = line.strip() #Remove extra spaces and newline characters
        if not line:
            pass  # Skip empty lines
        else:
            parts = line.split(",")
            if parts[0] == "e" and len(parts) == 6:
                event_id = int(parts[1])
                start = int(parts[2])
                end = int(parts[3])
                duration = int(parts[4])
                importance = float(parts[5])
                event = Event(start, end, duration, importance, event_id)
                s.add_event(event)
            elif parts[0] == "c" and len(parts) == 7:
                event_id = int(parts[1])
                start = int(parts[2])
                end = int(parts[3])
                duration = int(parts[4])
                importance = float(parts[5])
                course_name = parts[6]
                course = Course(start, end, duration, importance, event_id, course_name)
                s.add_event(course)
    
    #schdule the events
    s.schedule_events()
    #draw the schedule
    s.draw()
    #return the schedule
    return s

class Course(Event):
    def __init__(self, start, end, duration, importance, event_id, course_name):
        super().__init__(start, end, duration, importance, event_id)
        self.course_name = course_name
        
    def draw(self, ax):
        #call the parent class's draw method
        super().draw(ax)
        #determine the center of the rectangle
        if self.scheduled_time is not None:
            center_x = self.scheduled_time + self.duration/2
        else:
            center_x = self.available.left + self.available.get_width()/2
        center_y = self.get_id() #use the event ID as the y-coordinate
        
        #add the course name at the center of the rectangle
        ax.text(center_x, center_y, self.course_name, ha="center", va="center")
        
    def __str__(self):
        return f"{self.course_name}\n{super().__str__()}"
        
        


#### Script code
if __name__ == "__main__":
    pass # Uncomment the code below once you have completed classes Event and
         # Schedule and the function create_schedule
         
    #Create and visualize a schedule
    myschedule= create_schedule("eventdata2.txt", 0, 100, "Generated Schedule")
    #Show result in print
    print('----Scheduled events----')
    myschedule.print_selection('scheduled')
    print('----Unscheduled events----')
    myschedule.print_selection('unscheduled')
    