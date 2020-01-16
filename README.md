# image-encryptor
**Python app to encrypt images using AES**

Basic encryption of an image. First, the image to be encrypted is parsed as a binary and then an alphanumeric key is taken from the user. SHA256 hashing is used to increase the security of data by creation of a checksum purposed to represent private information. The process works by passing information as input to a hash function and using a returned hash string to represent the encrypted key. We then create the AES cipher and use it along with the hash string to encrypt the image.
The AES cipher is created with CFB (Cipher FeedBack) mode of operation wherein it allows the block encryptor be used as a stream cipher. Also, for AES encryption using pycrypto, we had to ensure that the data is a multiple of 16-bytes in length. Pad the buffer if it is not and include the size of the data at the beginning of the output, so the receiver can decrypt properly.

**Dependencies**


 ```sudo pip install Pillow```  
If you have both Pythons installed and want to install this for Python3:  
 ```python3 -m pip install Pillow```   

**Running the app**

Simply execute the run-me.py file.  
 ```python run-me.py```
