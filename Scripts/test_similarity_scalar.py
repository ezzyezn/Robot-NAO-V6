import math

a = [1, 1]
b = [1, 1]

dot_produkt = a[0] * b[0] + a[1] * b[1]

lenght_a = math.sqrt(a[0] ** 2 + a[1] ** 2)
lenght_b = math.sqrt(b[0] ** 2 + b[1] ** 2)

cosaine_similarity = dot_produkt / (lenght_a * lenght_b)


print("dot product: ",dot_produkt)
print("lenght a: ",lenght_a)
print("lenght b: ",lenght_b)
print("sum: ", cosaine_similarity)