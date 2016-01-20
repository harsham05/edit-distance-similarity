
## Edit Distance Similarity based on Metadata Values


### Dependencies

```
    pip install editdistance
```

### Usage

```
Usage: edit-value-similarity.py [-h] --inputDir INPUTDIR --outCSV OUTCSV [--accept [png pdf etc...]]

--inputDir INPUTDIR  path to directory containing files

--outCSV OUTCSV      path to directory for storing the output CSV File, containing pair-wise Similarity Scores based on edit distance

--accept [ACCEPT]    Optional: compute similarity only on specified IANA MIME Type(s)

```

```
Eg: python edit-value-similarity.py --inputDir /path/to/files --outCSV /path/to/output.csv --accept png pdf gif

```

**Similarity Score of 1 implies an identical pair of documents**


### License

This project is licensed under the [Apache License, version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
