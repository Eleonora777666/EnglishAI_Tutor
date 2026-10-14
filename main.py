import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit, QPushButton, QTabWidget, QFrame, QScrollArea, QComboBox, QGridLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Color Palette Configuration
COLOR_BG = "#80323C"             # Deep burgundy window background
COLOR_ACCENT_BLUE = "#415C7A"      # Blue-grey accent for tabs and send button
COLOR_PANEL_PURPLE = "#1B1528"     # Deep rich violet-purple background for cards and input boxes
COLOR_TEXT_LILAC = "#D0A9DE"       # Soft lilac/purple tint for headers and labels instead of harsh white
COLOR_TEXT_CONTENT = "#9EB8DE"     # Soft blue-cyan tint for text inside editing/viewing areas
COLOR_TEXT_MUTED = "#C0C6D0"       # Muted text for status and secondary labels

# Global application stylesheet
STYLESHEET = f"""
QMainWindow {{
    background-color: {COLOR_BG};
}}
QWidget {{
    background-color: {COLOR_BG};
    color: {COLOR_TEXT_LILAC};
    font-family: 'Segoe UI', Arial, sans-serif;
}}
QTabWidget::pane {{
    border: 1px solid {COLOR_ACCENT_BLUE};
    background-color: {COLOR_BG};
    border-radius: 8px;
}}
QTabBar::tab {{
    background-color: {COLOR_ACCENT_BLUE};
    color: {COLOR_TEXT_LILAC};
    padding: 10px 24px;
    margin-right: 6px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    font-weight: 600;
    min-width: 140px;
    border: 1px solid {COLOR_ACCENT_BLUE};
    border-bottom: none;
}}
QTabBar::tab:selected {{
    background-color: {COLOR_ACCENT_BLUE};
    color: {COLOR_TEXT_LILAC};
    border-bottom: 2px solid {COLOR_TEXT_LILAC};
}}
QPushButton {{
    background-color: {COLOR_ACCENT_BLUE};
    color: {COLOR_TEXT_LILAC};
    border: 1px solid {COLOR_ACCENT_BLUE};
    padding: 10px 18px;
    border-radius: 6px;
    font-weight: bold;
    font-size: 14px;
}}
QPushButton:hover {{
    background-color: #527298;
}}
QComboBox {{
    background-color: {COLOR_PANEL_PURPLE};
    color: {COLOR_TEXT_CONTENT};
    border: 1px solid {COLOR_ACCENT_BLUE};
    border-radius: 6px;
    padding: 8px;
    font-size: 14px;
}}
QComboBox::drop-down {{
    border: 0px;
}}
QComboBox QAbstractItemView {{
    background-color: {COLOR_PANEL_PURPLE};
    color: {COLOR_TEXT_CONTENT};
    selection-background-color: {COLOR_ACCENT_BLUE};
}}
QTextEdit {{
    background-color: {COLOR_PANEL_PURPLE};
    color: {COLOR_TEXT_CONTENT};
    border: 1px solid {COLOR_ACCENT_BLUE};
    border-radius: 6px;
    padding: 10px;
    font-size: 14px;
    font-weight: 500;
}}
QLabel {{
    color: {COLOR_TEXT_LILAC};
}}
"""

class EnglishAITutorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EnglishAI Tutor - Professional Language Environment")
        self.resize(1000, 750)
        self.setStyleSheet(STYLESHEET)

        self.init_ui()

    def init_ui(self):
        # Initialize the main user interface layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Header section layout
        header_layout = QHBoxLayout()

        title_label = QLabel("EnglishAI Tutor (☞ﾟヮﾟ)☞✨ Academic Workspace")
        title_font = QFont("Segoe UI", 18, QFont.Bold)
        title_label.setFont(title_font)
        header_layout.addWidget(title_label)

        header_layout.addStretch()

        status_label = QLabel("Status: Active & Ready")
        status_label.setStyleSheet(f"color: {COLOR_TEXT_MUTED}; font-style: italic;")
        header_layout.addWidget(status_label)

        main_layout.addLayout(header_layout)

        # Tab widget setup
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        self.tabs.addTab(self.create_about_tab(), "📚 About Project")
        self.tabs.addTab(self.create_tutor_tab(), "💬 Tutor Session")

    def create_card_with_foxes(self, inner_widget):
        """Creates a styled card container with decorative foxes placed strictly in the bottom corners."""
        wrapper = QWidget()
        wrapper.setStyleSheet(f"background-color: {COLOR_PANEL_PURPLE}; border: 1px solid {COLOR_ACCENT_BLUE}; border-radius: 6px;")
        layout = QGridLayout(wrapper)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        # Place the inner widget across the top width
        layout.addWidget(inner_widget, 0, 0, 1, 3)

        # Decorative fox emojis positioned at the bottom corners
        fox_left = QLabel("🦊")
        fox_right = QLabel("🦊")
        fox_left.setStyleSheet("background: transparent; border: none;")
        fox_right.setStyleSheet("background: transparent; border: none;")

        layout.addWidget(fox_left, 1, 0, alignment=Qt.AlignLeft | Qt.AlignBottom)
        layout.setColumnStretch(1, 1)  # Stretchable space between foxes
        layout.addWidget(fox_right, 1, 2, alignment=Qt.AlignRight | Qt.AlignBottom)

        return wrapper

    def create_about_tab(self):
        """Constructs the About Project tab with structured description cards."""
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(20)

        # 1. English section widget container
        en_widget = QWidget()
        en_widget.setStyleSheet("background: transparent; border: none;")
        en_inner_layout = QVBoxLayout(en_widget)
        en_inner_layout.setContentsMargins(0, 0, 0, 0)
        en_inner_layout.setSpacing(10)

        en_box = QTextEdit()
        en_box.setReadOnly(True)
        en_box.setPlainText(
            "EnglishAI Tutor is an advanced, context-aware artificial intelligence assistant engineered "
            "to accelerate English language acquisition through immersive interaction, dynamic vocabulary tracking, "
            "and real-time error correction.\n\n"
            "How this Agent helps you master the language:\n"
            "1. Contextual Immersion: Simulates authentic conversational scenarios tailored to your professional and personal interests.\n"
            "2. Active Correction & Feedback: Analyzes sentence structure, grammar nuances, and lexical choices instantaneously.\n"
            "3. Personalized Lexicon Building: Identifies weak spots and builds structured vocabulary lists for long-term retention.\n"
            "4. Cognitive Balance: Combines structured linguistic theory with adaptive conversational practice to minimize friction."
        )
        en_inner_layout.addWidget(en_box)

        desc_title_en = QLabel("Professional Language Acquisition System")
        desc_title_en.setFont(QFont("Segoe UI", 13, QFont.Bold))
        en_inner_layout.addWidget(desc_title_en)

        layout.addWidget(self.create_card_with_foxes(en_widget))

        # 2. Russian section widget container
        ru_widget = QWidget()
        ru_widget.setStyleSheet("background: transparent; border: none;")
        ru_inner_layout = QVBoxLayout(ru_widget)
        ru_inner_layout.setContentsMargins(0, 0, 0, 0)
        ru_inner_layout.setSpacing(10)

        ru_box = QTextEdit()
        ru_box.setReadOnly(True)
        ru_box.setPlainText(
            "EnglishAI Tutor — это передовой интеллектуальный ассистент, созданный для эффективного и глубокого освоения английского языка "
            "путем погружения в контекст, динамического отслеживания лексики и мгновенной корректировки ошибок.\n\n"
            "Как этот Агент помогает освоить язык:\n"
            "1. Контекстное погружение: Моделирует аутентичные диалоговые сценарии, адаптированные под ваши профессиональные и личные интересы.\n"
            "2. Активная коррекция и обратная связь: Мгновенно анализирует структуру предложений, грамматические нюансы и лексический выбор.\n"
            "3. Построение персонального словарного запаса: Выявляет слабые места и формирует структурированные списки слов для долгосрочного запоминания.\n"
            "4. Когнитивный баланс: Объединяет структурированную лингвистическую теорию с адаптивной разговорной практикой для снижения языкового барьера."
        )
        ru_inner_layout.addWidget(ru_box)

        desc_title_ru = QLabel("Профессиональная система освоения языка")
        desc_title_ru.setFont(QFont("Segoe UI", 13, QFont.Bold))
        ru_inner_layout.addWidget(desc_title_ru)

        layout.addWidget(self.create_card_with_foxes(ru_widget))

        scroll.setWidget(container)
        return scroll

    def create_tutor_tab(self):
        """Constructs the interactive Tutor Session tab with chat and control elements."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)

        # Chat message display area
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setPlainText("AI Tutor initialized. Ready for session...")
        layout.addWidget(self.chat_area)

        # Proficiency level selection controls
        control_layout = QHBoxLayout()
        level_label = QLabel("Select Proficiency Level:")
        level_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        control_layout.addWidget(level_label)

        self.level_combo = QComboBox()
        self.level_combo.addItems([
            "Beginner (Cyrillic Support)",
            "Intermediate (Standard English)",
            "Advanced (Professional & Academic)"
        ])
        control_layout.addWidget(self.level_combo)
        layout.addLayout(control_layout)

        # User input text field and send button layout
        input_layout = QHBoxLayout()

        self.input_field = QTextEdit()
        self.input_field.setMaximumHeight(60)
        self.input_field.setPlaceholderText("Type your message here (Cyrillic and Latin supported)...")
        input_layout.addWidget(self.input_field)

        btn_layout = QVBoxLayout()
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.handle_send)
        btn_layout.addWidget(send_btn)

        input_layout.addLayout(btn_layout)
        layout.addLayout(input_layout)

        return widget

    def handle_send(self):
        """Processes user message submission and generates simulated tutor responses."""
        text = self.input_field.toPlainText().strip()
        current_level = self.level_combo.currentText()
        if text:
            self.chat_area.append(f"You: {text}")
            self.input_field.clear()

            # Generate mode-specific feedback
            if "Beginner" in current_level:
                reply = f"[Beginner Mode]: Received Cyrillic/Latin input. Let's break it down step-by-step."
            elif "Intermediate" in current_level:
                reply = f"[Intermediate Mode]: Good phrasing. Let's expand your vocabulary on this."
            else:
                reply = f"[Advanced Mode]: Rigorous academic analysis applied to your input."

            self.chat_area.append(f"AI Tutor: {reply}\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EnglishAITutorApp()
    window.show()
    sys.exit(app.exec_())
