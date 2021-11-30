import csv 
import sys
import numpy as np
from sympy import * 

#https://www.geeksforgeeks.org/python-sympy-matrix-rref-method/
#https://numpy.org/doc/stable/user/quickstart.html
#https://stackoverflow.com/questions/8024896/augment-a-matrix-in-numpy

# p is the dampening factor and n is the number of rows/columns 
# of the n x n matrix
def pagerank(n, p = 0.15):
    # Retrieves the A matrix from a csv file and converts non-zero entries into M matrix entries
    a = [] 
    with open(sys.argv[1], "r") as file: 
        reader = csv.reader(file)
        for row in reader:
            for entry in range(n):
                if row[entry]=='':
                    row[entry] = 0  
                elif row[entry] != 0: 
                    row[entry] = (1 - p) * decimalizer(row[entry]) + p * (1 / n)
                

            a.append(row)
    # Transposes matrix so we can work with its column vectors more easily
    m = np.array(a)
    m = m.astype(np.float) 
    m = m.T
    print("ONe: ", m)
    # Converts the A matrix's zero columns into the M matrix 
    for col in range(n): 
        onlyzero = True
        for entry in range(n): 
            if m[col][entry] != 0:
                onlyzero = False 
            if (onlyzero and entry == n - 1):
                m[col][:] = 1/n
    m = m.T
    print("Two: ", m)
    # Finds the steady state vector 

    # Represent M - In
    m = m - np.identity(n)
    zeros = np.zeros((n, 1))
    augmented_m = np.concatenate((m, zeros), axis = 1)
    print("Augmented: ", augmented_m)
    augmented_m = Matrix(augmented_m)
    m_rref = augmented_m.rref()
    # x is the steady state vector
    x = []
    print(m_rref)

    return 0

def decimalizer(x): 
    if x == '0': 
        return 0
    elif x == '1': 
        return 1
    else: 
        print(x)
        return 1.0/float(x[2:])

if __name__ == "__main__":
    pagerank(39)
