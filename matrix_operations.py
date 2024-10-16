import random

def generate_random_matrix(rows, cols):
    matrix = []  
    for i in range(rows):  
        row = [] 
        for j in range(cols):
            number = random.randint(1, 100) 
            row.append(number) 
        matrix.append(row)  
    return matrix 

def get_column_sum(matrix, col_index):
    total = 0  
    for row in matrix: 
        total += row[col_index] 
    return total  

def get_row_average(matrix, row_index):
    row = matrix[row_index]  
    total = sum(row)  
    average = total / len(row)  
    return average  

matrix = generate_random_matrix(8, 9) 
print("Matrix:")
for cols in matrix:
    print(cols)  

print("Sum of column 0:", get_column_sum(matrix, 2))

print("Average of row 1:", get_row_average(matrix, 1))
