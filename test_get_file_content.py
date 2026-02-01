from functions import get_file_content

def main():
      
	print("\nTestando coleta de conteúdo:\n")  
    
	print(get_file_content.get_file_content("calculator", "main.py"))
	print(get_file_content.get_file_content("calculator", "pkg/calculator.py"))
	print(get_file_content.get_file_content("calculator", "/bin/cat"))
	print(get_file_content.get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()
