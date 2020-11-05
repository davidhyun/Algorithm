# 행렬곱 함수
def mat_mul(X, Y):
    Matrix_Multiplication = []
    for idx1 in range(len(X)):
        row = []
        for idx2 in range(len(Y[0])):
            tmp = 0
            for idx3 in range(len(X[0])):
                tmp += X[idx1][idx3] * Y[idx3][idx2]
            row.append(tmp)
        Matrix_Multiplication.append(row)
    return Matrix_Multiplication

X = [[0.93459321, 0.20840165],
     [0.53553147, 0.49286453]]

Y = [[0.98689162, 0.86354536],
     [0.87284605, 0.18337937]]

M1 = [[1,1,1],
      [2,2,2]]

M2 = [[3],
      [2],
      [1]]

print(mat_mul(X, Y))
print(mat_mul(M1, M2))

"""
# 행렬곱 함수 (2x3) X (3x2) 행렬곱은 계산 못함
def mat_mul(X, Y):
    Matrix_Multiplication = [[0] * len(Y[0]) for _ in range(len(X))] # 행렬곱 초기화

    for i in range(0, len(X)):
        for k in range(0, len(Y[0])):
            for j in range(0, len(X[0])-1):
                Matrix_Multiplication[i][k] = X[i][j] * Y[j][k] + X[i][j+1] * Y[j+1][k] + X[i][j+2] * Y[j+2][k]

    return Matrix_Multiplication
"""