class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Create a list of lists to represent the rails
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1 means going down, -1 means going up
        
        for char in plain_text:
            rails[rail_index].append(char)
            
            # Change direction at the top or bottom rail
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        # Join the rails into the final cipher text
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Find the length of each rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        
        # Count the number of characters that go to each rail
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Split the cipher text into the rails based on the calculated lengths
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Reconstruct the plain text by reading from the rails
        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index].pop(0)  # Pop the first character from the rail
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text
