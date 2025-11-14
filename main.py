import sys
import json
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QListWidgetItem, QLineEdit, QMessageBox
)
from PyQt6.QtGui import QFont, QColor, QIcon
from PyQt6.QtCore import Qt, QPropertyAnimation
import icons  # فایل آیکون‌ها
# حالت دارک/لایت
current_theme = "light"

TASK_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo App - Material Design")
        self.setMinimumSize(450, 600)

        # Load tasks
        self.tasks = load_tasks()

        # Layouts
        main = QVBoxLayout()
        input_layout = QHBoxLayout()
        btn_layout = QHBoxLayout()

        # Input field
        self.input = QLineEdit()
        self.input.setPlaceholderText("یک کار جدید وارد کن...")
        self.input.setFont(QFont("Segoe UI", 12))
        input_layout.addWidget(self.input)

        # Add button
        add_btn = QPushButton("افزودن")
        add_btn.setFont(QFont("Segoe UI", 12))
        add_btn.clicked.connect(self.add_task)
        input_layout.addWidget(add_btn)

        # Theme switcher
        theme_btn = QPushButton()
        theme_btn.setIcon(QIcon(icons.theme_icon))
        theme_btn.clicked.connect(self.switch_theme)
        theme_btn.setFixedWidth(40)
        input_layout.addWidget(theme_btn)

        # Task list
        self.list = QListWidget()
        self.list.setFont(QFont("Segoe UI", 12))
        self.load_list()

        # Buttons
        done_btn = QPushButton("انجام شد")
        done_btn.clicked.connect(self.mark_done)

        delete_btn = QPushButton("حذف")
        delete_btn.clicked.connect(self.delete_task)

        btn_layout.addWidget(done_btn)
        btn_layout.addWidget(delete_btn)

        # Build UI
        main.addLayout(input_layout)
        main.addWidget(self.list)
        main.addLayout(btn_layout)
        self.setLayout(main)

        # Apply theme
        self.apply_theme()

    def load_list(self):
        self.list.clear()
        for t in self.tasks:
            txt = ("✓ " if t["done"] else "✗ ") + t["task"]
            item = QListWidgetItem(txt)
            if t["done"]:
                item.setForeground(QColor("#888"))
            self.list.addItem(item)

    def add_task(self):
        text = self.input.text().strip()
        if not text:
            QMessageBox.warning(self, "خطا", "متن کار نمی‌تواند خالی باشد.")
            return

        self.tasks.append({"task": text, "done": False})
        save_tasks(self.tasks)
        self.input.clear()
        self.load_list()

        # Animation (fade in)
        item = self.list.item(self.list.count() - 1)
        anim = QPropertyAnimation(item, b"size")
        anim.setDuration(350)

    def mark_done(self):
        row = self.list.currentRow()
        if row < 0:
            QMessageBox.warning(self, "خطا", "هیچ کاری انتخاب نشده.")
            return

        self.tasks[row]["done"] = not self.tasks[row]["done"]
        save_tasks(self.tasks)
        self.load_list()

    def delete_task(self):
        row = self.list.currentRow()
        if row < 0:
            QMessageBox.warning(self, "خطا", "هیچ کاری انتخاب نشده.")
            return

        del self.tasks[row]
        save_tasks(self.tasks)
        self.load_list()

    def apply_theme(self):
        with open("style_light.qss" if current_theme == "light" else "style_dark.qss", "r", encoding="utf-8") as f:
            style = f.read()
            self.setStyleSheet(style)

    def switch_theme(self):
        global current_theme
        current_theme = "dark" if current_theme == "light" else "light"
        self.apply_theme()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())
