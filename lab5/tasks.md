# Lab 4 — Computations & Algorithms

### Hint: 4,5,6 without numpy

## 1. Compute roots of the quadratic equation y = ax*2 + bx + c given inputs a, b, c.

## 2. Sort numbers in descending order. Randomly generate 50 numbers—use the standard random function. Use the built-in sorting function only to verify results.

## 3. Compute the dot (scalar) product of vectors a = [1, 2, 12, 4] and b = [2, 4, 2, 8].

## 4. Sum two 128x128 matrices (generated randomly).

## 5. Multiply two 8x8 matrices.

## 6. Compute the determinant of a randomly generated matrix.

# Answers:

## [Ad. 1](ex1.py)
```bash
lab5 % python3 ex1.py 
Quadratic equation: 1x^2 + 5x + 6 has roots: ((-2+0j), (-3+0j))
Quadratic equation: 1x^2 + 2x + 1 has roots: ((-1+0j), (-1+0j))
Quadratic equation: 1x^2 + 0x + 1 has roots: (1j, -1j)
```

## [Ad. 2](ex2.py)
```bash
python3 ex2.py
Success! Sorting in descending order completed. Verification OK
Sorted array: [931, 794, 776, 751, 708, 669, 651, 594, 579, 549, 543, 539, 526, 509, 464, 463, 444, 428, 382, 346, 342, 298, 221, 181, -54, -63, -78, -82, -192, -195, -307, -336, -339, -386, -412, -424, -438, -479, -492, -540, -563, -600, -607, -645, -654, -821, -828, -893, -964, -984]
```

## [Ad. 3](ex3.py)
```bash
lab5 % python3 ex3.py
Scalar product of vectors [1, 2, 12, 4] and [2, 4, 2, 8] is:
 66
```

## [Ad. 4](ex4.py)
Verification for 2x2 matrices:
```bash
lab5 % python3 ex4.py
Sum two 128x128 matrices (generated randomly)
Matrix 1: size 2 x 2 
MATRIX 1: 
[[10, 1], [-1, 1]]
Matrix 2: size 2 x 2 
MATRIX 2: 
[[-4, 8], [-7, 6]]
sum_matrices(matrix1,matrix2):
 [[6, 9], [-8, 7]]
np_sum 2: 
[[ 6  9]
 [-8  7]]
Verification is OK - SUCCESS
```

Debugging off, 128x128 matrices:
```bash
lab5 % python3 ex4.py
Sum two 128x128 matrices (generated randomly)
Matrix 1: size 128 x 128 
MATRIX 1: 

Matrix 2: size 128 x 128 
MATRIX 2: 

sum_matrices(matrix1,matrix2):
 
np_sum 2: 

Verification is OK - SUCCESS
```

## [Ad. 5](ex5.py)
Verification for 2x2 matrices:
```bash
lab5 % python3 ex5.py
Multiply two 8x8 matrices (generated randomly)
Matrix 1: size 2 x 2 
MATRIX 1: 
[[-7, 6], [-5, -2]]
Matrix 2: size 2 x 2 
MATRIX 2: 
[[2, -1], [6, -1]]
sum_matrices(matrix1,matrix2):
 [[22, 1], [-22, 7]]
np_multi 2: 
[[ 22   1]
 [-22   7]]
Verification is OK - SUCCESS
```

Debugging off, 8x8 matrices:
```bash
lab5 % python3 ex5.py
Multiply two 8x8 matrices (generated randomly)
Matrix 1: size 8 x 8 
MATRIX 1: 

Matrix 2: size 8 x 8 
MATRIX 2: 

sum_matrices(matrix1,matrix2):
 
np_multi 2: 

Verification is OK - SUCCESS
```