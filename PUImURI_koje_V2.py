symbols = ["+", "-", "*", "/", "^", "|"]
ends = ["(", ")"]

def rearrange():
    global left
    global right
    n = -1
    while True: # rearrange equation
        if solve in left:
            left = left
            right = right
        elif solve in right:
            temp = left
            left = right
            right = temp

        if left[0] != "-" and left[0] != "+":
            left = "+" + left
        if right[0] != "-" and right[0] != "+":
            right = "+" + right
      
        if left[n] == "+":
            split_left = left[:n]
            split_right = left[n+1:]
            if solve in split_right:
                wanted = "+" + split_right
                left = split_left
            elif solve not in split_right:
                right = right + "-" + left[n+1:]
                left = split_left

            n = -1
        elif left[n] == "-":
            split_left = left[:n]
            split_right = left[n+1:]
            if solve in split_left:
                wanted = "-" + split_right
                left = split_left
            elif solve not in split_left:
                right = right + "+" + left[n+1:]
                left = split_left
            n = -1
        
        else:
            n = n - 1
        if len(left) == 0:
            left = wanted
            if left[0] == "+":
                left = left[1:]
            if right[0] == "+":
                right = right[1:]
            break

def multivision():
    global left
    global right
    global layer
    global layer_check
    global clear
    m = -1
    layer = 0
    layer_check = False
    clear = False
    while True: # divisions [ x/y ] and multiplications [ x*y ]

        if left[m] == ")": 
            layer = layer + 1
            layer_check = True # won't touch symbols inside parenthesies
        elif left[m] == "(":
            layer = layer - 1
        if layer == 0:
            layer_check = False
    
        if left[m] == "/" and layer_check == False:
            print("division")
            print(left[:m])
            print(left[m+1:])
            part1 = left[:m]
            part2 = left[m+1:]
            left = part1
            right = "(" + right + ")" + "*" + part2
            print(left + "=" + right)
            print()
            m = 0
        
        elif left[m] == "*" and layer_check == False:
            print("multiple")
            print(left[:m])
            print(left[m+1:])
            part1 = left[:m]
            part2 = left[m+1:]
            if part1[0] == "+":
                part1 = part1[1:]
            if part2[0] == "+":
                part2 = part2[1:]
        
            if solve in part1:
                left = part1
                right = "(" + right + ")" + "/" + "(" + part2 + ")"
            elif solve in part2:
                left = part2
                right = "(" + right + ")" + "/" + "(" + part1 + ")"
        
            if left[0] == "+":
                left = left[1:]
            if right[0] == "+":
                right = right[1:]
            print(left + "=" + right)
            print()
            m = 0

        if solve in left:
            left = left
            right = right
        elif solve in right:
            temp = left
            left = right
            right = temp

        m = m - 1
        if m < -len(left):
            clear = True
        if clear == True:
            if left[0] == "(" and left[-1] == ")":
                # opens parenthesies if left in form of (x1*x2*...) = y
                # and restarts cycle
                print("open parenthesies")
                left = left[1:-1]
                m = -1
                clear = False
                print(left + "=" + right)
                print()
            else:
                break

def exporoot():
    global left
    global right
    global layer
    global layer_check
    global clear
    k = -1
    layer_check = False
    clear = False
    while True: # exponents [ (x*y)^[z] ] and roots [ [z]|(x*y) ]
        if left[k] == ")":
            layer = layer + 1
            layer_check = True
        elif left[k] == "(":
            layer = layer - 1
        if layer == 0:
            layer_check = False

        if left[k] == "^" and layer_check == False:
            print("exponent")
            print(left[:k])
            print(left[k+1:])
            part1 = left[:k]
            part2 = left[k+1:]
            left = part1
            right = part2 + "|" "(" + right + ")"
            print(left + "=" + right)
            print()
            k = 0
    
        elif left[k] == "|" and layer_check == False:
            print("root")
            print(left[:k])
            print(left[k+1:])
            part1 = left[:k]
            part2 = left[k+1:]
            left = part2
            right = "(" + right + ")^" + part1
            print(left + "=" + right)
            print()
            k = 0

        k = k - 1
        if k < -len(left):
            clear = True
        if clear == True:
            if left[0] == "(" and left[-1] == ")":
                print("open parenthesies")
                left = left[1:-1]
                k = -1
                clear = False
                print(left + "=" + right)
                print()
            else:
                break


# START
# SYNTAX:
# x+y, x-y, x*y, x/y, x^[y], [y]|x
equation = "a/(t*(c*h)^[3])+d+[2]|(b*y)=e"
solve = "c"

print(equation)
print("solve for " + solve)
print()

print("rearrange equation")
separation = equation.split("=")

if solve in separation[0]:
    left = separation[0]
    right = separation[1]
elif solve in separation[1]:
    left = separation[1]
    right = separation[0]

# extra + added for rearrangement
# won't be shown in result
if left[0] != "-":
    left = "+" + left
if right[0] != "-":
    right = "+" + right

rearrange()

print(left + "=" + right)
print()

while len(left) != 1:
    multivision()
    exporoot()

print("end result:")
print(left + "=" + right)
