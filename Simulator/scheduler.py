def FCFS(burst_times):
    n = len(burst_times)
    wt = [0]*n
    tat = [0]*n
    for i in range(1, n):
        wt[i] = wt[i-1] + burst_times[i-1]
    for i in range(n):
        tat[i] = wt[i] + burst_times[i]
    return list(zip(wt, tat))

def SJF(burst_times):
    n = len(burst_times)
    processes = sorted([(i, bt) for i, bt in enumerate(burst_times)], key=lambda x: x[1])
    wt = [0]*n
    tat = [0]*n
    for i in range(1, n):
        wt[processes[i][0]] = wt[processes[i-1][0]] + processes[i-1][1]
    for i, bt in enumerate(burst_times):
        tat[i] = wt[i] + bt
    return list(zip(wt, tat))

def RoundRobin(burst_times, quantum):
    n = len(burst_times)
    rem_bt = burst_times.copy()
    wt = [0]*n
    tat = [0]*n
    t = 0
    done = False
    while not done:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - burst_times[i]
                    rem_bt[i] = 0
    for i in range(n):
        tat[i] = wt[i] + burst_times[i]
    return list(zip(wt, tat))
