
# coding: utf-8
# learning files and pandas
# Author Vee

#imports
import pandas

#get the file path
csv="files/sample.sql"

# read the file
print(pandas.read_csv(csv,sep='delimiter',error_bad_lines=False, engine='python'))

