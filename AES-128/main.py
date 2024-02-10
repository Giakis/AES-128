from Crypto.Cipher import AES
import random
import os
import bitarray

#Δημιουργία κλειδιού με 16Bytes=128Bits
bits_key = bitarray.bitarray() #Τα bitarrays είναι παρόμοια με τις λίστες, αλλά κάθε στοιχείο τους μπορεί να πάρει μόνο τις δύο τιμές
for i in range (128):
    j = random.randint(0, 1) #Με την βοήθεια της έτοιμης ψευδοτυχαίας συνάρτηστης
    bits_key.append(j)
print(bits_key)
key = bits_key.tobytes() #Μετατροπή αυτών των Bits σε Bytes με την έτοιμη συνάρτηση

#δημιουργεί ένα τυχαίο δυαδικό κλειδί μήκους 16 bytes, το οποίο χρησιμοποιείται ως Initialization Vector (IV)
iv = os.urandom(16)

#Δημιουργεία των 256 Bits με ψευδοτυχαίο τρόπο
i = 0
bits_1 = bitarray.bitarray()
bits_2 = bitarray.bitarray()
for i in range (256):
 j = random.randint(0,1)
 bits_1.append(j)
 if i==255: #Αλλαγή του τελευταίου Bit κάθε φορά που τρέχει ο συγκεκριμένος αλγόριθμος
     if j==0:
         bits_2.append(1)
     else:
         bits_2.append(0)
 else:
     bits_2.append(j)

#Μετατροπη των Bits σε Bytes
data_1 = bits_1.tobytes()
data_2 = bits_2.tobytes()

#Kρυπτογράφηση των δεδομένων με την έτοιμη συνάρτηση που βρήκα για την Java
#ECB MODE
# cipher = AES.new(key, AES.MODE_ECB )
# encrypted_data_1 = cipher.encrypt(data_1)
# encrypted_data_2 = cipher.encrypt(data_2)

#CBC MODE με IV
cipher = AES.new(key, AES.MODE_CBC ,iv)
encrypted_data_1 = cipher.encrypt(data_1)
encrypted_data_2 = cipher.encrypt(data_2)

#μετατροπή των κρυπτογραφημένων bytes σε bits
encrypted_bits_1 = bitarray.bitarray()
encrypted_bits_1.frombytes(encrypted_data_1)

encrypted_bits_2 = bitarray.bitarray()
encrypted_bits_2.frombytes(encrypted_data_2)

#Καταμέτρηση των ίδιων και τον διαφορετικών Bits του αποτελέσματος
Same      = 0
Different = 0
for i in range (256):
    if encrypted_bits_1[i]==encrypted_bits_2[i]:
        Same += 1
    else:
        Different += 1
print('Same Bits:', Same)
print('Different Bits:', Different)