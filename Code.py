#FCFS (First Come First Serve) 
def fcfs(requests, head): 
seek_time = 0 
sequence = [head] 
for req in requests: 
seek_time += abs(head - req) 
head = req 
sequence.append(head) 
return seek_time, sequence 
# SSTF (Shortest Seek Time First) 
def sstf(requests, head): 
seek_time = 0 
requests = requests.copy() 
sequence = [head] 
while requests: 
nearest = min(requests, key=lambda x: abs(x - head)) 
seek_time += abs(head - nearest) 
head = nearest 
sequence.append(head) 
requests.remove(nearest) 
return seek_time, sequence 
# SCAN (Elevator Algorithm) 
def scan(requests, head, disk_size, direction="right"): 
seek_time = 0 
sequence = [head] 
left = [r for r in requests if r < head] 
right = [r for r in requests if r >= head] 
left.sort(reverse=True) 
right.sort() 
if direction == "right": 
for r in right: 
seek_time += abs(head - r) 
head = r 
sequence.append(head) 
# go to end 
seek_time += abs(head - (disk_size - 1)) 
head = disk_size - 1 
sequence.append(head) 
for r in left: 
seek_time += abs(head - r) 
head = r 
sequence.append(head) 
else:  # left direction 
for r in left: 
seek_time += abs(head - r) 
head = r 
sequence.append(head) 
seek_time += abs(head - 0) 
head = 0 
sequence.append(head) 
for r in right: 
seek_time += abs(head - r) 
head = r 
sequence.append(head) 
return seek_time, sequence= 
# C-SCAN (Circular SCAN) 
def cscan(requests, head, disk_size): 
seek_time = 0 
sequence = [head] 
left = [r for r in requests if r < head] 
right = [r for r in requests if r >= head] 
left.sort() 
right.sort() 
# service right side 
for r in right: 
seek_time += abs(head - r) 
head = r 
sequence.append(head) 
# go to end 
seek_time += abs(head - (disk_size - 1)) 
head = disk_size - 1 
sequence.append(head) 
# jump to start 
seek_time += disk_size - 1 
head = 0 
sequence.append(head) 
# service left side 
for r in left: 
seek_time += abs(head - r) 
head = r 
sequence.append(head) 
return seek_time, sequence 
# Main Program 
def main(): 
print("Disk Scheduling Algorithms Simulation\n") 
n = int(input("Enter number of requests: ")) 
requests = list(map(int, input("Enter request sequence: ").split())) 
head = int(input("Enter initial head position: ")) 
disk_size = int(input("Enter disk size: ")) 
print("\nRequest Queue:", requests) 
print("Initial Head Position:", head) 
fcfs_time, fcfs_seq = fcfs(requests, head) 
sstf_time, sstf_seq = sstf(requests, head) 
scan_time, scan_seq = scan(requests, head, disk_size) 
cscan_time, cscan_seq = cscan(requests, head, disk_size) 
print("\n--- Results ---") 
print("FCFS Seek Time:", fcfs_time) 
print("Sequence:", fcfs_seq) 
print("\nSSTF Seek Time:", sstf_time) 
print("Sequence:", sstf_seq) 
print("\nSCAN Seek Time:", scan_time) 
print("Sequence:", scan_seq) 
print("\nC-SCAN Seek Time:", cscan_time) 
print("Sequence:", cscan_seq) 
results = { 
"FCFS": fcfs_time, 
"SSTF": sstf_time, 
"SCAN": scan_time, 
"C-SCAN": cscan_time 
} 
best = min(results, key=results.get) 
worst = max(results, key=results.get) 
print("\n--- Analysis ---") 
print(f"Best Algorithm: {best} (Minimum Seek Time = {results[best]})") 
print(f"Worst Algorithm: {worst} (Maximum Seek Time = {results[worst]})") 
if __name__ == "__main__": 
main() 
