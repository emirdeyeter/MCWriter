from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


def text_to_morse(text):
    text = text.upper()
    morse = []

    for char in text:
        if char in MORSE_CODE:
            morse.append(MORSE_CODE[char])
        else:
            morse.append('?')

    return ' '.join(morse)


def morse_to_text(morse_code):
    words = morse_code.strip().split(' / ')

    result = []

    for word in words:
        letters = word.split()
        word_text = []

        for letter in letters:
            if letter in REVERSE_MORSE:
                word_text.append(REVERSE_MORSE[letter])
            else:
                word_text.append('?')

        result.append(''.join(word_text))

    return ' '.join(result)


class MCWriterApp(App):

    def build(self):
        self.title = "MCWriter"

        main = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="MCWriter",
            font_size=32,
            size_hint_y=None,
            height=60
        )

        subtitle = Label(
            text="Morse Code Converter",
            font_size=16,
            size_hint_y=None,
            height=35
        )

        self.input_box = TextInput(
            hint_text="Metin veya Mors kodu gir...",
            multiline=True,
            font_size=20
        )

        self.result_box = TextInput(
            hint_text="Sonuç burada görünecek...",
            multiline=True,
            readonly=True,
            font_size=20
        )

        buttons = BoxLayout(
            size_hint_y=None,
            height=60,
            spacing=10
        )

        text_button = Button(
            text="Metin → Mors",
            font_size=16
        )
        text_button.bind(on_press=self.convert_to_morse)

        morse_button = Button(
            text="Mors → Metin",
            font_size=16
        )
        morse_button.bind(on_press=self.convert_to_text)

        clear_button = Button(
            text="Temizle",
            font_size=16
        )
        clear_button.bind(on_press=self.clear_all)

        buttons.add_widget(text_button)
        buttons.add_widget(morse_button)
        buttons.add_widget(clear_button)

        main.add_widget(title)
        main.add_widget(subtitle)
        main.add_widget(self.input_box)
        main.add_widget(buttons)
        main.add_widget(self.result_box)

        return main

    def convert_to_morse(self, instance):
        text = self.input_box.text
        self.result_box.text = text_to_morse(text)

    def convert_to_text(self, instance):
        morse = self.input_box.text
        self.result_box.text = morse_to_text(morse)

    def clear_all(self, instance):
        self.input_box.text = ""
        self.result_box.text = ""


if __name__ == "__main__":
    MCWriterApp().run()
