import math

# Noktaların Tanımlanması
points = [(1, 2), (3, 4), (6, 8), (2, 1)]

# Öklid Mesafesi için Fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])*2 + (point2[1] - point1[1])*2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonuçların Yazdırılması
print("Tüm mesafeler:", distances)
print("Minimum mesafe:", min_distance)