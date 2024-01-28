"""
Accept two positions as input: start and end. 
Print YES if a bishop at start can move to end in exactly one move. 
Print NO otherwise. Note that a bishop can only move along diagonals.
row: 1 to 8
col: A to H

"""

start = input()
end = input()
col_start= start[0].upper()
row_start=int(start[1])
col_end=end[0].upper()
row_end=int(end[1])
bishop="YES"
cols=["A","B","C","D","E","F","G","H`"]
if row_start == row_end:
    bishop="No"
elif  col_start == col_end: 
    bishop="No"
elif  row_start not in range(1,8):
    bishop="No" 
elif  row_end not in range(1,8):
    bishop="No" 
elif col_start not in cols:
    bishop="No" 
elif col_end not in cols:
    bishop="No"       

print(bishop)   
        

