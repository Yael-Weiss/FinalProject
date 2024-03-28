import sys
from typing import List, Tuple
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import yes_no_dialog

# Define style:
MY_STYLE = Style.from_dict({
        'dialog':             'bg:#ffe1c4',
        'dialog frame.label': 'bg:#ffc4c5 #000000',
        'dialog.body':        'bg:#f7ffff #000000',
        'dialog shadow':      'bg:#deffff',
    })



# class MyCompleter(Completer):
#     def get_completions(self, document, complete_event):
#         completions = [
#             Completion('apple', display='Red', style='class:red'),
#             Completion('sea', display='Blue', style='class:blue'),
#             Completion('banana', display='Yellow', style='class:yellow'),
#             Completion('apple', display='Purple', style='class:purple'),
#             Completion('apple', display='Green', style='class:green'),
#             Completion('orange', display='Orange', style='class:orange'),
#         ]
#         for completion in completions:
#             yield completion



def get_input_with_autocomplete(input_question: str, answers_options: List[str]) -> str:
    """
    Prompt the user with a question and provide autocomplete options for the answers.

    Args:
        input_question (str): The question to prompt the user with.
        answers_options (List[str]): A list of possible answers for autocomplete.

    Returns:
        str: The user's input.

    """
    return prompt(input_question, completer=WordCompleter(answers_options), style=MY_STYLE)

def get_input_dialog(question: str, cancel_text1: str = "Quit", title_on_top: str = 'Welcome to Chinese Checkers Game!') -> str:
    """
    Displays an input dialog box with the given question.

    Args:
        question (str): The question to be displayed in the input dialog.
        cancel_text1 (str, optional): The text for the cancel button. Defaults to "Quit".
        title_on_top (str, optional): The title to be displayed on top of the input dialog. Defaults to 'Welcome to Chinese Checkers Game!'.

    Returns:
        str: The user's input from the input dialog.
        None: if the user click on the cancel button.

    """
    if(cancel_text1 == "Quit"):
        while(True):
            result = input_dialog(
                title=title_on_top,
                text=question, cancel_text=cancel_text1, style=MY_STYLE).run()
            if(result == None):
                answer = make_yes_no_dialog("Chinese Checkers Game", "Are you sure that you want to quit the game?", yes_buttom="Quit", no_buttom="Back")
                if(answer):   
                    print_message_dialog("You quited the game.", "Bye Bye")
                    sys.exit()
            else:
                break
        return result
    return input_dialog(
        title=title_on_top,
        text=question, cancel_text=cancel_text1, style=MY_STYLE).run()

def print_message_dialog(message: str, clicker_message: str) -> None:
    """
    Displays a message dialog with the given message and clicker message.
    
    Args:
        message (str): The main message to be displayed in the dialog.
        clicker_message (str): The text to be displayed on the OK button.
        
    Returns:
        None
    """
    return message_dialog(
        title=HTML('<style fg="ansired">Chinese</style> '    
                '<style fg="ansired">Checkers Game</style>'),
        text=message,
        ok_text=clicker_message,
        style=MY_STYLE).run()

def get_input_in_radiolist_dialog(question: str, answers_options: List[Tuple[any, str]], cancel_text: str = "Quit", title_on_top: str = 'Welcome to Chinese Checkers Game!') -> any:
    """
    Displays a radiolist dialog with a given question and answer options.
    
    Args:
        question (str): The question to be displayed in the dialog.
        answers_options (List[Tuple[any, str]]): A list of tuples representing the answer options. Each tuple contains the value and the label for the option.
        cancel_text (str, optional): The text for the cancel button. Defaults to "Quit".
        title_on_top (str, optional): The title to be displayed on top of the dialog. Defaults to 'Welcome to Chinese Checkers Game!'.
    
    Returns:
        any: The selected value from the radiolist dialog.
    """
    while True:
        result = radiolist_dialog(title_on_top, question, ok_text="continue",
                                values=answers_options, cancel_text=cancel_text,
                                style=MY_STYLE).run()
        if result is None:
            answer = make_yes_no_dialog("Chinese Checkers Game", "Are you sure that you want to quit the game?", yes_buttom="Quit", no_buttom="Back")
            if answer:
                print_message_dialog("You quited the game.", "Bye Bye")
                sys.exit()
        else:
            break
    return result

def make_yes_no_dialog(title_on_top: str, question: str, yes_buttom: str = "Yes", no_buttom: str = "No") -> bool:
    """
    Creates a yes/no dialog box and returns the user's choice.

    Args:
        title_on_top (str): The title to be displayed on top of the dialog box.
        question (str): The question to be displayed in the dialog box.
        yes_buttom (str, optional): The label for the 'Yes' button. Defaults to "Yes".
        no_buttom (str, optional): The label for the 'No' button. Defaults to "No".

    Returns:
        bool: True if the user selects 'Yes', False if the user selects 'No'.
    """
    return yes_no_dialog(
        title=title_on_top,
        text=question, yes_text=yes_buttom, no_text=no_buttom, style=MY_STYLE).run()

    
    
