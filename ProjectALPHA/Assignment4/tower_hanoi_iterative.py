def move_disk(src, dest, s_name, d_name):
    disk = src.pop()
    dest.append(disk)
    print(f"Move Disk {disk} from {s_name} to {d_name}")


def legal_move(src, dest, s_name, d_name):
    if not src:
        move_disk(dest, src, d_name, s_name)
    elif not dest:
        move_disk(src, dest, s_name, d_name)
    elif src[-1] < dest[-1]:
        move_disk(src, dest, s_name, d_name)
    else:
        move_disk(dest, src, d_name, s_name)


n = int(input("Enter number of disks: "))

# Pegs represented as stacks
A = list(range(n, 0, -1))
B = []
C = []

# Swap auxiliary and destination for even number of disks
if n % 2 == 0:
    B, C = C, B
    b_name, c_name = "C", "B"
else:
    b_name, c_name = "B", "C"

total_moves = 2 ** n - 1

for i in range(1, total_moves + 1):
    if i % 3 == 1:
        legal_move(A, C, "A", c_name)
    elif i % 3 == 2:
        legal_move(A, B, "A", b_name)
    else:
        legal_move(B, C, b_name, c_name)
        


        """"" SECOND METHOD"""""""
def hanoi(n):
    moves = 2**n - 1
    src, aux, dest = 'A', 'B', 'C'

    if n % 2 == 0:
        aux, dest = dest, aux

    for i in range(1, moves + 1):
        if i % 3 == 1:
            move(src, dest)
        elif i % 3 == 2:
            move(src, aux)
        else:
            move(aux, dest)

def move(a, b):
    print(a, "->", b)

n = int(input("Enter number of disks: "))
hanoi(n)       
        
        -----OUTPUT------
        ubuntu@ubuntu-HP-Pro-SFF-280-G9-Desktop-PC:~/Downloads/TECOB11$ python3 tower_hanoi_iterative.py
Enter number of disks: 3
Move Disk 1 from A to C
Move Disk 2 from A to B
Move Disk 1 from C to B
Move Disk 3 from A to C
Move Disk 1 from B to A
Move Disk 2 from B to C
Move Disk 1 from A to C

