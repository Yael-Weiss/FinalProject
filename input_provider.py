import sys
from typing import List, Tuple
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.styles import Style
from BoardValues import BoardValues
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import yes_no_dialog

# Define custom style
custom_style = Style.from_dict({
    'completion-menu.completion': 'bg:#008998 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    # 'scrollbar.background': 'bg:#88aaaa',
    # 'scrollbar.button': 'bg:#222222',
})
MY_STYLE = Style.from_dict({
        'dialog':             'bg:#ffe1c4',
        'dialog frame.label': 'bg:#ffc4c5 #000000',
        'dialog.body':        'bg:#f7ffff #000000',
        'dialog shadow':      'bg:#deffff',
    })


# Define custom completer
class MyCompleter(Completer):
    def get_completions(self, document, complete_event):
        completions = [
            Completion('apple', display='Red', style='class:red'),
            Completion('sea', display='Blue', style='class:blue'),
            Completion('banana', display='Yellow', style='class:yellow'),
            Completion('apple', display='Purple', style='class:purple'),
            Completion('apple', display='Green', style='class:green'),
            Completion('orange', display='Orange', style='class:orange'),
        ]
        for completion in completions:
            yield completion


def get_input_with_autocomplete(input_question:str,answers_options:List[str])->str: 
    return prompt(input_question, completer=WordCompleter(answers_options),style=MY_STYLE)

def get_input_dialog(question:str,cancel_text1:str="Quit",title_on_top:str='Welcome to Chinese Checkers Game!')->str:
    if(cancel_text1=="Quit"):
        while(True):
            result= input_dialog(
                title=title_on_top,
                text=question,cancel_text=cancel_text1,style=MY_STYLE).run()
            if(result==None):
                    answer=make_yes_no_dialog("Chinese Checkers Game","Are you sure that you want to quit the game?",yes_buttom="Quit",no_buttom="Back")
                    if(answer):   
                        print_message_dialog_or_quit("You quited the game.","Bye Bye")
                        sys.exit()
            else:
                break
        return result
    return input_dialog(
        title=title_on_top,
        text=question,cancel_text=cancel_text1,style=MY_STYLE).run()
def print_message_dialog_or_quit(message:str,clicker_message:str)->None:
    return message_dialog(
        title=HTML('<style fg="ansired">Chinese</style> '    
                '<style fg="ansired">Checkers Game</style>'),
        text=message,
        ok_text=clicker_message,
        style=MY_STYLE).run()

def get_input_in_radiolist_dialog(question:str, answers_options:List[Tuple[any,str]],cancel_text:str="Quit",title_on_top:str='Welcome to Chinese Checkers Game!') ->any:
    while(True):
        result = radiolist_dialog(title_on_top,question,ok_text="continue",
                                values=answers_options,cancel_text=cancel_text,
                                style=MY_STYLE).run()
        if(result==None):
            answer=make_yes_no_dialog("Chinese Checkers Game","Are you sure that you want to quit the game?",yes_buttom="Quit",no_buttom="Back")
            if(answer):   
                print_message_dialog_or_quit("You quited the game.","Bye Bye")
                sys.exit()
        else:
            break
    return result

def make_yes_no_dialog(title_on_top:str,question:str,yes_buttom:str="Yes",no_buttom:str="No")->bool:
    return yes_no_dialog(
        title=title_on_top,
        text=question,yes_text=yes_buttom,no_text=no_buttom,style=MY_STYLE).run()


if __name__ == "__main__":
    pass
    
    
    
