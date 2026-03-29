def reverse_lookup(data,target):
    results=[]
    for k,v in data.items():
        if v==target:
            results.append(k)
    return results
my_dict={"dileep":"53","siva":"04","viswa":"89" }
print(reverse_lookup(my_dict,"89"))
