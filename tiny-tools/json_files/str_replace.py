
def str_replace(file, ori_str, sub_str):
    with open(file, 'r') as f:
        file_lines = f.readlines()

    with open(file, 'a') as f:
        for line in file_lines:
            line = line.replace(ori_str, sub_str)
            f.write(line)
            f.write("\n")

str_replace("new_words.json", "\'", "\"")

