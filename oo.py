n = int(input()) # часы
m = int(input()) # сколько человек проходит
queue = []
cust = input()
while cust != ".":
    for i in n:
        if cust == "Customer":
        queue.append("Customer")
        queue = queue[-m:]
    else:
        if len(queue) == 1:
            queue.insert(0, "VIP-customer")
        elif len(queue) % 2 == 0:
            queue.insert(len(queue) // 2, "VIP-customer")
            print(queue)
        else:
            queue.insert(len(queue) // 2 + 1, "VIP-customer")
            print(queue)
    cust = input()
print(queue)
