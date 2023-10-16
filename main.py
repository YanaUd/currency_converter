import tkinter as tk
from PIL import ImageTk, Image
import requests

class CurrencyConverter:
    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data["rates"]

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]
        amount = round(amount * self.rates[to_currency], 2)
        result_label.config(text='{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

def convert_currency():
    from_country = from_entry.get()
    to_country = to_entry.get()
    amount = float(amount_entry.get())
    converter.convert(from_country, to_country, amount)

# Создаем экземпляр CurrencyConverter
url = 'http://data.fixer.io/api/latest?access_key=7aa60d6884aea3e05e664f203d98dc5e'
converter = CurrencyConverter(url)

# Создаем графический интерфейс
window = tk.Tk()
window.title("Currency Converter")

# Устанавливаем розовый фон окна
window.configure(background='pink')

# Создаем Canvas для размещения картинки
canvas = tk.Canvas(window, width=300, height=300, bg='pink', highlightthickness=0)
canvas.pack()

# Загружаем и отображаем картинку котика
image = Image.open("cat.png")  # Замените "pngwing.com.png" на путь к вашей картинке
image = image.resize((250, 250), Image.ANTIALIAS)
cat_image = ImageTk.PhotoImage(image)
canvas.create_image(20, 20, anchor=tk.NW, image=cat_image)

# Создаем и размещаем элементы интерфейса
from_label = tk.Label(window, text="From Country:", bg='pink')
from_label.pack()
from_entry = tk.Entry(window)
from_entry.pack(ipadx=30, ipady=5)

to_label = tk.Label(window, text="To Country:", bg='pink')
to_label.pack()
to_entry = tk.Entry(window)
to_entry.pack(ipadx=30, ipady=5)

amount_label = tk.Label(window, text="Amount:", bg='pink')
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack(ipadx=30, ipady=5)

convert_button = tk.Button(window, text="Convert", command=convert_currency, bg='pink', height=2)
convert_button.pack(fill=tk.X, padx=50, pady=10)

result_label = tk.Label(window, text="", bg='pink')
result_label.pack()

# Запускаем главный цикл отображения интерфейса
window.mainloop()
