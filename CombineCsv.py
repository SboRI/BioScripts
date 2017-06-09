import glob
import pandas


def read_Csv(pathname):
    with open(pathname, 'r') as csvfile:
        return pandas.read_csv(csvfile, delimiter=csvDelimiter, decimal=decimalDelimiter_source)

pathnames = glob.glob("./*.sample.Raw.csv")

csvDelimiter = ";"
decimalDelimiter_source=','
decimalDelimiter_dest='.'



csv_files_with_pathnames = [(read_Csv(pathname), pathname)
                            for pathname in pathnames]


for csv, pathname in csv_files_with_pathnames:
    csv.columns = pandas.MultiIndex.from_tuples(list(zip((pathname, ''), csv.columns)))
    #print(csv.columns)

#print("merge file name?")
dest_file = 'mergedResults.csv'

merged = pandas.concat([csv for csv, pathname in csv_files_with_pathnames], axis=1)
merged.to_csv(dest_file, sep=csvDelimiter,decimal=decimalDelimiter_dest)
