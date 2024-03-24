# main.py
from input import process_text_input
from model import query
from output import generate_table_and_summary

# Step 1: Process input
def process_input(input_data):
    return process_text_input(input_data)

# Step 2: Process model
def process_model(text_data):
    return query({"inputs": text_data})

# Step 3: Generate output
def process_output(entities):
    return generate_table_and_summary(entities)

# Main function
def main(input_data):
    # Step 1: Process input
    processed_text = process_input(input_data)
    
    # Step 2: Process model
    model_output = process_model(processed_text)
    
    # Step 3: Generate output
    table = process_output(model_output)
    
    # Print structured table
    print("Structured Table:")
    print(table)
    
    

# Example usage
if __name__ == "__main__":
    input_data = "A 48 year-old female presented with vaginal bleeding and abnormal Pap smears. Upon diagnosis of invasive non-keratinizing SCC of the cervix, she underwent a radical hysterectomy with salpingo-oophorectomy which demonstrated positive spread to the pelvic lymph nodes and the parametrium. Pathological examination revealed that the tumour also extensively involved the lower uterine segment."
    main(input_data)
