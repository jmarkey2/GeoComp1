"""
This program solves a regular task of mine: creating a basemap of New York City to put data on top of. 
The code is both specific to NYC and, hopefully, easily adaptable to other locations. 
"""

import arcpy
import os

rootpath = r'C:\Users\jakem\OneDrive\Desktop\GIS\Data\NYCBasemap\Shapefiles'
layers = ['BoroughOutline.shp', 'PARK.shp', 'OPEN_SPACE_NO_PARK.shp', 'HYDROGRAPHY.shp','StreetsCenterline.shp']

#The following appearance_settings variable stores colors as RGB tuples and the desired line weight for each layer
appearance_settings = {
    'BoroughOutline': ([202,202,202, 100], None),
    'PARK': ([198, 226, 178, 100], 0),
    'OPEN_SPACE_NO_PARK': ([198, 226, 178, 100], 0),
    'HYDROGRAPHY': ([190,210,255,100], 0),
    'StreetsCenterline': ([255, 255, 255, 100], .5)
}


# Get the current ArcGIS project
aprx = arcpy.mp.ArcGISProject("CURRENT")
    
# Get the active map
active_map = aprx.activeMap

def add_shapefiles_to_map(folder_path, shapefile_list):
    added_layers = {}
    # Iterate through the shapefile list and add each shapefile to the active map
    for shapefile in shapefile_list:
        shapefile_path = os.path.join(folder_path, shapefile)
        added_layer = active_map.addDataFromPath(shapefile_path)
        layer_name = added_layer.name
        added_layers[layer_name] = added_layer
    return added_layers

def update_layer_appearance(layer, color_rgb, line_weight=None):
    # Get the layer's symbology
    symbology = layer.symbology

    # Get the feature class shape type
    feaure_class = layer.dataSource
    shape_type = arcpy.Describe(feaure_class).shapetype

    # Update the fill color for polygon layers
    if shape_type == 'Polygon':
        symbology.renderer.symbol.color = {'RGB': color_rgb}
        if line_weight is not None:
            symbology.renderer.symbol.size = line_weight


    # Update the line color and line weight for polyline layers
    elif shape_type == 'Polyline':
        symbology.renderer.symbol.color = {'RGB': color_rgb}
        if line_weight is not None:
            symbology.renderer.symbol.size = line_weight
   
    # Update the layer's symbology
    layer.symbology = symbology

added_layers = add_shapefiles_to_map(rootpath, layers)

for feature in appearance_settings: 
     # Check if the feature is in the added layers dictionary before updating symbology
    if feature in added_layers:
        layer_object = added_layers[feature]
        appearance_values = appearance_settings[feature]
        color = appearance_values[0]
        line = appearance_values[1]
        update_layer_appearance(layer_object, color, line)

    
