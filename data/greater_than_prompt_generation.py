import random

# Need to add a word bank of possible nouns

def generate_dataset(num_prompts):
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
    
    # Return
    return output

def generate_full_dataset():
    """
        Generates the complete dataset with XX from 01 to 99
    """

    output = []

    for i in range(1, 100):
        # Construct the prompt
        num = f"{i:02d}"
        prompt = "The war lasted from 18" + str(num) + " to 18"

        # Append prompt
        output.append((prompt, int(num)))
    
    # Return
    return output