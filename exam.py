A = 0
B = 0
C = 0
Vote = " "
while Vote != "END":
    Vote = input("Enter your vote A,B or C:")
    if Vote == A:
          A += 1
    
    if Vote == B:
        B += 1
    
    if Vote == C:
        C += 1

total_votes =A+B+C
print("votes for A",A)
print("votes for B",B)
print("votes for C",C)
print("Total votes",total_votes)
        
        