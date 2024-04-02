import math
import numpy as np

def affine_transformation_matrix(angle, center):
    # Параллельный перенос на точку center
    T_prime = np.array([[1, 0, center[0]],
                        [0, 1, center[1]],
                        [0, 0, 1]])

    # Поворот на угол angle
    R = np.array([[math.cos(angle), -math.sin(angle), 0],
                  [math.sin(angle), math.cos(angle),  0],
                  [0,               0,                1]])

    # Параллельный перенос на точку -center
    T = np.array([[1, 0, -center[0]],
                  [0, 1, -center[1]],
                  [0, 0, 1]])

    # Вычисление матрицы аффинного преобразования
    P = np.dot(np.dot(T_prime, R), T)

    return P

# Угол и точки для поворотов
angle_1 = -math.pi / 6
center_1 = (2, -1)
angle_2 = math.pi / 6
center_2 = (1, -2)

# Вычисление матрицы аффинного преобразования
P = np.dot(affine_transformation_matrix(angle_2, center_2), affine_transformation_matrix(angle_1, center_1))

print(P)
