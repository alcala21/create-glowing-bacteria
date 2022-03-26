complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
original = input()
complementary = "".join(complements[x] for x in original)

print(original)
print(complementary)