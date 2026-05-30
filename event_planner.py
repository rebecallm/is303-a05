'''
Rebeca Llontop 
IS 303 - A05

Event Planner
This program models a calendar that holds a collection of events.
Users can add events, find events by date, and check for overlapping events.

Inputs:
- Event title, category, date, and time from user input 

Processes:
- Event class: stores title, category, date, and time; displays info
- Calendar class: stores events in a list; adds events; finds events by date; checks for overlapping events; displays next upcoming event

Outputs:
- Each event's info, find specified events, upcoming events, total events 
'''
import re

class Event:
    def __init__(self, title, category, date, time):
        self.title = title
        self.category = category
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.title} ({self.category}) - {self.date} at {self.time}"

class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """Add an Event object to the calendar."""
        if self.check_overlapping(event):
            print("Error: This event overlaps with an existing event.")
        else:
            self.events.append(event)

    def find_events_by_date(self, date):
        """Return a list of events on the specified date."""
        found=[]
        for event in self.events:
            if event.date == date:
                found.append(event)
        return found

    def check_overlapping(self, event):
        """Return True if the event overlaps with any existing events."""
        for existing in self.events:
            if existing.date == event.date and existing.time == event.time:
                return True
        return False
     
    def display_upcoming_event(self):
        """Display the next upcoming event."""
        if self.events: 
            self.events.sort(key=lambda e: (e.date, e.time))  # Sort events by date and time
            print(f"Next upcoming event: {self.events[0]}")
        else:
            print("No upcoming events.") 

    def __str__(self):
        return f"Calendar with {len(self.events)} events."   
        

# --- Main Flow ---
 
if __name__ == "__main__":
    calendar = Calendar()

    num_events = input("How many events would you like to add? ").strip()
    while not num_events.isdigit() or int(num_events) <= 0:
        num_events = input("Please enter a valid positive integer for the number of events: ").strip()
    num_events = int(num_events)

    for i in range(num_events):
        print(f"\nEvent {i + 1}:")
        title = input("Enter event title: ").strip()
        while title == "" or not title.replace(" ", "").isalpha():
            title = input("Event title cannot be empty. Please enter event title: ").strip()
        title = title.title()  # Capitalize each word in the title
        category = input("Enter event category: ").strip()
        while category == "" or not category.replace(" ", "").isalpha():
            category = input("Event category cannot be empty. Please enter event category: ").strip()
        category = category.title()  # Capitalize each word in the category
        date = input("Enter event date (YYYY-MM-DD): ").strip()
        while not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            date = input("Event date cannot be empty. Please enter event date (YYYY-MM-DD): ").strip()
        time = input("Enter event time (HH:MM AM/PM): ").strip()
        while not re.match(r"^\d{2}:\d{2}\s?(AM|PM)$", time, re.IGNORECASE):
            time = input("Event time cannot be empty. Please enter event time (HH:MM AM/PM): ").strip()
        event = Event(title, category, date, time)
        calendar.add_event(event)

    print("\nAll events in the calendar:")
    for event in calendar.events:
        print(event)
    print(calendar)

    print("Upcoming event:")
    calendar.display_upcoming_event()

    search_date = input("\nEnter a date to find events (YYYY-MM-DD): ").strip()
    print(f"Events on {search_date}:")

    found_events = calendar.find_events_by_date(search_date)
    for event in found_events:
        print(event)
