import threading

def func2():
    print("hello", threading.currentThread.getName())


def func1():
    print('calling my thread', threading.currentThread().getName())
    T1 = threading.Thread(target=func1, name='T1')
    T2 = threading.Thread(target=func2, name='T2')
    T1.start()
    T2.start()
    T1.join()
    T2.join()

print('end the main thread')


def insert(data):
    queuelist.insert(0, data)


def remove():
    if len(queuelist) > 0:
        return queuelist.pop()
    return ("Queue Empty!")


def display():
    print("Elements on queue are:")
    for i in range(len(queuelist)):
        print(queuelist[i])


if _name_ == "_main_":
    queuelist = []
    insert(5)
    insert(6)
    insert(9)
    insert(5)
    insert(3)
    print("Popped Element is: " + str(remove()))
    display()
