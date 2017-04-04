import pandas as pd
import numpy as np
    
# Initialize paramaters
array = (input("please input your array in such form: 50,51,30,40: \n")).split(',')
array = [int(i) for i in array]
print_output = int(input("do you want to see the process? (1 for yes/0 for no): \n"))

angles = array
start_angle = angles[0]

def brute_force(angles, start_angle):
    
    if len(angles) == 0:
        return 0
    x = brute_force(angles[1:], start_angle+1)
    y = brute_force(angles[1:], start_angle-1)
    z = brute_force(angles[1:], start_angle)
    if angles[0] == start_angle:
        return max(x + 1, y + 1, z + 1)
    else:
        return max(x, y, z)
    
#brute_force(angles, start_angle, track)


df = pd.DataFrame(index = angles, columns = range(start_angle - len(angles),start_angle + len(angles)+1), data = 0)
def dynamic_programming(df, print_output = False):
    df.iloc[0][start_angle] = 1
    columns = list(df.columns)
    rows = list(df.index)
    
    for row in range(0, len(df)-1):
        # record the degree of the upcoming plane, which is in next row
        plane_degree = rows[row+1]
        
        for col in range(1, len(df.iloc[0])-1):
            # if the current column has data, the cannon can
            # go down left, go down, or go down right
            if df.iloc[row].iloc[col] != 0:
                data = df.iloc[row].iloc[col]
                
                # go down left
                left_column_degree = columns[col-1]
                # if our move results in a new destoryed plane: 
                if left_column_degree == plane_degree:
                    df.iloc[row+1].iloc[col-1] = max(df.iloc[row+1].iloc[col-1], data + 1)
                else:
                    df.iloc[row+1].iloc[col-1] = max(df.iloc[row+1].iloc[col-1], data)
                    
                # go down
                down_column_degree = columns[col]
                # if our move results in a new destoryed plane: 
                if down_column_degree == plane_degree:
                    df.iloc[row+1].iloc[col] = max(df.iloc[row+1].iloc[col], data + 1)
                else:
                    df.iloc[row+1].iloc[col] = max(df.iloc[row+1].iloc[col], data)
                    
                # go down right
                right_column_degree = columns[col+1]
                # if our move results in a new destoryed plane: 
                if right_column_degree == plane_degree:
                    df.iloc[row+1].iloc[col+1] = max(df.iloc[row+1].iloc[col+1], data + 1)
                else:
                    df.iloc[row+1].iloc[col+1] = max(df.iloc[row+1].iloc[col+1], data)
        
        if print_output == True:
            print(df)
            print("===============================================================")
    
    return max(df.iloc[-1])
    


dp_ouput = dynamic_programming(df, print_output)
print("\ninput data is ", angles)
print("dynamic programming can shoot down", dp_ouput, "planes")
print("brute force method can shoot down", brute_force(angles, start_angle), "planes")