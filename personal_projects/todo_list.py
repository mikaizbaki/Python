# step 1. create a list
todo_list = []

# step 2. ask how many things you need in your list
count = int(input("How many things do you want to add to your todo list? "))

# step 3. make a loop (depending on how many things you need)
    # inside of the loop, ask each time for what to add to your todo list
    # add the thing to your todo list

for i in range(count):
    item = input(f"Enter item #{i+1}: ")
    todo_list.append(item)

# step 4. print out your todo list
print("\nYour TODO list:")
for task in todo_list:
    print("-", task)

