list=["apples","oranges","bananas","lemons","pineapples"]

if len(list)>1:
    for i in range (len(list)-1):
      list[i]=f"{list[i]},"
    list[-1]=f"and {list[-1]}"
print(' '.join(list))