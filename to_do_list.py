#ver1 to do list 
content = None
def create_list():
    global content
    header=input("header: ")
    header=header.upper()
    note=input("note: ")
    progress = input("state: 1 done or 2 in progress or 3 in hold ")
    progress =int(progress) 
    if progress == 1:
        progress = "done"
    elif progress == 2:
        progress = "in progress"
    elif progress == 3:
        progress = "in hold"
    else:
        progress = input("choose your state")
    
    content=f"state: {progress}\nheader: {header}\nnote: {note}"
    return content
def reveal_content():
    global content
    if content is None:
        return "nothing to see here"
    return content
def delete_list():
    global content
    content = None
           
        
def main():
    print("write 1 for revealing lists")
    print("write 2 for making a new list")
    print("write 3 for deleting a list")
    print("exit for quiting")
    
    while True:
        
        user =input()
        if user == "exit":
                break
        try:
            user=int(user)
            if user not in {1,2,3}:
                print("invalid operation")
                continue
                
            if user == 1:
                print(reveal_content())
                
            elif user == 2:
                create_list()
            
                
            elif user == 3:
                 delete_list()
           
                
        except ValueError:
            print("int only")
            

main()
