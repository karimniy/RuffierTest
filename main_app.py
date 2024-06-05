# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import test
from kivy.clock import Clock
from seconds import Seconds
name = ""
age,result1,result2,result3 = 0,0,0,0
def check_int(str_num):
    try:
        a = int(str_num)
        return a
    except:
        a = False
        return a


class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        main_layout = BoxLayout(orientation ="vertical",spacing = 5)
        layout1 = BoxLayout(size_hint=(0.8,None),height="30sp")
        layout2 = BoxLayout(size_hint=(0.8,None),height="30sp")
        l_inst  = Label(text = txt_instruction)
        btn = Button(text="Начать",size_hint=(0.3,0.3),pos_hint={"center_x":0.5})
        btn.on_press = self.next
        label_name = Label(text = "Введите имя")
        self.name_inp = TextInput(multiline = False)
        layout1.add_widget(label_name)
        layout1.add_widget(self.name_inp)
        label_age = Label(text = "Введите возраст")
        self.age_inp = TextInput(multiline = False)
        layout2.add_widget(label_age)
        layout2.add_widget(self.age_inp)
        main_layout.add_widget(l_inst)
        main_layout.add_widget(layout1)
        main_layout.add_widget(layout2)
        main_layout.add_widget(btn)
        self.add_widget(main_layout)
    def next(self):
        global name,age
        name = self.name_inp.text
        age = check_int(self.age_inp.text)
        if age == False or age < 7 or name == "":
            age = 0
            self.age_inp.text = ""
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'second'




class SecondScr(Screen):
    def __init__(self, name='second'):
        self.next_screen = False
        super().__init__(name=name)
        main_layout = BoxLayout(orientation ="vertical",spacing = 5)
        layout1 = BoxLayout(size_hint=(0.8,None),height="30sp")
        l_inst  = Label(text = txt_test1)
        self.btn = Button(text="Начать",size_hint=(0.3,0.5),pos_hint={"center_x":0.5})
        self.btn.on_press = self.next
        result_label = Label(text = "Введите Результат")

        self.btn_back = Button(text="Назад",size_hint=(0.3,0.6),pos_hint={"center_x":0.5})
        self.btn_back.on_press = self.back
        
        self.timer = Seconds(total = 5)
        self.next_screen = False
        
        self.timer.bind(done = self.timer_finish)
        self.result_inp = TextInput(multiline = False)
        layout1.add_widget(result_label)
        layout1.add_widget(self.result_inp)
        main_layout.add_widget(l_inst)
        main_layout.add_widget(layout1)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(self.btn)
        main_layout.add_widget(self.btn_back)
        self.add_widget(main_layout)

    def timer_finish(self, *arg):
        self.result_inp.set_disabled(False)
        self.btn.text = "Далее"
        self.next_screen = True
        self.btn.set_disabled(False)
    def next(self):
        if self.next_screen == False:
            self.timer.start()
            self.btn.set_disabled(True)
            self.result_inp.set_disabled(True)
        else:
            global result1
            result1 =check_int(self.result_inp.text)
            if result1 == False or result1 <= 0:
                result1 = 0
                self.result_inp.text = ""
            else:
                self.manager.transition.direction = 'left'
                self.manager.current = "third"
    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        main_layout = BoxLayout(orientation ="vertical",spacing = 5)
        layout1 = BoxLayout(size_hint=(0.8,None),height="30sp")
        l_inst  = Label(text = "Выполните 30 приседаний")
        btn = Button(text="Продолжить",size_hint=(0.3,0.3),pos_hint={"center_x":0.5})
        btn_back = Button(text="Назад",size_hint=(0.3,0.3),pos_hint={"center_x":0.5})
        btn.on_press = self.next
        btn_back.on_press = self.back
        main_layout.add_widget(l_inst)
        main_layout.add_widget(btn)
        main_layout.add_widget(btn_back)
        self.add_widget(main_layout)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'fourth'
    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'second'

class FourthScr(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        main_layout = BoxLayout(orientation ="vertical",spacing = 5)
        layout1 = BoxLayout(size_hint=(0.8,None),height="30sp")
        layout2 = BoxLayout(size_hint=(0.8,None),height="30sp")
        l_inst  = Label(text = txt_test3)
        self.btn = Button(text="Продолжить",size_hint=(0.3,0.6),pos_hint={"center_x":0.5})
        self.btn_back = Button(text="Назад",size_hint=(0.3,0.6),pos_hint={"center_x":0.5})
        self.btn.on_press = self.next
        self.btn_back.on_press = self.back
        label_result_normal = Label(text = "Введите результат")
        self.result_normal_inp = TextInput(multiline = False)

        self.timer = Seconds(total = 5)
        self.timer.bind(done = self.timer_finish)
        self.next_screen = False
        self.stage = 0
        
        layout1.add_widget(label_result_normal)
        layout1.add_widget(self.result_normal_inp)
        label_result_rest = Label(text = "Результат после отдыха")
        self.result_rest_inp = TextInput(multiline = False)
        layout2.add_widget(label_result_rest)
        layout2.add_widget(self.result_rest_inp)
        main_layout.add_widget(l_inst)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(layout1)
        main_layout.add_widget(layout2)
        main_layout.add_widget(self.btn)
        main_layout.add_widget(self.btn_back)
        self.add_widget(main_layout)
    def timer_finish(self, *arg):
        if self.timer.done:
            if self.stage == 0:
                self.timer.restart(5)
                self.result_normal_inp.set_disabled(False)
                self.stage = 1
            elif self.stage == 1:
                self.timer.restart(5)
                self.stage = 2
            elif self.stage == 2:
                self.result_rest_inp.set_disabled(False)
                self.btn.text = "Продолжить"
                self.btn.set_disabled(False)
                self.stage = 3

    def next(self):
        if self.stage == 3:
            global result2,result3
            result2 = check_int(self.result_normal_inp.text)
            result3 =check_int(self.result_rest_inp.text)
            if result2 <= 0 or result3 <= 0:
                result2 = 0
                result3 = 0
                self.result_normal_inp.text = ""
                self.result_rest_inp.text = ""
            else:
                self.manager.transition.direction = 'left'
                self.manager.current = 'fifth'
        else:
            self.btn.set_disabled(True)
            self.result_normal_inp.set_disabled(True)
            self.result_rest_inp.set_disabled(True)   
            self.timer.start() 

    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'third'



class FifthScr(Screen):
    def __init__(self, name='fifth'):
        super().__init__(name=name)
        main_layout = BoxLayout(orientation ="vertical",spacing = 5)
        self.btn = Button(text="Назад!",size_hint=(0.3,0.6),pos_hint={"center_x":0.5})
        self.btn.on_press = self.back
        self.l_inst  = Label(text = "Результат - ")
        main_layout.add_widget(self.l_inst)
        main_layout.add_widget(self.btn)
        self.add_widget(main_layout)
        self.on_enter = self.before
    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'fourth'

    def before(self):
        global age, name, result1, result2, result3
        text_ruffier = f"{name},ваш индекс Руфье - {test(result1,result2,result3,age)}"
        self.l_inst.text = text_ruffier


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(FourthScr())
        sm.add_widget(FifthScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm

app = MyApp()
app.run()