# output.py
from tabulate import tabulate

def generate_table_and_summary(entities):
    if isinstance(entities, str):
        print("Error: Expected list of dictionaries, received a string.")
        return None, None
    
    # Convert output to a list of lists for tabulate
    table_data = [[entity['entity_group'],  entity['word']] for entity in entities]
    headers = ["Entity Group",  "Word"]

    print("Structured Table:")
    print(tabulate(table_data, headers=headers))

    

    return table_data
