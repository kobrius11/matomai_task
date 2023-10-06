import open3d as o3d
from las_parser import read_las_data

#   using first 1000 points since my pc cant handle len(POINTS)
FILE_PATH = 'las_data.las'
POINTS = read_las_data(FILE_PATH)[:1000]
#   octree depth
MAX_DEPTH = 16

#   Initialize point cloud
pcd = o3d.geometry.PointCloud()
#   put points, into point cloud, and paint those points gray color
pcd.points = o3d.utility.Vector3dVector(POINTS)
pcd.paint_uniform_color([0.5, 0.5, 0.5])

#   initialize octree
octree = o3d.geometry.Octree(max_depth=MAX_DEPTH)
#   put point cloud into octree, to make a structure
octree.convert_from_point_cloud(pcd, size_expand=0.01)

print("""
Displaying octree info:
    Dimmensions: {}
    Center: {}
    """.format(octree.dimension(), octree.get_center()))
# help(octree)


print('Displaying octree ..')
o3d.visualization.draw([octree])
