## Geodesignhub compatible Landuse Allocation Model
A demand-based, evaluation-weighted, geodesign designated land use allocation model

### Overview
This repository is a simple demand based evaluation weighted land use allocation model. It takes in a gridded evaluation geojson file and features for "urban" type landuses from Geodesignhub and allocates them based on a priority and also target (in acres or hectares) allocation. 

#### Pseudocode logic
- Iterate over all features / polygons of a evaluation map
  - Check if it is Red, Yellow, Green or Green2 or Green3 and store it in a rtree spatial index. For more information about what these are please refer to [this link](https://community.geodesignhub.com/t/making-evaluation-maps/62).
  - Store the id, polygon area and areatype classification of the evaluation layer.
- Sort the stored ids for each evaluation map grouped by the color (for performance)
- Get designed features from Geodesignhub using the API (synthesis is provided)
- Start with the first priority evaluation and first priority system. (based on the decision model)
- Start with Green2 (most feasable) location in the evaluation map. 
- Intersect the current feature with the evaluation, allocate if intersected
  - If not intersected move to the next designed feature or evaluation feature
- Contintue to the next most suitable (green) and next most capable (yello) till either there are no more features or target reached. Do not allocate on red features.


### Prerequisites
Install all dependencies on your computer (Rree and Shapely) in a Python3 environment
```
pip install -r requirements.txt
```
This should install Shapely and RTree and requests and a few other libraries. For Windows users please download binaries of the Shapely and RTree libraries from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/).

### Usage
Setup the evaluation maps, edit the config file with your paths, Geodesign Hub API key, project and change team name and inputs and then run the following command:

```python
python GDHAllocationModel.py
```

### Inputs
There is one input for this script both configured through config.py
- Gridded evaluation files (see below)
- The script uses the Geodesignhub [API](http://www.geodesignsupport.com/kb/get-methods/) to download the input features. Please configure the System ID correctly. 

### Outputs
In the output directory, the script will produce a allocated output for each of the systems based on the targets setup in the config file. For the moment, you can ignore the allocation type option. The output will be produced in GeoJSON and in EPSG 4326 projection. It can be uploaded back to Geodesign Hub automatically.

#### Creating gridded Evaluation GeoJSON
For the purposes of allocation the evaluation GeoJSON files built for Geodesignhub systems need to be split into a tiny grid. This can be done in a regular GIS software. The grid size should depend on the kind of area that you are studying. Following are the steps: 

1. Create a raster of the area from your vector maps, with resolution of 250 m and with all the cells with the same color (grid value);
2. Convert from raster to points;
3. Apply "Create Thiessen Polygons" using the value of the grid that are all the same. It works like Delaunay distributions and constructs regular quadrangular grids, as all the points have the same value and are distributed in regular grid composed by squares.
4. Cut the boundaries with the shape of the limit, and delete the polygons from the boundary that don't have the same area of the internal ones;
5. Using the points created in step 2, "extract values to points" from each raster of the evaluation maps. Use the same file of points, to make sure the points will always be in the same place. Observe you have to change the name of the column it creates because each time you extract the values from a raster, it creates a column with the same name, if it already exists can be a problem.
6. At this point all the values existing in the evaluation maps will be on columns in the table linked to the points. These values must go to the regular grid shape, composed by cells/squares. In the shape of regular grid squares do: “Join by Spatial Location” – to connect the values from the points to the regular grid composed by squares. Chose “Each polygon will be given all the attributes of the point that is closest to its boundary…”

Thank you to [Prof. Ana Clara Moura](http://geoproea.arq.ufmg.br/equipe/prof-ana-clara-mourao-moura) for these instructions. 

#### Update config.py
Config.py has a sample configuration, modify it for your purposes. 

#### Video tutorial
[![YouTube Video tutorial](http://i.imgur.com/3KNhYft.png)](https://www.youtube.com/watch?v=QFbOM5T2eQQ)

#### LICENSE
The MIT License (MIT)

Copyright (c) 2016 Hrishikesh Ballal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
