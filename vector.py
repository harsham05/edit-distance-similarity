import math

class Vector:
    '''
    An instance of this class represents a vector in n-dimensional space
    '''

    def __init__(self, vectorID, features):
        '''
        Create a vector
        @param vectorID identifier for vector 
        @param features 
        '''
        self.vectorID = vectorID
        self.dimensions = []
        self.magnitudes = []
        for dimension in features:
            self.dimensions.append(dimension)
            self.magnitudes.append(features[dimension])


    def __str__(self):
        vector_str = "( {0} ): {\n".format(self.vectorID)
        if this.dimensions and this.magnitudes:
            for i in range(0, len(dimensions)):
                vector_str += " {0}: {1} \n".format(dimensions[i], magnitudes[i])

        return vector_str+"}\n"


    def getMagnitude(self):
        totalMagnitude = 0.0
        for magnitude in magnitudes:
            totalMagnitude += magnitude ** 2
        return math.sqrt(totalMagnitude)


    def dotProduct(self, anotherVector):
        '''
        A = ax+by+cz
        B = mx+ny+oz
        A.B = a*m + b*n + c*o
        '''

        dot_product = 0.0
        intersect_features = set(self.dimensions) & set(anotherVector.dimensions)

        for feature in intersect_features:
            dot_product += self.magnitudes[feature] * anotherVector.magnitudes[feature]

        return dot_product



    def cosTheta(self, v2):
        '''
        cosTheta = (V1.V2) / (|V1| |V2|)
        cos 0 = 1 implies identical documents
        '''
        
        return self.dotProduct(v2) / (self.getMagnitude() * v2.getMagnitude())




