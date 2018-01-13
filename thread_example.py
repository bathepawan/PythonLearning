import threading
import time

class MyThread(threading.Thread):
    def __init__(self, thread_id=None, thread_name=None, thread_type=None):
        super().__init__()
        self.thread_it = thread_id
        self.thread_name = thread_name
        self.thread_type = thread_type

    def run(self):
        if self.thread_type == 1:
            self.print_linear()
        else:
            self.print_squares()

    def print_linear(self):
        i = 1
        while True:
            try:
                print(i,)
                i+=i
                time.sleep(2)
            except e:
                print('Exiting {}'.format(self.thread_name))
    def print_squares(self):
        i = 1
        while True:
            try:
                print(i,)
                i*=i
                time.sleep(2)
            except e:
                print('Exiting {}'.format(self.thread_name))


if __name__=='__main__':

    t1 = MyThread(1, 'sequence', 1)
    t2 = MyThread(2, 'squares', 2)

    t1.start()
    t2.start()

    print('exiting main')
