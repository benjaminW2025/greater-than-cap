import random

def generateDataset(num_prompts):
    """ 
    Generates prompts for GPT-2 in the form of 'x is less than
    y, a is less than" 
    """

    output = []
    
    for i in range(num_prompts):
        # Generate two unique numbers from 0 to 100, and comparison number
        distinct_pair = random.sample(range(0, 101), k=2)
        compare = 1800 + random.randint(0, 100)

        # Unpack the list into two variables
        num1, num2 = distinct_pair
        year1 = 0
        year2 = 0

        if (num1 < num2):
            year1 = 1800 + num1
            year2 = 1800 + num2
        else:
            year1 = 1800 + num2
            year2 = 1800 + num1

        # Construct the prompt
        prompt = year2 + " is greater than " + year1 + ". " + compare + " is greater than "

        output.append(prompt)
    
    # Return the output
    return output