import os
from food_map import create_random_food_map
from code_generation import create_code
x = 50
y = 50
life = 100

def main():
    #Create a thousand genetic code mutations and fifty foodmaps
    codeMutations = []
    foodMaps = []
    for _ in range(1000):
        codeMutations.push(getCodeMutation);
    for _ in range(50):
        foodMaps.push(create_random_food_map);
    results = [] # contains tuples of each mutation along with how long mutation survived

    #Run each mutation with ten random food maps.
    for codeMutation in codeMutations:
        currentMutation = convert_code_from_list_to_string(codeMutation)
        for _ in range(10):
            randomFoodMap = random.choice(foodMap)
            results.push(currentMutation, numIterations)
            resetGlobals()
    sorted(results, key=lambda result: result[1]) #sort by length of life
    print "The top mutation was as follows: \n" + results[0]



    
def resetGlobals():
    x = 50
    y = 50
    life = 100
    numIterations = 0


def modify_code(code):
    available_commands = ["if on_food_square():", "if not on_food_square():", "up()", "down()", "left()", "right()"]
    random_number = random.randrange(0, len(available_commands))
    indents = get_current_number_of_indents(code)
    if last_command_is_pass(code):
        # Replace pass with new command
        code[-1] = whitespace(indents) + available_commands[random_number]
    else:
        # Either add the command within the current block, or outside it by using one less indent
        if with_probability(50):
            indents = max(0, indents - 1)
        code.append(whitespace(indents) + available_commands[random_number])

    # If an 'if' command was added, also add a 'pass' to make it valid Python
    if random_number == 0 or random_number == 1:
        code.append(whitespace(indents + 1) + "pass")
    return code


def with_probability(probability):
    if random.randrange(0, 100) < probability:
        return True
    else:
        return False


def convert_code_from_list_to_string(input_code):
    output_code = ""
    for line in input_code:
        output_code = output_code + os.linesep + line
    return output_code


def update_everything():
    global x
    global y
    global FoodMap
    global life
    global numIterations
    numIterations += 1
    life -= 1
    if FoodMap[x][y] > 0:
        eat = min(FoodMap[x][y], 10)
        life += eat
        FoodMap[x][y] -= eat
    print "Position = [" + str(x) + "," + str(y) + "], Life = " + str(life) + ", length of life = " + numIterations


def up():
    global y
    y -= 1
    y = max(y, 0)
    update_everything()


def right():
    global x
    x += 1
    x = min(x, 99)
    update_everything()


def down():
    global y
    y += 1
    y = min(y, 99)
    update_everything()


def left():
    global x
    x -= 1
    x = max(x, 0)
    update_everything()


def on_food_square():
    return FoodMap[x][y] > 0


if __name__ == '__main__':
    main()

