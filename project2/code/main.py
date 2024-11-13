# import necessary package
import numpy as np
import os
import rasterio
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn import svm
from sklearn.metrics import accuracy_score
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV 

"""
This script performs classification on Sentinel-2 satellite imagery between 2020 and 2021, using ground truth data from ESA.

Steps:
1. Load Sentinel-2 data and ground truth TIFF files using `rasterio`.
2. Organize the four images into a dictionary, ensuring that each image’s third dimension represents its bands (through transposing).
3. Reshape each image to a 2D format for easier processing.
4. Check each image for NaN values to ensure data integrity.
5. Normalize the Sentinel data (ground truth data does not require normalization as it contains class IDs).
6. Calculate IDE and apply feature extraction followed by Principal Component Analysis (PCA) on the Sentinel data.
7. Apply classification using Support Vector Machine (SVM) and K-Nearest Neighbors (KNN).
8. For both classifiers, compute and compare accuracy scores and confusion matrices.
9. Visualize the ground truth, Sentinel-2 data, KNN classification, and SVM classification for result comparison.

"""


# # load tiff file by raster io
def load_tiffile(file_name):
    """_load tiff files_

    Args:
        file_name : the name of.tif file

    Returns:
        images and metadata of tif files
    """
    with rasterio.open(file_name) as src:
        # read all bands
        data = src.read()
        # get metadata
        profile = src.profile
        return data , profile


# create process class for preprocessing and classification
class process:
    def __init__(self,*,dictionary: dict,label: dict):
        """_initialization of class_

        Args:
            dictionary (_dict_): first input that is a dictionary of images 
            label (_dict_): second input that is a label of ground truth data
        """
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.label = label
        d,self.h,self.w = np.shape(self.dictionary[self.keys[1]])
        
        # create list of labels from the GT_2's value that use in confusion matrix
        listlabel = list(np.unique(self.dictionary[self.keys[1]]))
        labels = []
        for item in listlabel:
            label = self.label[item]
            labels.append(label)
        self.labels = labels

    def transpose(self) -> dict:
        """_transposing the shape of array_

        Returns:
            _dict_ : _transposing the shape of each image in dictionary
        """
        for item in self.keys:
            self.dictionary[item] = self.dictionary[item].transpose(2,1,0)
        return self.dictionary

    # reshape each data from 3D to 2D
    def reshape(self) -> dict:
        """_reshape array to 2D_

        Returns:
            _dict_: _reshape each array in dictioanry and then return it_
        """
        for item in self.keys:
            h = np.shape(self.dictionary[item])[0]
            w = np.shape(self.dictionary[item])[1]
            d = np.shape(self.dictionary[item])[2]
            self.dictionary[item] = self.dictionary[item].reshape(h*w,d)
        return self.dictionary

    # search for nan value in each data
    def nan_data(self):
        for item in self.keys:
            nan_mask = np.isnan(self.dictionary[item])
            sum_nan = np.sum(nan_mask)
            # print(f"there are {sum_nan} nan values in {item}")

    # apply normalization on sentinel images
    def normalization(self) -> dict:
        """_normalize train and test data for classification_

        Returns:
            _dict_: _normalize data by standard scaler and then return normalized dictionary_
        """
        for i in [2,3]:
            scaler = StandardScaler().fit(self.dictionary[self.keys[i]])
            self.dictionary[self.keys[i]]=scaler.transform((self.dictionary[self.keys[i]]))
        return self.dictionary 
    
    # find IDE by variance from PCA feature extraction that apply on sentinel images
    def ide(self) -> int:

        """_find IDE_

        Returns:
            _int_: _returns IDE for feature extraction sentinel images by pca_
        """
        d = np.shape(self.dictionary[self.keys[2]])[1]

        # apply pca on sentinel image just for finding ide
        pca = PCA(n_components=d)
        data = pca.fit_transform(self.dictionary[self.keys[2]])
        variance = pca.explained_variance_ratio_

        for i in range(len(variance)-1):
            if abs(variance[i+1] - variance[i]) < 0.001:
                self.ide = i
                break
        
        # showing the variance of each pca
        f1 = plt.figure('figure1')
        plt.plot(variance)
        plt.xlabel('IDE')
        plt.ylabel('variance')
        plt.text(0,0, f"IDE = {self.ide} ", fontsize=10, color='red')
        # plt.show()
        return self.ide
    
    # apply pca on sentinel data that number of components = ide and save it to dictionary
    def pca(self) -> dict:
        pca = PCA(n_components=self.ide)
        for i in [2,3]:
            self.dictionary[self.keys[i]] = pca.fit_transform(self.dictionary[self.keys[i]])
        return self.dictionary

    # create svc model for classification of imbalance data
    def svc(self):
        # flattening the groundtruth
        GT_1 = np.ravel(self.dictionary[self.keys[0]])
        GT_2 = np.ravel(self.dictionary[self.keys[1]])
        
        # use gridsearch for finding best parameters

        # c_g = np.logspace(-2,2,num = 4, base =2)
        # param_grid = {'C':c_g, 'gamma':c_g, 'kernel':['rbf']}
        # svc = GridSearchCV(svm.SVC(), param_grid, refit = True, verbose = 3, cv =2)
        # # train model by GT_1
        # model = svc.fit(self.dictionary[self.keys[2]],GT_1)

        # # find best parameter
        # best_param = model.best_params_
        # c = best_param['C']
        # g = best_param['gamma']
        c = 2
        g =0.5

        # tune the model by best parameter
        svc = svm.SVC(kernel='rbf', C=c, gamma=g)
        model = svc.fit(self.dictionary[self.keys[2]],GT_1)

        # predicted the sentinel_2 part2 from this model
        data_predict = model.predict(self.dictionary[self.keys[3]])
        data_predict_train = model.predict(self.dictionary[self.keys[2]])

        print('data predict' , np.unique(data_predict, return_counts=True))

        # evaluate svc for train and validation and compute accuracy
        accuracy_validation = accuracy_score(GT_2, data_predict)
        print(f"the validation accuracy of classification by rbf kernel in svc = \n {accuracy_validation *100 :.2f}")

        accuracy_train = accuracy_score(GT_1, data_predict_train)
        print(f"the train accuracy of classification by rbf kernel in svc = \n {accuracy_train *100 :.2f}")
        
        
        # compute confusion matrix for validation data
        cm = confusion_matrix(GT_2, data_predict, normalize='true')

        # # show confusion matrix of validation data
        f2 = plt.figure('figure2')
        sns.heatmap(cm, annot=True, cmap="Blues", xticklabels=self.labels, yticklabels=self.labels)
        plt.xlabel('predicted labels')
        plt.ylabel('acctual labels')
        plt.title("confusion matrix for svc classification")
        plt.tight_layout()
        plt.show()

        self.predict_svc = data_predict
        return self.predict_svc

    # create KNN model for calssification
    def KNN(self):
        k = 9
        # flattening the groundtruth
        GT_1 = np.ravel(self.dictionary[self.keys[0]])
        GT_2 = np.ravel(self.dictionary[self.keys[1]])

        knn = KNeighborsClassifier(n_neighbors=k , metric = 'euclidean' , weights="distance")
        # train model by GT_1
        model = knn.fit(self.dictionary[self.keys[2]],GT_1)
        # predict the calss of sentinel-2part2 
        data_predict = model.predict(self.dictionary[self.keys[3]])
        train_predict = model.predict(self.dictionary[self.keys[2]])
        print('number of class in predicted data by knn ', np.unique(data_predict,return_counts=True))
        
        # evaluate the knn classifier for train data and validation by accuracy
        accuracy_validation = accuracy_score(GT_2, data_predict)
        print(f"the validation accuracy of classification by KNN = {accuracy_validation *100:.2f}")

        accuracy_train = accuracy_score(GT_1, train_predict)
        print(f"the train accuracy of classification by KNN = {accuracy_train *100:.2f}")

        # compute confusion matrix for validation data
        cm = confusion_matrix(GT_2, data_predict)

        # # show confusion matrix of validation data
        f3 = plt.figure('figure3')
        sns.heatmap(cm, annot=True, cmap="Blues", xticklabels=self.labels, yticklabels=self.labels)
        plt.xlabel('predicted labels')
        plt.ylabel('acctual labels')
        plt.title("confusion matrix for KNN classification")
        plt.tight_layout()
        plt.show()

        self.predict_knn = data_predict

        return self.predict_knn
    
    def visualize(self):
        """_display model and groundtruth_

        Returns:
            _subplot_: _this function display a train sentinel data and ground truth and the result of KNN and SVC in each subplot_
        """
        
        f4 = plt.figure('figure4')
        result_data = {}
        # reshape groundtruth and predicted data for displaying
        GrTruthound = self.dictionary[self.keys[1]]
        GT = GrTruthound.reshape(self.h,self.w)
        knn_predict = self.predict_knn.reshape(self.h,self.w)
        svc_predict = self.predict_svc.reshape(self.h,self.w)
        sentinel2 = self.dictionary[self.keys[3]].reshape(self.h,self.w,self.ide)

        result_data['GT'] = GT
        result_data['KNN'] = knn_predict
        result_data['svc'] = svc_predict
        result_data['sentinel2'] = sentinel2
        label_title = list(result_data.keys())

        for i in range(4):
            if i == 3:
                plt.subplot(2,2,4)
                data_rgb = sentinel2[:,:,[0,1,2]]
                data_rgb = (data_rgb - data_rgb.min()) / (data_rgb.max() - data_rgb.min())
                plt.imshow(data_rgb)
                plt.title(label_title[3])
            
            else:
                plt.subplot(2,2,i+1)
                plt.imshow(result_data[label_title[i]])
                plt.title(label_title[i])
                plt.legend(self.labels, loc="upper left")
            plt.show()

    # write main method for calling othe method of class
    def main(self) -> dict:
        self.transpose()
        self.nan_data()
        self.reshape()
        self.ide()
        self.normalization()
        data = self.pca()
        self.svc()
        self.KNN()
        self.visualize()
        return data 

# Get the directory of the script (where main.py is located)
dir = os.path.dirname(__file__)
# create name list of images
filenames = ['GT_1.tif','GT_2.tif','sentinel-2_part1.tif', 'sentinel-2_part2.tif']
# define label of classes
labels = {10: 'tree',20:'Shrubland', 30:'Grassland',40:'Cropland', 50: 'Built-up',
        60: 'Bare', 70:'Snow and ice', 80:'Permanent water bodies' ,
        90: 'Herbaceous wetland' , 95: 'Mangroves', 100: 'Moss and lichen'}

# create dictionary for raster data
raster_data = {}
# create dictionary for metadata of each images
metadata ={}
for i in range(len(filenames)):
    filepath = os.path.join(dir,"..","image",filenames[i])
    key = os.path.splitext(filenames[i])[0]
    raster_data[key], metadata[key]= load_tiffile(filepath)
 

# create an object from process class
processing = process(dictionary = raster_data,label =labels)
# accessing class method
processed_data = processing.main()




