import os

# =========================
# Cross-platform getch()
# =========================
try:
    # Windows
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
except ImportError:
    # Linux / macOS
    import sys, tty, termios
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


# =========================
# Counter class
# =========================
class counter:
    @staticmethod
    def counter():
        try:
            with open('To Do list/list.txt', 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            return 0
        count = len(lines)
        return count + 1


# =========================
# File operations
# =========================
class file:
    @staticmethod
    def read():
        try:
            with open("To Do list/list.txt", "r") as lst:
                return lst.read()
        except FileNotFoundError:
            return ""
    
    @staticmethod
    def readlines():
        count = 0
        try:
            with open("To Do list/list.txt", "r") as lst:
                a = lst.readlines()
        except FileNotFoundError:
            return 0
        
        for i in a:
            if i.strip() == '':
                continue
            if "=== Done" in i:
                count += 1
        return count
        
    @staticmethod
    def write(task):
        if task.strip() == "":
            return
        count = counter.counter() 
        os.makedirs("To Do list", exist_ok=True)
        with open("To Do list/list.txt", "a") as lstw:
            lstw.write(f"{count}: {task}\n")
       
    @staticmethod     
    def done(num):
        try:
            with open("To Do list/list.txt", "r") as lst:
                lines = lst.readlines()
        except FileNotFoundError:
            return
        with open("To Do list/list.txt", "w") as lstw:
            for line in lines:
                if line.startswith(f"{num}:"):
                    lstw.write(f"{line.strip()} === Done\n")
                else:
                    lstw.write(line)

    @staticmethod
    def clear():
        os.makedirs("To Do list", exist_ok=True)
        with open("To Do list/list.txt", "w") as lst:
            lst.write("")

    @staticmethod
    def remove(num):
        try:
            with open("To Do list/list.txt", "r") as lst:
                lines = lst.readlines()
        except FileNotFoundError:
            return

        new_lines = []
        for line in lines:
            if not line.startswith(f"{num}:"):
                task = line.split(":", 1)[-1].strip()
                new_lines.append(task)
        file.clear()
        for t in new_lines:
            file.write(t)


# =========================
# Option handling
# =========================
class option:
    @staticmethod
    def option():
        while True:
            k = getch().lower()
            if k in ['x', 'd', 'a', 'z', 'c', 'y']:
                return k
            else:
                continue


# =========================
# Progress bar
# =========================
class progress:
    @staticmethod
    def progress():
        total_task = counter.counter()
        task_done = file.readlines()
        if total_task == 0:
            total_task = 1
        per = progress.percent(task_done, total_task)
        t = int(int(per) / 2)
        bar = "=" * t
        u = int(100 / 2)
        r = u - t
        
        h = "" if per == 100 else ">"
        emp = " " * r
        print(f"\t\t{int(per)}% [{bar + h + emp}]\n\n")
        return int(per)
    
    @staticmethod
    def percent(d, r):
        d = float(d)
        r = float(r) - 1 
        if d == 0 or r <= 0:
            return 0
        return (d / r) * 100


# =========================
# Main app
# =========================
class main:
    @staticmethod
    def main():
        os.system("cls" if os.name == "nt" else "clear")
        a = file.read()
        if a.strip() == "":
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
            try:
                done = int(input("Enter the task number which is done: "))  
                file.done(done)
                print("\t\tTask marked as done")  
            except ValueError:
                print("Invalid input")
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


# =========================
# Entry point
# =========================
if __name__ == "__main__":
    while True:
        main.main()
