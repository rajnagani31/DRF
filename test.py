
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

class Person:
    def __init__(self, age):
        self.age = age

person = Person('23')

# Safe check before accessing
if hasattr(person, 'age'):
    print(person.age)
else:
    print("Age not set")


def maltiplay(num):
    if not isinstance(num, int):
        return "Please enter a valid number"
    return num * num

print("num",maltiplay(5.3))


class Person:
    def __init__(self, name):
        self.name = name

class Plugin:
    def process(self): 
        print("Processing data...")

class AdvancedPlugin(Plugin):
    def initialize(self):
        print("Plugin initialized!")
    
    def cleanup(self):
        print("Cleaning up resources...")
    
    def process(self):
        print("Advanced processing...")

class BasicPlugin(Plugin):
    def process(self):
        print("Basic processing...")

# Cleanup registry
cleanup_functions = []

def register_cleanup(func):
    cleanup_functions.append(func)

def load_plugin(plugin):
    if hasattr(plugin, 'initialize'):
        plugin.initialize()
        print('1')
    
    if hasattr(plugin, 'cleanup'):
        register_cleanup(plugin.cleanup)
        print('2')

    plugin.process()
    print('3')

# Test with different plugins
print("Loading AdvancedPlugin:")
advanced = AdvancedPlugin()
load_plugin(advanced)

print("\nLoading BasicPlugin:")
basic = BasicPlugin()
load_plugin(basic)

print(f"\nCleanup functions registered: {len(cleanup_functions)}")


nums = [3,2,4]
import time

n = [(i,j) for i in range(len(nums)) for j in range(i+1 , len(nums)) if nums[i] + nums[j] == 9]
print(n)
print(list(n))

