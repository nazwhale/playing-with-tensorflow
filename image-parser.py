import weights
from weights import Weights2
import numpy as np
import PIL
from PIL import Image

I = np.asarray(PIL.Image.open('its_a_five.png'))

I = I.flatten()

J = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,84,185,159,151,60,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,222,254,254,254,254,241,198,198,198,198,198,198,198,198,170,52,0,0,0,0,0,0,0,0,0,0,0,0,67,114,72,114,163,227,254,225,254,254,254,250,229,254,254,140,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17,66,14,67,67,67,59,21,236,254,106,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,83,253,209,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,22,233,255,83,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,129,254,238,44,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,59,249,254,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,133,254,187,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,205,248,58,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,126,254,182,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,251,240,57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,221,254,166,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,203,254,219,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,38,254,254,77,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,224,254,115,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,133,254,254,52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,61,242,254,254,52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,121,254,254,219,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,121,254,207,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

bias = [-0.12531213, 0.34291193, -0.07756195, -0.15483579, 0.14375827,  0.38140905,
 0.04379947, 0.30139488, -0.70874661, -0.14681587]

w = Weights2

probability_0 = 0

i = 0
while i < 284:
    probability_0 = probability_0 + (w[i][0] * I[i])
    i = i+1

print("probability 0: ")
print(probability_0/255)

probability_1 = 0

i = 0
while i < 284:
    probability_1 = probability_1 + (w[i][1] * I[i])
    i = i+1

print("probability 1: ")
print(probability_1/255)

probability_2 = 0

i = 0
while i < 284:
    probability_2 = probability_2 + (w[i][2] * I[i])
    i = i+1

print("probability 2: ")
print(probability_2/255)

probability_3 = 0

i = 0
while i < 284:
    probability_3 = probability_3 + (w[i][3] * I[i])
    i = i+1

print("probability 3: ")
print(probability_3/255)

probability_4 = 0

i = 0
while i < 284:
    probability_4 = probability_4 + (w[i][4] * I[i])
    i = i+1

print("probability 4: ")
print(probability_4/255)

probability_5 = 0

i = 0
while i < 284:
    probability_5 = probability_5 + (w[i][5] * I[i])
    i = i+1

print("probability 5: ")
print(probability_5/255)

probability_6 = 0

i = 0
while i < 284:
    probability_6 = probability_6 + (w[i][6] * I[i])
    i = i+1

print("probability 6: ")
print(probability_6/255)

probability_7 = 0

i = 0
while i < 284:
    probability_7 = probability_7 + (w[i][7] * I[i])
    i = i+1

print("probability 7: ")
print(probability_7/255)

probability_8 = 0

i = 0
while i < 284:
    probability_8 = probability_8 + (w[i][8] * I[i])
    i = i+1

print("probability 8: ")
print(probability_8/255)

probability_9 = 0

i = 0
while i < 284:
    probability_9 = probability_9 + (w[i][9] * I[i])
    i = i+1

print("probability 9: ")
print(probability_9/255)

probability_array = [probability_0/255, probability_1/255, probability_2/255, probability_3/255, probability_4/255, probability_5/255, probability_6/255, probability_7/255, probability_8/255, probability_9/255]

mean = np.mean(probability_array)
print("mean:")
print(mean)

std = np.std(probability_array)
print("std:")
print(std)

z_score_array = []

i = 0
while i < 10:
    z_score_array.append((probability_array[i] - mean)/std)
    i = i + 1

print(z_score_array)

# fp = (np.dot(np.transpose(w), J))/2550 + bias
