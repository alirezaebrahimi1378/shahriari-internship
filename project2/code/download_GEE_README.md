## **Description:**

This code processes Sentinel-2 satellite imagery and applies a cloud mask, NDVI computation, and exports the data and ESA (ground Truth) for classification processing. The code uses Google Earth Engine (GEE) in combination with Python to fetch Sentinel-2 imagery based on a specific date range and geographical bounds (polygons).


## **Class Processor**

The **Processor** class manages the entire data preprocessing workflow for Sentinel-2 imagery and ground truth data from ESA.

### **Methods:**

1. **__init__**

   Initializes the **processor** with an ID, data dictionary, and polygon for processing.
   
   - **parameters**:
     - `id` (str): The Sentinel-2 image collection ID to be processed.
     - `data` (dict): Dictionary containing the start and end date, and bands to select from the Sentinel-2 collection.
     - `polygon` (ee.Geometry.Polygon): The region of interest (ROI) to clip the data to.


2. **load_image**

    - **Parameters**:
        
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - masks2cloudsFilters the image collection based on the given date range and geographical bounds.
        - Applies a cloud mask to remove cloudy pixels using the `masks2clouds` method.
        - Creates a median composite image and clips it to the given polygon.

        Returns the composite image of Sentinel-2.


3. **masks2clouds**

    - **parameters**:

        - `image`: The Sentinel-2 image

    - **How the function works**:

        - Applies a cloud mask to Sentinel-2 images based on the 'QA60' band.

        Returns the image with the cloud mask applied.


4. **add_ndvi**

    - **parameters**:
       
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Adds an NDVI (Normalized Difference Vegetation Index) band to the image using the B5 and B4 bands.

        Returns the image with the added NDVI band.


5. **main**

    - **Parameters**:
        This method does not take any parameters directly but relies on the class attributes.

    - **How the function works**:

        - This method orchestrates the loading of Sentinel-2 images and the addition of the NDVI band by calling **load_image** and **add_ndvi**

        Destail Steps:

        1. **load sentinel data:**

            - Calls **load_image** method to create composite image of Sentinel-2 data (2021-22) that remove cloudy pixels and clipped by polygon.

        2.  **add NDVI to image:**

            - Calls **add_ndvi** to create NDVI from B4 and B5 bands and add it to image as **ndvi** band

        Example:
        
        ````python
        process = processor("COPERNICUS/S2_SR_HARMONIZED",data,polygon_dict)
        processed_data = process.main()
        ````


## **export function**

The **export** function export processed imagery as GeoTIFF files to Google Drive.

- **Parameters**:
    - `image` (ee.Image): The image to export.
    - `name` (str): The name of the exported file.

- **How the function works**:

    - starts an export task and saves the image with the specified name to a folder in Google Drive.

    Example:
        
    ````python
    export(processed_image, 'sentinel_image')
    ````

## **Usage**

To run the code:
- Ensure you have the required dependencies installed:

Example:

````python
pip install earthengine-api
````
- You haveto define polygons and a date range for filtering the Sentinel-2 imagery

Example:

````python
data = {'start_date': '2021-01-01', 'end_date': '2022-01-01', 'bands': ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B11', 'B12']}
````
