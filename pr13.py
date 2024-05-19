import arcpy
points = r"E:\university\3 course\programming in gis\lections\arcpy, raster pr8, l13\data\rec_sites.shp"
raster = arcpy.Raster(r"E:\university\3 course\programming in gis\lections\arcpy, raster pr8, l13\data\elevation")
with arcpy.da.SearchCursor(points,"SHAPE@XY") as cursor:
    for row in cursor:
        print('X:{}, Y:{}'.format(row[0][0], row[0][1]))
