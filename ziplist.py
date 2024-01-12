a=[1,2,3]
b=["a","b","c"]
c=["x","y","z"]
result=zip(a,b,c)
zipped_list=list(result)
print(zipped_list)
unzipped_list=zip(*zipped_list)
unzipped_result=[list(item) for item in unzipped_list]
print(unzipped_result)