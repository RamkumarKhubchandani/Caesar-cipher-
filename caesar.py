import string
import sys

# Caesar cipher implementation
def encode_text(text, key):
   result = ''
   for char in text:
       if char.isalpha():
           base = ord('A') if char.isupper() else ord('a')
           offset = ord(char) - base
           new_offset = (offset + key) % 26
           new_char = chr(base + new_offset)
           result += new_char
       else:
           result += char
   return result

# Frequency calculation
def frequencies(text):
   text = text.lower()
   freq = [0] * 26
   total = sum(1 for char in text if char.isalpha())
   for char in text:
       if char.isalpha():
           index = ord(char) - ord('a')
           freq[index] += 1
   freq = [count / total for count in freq]
   return freq

# String histogram
def string_histogram(text):
   histogram = {}
   for char in text.lower():
       if char.isalpha():
           histogram[char] = histogram.get(char, 0) + 1
   return histogram

# Chi-squared distance
def chi_squared(expected, observed):
    distance = 0
    for i in range(26):
        if expected[i] == 0:
            if observed[i] == 0:
                # If both expected and observed are zero, skip this letter
                continue
            else:
                # If expected is zero but observed is not, treat it as a maximum difference
                distance += observed[i]
        else:
            distance += (observed[i] - expected[i])**2 / expected[i]
    return distance

# Cracking the Caesar cipher
def crack_caesar(example_text, encrypted_text):
   example_freq = frequencies(example_text)
   best_key = None
   min_distance = float('inf')
   for key in range(26):
       decrypted_text = encode_text(encrypted_text, -key)
       decrypted_freq = frequencies(decrypted_text)
       distance = chi_squared(example_freq, decrypted_freq)
       if distance < min_distance:
           min_distance = distance
           best_key = key
   return encode_text(encrypted_text, -best_key)

# Main program
# def main():
#     if len(sys.argv) < 3:
#         print("Usage: python caesar.py 'text' key")
#         sys.exit(1)

#     text = ' '.join(sys.argv[1:-1])
#     try:
#         key = int(sys.argv[-1])
#     except ValueError:
#         print("Error: The key must be an integer.")
#         sys.exit(1)

#     encrypted_text = encode_text(text, key)
#     print(f"Encrypted text: {encrypted_text}")
#     decrypted_text = encode_text(encrypted_text, -key)
#     print(f"Decrypted text: {decrypted_text}")

#     example_text = "This is an example text from the play Julius Caesar by William Shakespeare."
#     cracked_text = crack_caesar(example_text, encrypted_text)
#     print(f"Cracked text: {cracked_text}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python caesar.py 'text' key")
        sys.exit(1)

    text = ' '.join(sys.argv[1:-1])
    try:
        key = int(sys.argv[-1])
    except ValueError:
        print("Error: The key must be an integer.")
        sys.exit(1)

    encrypted_text = encode_text(text, key)
    print(f"Encrypted text: {encrypted_text}")
    decrypted_text = encode_text(encrypted_text, -key)
    print(f"Decrypted text: {decrypted_text}")

    example_text = "This is an example text from the play Julius Caesar by William Shakespeare."
    cracked_text = crack_caesar(example_text, encrypted_text)
    print(f"Cracked text: {cracked_text}")

    # Print letter frequencies
    print("\nLetter frequencies for the input text:")
    text_freq = frequencies(text)
    print_frequencies(text_freq)

    print("\nLetter frequencies for the example text:")
    example_freq = frequencies(example_text)
    print_frequencies(example_freq)

def print_frequencies(freq_vector):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter, freq in zip(alphabet, freq_vector):
        print(f"Letter '{letter}' has a frequency of {freq:.4f}")

if __name__ == "__main__":
   main()