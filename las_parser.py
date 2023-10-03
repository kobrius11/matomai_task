import laspy
import numpy as np

def read_las_data(file_path: str):
    las_data = laspy.read(file_path)
    return las_data.xyz

points = read_las_data('las_data.las')

if __name__ == '__main__':
    print(points)

