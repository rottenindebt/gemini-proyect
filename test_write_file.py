from functions.write_file import write_file

def main():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsun"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/tem.txt", "this should not be allowed"))


main()
