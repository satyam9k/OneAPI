# output.py
from tabulate import tabulate

def generate_table_and_summary(entities):
    # Check if entities is a string
    if isinstance(entities, str):
        print("Error: Expected list of dictionaries, received a string.")
        return None, None
    
    # Convert output to a list of lists for tabulate
    table_data = [[entity['entity_group'],  entity['word']] for entity in entities]
    
    # Define headers for the table
    headers = ["Entity Group",  "Word"]

    # Print the table
    print("Structured Table:")
    print(tabulate(table_data, headers=headers))

    

    return table_data
