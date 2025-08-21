import os

#Python I/O

#how to read a file

dir_path = os.path.dirname(os.path.realpath(__file__))
# print('dir path: ', dir_path)

# with open(f'{dir_path}\secrets.txt', 'r', encoding='utf-8') as file_obj:
#     file_content = file_obj.read()

#     print(file_content)


#STAR WARS EXERCISE

# Read the file line by line

with open(f'{dir_path}\star_wars.txt', 'r', encoding='utf-8') as f:
    txt_list = f.readlines()
    for line in txt_list:
        print(line)
    print('end of document')

# Read only the 5th line of the file
print(txt_list[4])


# Read only the 5 first characters of the file
print(txt_list[0][:4])


# Read all the file and return it as a list of strings. Then split each word into letters
# using list comprehension
# temp = [list(line) for line in txt_list]
# print(temp)


# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
counts = {'Darth':0, 'Luke': 0, 'Lea': 0}

for line in txt_list:
    line = line.strip()
    if line == 'Darth':
        counts['Darth'] += 1

    elif line == 'Luke':
        counts['Luke'] += 1

    elif line == 'Lea':
        counts['Lea'] += 1

print(counts)
    

# Append your first name at the end of the file
# with open(f'{dir_path}\star_wars.txt', 'a', encoding='utf-8') as f:
#     # f.seek(0) #the cursor goes to the beginning of the file
#     f.seek(0, os.SEEK_END) # we make sure the cursor is in the end of the file
#     f.write('\nJuliana')
#     print('sucessfully added')

# Append "SkyWalker" next to each first name "Luke"
# for i, name in enumerate(txt_list):
#     if name.strip() == 'Luke':
#         txt_list[i] = f'{name} Skywalker'
# print('Sucessfuly changed')
# IT IS NOT WORKING BECAUSE WE CAN'T CHANGE THE OBJECT FILE DIRECTLY. YOU NEED TO "COPY" THE CONTENT, CHANGE IT AND THEN OVERWRITE THE CONTENT YOU CHANGED

modified_lines = []
for line in txt_list:
    if line.strip() == 'Luke':
        modified_lines.append('Luke Skywalker\n')
    else:
        modified_lines.append(line)

#Challenge:make this six lines code a list comprehension

with open(f'{dir_path}\star_wars.txt', 'w', encoding='utf-8') as f:
    f.seek(0) #make sure the cursor is in the beginning of the file
    f.writelines(modified_lines)