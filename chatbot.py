#!/usr/local/bin/

import ev3dev.ev3 as ev3
from chatterbot import ChatBot
import rpyc


def get_feedback():
    from chatterbot.utils import input_function
    text = input_function()
    if 'yes' in text.lower():
        return False
    elif 'no' in text.lower():
        return True
    elif 'maybe' in text.lower():
        print('ok')
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()

def chatbot():
    
    conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
    ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
    
    bot = ChatBot(
        'Luigi',
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        logic_adapters=[
            "chatterbot.logic.BestMatch"
        ],
        input_adapter='chatterbot.input.TerminalAdapter',
        output_adapter='chatterbot.output.TerminalAdapter',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
        database='chatterbot-database'
    )

    bot.train("chatterbot.corpus.english")

    CONVERSATION_ID = bot.storage.create_conversation()
    ev3.Sound.volume = 200
    ev3.Sound.speak('Hello ! Say something to begin').wait
    
    m = ev3.MediumMotor('outA')
    m.run_to_rel_pos(position_sp=30, speed_sp=900, stop_action="hold")
    m.run_to_rel_pos(position_sp=-30, speed_sp=900, stop_action="hold")
    
    
    print('Hello ! Say something to begin')


    
    # The following loop will execute each time the user enters input
    while True:
        try:
            input_statement = bot.input.process_input_statement()
            statement, response = bot.generate_response(input_statement, CONVERSATION_ID)
            ev3.Sound.speak('%s'%bot.output.process_response(response)).wait()
            reaction_tete = 'no'
            if reaction_tete in bot.output.process_response(response):
                m.run_to_rel_pos(position_sp=45, speed_sp=900, stop_action="hold")
                m.run_to_rel_pos(position_sp=-45, speed_sp=900, stop_action="hold")
            #print('\n Is "{}" a coherent response to "{}"? \n'.format(response, input_statement))
            # if get_feedback():
                #print("please input the correct one")
                #response1 = bot.input.process_input_statement()
                #bot.learn_response(response1, input_statement)
                #bot.storage.add_to_conversation(CONVERSATION_ID, statement, response1)
                #print("Responses added to bot!")
        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
