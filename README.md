# Euclidean-Mahalanobis-Distance-Classifier
Classifies object type on the map, by analyzing 4 spectral satellite images


# Input
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/1.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/2.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/3.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/4.png)



# Output
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/classified.jpg)





# Based on this scientific work
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-1.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-2.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-3.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-4.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-5.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-6.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-7.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-8.png)
![alt text](https://github.com/sinevmaxim/Euclidean-Mahalanobis-Distance-Classifier/blob/main/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F%2C%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B8%CC%86%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-9.png)
