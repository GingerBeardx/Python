def stars(arr):
    for each in arr:
        string = ""
        count = 0
        if isinstance(each, basestring) == True:
            while count < len(each):
                string += each[0].lower()
                count += 1
        else:
            while count < each:
                string += "*"
                count += 1
        print string


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(x)
