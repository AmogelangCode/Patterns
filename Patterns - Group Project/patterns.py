
# TODO: Step 1 - return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape():
    '''Function to request the user input to choose a 
    shape between a triangle, square, pyramid then return a valid shape'''
    while True:
        valid_shapes = ["triangle", "square", "pyramid"]
        shape = input("Shape: ").strip().lower()

        if shape not in valid_shapes:
            continue

        if shape == " ":
            continue
        else:
            break
        
    return shape


# TODO: Step 2 - return height from user input (it must be int!)
#       The maximum possible height must be 80
def get_height():
    '''This function takes the user input for height and returns
      height that is less than 80''' 

    while True:
        height = int(input("Height?: "))

        if height > 80:
            continue

        else:
            break

    return height


# TODO: Step 3 Complete the required shapes below
#       with reference to the unittests
def draw_square(height):
    ''' This function takes the height as an argument to print stars
        in a square shape
    '''
    pass


def draw_triangle_reversed(height):
    '''
    This function takes the height as an argument to draw a reversed right
    angled triangle 
    '''
    for i in range(height):
        for _ in range(i,height):
            print(i+1,end=" ")
        print()


def draw_triangle(height):
    ''' This function uses the height as an argument to draw a right angled 
        triangle
    '''
    pass


def draw_triangle_multiplication(height):
    
    '''
    function that draws a multiplication triangle 
    '''

    for i in range(1,height+1):
        for j in range(1,i+1):
            print(j*i,end=" ")
        print()

def draw_pyramid(height):
    ''' A function that uses the height to a pyramid shape
    '''
    pass

def is_prime(height):
    if height < 2:
        return False
    for i in range(2, int(height**0.5) + 1):
        if height % i == 0:
            return False
    return True


def draw_triangle_prime(height):
    """ 
    This function returns prime numbers and use the prime numbers to print a right
    angled triangle with prime numbers
    """

    current = 2  # Starting number

    for i in range(1, height + 1):
        j = 0
        while j < i:
            if is_prime(current):
                print(current, end=" ")
                j += 1
            current += 1
        print()



    return is_prime(height)
         
                
# TODO: Step 4 - add support for other shapes
def draw(shape, height):
    if shape == "pyramid":
        draw_pyramid(height)



def tower_of_hanoi(n, source, auxiliary, target):
    """
    *This function is used to show how the rings move from one pole to the next.
    *When moving these rings make sure the bigger ones are at the bottom and the smalled ones at the top.
    *Since there are 3 different poles if you encounter a small ring put it at the 3rd pole and and move
     back to the second one when all the big ones have been filled.
    """
    if n == 1:
        return [(source,target)]
    else:
    
        return tower_of_hanoi(n-1, source, target, auxiliary) + [(source,target)] + tower_of_hanoi(n-1, auxiliary, source, target)

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)