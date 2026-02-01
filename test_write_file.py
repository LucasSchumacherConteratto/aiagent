from functions import write_file

def main():
     
    print("\nTestando escrita de conteúdo:\n")  
    
    print(write_file.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file.write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


if __name__ == "__main__":
    main()
