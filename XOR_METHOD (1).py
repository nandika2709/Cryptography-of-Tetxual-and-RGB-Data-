#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PIL import Image
from IPython.display import display
import numpy as np
import math
import time

#reading the image into a 3d array 
#ROW (height) x COLUMN(Width) x COLORS(3)
src_image = np.array(Image.open('pic1.png').convert('RGB'))
display(Image.open('pic1.png'))
print('Input Image Shape = ',src_image.shape)
# start time
start = time.time()

#generating a key for encryption and decryption
key= np.random.randint(1000, size=(280, 500, 3))
print('Key Matrix Shape = ',key.shape)
# XOR opertion between input image and the key
encrypt = np.bitwise_xor(src_image,key)
np.array_equal(encrypt,src_image)

# save the encrypted image
img = Image.fromarray((encrypt * 255).astype(np.uint8))
img.save('xor3_encrypt.png')
display(img)

# Decrypt the image by performing XOR between encrypted matrix and key matrix
decrypt = np.bitwise_xor(key,encrypt)
decrypt=decrypt.astype(np.uint8)
print('Decrypted Image Shape = ',decrypt.shape)
# end image
end = time.time()

# save image
i = Image.fromarray(decrypt)
i.save('xor3_decrypt.png')
display(i)

print('Time',round(end - start,4))


# In[ ]:




