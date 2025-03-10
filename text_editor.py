import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Text Editor")
        self.root.geometry("800x500")

        # Store font size, alignment, and font name for future use
        self.font_size = 12
        self.font_name = "Arial"
        self.alignment = 'left'
        self.underline = False
        self.strikethrough = False

        # Create Text widget
        self.text_area = tk.Text(self.root, wrap=tk.WORD, undo=True, font=(self.font_name, self.font_size))
        self.text_area.pack(expand="true", fill="both")

        # Create toolbar frame
        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack(fill="x")

        # Font size buttons
        self.increase_font_button = tk.Button(self.toolbar, text="A+", command=self.increase_font_size)
        self.decrease_font_button = tk.Button(self.toolbar, text="A-", command=self.decrease_font_size)
        self.increase_font_button.pack(side="left", padx=5)
        self.decrease_font_button.pack(side="left", padx=5)

        # Alignment buttons
        self.left_align_button = tk.Button(self.toolbar, text="Left", command=lambda: self.set_alignment('left'))
        self.center_align_button = tk.Button(self.toolbar, text="Center", command=lambda: self.set_alignment('center'))
        self.right_align_button = tk.Button(self.toolbar, text="Right", command=lambda: self.set_alignment('right'))
        self.left_align_button.pack(side="left", padx=5)
        self.center_align_button.pack(side="left", padx=5)
        self.right_align_button.pack(side="left", padx=5)

        # Font change button
        self.font_button = tk.Button(self.toolbar, text="Font", command=self.change_font)
        self.font_button.pack(side="left", padx=5)

        # Underline and strike-through buttons
        self.underline_button = tk.Button(self.toolbar, text="U", command=self.toggle_underline)
        self.strikethrough_button = tk.Button(self.toolbar, text="S", command=self.toggle_strikethrough)
        self.underline_button.pack(side="left", padx=5)
        self.strikethrough_button.pack(side="left", padx=5)

        # Numbering and Bullets buttons
        self.numbering_button = tk.Button(self.toolbar, text="Num", command=self.add_numbering)
        self.bullets_button = tk.Button(self.toolbar, text="Bullets", command=self.add_bullets)
        self.numbering_button.pack(side="left", padx=5)
        self.bullets_button.pack(side="left", padx=5)

        # File buttons (New, Open, Save)
        self.new_file_button = tk.Button(self.toolbar, text="New", command=self.new_file)
        self.open_file_button = tk.Button(self.toolbar, text="Open", command=self.open_file)
        self.save_file_button = tk.Button(self.toolbar, text="Save", command=self.save_file)
        self.new_file_button.pack(side="left", padx=5)
        self.open_file_button.pack(side="left", padx=5)
        self.save_file_button.pack(side="left", padx=5)

    def new_file(self):
        if self.text_area.get("1.0", "end-1c"):  # Check if there's any text
            if messagebox.askyesno("Save Changes?", "Do you want to save your changes?"):
                self.save_file()
        self.text_area.delete("1.0", "end-1c")  # Clear text area

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", "end-1c")  # Clear the text area
                self.text_area.insert("1.0", content)  # Insert file content

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", "end-1c"))

    def increase_font_size(self):
        """Increase font size"""
        self.font_size += 2
        self.text_area.config(font=(self.font_name, self.font_size))

    def decrease_font_size(self):
        """Decrease font size"""
        if self.font_size > 8:  # Prevent font from becoming too small
            self.font_size -= 2
            self.text_area.config(font=(self.font_name, self.font_size))

    def set_alignment(self, alignment):
        """Set text alignment"""
        self.alignment = alignment
        if alignment == 'left':
            self.text_area.tag_configure("left", justify=tk.LEFT)
            self.text_area.tag_add("left", "1.0", "end")
        elif alignment == 'center':
            self.text_area.tag_configure("center", justify=tk.CENTER)
            self.text_area.tag_add("center", "1.0", "end")
        elif alignment == 'right':
            self.text_area.tag_configure("right", justify=tk.RIGHT)
            self.text_area.tag_add("right", "1.0", "end")

    def add_numbering(self):
        """Add line numbering to the text"""
        lines = self.text_area.get("1.0", "end-1c").splitlines()
        numbered_text = "\n".join(f"{i + 1}. {line}" for i, line in enumerate(lines))
        self.text_area.delete("1.0", "end-1c")
        self.text_area.insert("1.0", numbered_text)

    def add_bullets(self):
        """Add bullet points to the text"""
        lines = self.text_area.get("1.0", "end-1c").splitlines()
        bulleted_text = "\n".join(f"• {line}" for line in lines)
        self.text_area.delete("1.0", "end-1c")
        self.text_area.insert("1.0", bulleted_text)

    def change_font(self):
        """Change font style"""
        font_list = sorted(list(font.families()))
        selected_font = simpledialog.askstring("Select Font", "Choose a font:", initialvalue=self.font_name)
        if selected_font in font_list:
            self.font_name = selected_font
            self.text_area.config(font=(self.font_name, self.font_size))

    def toggle_underline(self):
        """Toggle underline on the selected text"""
        if self.underline:
            self.text_area.tag_remove("underline", "sel.first", "sel.last")
            self.underline = False
        else:
            self.text_area.tag_add("underline", "sel.first", "sel.last")
            self.text_area.tag_configure("underline", underline=True)
            self.underline = True

    def toggle_strikethrough(self):
        """Toggle strike-through on the selected text"""
        if self.strikethrough:
            self.text_area.tag_remove("strikethrough", "sel.first", "sel.last")
            self.strikethrough = False
        else:
            self.text_area.tag_add("strikethrough", "sel.first", "sel.last")
            self.text_area.tag_configure("strikethrough", overstrike=True)
            self.strikethrough = True


if __name__ == "__main__":
    root = tk.Tk()
    editor = SimpleTextEditor(root)
    root.mainloop()
