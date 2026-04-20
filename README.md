# 💽 Disk Scheduling Algorithms Simulator

## 📌 Overview

This project implements and analyzes common **disk scheduling algorithms** used in operating systems to optimize disk I/O operations.

Algorithms implemented:

* FCFS (First Come First Serve)
* SSTF (Shortest Seek Time First)
* SCAN (Elevator Algorithm)
* C-SCAN (Circular SCAN)

---

## 🎯 Objectives

* Understand disk scheduling concepts
* Implement scheduling algorithms
* Calculate total seek time
* Compare performance

---

## 🛠️ Technologies Used

* Python 3.x
* Basic Python libraries
* VS Code / PyCharm / IDLE
* Linux / Ubuntu (optional)

---

## ⚙️ How to Run

1. Clone or download the project
2. Open terminal in project folder
3. Run:

```bash
python main.py
```

4. Enter:

   * Number of requests
   * Disk request sequence
   * Initial head position
   * Disk size

---

## 📥 Sample Input

```
Number of requests: 8
Request sequence: 98 183 37 122 14 124 65 67
Initial head position: 53
Disk size: 200
```

---

## 📤 Sample Output

```
FCFS Seek Time: 640
SSTF Seek Time: 236
SCAN Seek Time: 331
C-SCAN Seek Time: 382
```

---

## 📊 Algorithms Description

### 🔹 FCFS

Processes requests in order of arrival.

### 🔹 SSTF

Selects the closest request to current head.

### 🔹 SCAN

Moves in one direction servicing requests, then reverses.

### 🔹 C-SCAN

Moves in one direction and jumps back to start.

---

## 📈 Performance Comparison

* SSTF reduces seek time significantly
* SCAN provides balanced performance
* C-SCAN ensures uniform wait time
* FCFS is simple but inefficient

---

## 🧠 Conclusion

Disk scheduling algorithms improve performance by minimizing seek time. SSTF and SCAN generally outperform FCFS, while C-SCAN provides fairness.

---

## 📌 Future Improvements

* Graph visualization of head movement
* GUI simulation
* Real-time disk animation

---


# Output
<img width="647" height="515" alt="Screenshot 2026-04-20 120614" src="https://github.com/user-attachments/assets/a75c69d4-dda6-40cd-8562-260cae970846" />
