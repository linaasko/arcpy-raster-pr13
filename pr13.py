import arcpy
points = arcpy.GetParameterAsText(0)
raster = arcpy.Raster(arcpy.GetParameterAsText(1))
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
result = arcpy.GetParameterAsText(2)
arcpy.MakeFeatureLayer_management(points, result)
arcpy.management.AddField(points, "HEIGHT", "FLOAT")
arcpy.AddMessage('add field "HEIGHT" to feature class')
with arcpy.da.UpdateCursor(result, ["SHAPE@XY", "HEIGHT"]) as cursor:
    for row in cursor:
        x, y = row[0]
        raster_value = arcpy.GetCellValue_management(raster, str(x)+" "+str(y))
        row[1] = float(raster_value.getOutput(0))
        cursor.updateRow(row)
arcpy.AddMessage('fill field "HEIGHT" with Dem values')
