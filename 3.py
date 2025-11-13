class UndoRedoSystem:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.document = ""

    def make_change(self, change):
        self.undo_stack.append(self.document)
        self.document = change
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.document)
            self.document = self.undo_stack.pop()
        else:
            print("No actions to undo.")

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.document)
            self.document = self.redo_stack.pop()
        else:
            print("No actions to redo.")

    def display(self):
        print("Current Document State:", self.document)

# Usage example
editor = UndoRedoSystem()
editor.make_change("Hello")
editor.make_change("Hello, World")
editor.display()
editor.undo()
editor.display()
editor.redo()
editor.display()