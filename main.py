import os
import msvcrt as m

class counter:
    @staticmethod
    def counter():
        with open('To Do list/list.txt', 'r') as f:
            lines = f.readlines()
        count = len(lines)
        return count + 1

class file:
    @staticmethod
    def read():
        with open("To Do list/list.txt","r") as lst:
            a = lst.read()
        return a
    
    @staticmethod
    def readlines():
        count = 0
        with open("To Do list/list.txt","r") as lst:
            a = lst.readlines()
        
        for i in a:
            if i == '':
                a.remove(i)
                continue
            if "=== Done" in i:
                count += 1
        return count
        
    @staticmethod
    def write(task):
        if task == 'M1\to do list\main.py"' or task == '':
            return
        count = counter.counter() 
        with open("To Do list/list.txt","a") as lstw:
            lstw.write(f"{count}: {task}\n")
       
    @staticmethod     
    def done(num):
        with open("To Do list/list.txt","r") as lst:
            lines = lst.readlines()
        with open("To Do list/list.txt","w") as lstw:
            for line in lines:
                if line.startswith(f"{num}:"):
                    lstw.write(f"{line.strip()} === Done\n")
                else:
                    lstw.write(line)

    @staticmethod
    def clear():
        with open("To Do list/list.txt","w") as lst:
            lst.write("")

    @staticmethod
    def remove(num):
        with open("To Do list/list.txt","r") as lst:
            lines = lst.readlines()

        new_lines = []
        for i, line in enumerate(lines, start=1):
            if not line.startswith(f"{num}:"):
                task = line.split(":", 1)[-1].strip()
                new_lines.append(f"{task}")
        file.clear()
        for t in new_lines:
            file.write(t)
     
class option:
    @staticmethod
    def option():
        while True:
            k = m.getch()
            if   k == b'x' or k == b'X':
                return 'x'
            elif k == b'd' or k == b'D':
                return 'd'
            elif k == b'a' or k == b'A':
                return 'a'
            elif k == b'z' or k == b'Z':
                return 'z'
            elif k == b'c' or k == b'C':
                return 'c'
            elif k == b'y' or k == 'Y':
                return 'y'
            else:
                continue

class progress:
    @staticmethod
    def progress():
        total_task = counter.counter()
        task_done = file.readlines()
        if total_task == 0:
            total_task = 1
        per = progress.percent(task_done,total_task)
        t = int(int(per)/2)
        bar = "=" * t
        u = int(int(100)/2)
        r = u - t
        
        if per == 100:
            h = ''
        else:
            h = ">"
        emp = " " * r
        print(f"\t\t{int(per)}% [{bar + h + emp}]\n\n")
        return int(per)
    
    @staticmethod
    def percent(d,r):
        d = float(d)
        r = float(r) -1 
        if d == 0:
            return 0
        return (d / r) * 100
    
class main:
    @staticmethod
    def main():
        os.system("cls")
        a = file.read()
        if a == '':
            print("\n\t\t\t\t      The list is empty\n\n")
        else:
            print("\n\t\t\t\t      Your To Do list:\n\n")
            print(a)
        per = progress.progress()
        if per == 100:
            file.clear()
            print("\t\tAll tasks are done! List cleared.\n\n")
        print("A:Add   Z:Remove   D:Done   X:Exit   C:Clear")
        o = option.option()
        if o == 'x':
            exit()
        if o == 'd':
            done = int(input("Enter the task number which is done: "))  
            file.done(done)
            print("\t\tTask marked as done")  
        if o == 'a':
            task = input("Enter the task: ").capitalize()
            file.write(task)
            print("\t\tTask added")
        if o == 'z':
            task = input("Enter task no. to remove: ")
            file.remove(task)
            print(f"\nTask No.{task} removed\n")
            
        if o == 'c':
            print("\n\nPress Y to clear all the list: ")
            a = option.option()
            if a == 'y':
                file.clear()
                print("\n\nThe list is cleared")
 
if __name__ == "__main__":
    while True:
        main.main()