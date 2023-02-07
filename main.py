# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
#
# print(queue)
#
# queue.pop(0)
# print(queue)

# # reverse queue is achieved with insert at zero and normal pop


# queue2 = []
# queue2.insert(0, 10)
# queue2.insert(0, 20)
# queue2.insert(0, 30)
# print(queue2)
#
# queue2.pop()
# print(queue2)

queue = []


def enqueue():
    element = input('Enter a value to add to queue')
    queue.append(element)
    print(f'element added to queue = {element}')
    print(queue)


def dequeue():
    if not queue:
        print('Queue is empty!')
        return
    element = queue.pop(0)
    print(f'element removed from queue = {element}')
    print(queue)


while True:
    print('Press 1 for adding to queue')
    print('Press 2 for removing from queue')
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    else:
        print('Invalid option')
