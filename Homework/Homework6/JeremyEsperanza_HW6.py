#Jeremy Esperanza
from functools import reduce
#even or odd lambda
evenOdd = lambda a: "odd" if a % 2 > 0 else "even"

print(evenOdd(4))
print(evenOdd(7))
print(evenOdd(3471847139))

#lambda list sum
examplelist1 = [3, 1, 2, 4]
examplelist2 = [4, 8, 6, 2]
listsum = lambda b: sum(b)

print(listsum(examplelist1))
print(listsum(examplelist2))

#lambda sorting
listsort = lambda c: sorted(c)

print(listsort(examplelist1))
print(listsort(examplelist2))

#lambda filtering
examplelist3 = [1, 2, 3, 4, 5, 6]
listfilter = lambda d: filter(evenOdd, d)

print(listfilter(examplelist3))

#lambda mapping
listmapstr = lambda z: map(str, z)

print(listmapstr(examplelist3))

#lambda reduce
red = lambda g: reduce(evenOdd, g)

#print(red(examplelist3))

#lambda enumerate
enumer = lambda f: enumerate(f, 0)

print(enumer(examplelist3))

#lambda zip
ex3 = [1,2,3]
ex4 = ["a", "b", "c"]
zipper = lambda q, w: zip(q,w)

print(zipper(ex3,ex4))