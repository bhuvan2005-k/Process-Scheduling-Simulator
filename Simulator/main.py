from scheduler import FCFS, SJF, RoundRobin

def display_metrics(processes, algorithm_name):
    print(f"\n=== {algorithm_name} Scheduling ===")
    print("Process | Waiting Time | Turnaround Time")
    total_wt = 0
    total_tat = 0
    for i, (wt, tat) in enumerate(processes):
        print(f"P{i+1}      | {wt}           | {tat}")
        total_wt += wt
        total_tat += tat
    n = len(processes)
    print(f"Average Waiting Time: {total_wt/n:.2f}")
    print(f"Average Turnaround Time: {total_tat/n:.2f}\n")

if __name__ == "__main__":
  
    burst_times = [5, 3, 8, 6]
    quantum = 3

    fcfs_result = FCFS(burst_times)
    display_metrics(fcfs_result, "FCFS")

    sjf_result = SJF(burst_times)
    display_metrics(sjf_result, "SJF")

    rr_result = RoundRobin(burst_times, quantum)
    display_metrics(rr_result, "Round Robin")
