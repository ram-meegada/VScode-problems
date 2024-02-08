def circles(info):
   result = []
   for i in info:
       # Parse the descriptors for circle A and circle B
       xA, yA, rA, xB, yB, rB = map(int, i.split())
       
       # Calculate the distance between the centers of the circles
       distance = ((xA - xB) ** 2 + (yA - yB) ** 2) ** 0.5
       print(distance, rA + rB)
       # Check the relationship between the circles based on their positions and sizes
       if distance == rA + rB:
           result.append("Touching")
       elif distance == 0 and rA == rB:
           result.append("Concentric")
       elif distance < rA + rB:
           result.append("Intersecting")
       elif distance > rA + rB:
           if distance > max(rA, rB):
               result.append("Disjoint-Outside")
           else:
               result.append("Disjoint-Inside")
   return result

# circlePairs = ['12 0 21 14 0 23', '0 45 8 0 94 9', '35 0 13 10 0 38', '0 26 8 0 9 25']
circlePairs = ['0 5 9 0 9 7', '0 15 11 0 20 16', '26 0 10 39 0 23', '37 0 5 30 0 11', '41 0 0 28 0 13']
print(circles(circlePairs))