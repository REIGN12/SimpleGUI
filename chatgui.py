import PySimpleGUI as sg

if __name__ == "__main__":
    # open some src file
    prompt_file = 'useful_prompt.txt'
    with open(prompt_file, 'r',encoding='utf-8') as f:
        prompts = "".join(f).split("\n\n")
    print(prompts)


    # define the layout for the GUI
    layout = [
        [sg.Text('Enter your text:')],
        [sg.Input(key='InputText', size=(50, 10), do_not_clear=False)],
        [sg.Text('Enter your prompt template id, if nothing provide, will use 0:')],
        [sg.Input(key='PromptID', size=(50, 10), do_not_clear=False)],
        [sg.Button('Process',bind_return_key=True)],
        [sg.Text('', key='output')]  # add a Text element to display the output
    ]

    # create the GUI window
    window = sg.Window('Text Processor', layout)

    # run the GUI event loop
    while True:
        event, values = window.read()

        # process the text when the 'Process' button is clicked or the user hits "Enter"
        if event == 'Process':
            input_text,prompt_id = values['InputText'],values['PromptID']
            prompt_template = prompts[int(prompt_id) if prompt_id else 0]
            processed_text = prompt_template.format(input_text)

            # set the value of the 'output' Text element to the processed text
            window['output'].update(
                f"Processed text:\n{processed_text}"
            )
            # cp processed text to clipboard
            sg.clipboard_set(processed_text)
        # exit the GUI when the window is closed
        if event == sg.WIN_CLOSED:
            break

    window.close()

