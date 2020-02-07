uncompressed_file = 'needlessly large'
compressed_file = 'small'

with open(uncompressed_file, 'r') as reading_file:  # reads the uncompressed content as a string
    content = reading_file.read()

list_content = content.split(sep='\n')  # splits the string into a list with multiple strings. each string represents a
                                        # line in the original uncompressed file.

list_content_compressed = []  # list for not void content (content in a line starting with a char that isn't blank).
content_compressed = ''  # final string

for line in list_content:  # repeats these actions for every line present in the uncompressed file.
    for i in range(len(line)):  # checks every character in the line.
        if line[i] != ' ':                            # if a character other than a whitespace is found.
            list_content_compressed.append(line[i:])  # saves the string from that character on.
            break

for i in range(len(list_content_compressed) - 1):  # composes the final string
    content_compressed = content_compressed + list_content_compressed[i] + '\n'
content_compressed += list_content_compressed[-1]

with open(compressed_file, 'w') as writing_file:  # writes the compressed content to a new file.
    writing_file.write(content_compressed)
