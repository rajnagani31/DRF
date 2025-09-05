from httpresponse import Http

nums =[1,2,3,4]

n =5
print(n * (n+1)//2 - sum(nums))
print(n * (n+1)//2)
print(sum(nums))

A = ord('A')
B= ord('B')
a= ord('a')
b= ord('b')

print(f"A:{A} B:{B} a:{a} b:{b}")

def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse('apple'))

print(3 * ord('a'))


# toggel

value = [1,0,0,1,1,0,1,0,1]
v1=[]
for v in value:
    # v = not v
    # print(bool(v))
    # v1.append(v)

    if v == 0:
        v =1
        # v1.append(v)
    else:
        v =0
    v1.append(v)
            

print(v1)    

a= ord('A')
z =ord('Z')
for i in range(a,z):
    print((i))


def request():
    return Http