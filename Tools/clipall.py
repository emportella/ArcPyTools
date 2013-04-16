# -*- coding: utf-8 -*-

"""
Batch Clip files form a folder.

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
__date__ ="$14/04/2013 00:17:08$"
__copyright__ = "Copyright 2013, Eduardo Portella"
__license__ = "GPL 3.0"
__version__ = "0.1"
__maintainer__ = "Eduardo Portella"
__email__ = "emportella@gmail.com"
__status__ = "Production"


import arcpy as ap
from arcpy import env

 
def clipAll(featureclasses, clip_feature, destination_folder): 
    """
    Clip all shape files in a folder to a new folder
    using a clip feature.
    
    Args:
    ----------
    folder: String
        Path to original folder.
        
    clip_feature: Shapefile
        Polygon to be used as clipping feature.
    
    destination_folder: String
        Path to destination folder
    """
    #Setting destination_folder as default workingspace
    env.workspace = destination_folder
    
    #For loop over shapefiles Clipping them
    for fc in featureclasses:
        output = destination_folder +"/" + fc + ".shp"
        ap.Clip_analysis(fc, clip_feature, output )
        ap.AddMessage("Feature " + fc + " Done" )


if __name__ == '__main__':
    # Retrieve input parameter values and run main.
    #Setting Parameter 0 as default workspace
    env.workspace = ap.GetParameterAsText(0)
    clip_feature = ap.GetParameterAsText(1)
    """
    WildCards
    The feature type to limit the results returned by the wild card argument. 
    Valid feature types are:
    Annotation —Only annotation feature classes are returned.
    Arc —Only arc (or line) feature classes are returned.
    Dimension —Only dimension feature classes are returned.
    Edge —Only edge feature classes are returned.
    Junction —Only junction feature classes are returned.
    Label — Only label feature classes are returned.
    Line —Only line (or arc) feature classes are returned.
    Multipatch —Only multipatch feature classes are returned.
    Node —Only node feature classes are returned.
    Point —Only point feature classes are returned.
    Polygon —Only polygon feature classes are returned.
    Polyline —Only line (or arc) feature classes are returned.
    Region —Only region feature classes are returned.
    Route —Only route feature classes are returned.
    Tic —Only tic feature classes are returned.
    All — All datasets in the workspace. This is the default value.
    (The default value is All)
    """
    wildcard = ap.GetParameterAsText(2)
    destinatio_folder = ap.GetParameterAsText(3)
    #Loading list of files form workspace
    featureclasses = ap.ListListFeatureClasses(wildcard)
    clipAll(featureclasses, clip_feature, destination_folder)
