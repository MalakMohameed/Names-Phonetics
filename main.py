import jellyfish
from unidecode import unidecode

def find_closest_english_name(arabic_name, english_names):
    arabic_soundex = jellyfish.soundex(unidecode(arabic_name))
    
    closest_name = None
    highest_similarity = 0
    
    for english_name in english_names:
        english_soundex = jellyfish.soundex(unidecode(english_name))
        distance = jellyfish.damerau_levenshtein_distance(arabic_soundex, english_soundex)
        
        # Compute a similarity score based on distance
        similarity_score = 100 - distance
        
        if similarity_score > highest_similarity:
            highest_similarity = similarity_score
            closest_name = english_name
    
    return closest_name, highest_similarity

# Example usage
if __name__ == "__main__":
    # Example Arabic name (without extra quotes)
    arabic_name = "عبد الرازق"
    
    # Example list of English names
    english_names = [
        "Mohammed", "Muhammad", "Mahmoud", "Ahmad", "Mehmet", "Abd el razeq",
        "Abdelrazek", "Ali", "Aly", "ُAely", "Aaly", "Sama", "John", "Mohamed", "Malak", "Malk", "Jana Bahey", "Janna", "Jannah"
    ]
    
    # Find the closest sounding English name using Soundex from jellyfish
    closest_name, similarity_score = find_closest_english_name(arabic_name, english_names)
    
    print(f"Arabic Name: {arabic_name}")
    print(f"Closest English Name: {closest_name}")
    print(f"Similarity Score: {similarity_score:.2f}%")
