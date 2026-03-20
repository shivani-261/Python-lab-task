def validate_name_and_contact(func):
    def wrapper(name,contact_number):
        if not name or not isinstance(name,str):
            return "Name must be a non-empty string."
        if len(contact_number)!=10 or not contact_number.isdigit():
            return"contact number must be a 10-digit number."
        return func(name,contact_number)
    return wrapper

validate_name_and_contact
def register_user(name,contact_number):
    return f"User{name}with contact number{contact_number}has been successfully registerd."
print(register_user("Alice","1234567890"))
print(register_user("","1234567890"))
print(register_user("Bob","12345"))
print(register_user("Charlie","123abc7890"))
