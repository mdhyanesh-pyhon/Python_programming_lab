import numpy
marks = [5,5,5,5]
a_m = numpy.array(marks)
print(f"{numpy.max(a_m)} heighest CGP in the class")
print(f"{numpy.min(a_m)} low CGP in the class")
print(f"{numpy.mean(a_m)} average CGP of the class")
avg = numpy.mean(a_m)
print(numpy.where(avg>5,"above average",numpy.where(avg<5,"Below average","Average")))

