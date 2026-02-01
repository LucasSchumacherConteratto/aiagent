from functions import get_files_info

def main():

	print("Testando coleta de informações:\n")  
	
	print(get_files_info.get_files_info("calculator", "."))
	print(get_files_info.get_files_info("calculator", "pkg"))
	print(get_files_info.get_files_info("calculator", "/bin"))
	print(get_files_info.get_files_info("calculator", "../"))

if __name__ == "__main__":
    main()
