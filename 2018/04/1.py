import re

# Examples are built on model building and then asking the questions from the model

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

with open(r'input', 'r') as f:
    inputlist = f.read().splitlines()

time_pattern = re.compile(r'^\[1518-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\]')
guard_asleep_minutes = {}
for line in inputlist:
    if 'Guard' in line:
        current_guard = re.match(r'^\[1518-(?:\d+)-(?:\d+) (?:\d+):(?:\d+)\] Guard #(?P<id>\d+) begins shift', line).group('id')
        
        if current_guard not in guard_asleep_minutes.keys():
            guard_asleep_minutes[current_guard] = 0
    if 'falls asleep' in line:
        fall_time = time_pattern.match(line).group('minute')

    if 'wakes up' in line:
        wake_time = time_pattern.match(line).group('minute')
        guard_asleep_minutes[current_guard] += time_asleep(fall_time, wake_time)

for guard_id, mins in guard_asleep_minutes.items():
    print(f"Guard #{guard_id} was asleep {mins} minutes")
most_sleepy_guard_id = dict_max_item(guard_asleep_minutes)
print(f'The guard who slept the most: #{most_sleepy_guard_id}')

# Now go through the list again but only look for the choosen guard
asleep_minutes = []
for line in inputlist:
    if 'Guard' in line:
        current_guard = re.match(r'^\[1518-(?:\d+)-(?:\d+) (?:\d+):(?:\d+)\] Guard #(?P<id>\d+) begins shift', line).group('id')
        
        if current_guard not in guard_asleep_minutes.keys():
            guard_asleep_minutes[current_guard] = 0
    if 'falls asleep' in line and current_guard==most_sleepy_guard_id:
        fall_time = time_pattern.match(line).group('minute')

    if 'wakes up' in line and current_guard==most_sleepy_guard_id:
        wake_time = time_pattern.match(line).group('minute')
        asleep_minutes.extend(minutes_slept_through(fall_time, wake_time))
for minute in list(range(60)):
    print(f'{minute}: {asleep_minutes.count(minute)}')


# This is a way more difficult solution but I has fun duing it. guard_asleep_minutes and asleep minutes could have been calculated in one loop