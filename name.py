import sys

# # print("hello, my name is", sys.argv[1])
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello ny name is ", sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv:
#     print("Hello, my name is", arg)    

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("Hello, my name is", arg)    