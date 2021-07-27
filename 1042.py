x,y,z = input().split()

x = int(x)
y = int(y)
z = int(z)


if x > y and x > z and y > z:
    print('{}\n{}\n{}\n'.format(z,y,x))
    print('{}\n{}\n{}'.format(x,y,z))
if x > y and x > z and y < z:
    print('{}\n{}\n{}\n'.format(y,z,x))
    print('{}\n{}\n{}'.format(x,y,z))
if y > x and y > z and x > z:
    print('{}\n{}\n{}\n'.format(z,x,y))
    print('{}\n{}\n{}'.format(x,y,z))   
if y > x and y > z and x < z:
    print('{}\n{}\n{}\n'.format(x,z,y))
    print('{}\n{}\n{}'.format(x,y,z))   
if z > x and z > y and y > x:
    print('{}\n{}\n{}\n'.format(x,y,z))
    print('{}\n{}\n{}'.format(x,y,z))
if z > x and z > y and y < x:
    print('{}\n{}\n{}\n'.format(y,x,z))
    print('{}\n{}\n{}'.format(x,y,z))