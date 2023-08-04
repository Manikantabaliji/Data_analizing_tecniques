import csv

with open('sample.csv','r') as csvfile:
    reader=csv.DictReader(csvfile)
    # rows=1
    # for row in reader:
    #     if rows==101:
    #         break
    #     else:
    #         print(row)
    #     rows+=rows
    # print(reader.fieldnames)

    year_list=[row for row in reader if row["industry_name_ANZSIC"]=="Agriculture, Forestry and Fishing"]
    # print(len(year_list))
    # for l in year_list:
    #     print(l["industry_name_ANZSIC"],"by",l["rme_size_grp"])

    def isyear(string):
        try:
            year=int(string)
        except ValueError:
            return False
        else:
            return year
    revalue=[int(row["value"]) for row in year_list if isyear(row["value"])]
    print(max(revalue))
