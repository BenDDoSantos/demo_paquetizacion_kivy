import logging
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

logging.basicConfig(filename='app_metrics.log', level=logging.INFO)

class HolaMundoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(1, 1))
        top_spacer = Label(size_hint_y=0.4)
        center_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=200, padding=10, spacing=10)
        label = Label(text="¡Hola Mundo!", font_size='24sp', size_hint_y=None, height=100)
        btn = Button(text="Presióname", size_hint_y=None, height=50, width=150, size_hint_x=None, pos_hint={'center_x': 0.5})
        btn.bind(on_press=self.registrar_evento)
        center_layout.add_widget(label)
        center_layout.add_widget(btn)
        
        # Espacio inferior
        bottom_spacer = Label(size_hint_y=0.4)
        
        layout.add_widget(top_spacer)
        layout.add_widget(center_layout)
        layout.add_widget(bottom_spacer)
        return layout

    def registrar_evento(self, instance):
        logging.info("Botón presionado")
        print("Registrado en logs")

if __name__ == '__main__':
    HolaMundoApp().run()