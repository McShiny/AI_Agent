from functions.write_file import write_file

def test():
    print("Result for lorem.txt file")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("Result for pkg/morelorem.txt file")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("Result for /tmp/temp.txt file")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    test()