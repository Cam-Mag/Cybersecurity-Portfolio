import hashlib
import getpass


password_manager = {}

def create_account():
	username = input("Please enter your desired username: ")
	password = getpass.getpass("Please enter your desired password: ")
	hashed_password = hashlib.sha256(password.encode()).hexdigest()
	password_manager[username] = hashed_password
	print("Account created successfully!")
	
def login():
	username = input("Please enter your username: ")
	password = getpass.getpass("Please enter your password: ")
	hashed_password = hashlib.sha256(password.encode()).hexdigest()
	if username in password_manager.keys() and password_manager[username] == hashed_password:
		print("Login successful!")
	else:
		print("Invalid username or password.")
		
def main():
	while True:
		choice = input("Please enter 'create' to create an account, 'login' to login, or 'exit' to exit: ")
		if choice == "create":
			create_account()
		elif choice == "login":
			login()
		elif choice == "exit":
			break
		else:
			print("Invalid choice.")
			
if __name__ == "__main__":
	main()
