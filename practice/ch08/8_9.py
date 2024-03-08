short_messages = ['hello', 'goodbye', 'hi']
sent_messages1 = []
sent_messages2 = []

def show_message(short_messages):
    """짧은 문자를 모두 출력"""
    for short_message in short_messages:
        print(f"show_messages : {short_message}")

def send_messages1(short_messages):
    """문자열을 수정"""
    sent_messages1=short_messages[:] #deepcopy
    sent_messages1.append('byebye')
    for  sent_message1 in  sent_messages1:
        print(f"send_messages1 : {sent_message1}")

def send_messages2(short_messages):
    while short_messages:
        current_messages = short_messages.pop() #for short_message in short_message하면 copy만 됨
        sent_messages2.append(current_messages)
    for  sent_message2 in  sent_messages2:
        print(f"send_messages2 : {sent_message2}")
   
        


show_message(short_messages)
send_messages1(short_messages)
send_messages2(short_messages)

