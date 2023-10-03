import open3d as o3d
import numpy as np
from las_parser import points


pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
# o3d.visualization.draw([pcd])
o3d.visualization.draw_geometries([pcd], 'Open3D', 1920, 1080, 50, 50, False, False, False)
