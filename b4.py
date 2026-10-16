voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

max_streak = 0
current_streak = 0
start_v = voltages[0]
end_v = voltages[0]
temp_start = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i-1]:
        if current_streak == 0:
            temp_start = voltages[i-1]
        current_streak += 1
    else:
        current_streak = 0
    
    if current_streak > max_streak:
        max_streak = current_streak
        start_v = temp_start
        end_v = voltages[i]

print(f"Longest continuous drop: {max_streak} minutes")
print(f"Started at: {start_v} V")
print(f"Ended at: {end_v} V")
