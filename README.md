# Team: TensorAI (oneAPI GenAI Hackathon)

## Introduction:
The tool is designed to assist healthcare professionals in efficiently reviewing patient records, medical history, and generating comprehensive reports in simple language for non-medical personnel to understand. Leveraging advanced technology, it streamlines the process of extracting and summarizing key information from medical documents.

## Functionality:
1. **Input Processing:**
   - Accepts input in the form of text or PDF documents.
   - Performs optical character recognition (OCR) to extract text data. *(PDF yet to be implemented)*
   
2. **Analysis and Extraction:**
   - Utilizes a fine-tuned DeBERTa Large Language Model (LLM) trained on the PubMed dataset. (It recognizes 41 Medical entities)
   - Extracts essential details such as patient age, sex, clinical events, procedures, and more.

3. **Output Generation:**
   - Presents information in two main components:
     - **Structured Table:** Contains demographics and clinical events, organized for easy reference.
     - **Generative Report:** Generates a comprehensive overview of the patient's medical journey, including consultations, medications, procedures, and treatments in simple English for non-medical personnel to understand. *(Yet to be implemented)*

## Benefits:
- Saves time for healthcare professionals by streamlining the review process.
- Enables quicker understanding and decision-making when managing patient care.
- Enhances the quality and efficiency of patient care delivery.

## Use of Intel oneAPI:
- Intel oneAPI Toolkit
- Intel HuggingFace
- Intel Distribution of Python
- Intel DevCloud Platform

## Conclusion:
The tool serves as a valuable asset for healthcare professionals, offering a streamlined approach to analyzing and summarizing medical documents. By leveraging advanced technology, it facilitates improved patient care and workflow efficiency.

## Demo:

### Input--
![Input](https://github.com/satyam9k/OneAPI/assets/75788300/b5bfef23-9675-4946-9af9-270a5ab230b0)

### Output--
![Output](https://github.com/satyam9k/OneAPI/assets/75788300/a2bdccc1-b184-44a8-9e3f-4c1208439ad3)
