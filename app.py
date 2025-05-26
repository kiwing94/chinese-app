
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.core.window import Window
import json

Window.size = (360, 640)

# Register fonts
LabelBase.register(name="HanFont", fn_regular="NotoSansCJKsc-Regular.otf")           # Chinese
LabelBase.register(name="PinyinFont", fn_regular="CharisSIL-Regular.ttf")         # Pinyin
LabelBase.register(name="SymbolFont", fn_regular="NotoSansSymbols2-Regular.ttf")  # Icons / fallback

class FlashcardLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        with open("hsk_vocab_1_to_4_cleaned.json", encoding="utf-8") as f:
            self.hsk_data = json.load(f)

        self.level = "HSK1"
        self.vocab = self.hsk_data.get(self.level, [])
        self.index = 0
        self.xp = 0

        self.spinner = Spinner(
            text=self.level,
            values=sorted(self.hsk_data.keys()),
            size_hint=(1, None),
            height=44
        )
        self.spinner.bind(text=self.change_level)

        self.hanzi_label = Label(text="", font_size=40, size_hint=(1, 0.2), font_name="HanFont")
        self.pinyin_label = Label(text="", font_size=24, font_name="PinyinFont")
        self.translation_label = Label(text="", font_size=24)
        self.stats_label = Label(text="XP: 0", font_size=20)

        nav_layout = BoxLayout(size_hint=(1, None), height=44, spacing=10)
        self.prev_btn = Button(text="◀", on_press=self.show_prev, font_name="SymbolFont")
        self.know_btn = Button(text="✅ Jag kan det!", on_press=self.add_xp, font_name="SymbolFont")
        self.next_btn = Button(text="▶", on_press=self.show_next, font_name="SymbolFont")
        nav_layout.add_widget(self.prev_btn)
        nav_layout.add_widget(self.know_btn)
        nav_layout.add_widget(self.next_btn)

        self.add_widget(self.spinner)
        self.add_widget(self.hanzi_label)
        self.add_widget(self.pinyin_label)
        self.add_widget(self.translation_label)
        self.add_widget(nav_layout)
        self.add_widget(self.stats_label)

        self.update_card()

    def change_level(self, spinner, level):
        self.level = level
        self.vocab = self.hsk_data.get(level, [])
        self.index = 0
        self.update_card()

    def update_card(self):
        if not self.vocab:
            self.hanzi_label.text = "Ingen data"
            self.pinyin_label.text = ""
            self.translation_label.text = ""
            return
        word = self.vocab[self.index]
        self.hanzi_label.text = word["hanzi"]
        self.pinyin_label.text = word["pinyin"]
        self.translation_label.text = word["translation"]
        self.stats_label.text = f"XP: {self.xp}"

    def show_prev(self, instance):
        if self.index > 0:
            self.index -= 1
            self.update_card()

    def show_next(self, instance):
        if self.index < len(self.vocab) - 1:
            self.index += 1
            self.update_card()

    def add_xp(self, instance):
        self.xp += 5
        self.stats_label.text = f"XP: {self.xp}"
        popup = Popup(title="Bra jobbat!", content=Label(text="+5 XP"), size_hint=(None, None), size=(200, 150))
        popup.open()

class FlashcardApp(App):
    def build(self):
        return FlashcardLayout()

if __name__ == "__main__":
    FlashcardApp().run()
