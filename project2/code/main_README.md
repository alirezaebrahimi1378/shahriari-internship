## **Description:**

This code performs classification on Sentinel-2 satellite imagery captured between 2020 and 2021 using ground truth data provided by ESA. It preprocesses and analyzes the data, applies dimensionality reduction using PCA, and performs classification using Support Vector Machines (SVM) and K-Nearest Neighbors (KNN). Additionally, it computes metrics like accuracy and confusion matrices to evaluate the models and visualizes the classification results.


>## **load_tiffile function**

The **load_tiffile** function reads Sentinel-2 and ESA images and stored in GeoTIFF format after that extracts data and metadata.

- **How the function works**:

    - Opens a TIFF file using **rasterio**
    - Reads all bands and captures metadata 
    - Returns the image data and associated metadata.

    Example:
    ````python
    dir = os.path.dirname(__file__)
    filepath = os.path.join(dir,"..","image","GT_1.tif")
    raster_data, metadata= load_tiffile(filepath)
    ````

## **class Process**

The **process** class manages the preprocessing and classification tasks for Sentinel-2 imagery.

**Methods**

1. **__init__**
    (self,*,dictionary,label)

    Initializes the **Process** with Sentinel-2 imagery data and ground truth labels.

    - **parameters**:
        - `dictionary`(dict): Contains Sentinel-2 and ESA images.
        - `label` (dict): Maps ground truth classes to their respective labels.


2. **transpose**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Transposes the image data to ensure that the third dimension represents the bands.

        Returns: Updated dictionary with transposed arrays.


3. **reshape**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Reshapes 3D arrays into 2D arrays for easier processing.

        Returns: Dictionary with reshaped data.
    

4. **nan_data**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Checks for NaN values in the imagery data and reports the count.

        Returns: None


5. **normalization**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Normalizes Sentinel-2 images using **StandardScaler** for consistent feature scaling.

        Returns: Dictionary with normalized data.


6. **ide**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Computes the intrinsic dimensionality estimate (IDE) by analyzing PCA variance.

        Visualization: Plots variance explained by PCA components.

        Returns: The calculated IDE value.

7. **pca**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Reduces data dimensions based on the computed IDE using PCA.

        Returns: Dictionary with reduced data.


8. **svc**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Classifies the data using a Support Vector Classifier with hyperparameter optimization **(GridSearchCV)**. calculates Validation/train accuracy, confusion matrix, and computes processing time.

        Returns: Predicted classifications for test data.


9. **KNN**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Classifies the data using K-Nearest Neighbors with **k=9**. calculates Validation/train accuracy and confusion matrix.

        Returns: Predicted classifications for test data.


10. **visualize**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - Displays side-by-side visualizations of ground truth, Sentinel-2 images, and classification results from SVM and KNN.


11. **main**

    - **Parameters**:
        This method does not take any parameters directly but relies on the class attributes.

    - **How the function works**:

        - The **main** method orchestrates the preprocessing, feature extraction, classification, and visualization steps for analyzing and classifying Sentinel-2 satellite imagery. It serves as the entry point for executing the code.

        Destail Steps:

        1. **Transpose Data:**

            - Calls the **transpose** method to reorient the data. This ensures that the third dimension represents the bands.

        2. **Handle Missing Values:**

            - Calls the **nan_data** method to detect and handle missing values (e.g., NaN) in the dataset.

        3. **Reshape Data:**

            - Calls the **reshape** method to Reshapes 3D arrays into 2D arrays.

        4. **find IDE:**

            - Calls the **ide** method to Computes the intrinsic dimensionality estimate (IDE) by analyzing PCA variance.

        5. **normalization:**

            - Calls the **normalization** method to scale the data, ensuring all features are on a comparable scale.

        6. **Dimensionality Reduction:**

            - Calls the **pca** method to reduce the dataset's dimensionality using Principal Component Analysis. This step improves computational efficiency and highlights important features.

        7. **Support Vector Classification:**

            - Calls the **svc** method to classify the processed data using a Support Vector Machine (SVM) model.

        8. **K-Nearest Neighbors Classification:**

            - Calls the **KNN** method to classify the data using the KNN algorithm, providing a comparison to the SVM model.

        9. **Visualization:**

            - Calls the **visualize** method to create graphical representations of the classification results.

        Example:
        
        ````python
        processing = process(dictionary = raster_data,label =labels)
        processed_data = processing.main()
        ````


## **Usage**

To run the code:
- Make sure to provide the correct path as the filepath.
- Ensure you have the required dependencies installed by running the following command:
    
Example:

````python
pip install -r requirements.txt
````
- Load Sentinel-2 and ground truth data
