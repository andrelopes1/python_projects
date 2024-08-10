import os

# Specify the directory to "infect"
target_dir = "/path/to/target/directory"

# Function to "encrypt" (rename) files
def encrypt_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Let's pretend we're targeting text files
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, f"ENCRYPTED_{filename}")
            )
    print("Files have been 'encrypted'.")

# Function to "decrypt" (rename back) files
def decrypt_files(directory, key):
    if key == "correct_key":
        for filename in os.listdir(directory):
            if filename.startswith("ENCRYPTED_"):
                os.rename(
                    os.path.join(directory, filename),
                    os.path.join(directory, filename.replace("ENCRYPTED_", ""))
                )
        print("Files have been 'decrypted'.")
    else:
        print("Incorrect key. Files remain 'encrypted'.")

# Simulate the attack
encrypt_files(target_dir)

# Simulate the decryption with the correct key
decrypt_key = input("Enter decryption key: ")
decrypt_files(target_dir, decrypt_key)