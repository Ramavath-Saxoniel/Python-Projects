import PySimpleGUI as sg    

layout = [[sg.Txt(''  * 10)],                      
          [sg.Text('', size=(20, 1), font=('Calibri', 20), text_color='white', key='input')],
          [sg.Txt(''  * 10)],
          [sg.ReadFormButton('('), sg.ReadFormButton(')'), sg.ReadFormButton('C'), sg.ReadFormButton('<<')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('/')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('x')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')],
          ]

form = sg.FlexForm('SIMPLE CALCULATOR', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)

Equal = ''
List_Op_Error =  ['+','-','*','/','(']

while True:
    button, value = form.Read()
    
    if button == 'C':
        Equal = ''
        form.FindElement('input').Update(Equal)
    elif button == '<<':
        Equal = Equal[:-1]
        form.FindElement('input').Update(Equal)
    elif len(Equal) == 16 :
        pass
    elif str(button) in '1234567890+-()./':
        Equal += str(button)
        form.FindElement('input').Update(Equal) 
    elif button == 'x':
        Equal += '*'
        form.FindElement('input').Update(Equal)
    
    elif button == '=':
        for i in List_Op_Error :  
            if '*' == Equal[0] or '/' == Equal[0] or ')' == Equal[0]  or i == Equal[-1]:
                Answer = "Error Operation" 
                break
            elif Equal == '6001012630187':
                Answer = 'Apisit.Khomcharoen'
                break
            elif '/0' in Equal or '*/' in Equal or '/*' in Equal :
                Answer = "Error Operation" 
                break
            elif '(' in Equal :
                if ')' not in Equal :
                    Answer = "Error Operation" 
                    break   
            elif '(' not in Equal:
                if ')' in Equal:
                    Answer = "Error Operation" 
                    break
        else :
            Answer = str("%0.2f" %(eval(Equal)))
            if '.0' in Answer:
                Answer = str(int(float(Answer)))
        form.FindElement('input').Update(Answer)
        Equal = Answer

    elif button == 'Quit'  or button is None:
        break
