import pandas as pd
from fuzzywuzzy import fuzz
from unidecode import unidecode

def find_closest_english_name(arabic_name, english_names, threshold=35):
    transliterated_arabic_name = unidecode(arabic_name)
    
    closest_name = None
    highest_similarity = 0
    
    for english_name in english_names:
        similarity = fuzz.ratio(transliterated_arabic_name, english_name)
        
        if similarity > highest_similarity:
            highest_similarity = similarity
            closest_name = english_name
    
    if highest_similarity >= threshold:
        return closest_name, highest_similarity
    else:
        return None, highest_similarity

# Example usage
if __name__ == "__main__":
    try:
        # Read Arabic names from a CSV file
        arabic_names_df = pd.read_csv('Datasets/Arabic_Names.csv')
        arabic_names = arabic_names_df['names'].tolist()
        
        # Read English names from another CSV file
        english_names_df = pd.read_csv('Datasets/English_Names.csv')
        english_names = english_names_df['names'].tolist()
        
        # Create a list to store the results
        results = []
        
        # Iterate over each Arabic name
        for arabic_name in arabic_names:
            closest_name, similarity_score = find_closest_english_name(arabic_name, english_names)
            if closest_name is None:
                results.append((arabic_name, "No Match", "No Match"))
            else:
                results.append((arabic_name, closest_name, similarity_score))
        
        # Convert the results to a DataFrame and save to a new CSV file
        results_df = pd.DataFrame(results, columns=['Arabic Name', 'Closest English Name', 'Similarity Score'])
        print("DataFrame created successfully")
        
        # Debugging: print first few rows to ensure correctness
        print(results_df.head())
        
        # Save to CSV
        results_df.to_csv('Datasets/Matched_Names.csv', index=False)
        print("File saved successfully")
    
    except Exception as e:
        print(f"An error occurred: {e}")
