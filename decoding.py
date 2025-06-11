def encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decode(text, shift):
    return encode(text, -shift)

# Get input from user
message = input("Enter message: ")
shift = int(input("Enter shift value (number): "))

# Choose to encode or decode
choice = input("Type 'e' to encode or 'd' to decode: ").lower()

if choice == 'e':
    print("Encoded message:", encode(message, shift))
elif choice == 'd':
    print("Decoded message:", decode(message, shift))
else:
    print("Invalid choice. Use 'e' or 'd'.")


