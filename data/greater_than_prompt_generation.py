import random

# Need to add a word bank of possible nouns

def generateDataset(num_prompts):
    """ 
    Generates prompts for GPT-2 in the form of 'x is less than
    y, a is less than" 
    """

    output = []
    
    for i in range(num_prompts):
        # Generate two unique numbers from 0 to 100, and comparison number
        num = random.randint(1, 99)
        compare = "18" + str(num)

        # Construct the prompt
        prompt = "The war lasted from " + compare + " to 18"

        # Save the generated number and prompt
        output.append((prompt, num))
    
    # Return the output
    return output