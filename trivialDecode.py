#!/usr/bin/env python
# import sys

alphaL = "abcdefghijklnmopqrstuvqxyz"
alphaU = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
num    = "0123456789"
keychars = num+alphaL+alphaU

# if len(sys.argv) != 3:
#   print "Usage: %s SECRET_KEY PLAINTEXT"%(sys.argv[0])
#   sys.exit()

# key = sys.argv[1]
# if not key.isalnum():
#   print "Your key is invalid, it may only be alphanumeric characters"
#   sys.exit()

# plaintext = sys.argv[2]

ciphertext = ""
# for i in range(len(plaintext)):
#   rotate_amount = keychars.index(key[i%len(key)])
#   if plaintext[i] in alphaL:
#     enc_char = ord('a') + (ord(plaintext[i])-ord('a')+rotate_amount)%26
#   elif plaintext[i] in alphaU:
#     enc_char = ord('A') + (ord(plaintext[i])-ord('A')+rotate_amount)%26
#   elif plaintext[i] in num:
#     enc_char = ord('0') + (ord(plaintext[i])-ord('0')+rotate_amount)%10
#   else:
#     enc_char = ord(plaintext[i])
#   ciphertext = ciphertext + chr(enc_char)

# print "Encryption complete, ENC(%s,%s) = %s"%(plaintext,key,ciphertext)
 

key= "T0pS3cre7key"
secret="Bot kmws mikferuigmzf rmfrxrwqe abs perudsf! Nvm kda ut ab8bv_w4ue0_ab8v_DDU"
for i in range(len(secret)):
  rotate_amount = keychars.index(key[i%len(key)])
  if secret[i] in alphaL:
    enc_char=ord(secret[i])+ 96 -rotate_amount
  elif secret[i] in alphaU:
    enc_char=ord(secret[i])+ 96 -rotate_amount
  else:
    enc_char=ord(secret[i])
  print enc_char
  ciphertext=ciphertext+chr(enc_char)
print "hi"
