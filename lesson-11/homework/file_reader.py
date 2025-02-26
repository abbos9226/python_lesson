def read_file(file_path):
    with open(file_path,'r') as test:
        data=test.read()
        print(data)
        