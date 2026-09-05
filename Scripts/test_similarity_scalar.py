import math

def cosine_similarity(a ,b):
    dot_product = 0
    sum_a = 0
    sum_b = 0
    
    for i in range(len(a)):
        dot_product += a[i] * b[i]
        
    for i in range(len(a)):
        sum_a += a[i] ** 2
    
    for i in range(len(b)):
        sum_b += b[i] ** 2
        
    length_a = math.sqrt(sum_a)
    length_b = math.sqrt(sum_b)
    
    return dot_product / (length_a * length_b)

a = [1, 1, 1]
b = [1, 1, 1]

result = cosine_similarity(a, b)

print(result)