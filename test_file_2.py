n = int(input())
m = int(input())
queue = []
cust = input()
while cust != ".":
    if cust == "Customer":
        queue.append("Customer")
    cust = input()
print(queue)

