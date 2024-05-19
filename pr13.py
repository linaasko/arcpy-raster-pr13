import arcpy
points = r"E:\university\3 course\programming in gis\lections\arcpy, raster pr8, l13\data\rec_sites.shp"
raster = arcpy.Raster(r"E:\university\3 course\programming in gis\lections\arcpy, raster pr8, l13\data\elevation")
with arcpy.da.SearchCursor(points,"SHAPE@XY") as cursor:
    for row in cursor:
        print('X:{}, Y:{}'.format(row[0][0], row[0][1]))
spatial_ref_points = arcpy.Describe(points).spatialReference.name
spatial_ref_raster = arcpy.Describe(raster).spatialReference.name
print(spatial_ref_points, spatial_ref_raster)
if spatial_ref_points == spatial_ref_raster:
    print('Feature class and raster have the same coordinate systems')
else:
    print('Feature class and raster have different coordinate systems')
