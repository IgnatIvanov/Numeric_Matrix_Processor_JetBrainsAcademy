class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.S = round(0.5 * self.a * self.b, 1)
        # calculate the area here


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(input_c, input_a, input_b)
if pow(triangle.c, 2) == (pow(triangle.a, 2) + pow(triangle.b, 2)):
    print(triangle.S)
else:
    print("Not right")
