
# TODO: Step 1 - return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape():
    while True:
        valid_shapes = ["triangle", "square", "pyramid", "triangle_multiplication", "triangle_prime", "triangle_reversed", "tower of hanoi"]
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
    pass


def draw_triangle_reversed(height):
    """
    function that draws a reversed triangle 
    """
    for i in range(height):
        for _ in range(i,height):
            print(i+1,end=" ")
        print()


def draw_triangle(height):
    pass


def draw_triangle_multiplication(height):
    
    """
    function that draws a multiplication triangle 
    """

    for i in range(1,height+1):
        for j in range(1,i+1):
            print(j*i,end=" ")
        print()

def draw_pyramid(height):
    '''args:
    height
    
    return a 2d shape of a pyramid using asterisks'''


    k = height-1
    for y in range(1,height*2,2):
        print(" "*k+"*"*y)
        k-=1

    

def is_prime(height):
    if height < 2:
        return False
    for i in range(2, int(height**0.5) + 1):
        if height % i == 0:
            return False
    return is_prime(height)

def draw_triangle_prime(height):
    current = 2  # Starting number

    for i in range(1, height + 1):
        j = 0
        while j < i:
            if is_prime(current):
                print(current, end=" ")
                j += 1
            current += 1
        print()

                
# TODO: Step 4 - add support for other shapes
def draw(shape, height):

    if shape == "pyramid":
        draw_pyramid(height)

    elif shape == "square":
        draw_square(height)

    elif shape == "triangle":
        draw_triangle(height)

    elif shape == "triangle_multiplication":
        draw_triangle_multiplication(height)

    elif shape == "triangle_prime":
        draw_triangle_prime(height)

    elif shape == "triangle_reversed":
        draw_triangle_reversed(height)

    # elif shape == "tower of hanoi":
    #     draw_tower_of_hanoi(n, source, auxiliary, target)



# TODO: Step 5 (standalone function) - Solve The Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    if n == 1:
        # Base case: If there's only one disk, move it from the source to the target peg.
        return [(source, target)]
    else:
        # Recursive case:
        # 1. Move n-1 disks from the source peg to the auxiliary peg using the target peg.
        # 2. Move the largest disk from the source peg to the target peg.
        # 3. Move the n-1 disks from the auxiliary peg to the target peg using the source peg.
        # Combine all the moves and return them as a list.
        moves = []
        moves += tower_of_hanoi(n - 1, source, target, auxiliary)  # Step 1
        moves.append((source, target))  # Step 2
        moves += tower_of_hanoi(n - 1, auxiliary, source, target)  # Step 3
        return moves
    


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)
    