fnumber = input("Enter a file number: ")
fhand = open(f"finding_anagrams_input_data{fnumber}.txt")
flist = [line.strip() for line in fhand]

sentence = flist[0].split()
flist.pop(0)

anagram = []

for i in flist:
    if i in sentence:
        anagram.append(i)
if len(sentence) != len(anagram):
    print("No anagrams for this sentence.")
else:
    print(" ".join(anagram))
