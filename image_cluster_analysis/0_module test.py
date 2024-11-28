from imgtoarray import load_images, draw_images
import numpy as np

apple = load_images("Training\Apple Red 1") # 492장
banana = load_images("Training\Banana 1") # 490장
cherry = load_images("Training\Cherry 1") # 492장
for fruit in apple, banana, cherry:
    print(fruit.shape[0])

sample_fruit = np.concatenate((apple[0:1], banana[0:1], cherry[0:1]), axis=0)
draw_images(sample_fruit, ratio=3, titles=["apple", "banana", "cherry"], axis="on", cmap="gray", save=r"Images\0_sample")