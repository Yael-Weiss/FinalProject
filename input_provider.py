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
# Define custom style
custom_style = Style.from_dict({
    'completion-menu.completion': 'bg:#008998 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    # 'scrollbar.background': 'bg:#88aaaa',
    # 'scrollbar.button': 'bg:#222222',
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
    return prompt(input_question, completer=WordCompleter(answers_options),style=custom_style)

def get_input_dialog(question:str,title_on_top:str='Welcome to Chinese Checkers Game!')->str:
    return input_dialog(
        title=title_on_top,
        text=question).run()

def print_message_dialog_or_quit(message:str,clicker_message:str)->None:
    my_style = Style.from_dict({
        'dialog':             'bg:#ffe1c4',
        'dialog frame.label': 'bg:#ffc4c5 #000000',
        'dialog.body':        'bg:#f7ffff #000000',
        'dialog shadow':      'bg:#deffff',
    })
    message_dialog(
        title=HTML('<style fg="ansired">Chinese</style> '    
                '<style fg="ansired">Checkers Game</style>'),
        text=message,
        ok_text=clicker_message,
        style=my_style).run()

def get_input_in_radiolist_dialog(question:str, answers_options:List[Tuple[any,str]],title_on_top:str='Welcome to Chinese Checkers Game!') ->any:
    result = radiolist_dialog(title_on_top,question,ok_text="continue",
                              values=answers_options).run()
    return result

if __name__ == "__main__":
    #r=get_input_in_radiolist_dialog("welcome","how many",[(111,"1"),(BoardValues.RED,"2")])
    # print(type(r))
    # # print_message_dialog_or_quit('lets start the game! Press ENTER to quit.',"lets go!")
    # print(type(get_input_dialog("what is your name?")))
    print(get_input_with_autocomplete("what is your name?",["🫎","🐕","🐼"]))