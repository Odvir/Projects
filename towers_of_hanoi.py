#towers of Hanoi

def solve_hanoi(n, start_peg, end_peg):
    if n==1:
        move_disk(n, start_peg, end_peg)
    else:
       spare_peg = 6-end_peg-start_peg
       solve_hanoi(n-1,start_peg,spare_peg)
       move_disk(n, start_peg,end_peg)
       solve_hanoi(n-1,spare_peg,end_peg)
def move_disk(disk_num, from_peg, to_peg):
    print("Move disk",disk_num, "from peg", from_peg,"to",to_peg)
    
