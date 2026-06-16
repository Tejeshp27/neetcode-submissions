class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string


    def decode(self, encoded_string: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(encoded_string):
            j = encoded_string.find('#', i)
            length = int(encoded_string[i:j])
            word = encoded_string[j+1:j+1+length]
            decoded_strs.append(word)
            i = j + 1 + length

        return decoded_strs

