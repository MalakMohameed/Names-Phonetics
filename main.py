from fuzzywuzzy import fuzz
from unidecode import unidecode

def find_closest_english_name(arabic_name, english_names):
    transliterated_arabic_name = unidecode(arabic_name)
    
    closest_name = None
    highest_similarity = 0
    
    for english_name in english_names:
        similarity = fuzz.ratio(transliterated_arabic_name, english_name)
        
        if similarity > highest_similarity:
            highest_similarity = similarity
            closest_name = english_name
            
    return closest_name, highest_similarity

# Example usage
if __name__ == "__main__":
    # Example Arabic name
    arabic_name = "عبد الرازق"
    
    # Example list of English names
    english_names = ["Mohammed", "Muhammad", "Mahmoud", "Ahmad", "Mehmet", "Abdelrazeq","Abdelrazek"]
    
    # Find the closest sounding English name
    closest_name, similarity_score = find_closest_english_name(arabic_name, english_names)
    
    print(f"Arabic Name: {arabic_name}")
    print(f"Closest English Name: {closest_name}")
    print(f"Similarity Score: {similarity_score}")
