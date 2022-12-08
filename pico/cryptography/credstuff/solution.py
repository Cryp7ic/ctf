# You can use the 'tr' command in linux to unencrypt rot13 like this:
# echo "cvpbPGS{P7e1S_54I35_71Z3}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'

# You can also do this in Python:

def caesar_decrypt(ciphertext, key):
  # create a string of all the possible lowercase and uppercase letters
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
  # create a string that will be used to store the decrypted message
  decrypted = ''
  
  # loop through each character in the ciphertext
  for char in ciphertext:
    # if the character is a letter, encrypt it using the key
    if char in alphabet:
      # get the position of the character in the alphabet
      pos = alphabet.index(char)
      # shift the character by the key
      new_pos = (pos - key) % len(alphabet)
      # add the encrypted character to the decrypted message
      decrypted += alphabet[new_pos]
    # if the character is not a letter, simply add it to the decrypted message
    else:
      decrypted += char
  
  # return the decrypted message
  return decrypted

# test the function with a simple ciphertext and key
ciphertext = 'cvpbPGS{P7e1S_54I35_71Z3}'
key = 13
print(caesar_decrypt(ciphertext, key))



