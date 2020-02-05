class Codec:
#     method 1: join with Delimiter
#     def encode(self, strs: [str]) -> str:
#         """Encodes a list of strings to a single string.
#         """
#         if not strs:
#             return '\n'
#         return '\t'.join(strs)
        

#     def decode(self, s: str) -> [str]:
#         """Decodes a single string to a list of strings.
#         """
#         if s == '\n':
#             return []
#         return s.split('\t')
    
    # method 2: Chunked Transfer Encoding
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join([f'{len(s)}:{s}' for s in strs])
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        while s:
            length, s = s.split(':', 1)
            result.append(s[:int(length)])
            s = s[int(length):]
        return result
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))