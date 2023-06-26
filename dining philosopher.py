
import threading

class Philosopher(threading.Thread):

    def __init__(self, index, left_fork, right_fork, mutex):
        
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.mutex = mutex

    def run(self):
        while True:

            # eat
            self.mutex.acquire()
            self.left_fork.acquire()
            self.right_fork.acquire()
            self.mutex.release()

            print(f"Philosopher {self.index} is eating.")

            # think
            self.left_fork.release()
            self.right_fork.release()

            print(f"Philosopher {self.index} is thinking.")


if __name__ == "__main__":

    forks = [threading.Lock() for i in range(5)]
    mutex = threading.Lock()
    philosophers = [Philosopher(i, forks[i], forks[(i+1)%5], mutex) for i in range(5)]
    
    for p in philosophers:
        p.start()