
file = open("file.txt")
counter = 0
# data = "My Name is Haroon. I like in DHA. I work at Eurus Technologies. My main Fou=cus is to lear Dev-Ops."
data = file.read()
print(data)


#Count lines
no_lines = len(data.split("\n"))
print(no_lines)

# for i in no_lines:
#     if i:
#         counter += 1
# print("No. of Lines are:", counter)


#Count Words
word_count = len(data.split())
print("No of Words are:", word_count)


#Count Characters
count = len(data)
print('Total Number of Words are:', count)


#Count Average
words = data.split()
word_average = sum(len(word) for word in words) / len(words)
print(word_average)
