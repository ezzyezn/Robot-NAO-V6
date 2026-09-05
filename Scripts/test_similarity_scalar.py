import math

a = [1, 1, 1]
b = [1, 1, 1]

dot_product = 0

sum_a = 0

sum_b = 0

##dot product
for i in range(len(a)):
    dot_product += a[i] * b[i]
    
    
## lenght a
for i in range(len(a)):
    sum_a += a[i] ** 2
    
length_a = math.sqrt(sum_a)

## lenght b
for i in range(len(b)):
    sum_b += b[i] ** 2

length_b = math.sqrt(sum_b)

##similarity

cosine_similarity = dot_product / (length_a * length_b)


print(cosine_similarity)