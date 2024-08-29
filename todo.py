import tkinter as tk
from tkinter import messagebox
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x500")

        self.tasks = self.load_tasks()

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)
        self.add_task_button = tk.Button(self.root, text="Add Task", bg="green", fg="white", command=self.add_task)
        self.add_task_button.pack(pady=5)
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)
        self.update_task_list()
        self.mark_completed_button = tk.Button(self.root, text="Mark as Completed", bg="blue", fg="white", command=self.mark_as_completed)
        self.mark_completed_button.pack(pady=5)
        self.delete_task_button = tk.Button(self.root, text="Delete Task", bg="red", fg="white", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

    def add_task(self):
        task_description = self.task_entry.get().strip()
        if task_description:
            self.tasks.append({"description": task_description, "completed": False})
            self.save_tasks()
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")

    def mark_as_completed(self):
        s = self.task_listbox.curselection()
        if s:
            index = s[0]
            if 0 <= index < len(self.tasks):
                self.tasks[index]["completed"] = True
                self.save_tasks()
                self.update_task_list()
            else:
                messagebox.showwarning("Selection Error", "Invalid task selected.")
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    def delete_task(self):
        s = self.task_listbox.curselection()
        if s:
            index = s[0]
            if 0 <= index < len(self.tasks):
                del self.tasks[index]
                self.save_tasks()
                self.update_task_list()
            else:
                messagebox.showwarning("Selection Error", "Invalid task selected.")
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Incomplete"
            self.task_listbox.insert(tk.END, f"{task['description']} ({status})")

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                tasks = json.load(f)
                # Ensure tasks are in the correct format
                if not isinstance(tasks, list):
                    return []
                return tasks
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()