from message_formatter.message_formatter import space_border, galaxy_effect

@space_border
@galaxy_effect
def greet(message):
    return message

if __name__ == "__main__":
    print(greet("Welcome to Space Adventures!"))
