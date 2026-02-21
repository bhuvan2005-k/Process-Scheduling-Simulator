# CPU Scheduling Algorithms Simulation

This project implements three classic CPU scheduling algorithms in Python: "FCFS (First-Come-First-Serve)", "SJF (Shortest Job First)", and "Round Robin (RR)". It calculates "Waiting Time (WT)" and "Turnaround Time (TAT)" for a set of processes and displays average metrics.  

Files

1. 'scheduler.py' – Contains the implementations of the scheduling algorithms:  
       FCFS(burst_times)
       SJF(burst_times) 
       RoundRobin(burst_times, quantum) 

2. 'main.py' – Script to run the scheduling simulations and display results using sample burst times.

Features

1. Compute **Waiting Time** and **Turnaround Time** for each process.
2. Calculate **average waiting time** and **average turnaround time**.
3. Supports **Round Robin scheduling** with a configurable time quantum.
4. Easy-to-read console output.

Usage

1. Clone the repository:

bash
git clone <https://github.com/bhuvan2005-k/Process-Scheduling-Simulator.git>
cd Process-Scheduling-Simulator

2. Run the main program:

python main.py

3.You will see the waiting time and turnaround time for each process, along with the averages.

