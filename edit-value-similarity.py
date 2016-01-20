from tika import parser
import os, editdistance, itertools, argparse, csv

def stringify(attribute_value):
    if isinstance(attribute_value, list):
        return str((", ".join(attribute_value)).encode('utf-8').strip())
    else:
        return str(attribute_value.encode('utf-8').strip())


if __name__ == "__main__":

    na_metadata = ["resourceName"]
    argParser = argparse.ArgumentParser('Edit Distance Similarity based on Metadata values')
    argParser.add_argument('--inputDir', required=True, help='path to directory containing files')
    argParser.add_argument('--outCSV', required=True, help='path to directory for storing the output CSV File, containing pair-wise Similarity Scores based on edit distance')
    argParser.add_argument('--accept', nargs='+', type=str, help='Optional: compute similarity only on specified IANA MIME Type(s)')
    args = argParser.parse_args()

    if args.inputDir and args.outCSV:
        with open(args.outCSV, "wb") as outF:
            a = csv.writer(outF, delimiter=',')
            a.writerow(["x-coordinate","y-coordinate","Similarity_score"])

            filename_list = []

            for root, dirnames, files in os.walk(args.inputDir):
                dirnames[:] = [d for d in dirnames if not d.startswith('.')]
                for filename in files:
                    if not filename.startswith('.'):
                        filename_list.append(os.path.join(root, filename))

            filename_list = [filename for filename in filename_list if parser.from_file(filename)]       #print "Debug, total files in directory", len(filename_list)
            if args.accept:                
                filename_list = [filename for filename in filename_list if str(parser.from_file(filename)['metadata']['Content-Type'].encode('utf-8')).split('/')[-1] in args.accept]
            else:
                print "Accepting all MIME Types....."
 
            files_tuple = itertools.combinations(filename_list, 2)
            for file1, file2 in files_tuple:

                row_edit_distance = []
                row_edit_distance.append(file1)
                row_edit_distance.append(file2)

                file1_parsedData = parser.from_file(file1)
                file2_parsedData = parser.from_file(file2)
        
                intersect_features = set(file1_parsedData["metadata"].keys()) & set(file2_parsedData["metadata"].keys())
                intersect_features = [feature for feature in intersect_features if feature not in na_metadata ]

                file_edit_distance = 0.0
                for feature in intersect_features:

                    file1_feature_value = stringify(file1_parsedData["metadata"][feature])
                    file2_feature_value = stringify(file2_parsedData["metadata"][feature])

                    #print feature                print file1_feature_value                    print file2_feature_value
                                  
                    feature_distance = float(editdistance.eval(file1_feature_value, file2_feature_value))/(len(file1_feature_value) if len(file1_feature_value) > len(file2_feature_value) else len(file2_feature_value))
                    #print feature_distance, "\n\n"

                    file_edit_distance += feature_distance

                file_edit_distance /= float(len(intersect_features))    #average edit distance

                row_edit_distance.append(1-file_edit_distance)
                a.writerow(row_edit_distance)