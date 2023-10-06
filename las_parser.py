import laspy
import numpy as np

FILE_PATH = 'las_data.las'

def read_las_data(file_path: str) -> np.ndarray:
    """
    Reads las file https://en.wikipedia.org/wiki/LAS_file_format
    returns Point data records

    Args:
        file_path (str): path to a file 

    Returns:
        np.ndarray: 3-dimensional array
    """
    las_data = laspy.read(file_path)
    return las_data.xyz


if __name__ == '__main__':
    print(read_las_data(FILE_PATH))

