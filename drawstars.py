x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars_and_char(list_a):
    for i in list_a:
        new_str = ""
        if isinstance(i, int):
            for char in range (i):
                new_str += "*"
        elif isinstance(i, str):
            for char in range( len(i)):
                new_str += i[0].lower()
        print new_str

draw_stars_and_char(x)

print "...end of draw_stars_and_char...."
x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(arr):
    for i in arr:
        num = ""
        for char in range(0, i):
            num += "*"
        print num

draw_stars(x)
