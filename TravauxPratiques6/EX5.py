def process_input(user_input):
    try:
        return int(user_input)/10
    except ValueError:
        return f"type invalid"
    except ZeroDivisionError:
        return f"dans la division \'diviseur\' = 0"

"""a = input("taper un nombre:")
print(process_input(a))"""
