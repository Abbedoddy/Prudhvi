alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
  cipher_text=""
  for char in plain_text:   #if decrypt shift_key=shift_key*-1
    if char in alphabet:
      position=alphabet.index(char)
      new_position=(position+shift_key)%26
      cipher_text+=alphabet[new_position]
    else:
      cipher_text+=char
  print(f"Here's is the your message after encryption: {cipher_text}")
def decryption(cipher_text,shift_key):
  plain_text=""
  for char in cipher_text:
    if char in alphabet:
      position=alphabet.index(char)
      new_position=(position-shift_key)%26
      plain_text+=alphabet[new_position]
    else:
      plain_text+=char
  print(f"Here's is the your message after decryption: {plain_text}")
wanna_end=False
while not wanna_end:
  what_to_do=input("Type 'encrypt' for encryption,type 'decrypt' for decryption:")
  text=input("Type your message:").lower()
  shift=int(input("Enter shift key:"))
  if what_to_do=="encrypt":
    encryption(plain_text=text,shift_key=shift)
  elif what_to_do=="decrypt":
    decryption(cipher_text=text,shift_key=shift)
  play_again=input("Type 'yes' to continue, type 'no' to exit...")
  if play_again=='no':
    wanna_end=True
    print("Have a nice day! Bye...")