import os, datetime

def parse_between_time(_start, _end, filename="application-event-log.txt") -> int:
    '''
    Parses a windows event log given a start and end time counting how many
    entries were made that occurred between the start and end times. 

    returns: int: count # Of entries made
    '''
    # opening log file to parse and removing header line
    events = open(filename, "r")
    header = events.readline()

    # converting start and end into time objects
    start = datetime.datetime.strptime(_start, "%H:%M:%S").time()
    end = datetime.datetime.strptime(_end, "%H:%M:%S").time()

    # Comparing time of each entry to start and end, increment count if time inbetween
    count = 0
    for event in events:
        temp = event.split("\t")
        event_time = datetime.datetime.strptime(temp[2], "%I:%M:%S %p").time()
        
        if event_time <= end and event_time >= start:
            count +=1

    return count


test_start = "01:34:00"
test_end = "01:39:59"

test_count = parse_between_time(test_start, test_end)

print(f"Final count of entries between {test_start} and {test_end} was {test_count}")
