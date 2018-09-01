import json, boto3, itertools

# Without SSML, Alexa says 995 as "nine hundred and ninety five"
def sub_995(s):
    return s.replace('995', '<say-as interpret-as="digits">995</say-as>')

WELCOME_MSG = 'Welcome to Akinjury. How can I help you?'
ABOUT_MSG = sub_995("Hi there, I'm a first aid assistant. I can diagnose injuries and give step by step treatment. However, if you are unsure of any of the steps, please seek a doctor or call 995 immediately.")
NO_INJURY_MSG = 'You have to tell me what injury you have first before I can give you the treatment.'
DK_INJURY_MSG = sub_995("Sorry, I don't know how to treat that injury. Please ask a doctor or call 995 immediately.")
UNSURE_MSG = sub_995('If you are unsure about any of the steps, please see a doctor or call 995 immediately.')
DIDNT_UNDERSTAND_MSG = "Sorry, I didn't understand that."

cur_injury = None
tries = 0

STOP_DIALOG = 0
CONTINUE_DIALOG = 1
NO_INJURY = 0
MULTIPLE_INJURIES = 1

step = -1
injury = ''
diagnosed_injury = ''

# OUTPUT FUNCTIONS
def build_response(speech_message):
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": speech_message,
    }

def speech_response(output):
    return build_response({
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            }
        },
        'shouldEndSession': False
    })

def ssml_response(output):
    output = '<speak>' + output + '</speak>'
    return build_response({
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': output
            }
        },
        'shouldEndSession': False
    })

def response(output):
    if '<' in output and '>' in output:
        return ssml_response(output)
    return speech_response(output)

# UTILITY FUNCTIONS
def slot_filled(req, name):
    return 'value' in req['intent']['slots'][name].keys()

def get_slot(req, name):
    if not slot_filled(req, name): return ''
    if 'resolutions' in req['intent']['slots'][name].keys() and name != 'loc':
        try:
            return req['intent']['slots'][name]['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
        except KeyError: return ''
    else:
        return req['intent']['slots'][name]['value']

def load_data():
    global locationd, typed, paind, symptomsd, treatmentd, injuries, injuries
    with open("location.json") as f:
        data = json.load(f)
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table("akinjurydata")
    res = list(table.scan()["Items"])

    locationd = res[0]
    typed = res[1]
    paind = res[2]
    symptomsd = res[3]
    treatmentd = res[4]

    for i in locationd.keys(): locationd[i] = locationd[i].split(";")
    for i in typed.keys(): typed[i] = typed[i].split(";")
    for i in paind.keys(): paind[i] = paind[i].split(";")
    for i in symptomsd.keys(): symptomsd[i] = symptomsd[i].split(";")
    for i in treatmentd.keys(): treatmentd[i] = treatmentd[i].split(';')
    del locationd["akinjury"], typed["akinjury"], paind["akinjury"], symptomsd["akinjury"], treatmentd['akinjury']

    injuries = set([i for j in typed.values() for i in j])


# DIALOG FLOW
def continue_dialog():
    return build_response(
        {'shouldEndSession': False,
         'directives': [{'type':'Dialog.Delegate'}]}
    )

def on_session_started(): return
def on_session_ended(): return
def on_launch(request):
    load_data()
    return response(WELCOME_MSG)


# ON_INTENT
def on_intent(request, session):
    global tries, injuries, step, diagnosed_injury, injury
    name = request["intent"]["name"]

    if name == "init":
        step = -1
        return response(WELCOME_MSG)

    if name == 'about':
        step = -1
        return response(ABOUT_MSG)

    if name == "treat":
        if not slot_filled(request, 'injury'): return continue_dialog()

        # If the skill has already identified the injury and the user
        # then wants to know how to treat it, use the diagnosed injury
        injury = (get_slot(request, 'injury') if diagnosed_injury == '' else diagnosed_injury)
        diagnosed_injury = ''

        print(injury, injuries)

        if injury in injuries:
            # Start from the beginning
            step = 0
            return response(cur_step(treatmentd[injury]))
        else:
            return response(DK_INJURY_MSG)

    if name == "next_step":
        # The user has not indicated what injury to treat yet
        if step == -1: return response(NO_INJURY_MSG)
        step += 1
        return response(cur_step(treatmentd[injury]))

    if name == 'repeat_step':
        # The user has not indicated what injury to treat yet
        if step == -1: return response(NO_INJURY_MSG)
        return response(cur_step(treatmentd[injury]))

    if name == 'previous_step':
        # The user has not indicated what injury to treat yet
        if step == -1: return response(NO_INJURY_MSG)
        step -= 1
        return response(cur_step(treatmentd[injury]))

    if name == 'start_over':
        # The user has not indicated what injury to treat yet
        if step == -1: return response(NO_INJURY_MSG)
        step = 0
        return response(cur_step(treatmentd[injury]))

    if name == 'not_sure':
        if step == -1: return response(DIDNT_UNDERSTAND_MSG)
        return response(UNSURE_MSG)

    if name == "identify":
        step = -1
        diagnosed_injury = ''
        for i in ['painlvl', 'loc', 'symone', 'type']:
            if not slot_filled(request, i):
                return continue_dialog()

    # This intent is meant to handle the response to the question 'Would you like to know the treatment steps?'
    if name == 'give_treatment':
        # If the user did not ask for injury diagnosis
        if diagnosed_injury == '':
            return response(DIDNT_UNDERSTAND_MSG)

        injury = diagnosed_injury
        diagnosed_injury = ''
        print(injury, diagnosed_injury)
        if injury in injuries:
            step = 0
            return response(cur_step(treatmentd[injury]))
        else:
            return response(DK_INJURY_MSG)

    if name == 'dont_give_treatment':
        # If the user did not ask for injury diagnosis
        if diagnosed_injury == '':
            return response(DIDNT_UNDERSTAND_MSG)

        return response('Okay.')

    type = get_slot(request, 'type')
    try:
        pain = int(get_slot(request, 'painlvl'))
    except ValueError:
        pain = 0
    location = get_slot(request, 'loc')

    # STOP ASKING FOR SYMPTOMS IF NO

    symptoms = []
    if slot_filled(request, 'symone') and not slot_filled(request, 'symtwo'):
        tries = 1
        symptoms.append(get_slot(request, 'symone'))
    elif slot_filled(request, 'symtwo') and not slot_filled(request, 'symthree'):
        tries = 2
        symptoms.append(get_slot(request, 'symtwo'))
    elif slot_filled(request, 'symthree') and not slot_filled(request, 'symfour'):
        tries = 3
        symptoms.append(get_slot(request, 'symthree'))
    else:
        tries = 4
        symptoms.append(get_slot(request, 'symfour'))

    res_type, res = classify(type, location, symptoms, pain)
    if res_type == STOP_DIALOG:
        if res == NO_INJURY:
            return response(sub_995('Sorry, I could not find an injury matching your symptoms. Please see a doctor or call 995 immediately.'))
        elif res == MULTIPLE_INJURIES:
            return response(sub_995('Sorry, I do not have enough data to make a diagnosis. Please see a doctor or call 995 immediately.'))
        else:
            diagnosed_injury = res
            prefix = ('an' if res[0] in ('aeiou') else 'a')
            return response('It seems that you have {} {}. Would you like to know the treatment steps?'.format(prefix, res))
    else:
        return continue_dialog()


def cur_step(treatment):
    global step
    if step >= len(treatment):
        step -= 1
        return 'There are no more steps to the treatment. Do recover soon!'
    if step < 0:
        step = 0
        return 'You are already at the first step.'
    return 'Step {}, {}'.format(step+1, treatment[step])


def classify(type, location, symptoms, pain):
    global locationd, typed, paind, symptomsd, injuries, injuries, tries

    ans = injuries

    if 1 <= pain <= 3: ans = ans.intersection(set(paind["minor"]))
    elif 3 <= pain <= 7: ans = ans.intersection(set(paind["moderate"]))
    elif 8 <= pain <= 10: ans = ans.intersection(set(paind["fatal"]))

    injuries_with_locs = [i for j in locationd.values() for i in j]
    ans_list = list(ans)
    ans_applicable = set([i for i in ans if i in injuries_with_locs])
    ans_inapplicable = set([i for i in ans if i not in injuries_with_locs])
    if location in locationd.keys():
        ans_applicable = ans_applicable.intersection(set(locationd[location]))
        ans = ans_applicable.union(ans_inapplicable)

    if type in typed.keys():
        ans = ans.intersection(set(typed[type]))

    for s in symptoms:
        if s in symptomsd.keys():
            print(ans, set(symptomsd[s]))
            ans = ans.intersection(set(symptomsd[s]))

    if len(ans) == 0:
        return STOP_DIALOG, NO_INJURY
    elif len(ans) == 1:
        return STOP_DIALOG, list(ans)[0]
    elif len(ans) > 1 and tries >= 4:
        return STOP_DIALOG, MULTIPLE_INJURIES
    elif len(ans) > 1 and tries < 4:
        return CONTINUE_DIALOG, None


# LAMBDA HANDLER
def lambda_handler(event, context):
    load_data()
    if event["session"]["new"]: on_session_started()
    if event["request"]["type"] == "LaunchRequest": return on_launch(event["request"])
    elif event["request"]["type"] == "SetssionEndedRequest": return on_session_ended()
    elif event["request"]["type"] == "IntentRequest": return on_intent(event["request"], event["session"])
    
