import tkinter as tk
from tkinter import messagebox
import json

class SpreadsheetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel-like Application")
        self.num_rows = 20
        self.num_cols = 10

        # Creating the grid of entry widgets (cells)
        self.cells = {}

        self.create_grid()

        # Adding Buttons for saving and loading
        self.save_button = tk.Button(root, text="Save", command=self.save_data)
        self.save_button.grid(row=self.num_rows, column=0, columnspan=5)

        self.load_button = tk.Button(root, text="Load", command=self.load_data)
        self.load_button.grid(row=self.num_rows, column=5, columnspan=5)

    def create_grid(self):
        """Creates a grid of Entry widgets for the spreadsheet."""
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell = tk.Entry(self.root, width=10, justify="center")
                cell.grid(row=row, column=col)
                self.cells[(row, col)] = cell  # Store cell references

    def save_data(self):
        """Save data to a JSON file."""
        data = {}
        for (row, col), cell in self.cells.items():
            data[(row, col)] = cell.get()

        try:
            with open("spreadsheet_data.json", "w") as file:
                json.dump(data, file)
            messagebox.showinfo("Save", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")

    def load_data(self):
        """Load data from a JSON file."""
        try:
            with open("spreadsheet_data.json", "r") as file:
                data = json.load(file)

            # Update the cells with the loaded data
            for (row, col), value in data.items():
                if (row, col) in self.cells:
                    self.cells[(row, col)].delete(0, tk.END)  # Clear the cell
                    self.cells[(row, col)].insert(0, value)  # Insert loaded value

            messagebox.showinfo("Load", "Data loaded successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved data found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpreadsheetApp(root)
    root.mainloop()
