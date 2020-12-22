fin = open('input', 'r')
box = 0
ribbon = 0
f = fin.readlines()
for dimension in f:
    l, b, h = map(int, dimension.split('x'))
    
    smallest = min([l*b, b*h, h*l])
    
    box += 2 * (l*b + b*h + h*l) + smallest
    
    #PART 2
    smallest_peri = 2 * min([l+b, b+h, h+l])
    ribbon += l * b * h + smallest_peri
print(box)
print(ribbon)
