from tika import parser
from pprint import pprint
import os, editdistance, itertools, argparse

def stringify(attribute_value):
    if isinstance(attribute_value, list):
        return str((", ".join(attribute_value)).encode('utf-8').strip())
    else:
        return str(attribute_value.encode('utf-8').strip())


if __name__ == "__main__":

    na_metadata = ["resourceName"]
    argParser = argparse.ArgumentParser('Edit Distance Similarity based on Metadata values')
    argParser.add_argument('--inputDir', required=True, help='path to directory containing files')
    #argParser.add_argument('--outFile', required=True, help='path to directory for storing the output CSV File')
    args = argParser.parse_args()

    if args.inputDir:# and args.outFile:

        #with open(args.outFile, "wb") as outF:
        # a = csv.writer(delimiter=',')

        filename_list = []

        for root, dirnames, files in os.walk(args.inputDir):
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for filename in files:
                if not filename.startswith('.'):
                    filename_list.append(os.path.join(root, filename))

        filename_list = [filename for filename in filename_list if parser.from_file(filename)]       #print "Debug, total files in directory", len(filename_list)

        files_tuple = itertools.combinations(filename_list, 2)
        for file1, file2 in files_tuple:
            
            print file1, file2
            file1_parsedData = parser.from_file(file1)
            file2_parsedData = parser.from_file(file2)
    

            intersect_features = set(file1_parsedData["metadata"].keys()) & set(file2_parsedData["metadata"].keys())
    
            intersect_features = [feature for feature in intersect_features if feature not in na_metadata ]
    
            print len(intersect_features)

            file_edit_distance = 0.0

            for feature in intersect_features:

                file1_feature_value = stringify(file1_parsedData["metadata"][feature])
                file2_feature_value = stringify(file2_parsedData["metadata"][feature])

                print feature
                print file1_feature_value
                print file2_feature_value
                              
                feature_distance = float(editdistance.eval(file1_feature_value, file2_feature_value))/(len(file1_feature_value) if len(file1_feature_value) > len(file2_feature_value) else len(file2_feature_value))
                print feature_distance, "\n\n"

                file_edit_distance += feature_distance

            file_edit_distance /= float(len(intersect_features))

            print "File edit distance metric", (1-file_edit_distance)
        
            
            break
                
        
    
    
            




        



        


             
        
            
        