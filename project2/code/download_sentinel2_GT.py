# install necessary package
!pip install earthengine-api

# import google earth engine in colab
import ee
# Authenticate and initialize earth engine in colab
ee.Authenticate()
ee.Initialize(project = 'ee-monashahriari1378')

# # # create class for processing
class processor:
  
  def __init__(self,id,data,polygon):
    self.id= id
    self.data = data
    self.polygon = polygon

  def load_image(self):

    """_create composite of sentinel2 collection_

      Returns:
          _image_: _this method get the ID of sentinel2 collection and filter it by data, boundry then apply cloud mask and at the end create composite
           image by median and clip that image by polygon _
    """
    self.collection_s2 = ee.ImageCollection(self.id).filterDate(self.data['start_date'],self.data['end_date']) \
    .filterBounds(self.polygon) \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',5)) \
    .map(lambda image: self.masks2clouds(image)) \
    .select(self.data['bands']).median().clip(self.polygon)
    return self.collection_s2

  def masks2clouds(self,image):
    cloud_mask = image.select('QA60').bitwiseAnd(1 << 10).eq(0) \
                      .And(image.select('QA60').bitwiseAnd(1 << 11).eq(0))
    return image.updateMask(cloud_mask)

  def add_ndvi(self):
    """_add NDVI as band to image_

    Returns:
          _image_: _this method calculate NDVI with B5 and B4 bands then add it as ndvi band to image _
    """
    ndvi = self.collection_s2.normalizedDifference(['B5', 'B4']).rename('ndvi')
    return self.collection_s2.addBands(ndvi)

  def main(self):
    self.load_image()
    image_with_ndvi = self.add_ndvi()
    return image_with_ndvi


# export
def export(image, name):
    # Convert all bands to Float32 for consistency
    image = image.toFloat()
    task = ee.batch.Export.image.toDrive(**{
        'image' :ee.Image(image),
        'description':name,
        'folder': 'export',
        'region':image.geometry(),
        'scale': 10,
        'maxPixels': 1e13  })
    task.start()
    print(f"Export task {name} started.")
    return task

# define polygons
polygon_coord = {1:{'upper_left':[51.26,35.72] , 'upper_right':[51.26,35.75], 'lower_right':[51.22,35.75], 'lower_left': [51.22,35.72]},
                2:{'upper_left':[51.28,35.69] , 'upper_right':[51.33,35.69], 'lower_right':[51.33,35.73], 'lower_left': [51.28,35.73]}}


data = {'start_date':'2021-01-01', 'end_date': '2022-01-01', 'bands':['B2','B3','B4','B5','B6','B7','B8','B11','B12']}

def create_polygon(coords):
    return ee.Geometry.Polygon(coords)

polygon_dict = {}
for item in polygon_coord.keys():
  polygon_dict[item] = create_polygon([
    polygon_coord[item]['upper_left'],polygon_coord[item]['upper_right'],
    polygon_coord[item]['lower_right'],polygon_coord[item]['lower_left']
    ])

# load GT data
GT = ee.Image('ESA/WorldCover/v200/2021')

# clip ground truth based on each polygon
GT_dic = {}
for item in polygon_dict.keys():
  GT_dic[item] = GT.clip(polygon_dict[item])

images = []
for item in polygon_dict.keys():
  process = processor("COPERNICUS/S2_SR_HARMONIZED",data,polygon_dict[item])
  images.append(process.main())


for item in GT_dic:
  images.append(GT_dic[item])

names = ['sentinel-2_part1', 'sentinel-2_part2','GT_1', 'GT_2' ]

# # # Batch export each image with the specified name
for i in range(len(names)):
    export(images[i], names[i])

