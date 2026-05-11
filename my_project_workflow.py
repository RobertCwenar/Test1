def assign_level(title):

    title = title.lower()
    
    junior_words = ["młodszy", "junior", "młodsza", "intern", "staż"]

    mid_words = ["specjalista", "specjalistka", "mid"]
    
    if any(word in title for word in junior_words):
        return "junior"
    if any(word in title for word in mid_words):
        return "mid"

    
    return "senior"


