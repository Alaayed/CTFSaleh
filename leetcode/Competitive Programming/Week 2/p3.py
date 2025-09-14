from sortedcontainers import SortedList

def intersecting_rectangles():
    n = int(input())
    rectangles = [tuple(map(int, input().split())) for _ in range(n)]
    start_events, end_events = getStartEnd(rectangles)
    hseg = SortedList([])
    s1, e1, score = 0 , 0 , 0
    while s1 != len(start_events):
        if start_events[s1][0] < end_events[e1][0]:
            y1,y2 = start_events[s1][1], start_events[s1][2]
            # inc start event
            s1+=1
            # Process vertical segments
            score += process_vertical_segment(hseg,y1,y2)
            # Add horizontal segments
            hseg.update([y1,y2])
        else:
            y1,y2 = end_events[e1][1], end_events[e1][2]
            e1+=1
            # Process hseg FIRST
            hseg.remove(y1)
            hseg.remove(y2)
            score += process_vertical_segment(hseg,y1,y2)
    return score
def getStartEnd(rectangles):
    startEvents = []
    endEvents = []
    for i , (x1, y1, x2, y2) in enumerate(rectangles):
        startEvents.append((x1, y1 , y2))
        endEvents.append((x2, y1 , y2))
    startEvents.sort()
    endEvents.sort()
    return startEvents, endEvents
def process_vertical_segment(hseg,y1,y2):
    return hseg.bisect_left(y1)-hseg.bisect_left(y2)

