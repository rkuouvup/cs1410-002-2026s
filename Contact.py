class Contact:
    all_contacts: list["Contact"] = []
    def __init__(self, name:str = "No Name", email:str = "") -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order() -> None:
        print("Order")
def main() -> None:
    c = Contact("Amy", "amy@example.com")
    s = Supplier("Betty", "betty@example.com")
    print(c.name)
    print(s.name)
    s.order()
    c.order()
if __name__ == "__main__":
    main()