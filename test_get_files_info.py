from functions.get_files_info import get_files_info

def main():
    get_files_info("calculator", ".")
    print("--------------------------------\n")
    get_files_info("calculator", "pkg")
    print("--------------------------------\n")
    get_files_info("calculator", "/bin")
    print("--------------------------------\n")
    get_files_info("calculator", "../")
    print("--------------------------------\n")


main()
