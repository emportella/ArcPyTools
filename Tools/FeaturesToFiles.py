# -*- coding: cp1252 -*-

"""
FeaturetoFiles.
Copyright (C),2013 Eduardo Portella
his program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__="Eduardo Portella"
__date__ ="$26/03/2018 16:17:08$"
__copyright__ = "Copyright 2013, Eduardo Portella"
__license__ = "GPL 3.0"
__version__ = "0.1"
__maintainer__ = "Eduardo Portella"
__email__ = "emportella@gmail.com"
__status__ = "Production"

import arcpy
import os

input_file = r"c:\path\to\file.shp"
input_field = "name of field"
output_path = r"c:\path\to\output\folder"


arcpy.MakeFeatureLayer_management(input_file, "lyr") #make shapfile usable by SelectLayerBy..
arcpy.env.overwriteOutput = True

for row in arcpy.SearchCursor("lyr"):#iterate over table
    try:
        #Select indiviual features in shapefile. make sure all rows have a unique value
        arcpy.SelectLayerByAttribute_management("lyr",
                                            "NEW_SELECTION",
                                            input_field + " = " + "\'{0}\'".format(
                                                row.getValue(input_field).encode("UTF-8")))# .decode("UTF-8") is used for txt fields, otherwise delete it
        #save new shp.
        arcpy.CopyFeatures_management("lyr",
                                  os.path.join(output_path, row.getValue(input_field)+".shp"))
        #save new dwg
        arcpy.conversion.ExportCAD("lyr", "DWG_R2013",
                                   os.path.join(output_path, row.getValue(input_field)+".dwg"))
    except:
        #error messages
        print(arcpy.GetMessage(0))
        print(arcpy.GetMessage(1))
        print(arcpy.GetMessage(2))
