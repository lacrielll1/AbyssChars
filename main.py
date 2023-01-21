import random
import matplotlib.pyplot as plt

path = 'char_icons/'

with open('least_popular.txt', 'r') as lp, open('my_chars.txt', 'r') as mc, open('char_to_icon.txt', 'r') as dictionary:
    least_popular = lp.read().split('\n')
    ban_chars = mc.read().split('\n')
    d = dictionary.read().split('\n')
    d = dict([(pair.split(',')[0], pair.split(',')[1]) for pair in d])
    pick = random.sample(least_popular, 3)
    ban = random.sample(ban_chars, 5)
    pick_images = [d[key] for key in pick]
    ban_images = [d[key] for key in ban]

fig = plt.figure(figsize=(15, 15))
columns = 5
rows = 2
for i in range(1, 4):
    img = plt.imread(path + pick_images[i - 1])
    fig.add_subplot(rows, columns, i)
    plt.title('pick')
    plt.imshow(img)

for i in range(1, 6):
    img = plt.imread(path + ban_images[i - 1])
    fig.add_subplot(rows, columns, i + 3)
    plt.title('ban')
    plt.imshow(img)

plt.show()