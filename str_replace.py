
def str_replace(file, ori_str, sub_str):
    with open(file, 'r') as f:
        file_data = f.read()
        file_data = file_data.replace(ori_str, sub_str)

    with open(file, 'w') as f:
        f.write(file_data)


str_replace("README.adoc", "#", "=")