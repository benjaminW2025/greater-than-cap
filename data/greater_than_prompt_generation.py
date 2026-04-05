import random

def generate_full_dataset():
    """
        Generates the complete dataset with XX from 01 to 99
    """

    output = []

    for i in range(1, 100):
        # Construct the prompt
        num = f"{i:02d}"
        prompt = "The war lasted from the year 18" + str(num) + " to the year 18"

        # Append prompt
        output.append((prompt, int(num)))
    
    # Return
    return output

def generate_extension_dataset():
    """
        Generates the complete dataset of the extension portion of the project
    """

    output = []

    for i in range(1, 100):
        num = f"{i:0d}"
        prompt = f"1599, 1607, 1633, 1679, 17{num}, 17"
        output.append((prompt, int(num)))

    return output