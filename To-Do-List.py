tasks=[]

print("\n**welcome to your To-Do List**\n")

while True:
    print("\n------------------------------")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    print("------------------------------")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        task_new=input("Enter the task you want to add: ")
        tasks.append(task_new)
        print(f"\n✅Task '{task_new}' added successfully!\n")
    elif choice == "2":
        if not tasks :
            print("\n⚠️ No tasks in the list.\n")
        else:
            print("\n📋 Your To-Do List:")
            i=1
            for data in tasks :
                print(i,".",data)
                i+=1
    elif choice == "3":
        if not tasks :
            print("\n⚠️ No tasks to remove.\n")
        else:
            print("\n📋 Your To-Do List:")
            i=1
            for data in tasks :
                print(i,".",data)
                i+=1
            task_number=int(input("\nEnter the number of the task you want to remove: ")) 
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"\n✅ Task '{removed_task}' removed successfully!\n")
            else:
                print("\n⚠️ Invalid task number.\n")     
    elif choice == "4":
        print("\n👋 Goodbye!")
        break
