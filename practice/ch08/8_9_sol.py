def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "how are u?", ":)"]
#8-9
show_messages(messages)

#8-10
sent_messages = []
send_messages(messages, sent_messages)

8-11
print("\nFinal lists:")
print(messages)
print(sent_messages)