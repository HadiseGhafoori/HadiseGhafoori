#include <iostream>
#include <queue>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

const int BUFFER_SIZE = 10;

queue<int> buffer;
mutex mtx;
condition_variable produce_cv, consume_cv;

void producer() {
    for (int i = 0; i < BUFFER_SIZE; i++) {
        unique_lock<mutex> lck(mtx);
        while (buffer.size() == BUFFER_SIZE) {
            produce_cv.wait(lck);
        }
        buffer.push(i);
        cout << "Producer produced " << i << endl;
        lck.unlock();
        consume_cv.notify_one();
    }
}

void consumer() {
    for (int i = 0; i < BUFFER_SIZE; i++) {
        unique_lock<mutex> lck(mtx);
        while (buffer.empty()) {
            consume_cv.wait(lck);
        }
        int item = buffer.front();
        buffer.pop();
        cout << "Consumer consumed " << item << endl;
        lck.unlock();
        produce_cv.notify_one();
    }
}

int main() {
    thread t1(producer);
    thread t2(consumer);
    thread t3(consumer);

    t1.join();
    t2.join();
    t3.join();

    return 0;
}
