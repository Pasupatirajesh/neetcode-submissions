class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        # populate the frequency of task and task to max heap
        task_freq = Counter(tasks)
        cpu_heap = [(-task_freq, task) for task, task_freq in task_freq.items()]
        heapq.heapify(cpu_heap)

        q = deque()
        while q or cpu_heap:
            #Pop the queue only if the available_time < time and push it back to the heap
            if q and q[0][0] <=time:
                available_time, task, freq = q.popleft()
                heapq.heappush(cpu_heap, (freq, task))
            
            if cpu_heap:
                freq_task, task = heapq.heappop(cpu_heap)
                freq_task+=1
                if freq_task < 0:
                    q.append((time + n + 1, task, freq_task))
            time+=1
        return time
