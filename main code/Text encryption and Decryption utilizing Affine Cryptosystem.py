# Define the Turkish alphabet with 29 letters
turkish_alphabet = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

# Create mappings from letters to indices and vice versa
char_to_index = {char: idx for idx, char in enumerate(turkish_alphabet)}
index_to_char = {idx: char for idx, char in enumerate(turkish_alphabet)}

# Affine cipher parameters
a = 5
b = 20
m = 29  # Length of Turkish alphabet
a_inverse = 6  # Modular inverse of a under mod 29

# Text to encrypt
plaintext = "SELÇUK ÜNİVERSİTESİ TEKNOLOJİ FAKÜLTESİ BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ"
# Ensure the text is uppercase for uniformity
plaintext = plaintext.upper()

# Affine encryption function
def affine_encrypt(text):
    encrypted_text = ""
    for char in text:
        if char in char_to_index:
            x = char_to_index[char]  # Get the index of the character
            # Apply the encryption formula: (a * x + b) % m
            encrypted_index = (a * x + b) % m
            encrypted_text += index_to_char[encrypted_index]
        else:
            encrypted_text += char  # Preserve spaces and other characters
    return encrypted_text

# Affine decryption function
def affine_decrypt(text):
    decrypted_text = ""
    for char in text:
        if char in char_to_index:
            y = char_to_index[char]  # Get the index of the encrypted character
            # Apply the decryption formula: (a_inverse * (y - b)) % m
            decrypted_index = (a_inverse * (y - b)) % m
            decrypted_text += index_to_char[decrypted_index]
        else:
            decrypted_text += char  # Preserve spaces and other characters
    return decrypted_text

print("Original Text:", plaintext)
# Encrypt the plaintext
encrypted_text = affine_encrypt(plaintext)
print("Encrypted Text:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = affine_decrypt(encrypted_text)
print("Decrypted Text:", decrypted_text)

output:
Original Text: SELÇUK ÜNİVERSİTESİ TEKNOLOJİ FAKÜLTESİ BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
Encrypted Text: HNÇFUY AKOENDHOPNHO PNYKÖÇÖŞO SRYAÇPNHO ÜOÇVOHRIRD ĞAGNKİOHÇOCO ÜTÇAĞA
Decrypted Text: SELÇUK ÜNİVERSİTESİ TEKNOLOJİ FAKÜLTESİ BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
