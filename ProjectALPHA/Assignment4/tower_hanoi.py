def tower_hanoi(n,source,auxiliary,destination):
   if n==1:
     print(f"Move the disk from source {source} to destination {destination}")
     return
     
   tower_hanoi(n-1 , source , destination , auxiliary)
   
   print(f"Move disk {n} from source {source} to destination {destination}")
   
   tower_hanoi(n-1 , auxiliary , source , destination)
   
n = int(input("Enter no of disks :"))
tower_hanoi(n , 'A', 'B' , 'C')

print("\n Total Moves = " , 2**n-1)
   
   
   
           -------OUTPUT-------
           
           
           ubuntu@ubuntu-HP-Pro-SFF-280-G9-Desktop-PC:~/Downloads/TECOB11$ python3 tower_hanoi.py
Enter no of disks :3
Move the disk from source A to destination C
 Move largest disk from A to C 
Move the disk from source C to destination B
 Move largest disk from A to C 
Move the disk from source B to destination A
 Move largest disk from A to C 
Move the disk from source A to destination C

 Total Moves =  7

