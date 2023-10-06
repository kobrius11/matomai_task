import open3d as o3d
from las_parser import read_las_data

#   using first 1000 points since my pc cant handle len(POINTS)
FILE_PATH = 'las_data.las'
POINTS = read_las_data(FILE_PATH)[:1000]
#   octree depth
MAX_DEPTH = 16


pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(POINTS)
#   boundingBox = o3d.geometry.AxisAlignedBoundingBox.create_from_points(pcd.points)
#   downpcd = pcd.voxel_down_sample(voxel_size=0.05)
pcd.paint_uniform_color([0.5, 0.5, 0.5])

octree = o3d.geometry.Octree(max_depth=MAX_DEPTH)
octree.convert_from_point_cloud(pcd, size_expand=0.01)

print("""
Displaying octree info:
    Dimmensions: {}
    Center: {}
    """.format(octree.dimension(), octree.get_center()))
# help(octree)


print('Displaying octree ..')
o3d.visualization.draw([octree])
