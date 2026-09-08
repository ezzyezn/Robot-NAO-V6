import math

# Calculate cosine similarity between two vectors
def cosine_similarity(a, b):
    dot_product = 0
    sum_a = 0
    sum_b = 0
    
    # Calculate the dot product
    for i in range(len(a)):
        dot_product += a[i] * b[i]
    
    # Calculate the sum of squares for vector a    
    for i in range(len(a)):
        sum_a += a[i] ** 2
    
    # Calculate the sum of squares for vector b
    for i in range(len(b)):
        sum_b += b[i] ** 2
    
    # Calculate vector lengths
    length_a = math.sqrt(sum_a)
    length_b = math.sqrt(sum_b)
    
    # Return cosine similarity
    return dot_product / (length_a * length_b)
