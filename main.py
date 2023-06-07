with open("books/frankenstein.txt", "r") as f:
    file_contents = f.read()

def words_in_file(str):
    return len(str.split())

def letter_count(content):
    letters = {}
    for i in content:
        if(i.isalpha()):
            if i.lower() in letters:    
                letters[i.lower()] += 1
            else:
                letters[i.lower()] = 1

    return letters


sorted_letters = sorted(list(letter_count(file_contents).items()), key = lambda x: x[1], reverse = True)

for i in range(len(sorted_letters)):
    print(f"The '{sorted_letters[i][0]}' character was found {sorted_letters[i][1]} times")




# print(words_in_file(file_contents))