tasks = []
#i = 0
def addTask():
        task = (input(f"Enter an task: "))
        tasks.append(task)
        #i += 1
def removeTask(task):
    tasks.remove(task)
     # can use del for index removing

def deleteList():
    tasks.clear()


while(True): 
    choice = int(input("""1.For add a task in list
          2.For remove a task in list
          3.For View the list
          4.For reset the list
          5.For quit
            Selection: """))
    
    if(choice == 1):
        addTask()
    if(choice == 2):
        task = input("Enter a task to remove it: ")
        removeTask(task)
    if(choice == 3):
        print(tasks)
    if(choice == 4):
        deleteList()
    if(choice == 5):
        break
    #print(tasks)
    #deleteList()
    #print(tasks)