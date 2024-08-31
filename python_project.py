# Project Description:
# Develop a system to process a list of Event objects, which capture user login and logout activities across various machines.
# The system should sort these events by date, track user sessions, and generate a report listing all users currently logged in to each machine.

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].discard(event.user)  # Use discard to avoid KeyError
    return machines

def generate_report(machines):
    for machine, users in machines.items():  # Use machines here instead of machine
        if len(users) > 0:
            user_list = ",".join(users)
            print("{}: {}".format(machine, user_list))

class Event:
    def __init__(self, event_date, event_type, machine_name, user):  # Use __init__ instead of _int_
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

Events = [
    Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(Events)
print(users)

generate_report(users)

     
 
 
    