
     
def get_shape():
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


def get_height():
    
    while True:
        height = int(input("Height?: "))

        if height > 80:
            continue

        else:
            break

    return height


def draw_square(height):
    pass


def draw_triangle_reversed(height):
    pass


def draw_triangle(height):
    pass


def draw_triangle_multiplication(height):
    pass


def draw_pyramid(height):
    pass


def draw_triangle_prime(height):
 
    def is_prime(height):
        if height < 2:
            return False
        for i in range(2, int(height**0.5) + 1):
            if height % i == 0:
                return False
        return True
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