from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
import random

class LoveCalculatorApp(App):
    
    def build(self):
        # Layout principal
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.image = Image(source='love.png', size_hint=(1, 0.8))
        self.layout.add_widget(self.image)
        
        # Título
        self.title_label = Label(text='Love Calculator - Quanto ele/ela está a fim de você', font_size=24)
        self.layout.add_widget(self.title_label)
        
        # Campo de entrada para o nome do usuário
        self.name1_label = Label(text="Escreva seu nome:")
        self.layout.add_widget(self.name1_label)
        self.name1_input = TextInput(multiline=False)
        self.layout.add_widget(self.name1_input)
        
        # Campo de entrada para o nome do parceiro
        self.name2_label = Label(text="Escreva o nome do seu/sua pareceiro(a):")  # Corrigido aqui
        self.layout.add_widget(self.name2_label)
        self.name2_input = TextInput(multiline=False)
        self.layout.add_widget(self.name2_input)
        
        # Botão de calcular
        self.calc_button = Button(text="Calcular", size_hint=(None, None), size=(150, 50))
        self.calc_button.bind(on_press=self.calculate_love)
        self.layout.add_widget(self.calc_button)
        
        # Resultado
        self.result_label = Label(text='Porcentagem de amor entre vocês dois:', font_size=18)
        self.layout.add_widget(self.result_label)
        
        return self.layout

    # Função para calcular a porcentagem do amor
    def calculate_love(self, instance):
        name1 = self.name1_input.text
        name2 = self.name2_input.text

        combined_names = (name1 + name2).lower()
        t = combined_names.count("t")
        r = combined_names.count("r")
        u = combined_names.count("u")
        e = combined_names.count("e")
        first_digit = t + r + u + e

        l = combined_names.count("l")
        o = combined_names.count("o")
        v = combined_names.count("v")
        e = combined_names.count("e")
        second_digit = l + o + v + e 

        score = int(f"{first_digit}{second_digit}")

        if (score < 10) or (score > 90):
            result_text = f"Sua pontuação é {score}, vocês combinam como coca e mentos."
        elif (score >= 40) and (score <= 50):
            result_text = f"Sua pontuação é {score}, vocês são mais ou menos."
        else:
            result_text = f"Sua pontuação é {score}."

        popup = Popup(title='Resultado do Amor', content=Label(text=result_text), 
                      size_hint=(None, None), size=(300, 200))
        popup.open()   

if __name__ == '__main__':
    LoveCalculatorApp().run()