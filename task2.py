from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_image(image_path, encrypted_path, key):
    cipher_suite = Fernet(key)
    with open(image_path, 'rb') as file:
        original_image = file.read()
    encrypted_image = cipher_suite.encrypt(original_image)
    with open(encrypted_path, 'wb') as file:
        file.write(encrypted_image)

def decrypt_image(encrypted_path, decrypted_path, key):
    cipher_suite = Fernet(key)
    with open(encrypted_path, 'rb') as file:
        encrypted_image = file.read()
    decrypted_image = cipher_suite.decrypt(encrypted_image)
    with open(decrypted_path, 'wb') as file:
        file.write(decrypted_image)

def main():
    choice = input("Would you like to encrypt or decrypt an image? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    key_file = 'secret.key'
    
    if choice == 'encrypt':
        image_path = input("Enter the path of the image to encrypt: ").strip()
        encrypted_path = input("Enter the path to save the encrypted image: ").strip()
        key = generate_key()
        save_key(key, key_file)
        encrypt_image(image_path, encrypted_path, key)
        print("Image encrypted and saved to", encrypted_path)
        print("Encryption key saved to", key_file)
    elif choice == 'decrypt':
        encrypted_path = input("Enter the path of the encrypted image: ").strip()
        decrypted_path = input("Enter the path to save the decrypted image: ").strip()
        key = load_key(key_file)
        decrypt_image(encrypted_path, decrypted_path, key)
        print("Image decrypted and saved to", decrypted_path)
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == '__main__':
    main()
