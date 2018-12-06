import re

def time_asleep(fall, wake):
    return int(wake)-int(fall)

def dict_max_item(dictionary):
    max_key = None
    max_value = 0
    for key, item in dictionary.items():
        if item > max_value:
            max_key = key
            max_value = item
    return max_key

def minutes_slept_through(fell, wake):
    return list(range(int(fell), int(wake)))

with open(r'04\input', 'r') as f:
    inputlist = f.read().splitlines()

time_pattern = re.compile(r'^\[1518-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\]')

guard_asleep_minutes = {}
for line in inputlist:
    if 'Guard' in line:
        current_guard = re.match(r'^\[1518-(?:\d+)-(?:\d+) (?:\d+):(?:\d+)\] Guard #(?P<id>\d+) begins shift', line).group('id')
        
        if current_guard not in guard_asleep_minutes.keys():
            guard_asleep_minutes[current_guard] = []
    if 'falls asleep' in line:
        fall_time = time_pattern.match(line).group('minute')

    if 'wakes up' in line:
        wake_time = time_pattern.match(line).group('minute')
        guard_asleep_minutes[current_guard].extend(minutes_slept_through(fall_time, wake_time))

top = 0
for id, minute_list in guard_asleep_minutes.items():
    print('#',id)
    for minute in list(range(60)):
        count = minute_list.count(minute)
        if count > top:
            top = count
        print(f'{minute}: {count}')
print(top)

# after this a search and you find the id you want, the minute is abvioius (the top values minute...)
