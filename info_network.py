from datetime import datetime

print("Jade Ashley Villanueva")
print("211-0738")
print(f"Date: {datetime.now().date()}")

concern = input("What is your networking issue? \n")

with open("network_issue.txt", "w") as file:
	file.write(concern)


