from address_book import *


def test_contact_instantiate():
    """"Test whether contact can be instantiated without crashing."""
    
    person1 = Contact(last_name="Busch", first_name="Maia", 
                     street="123 S 2nd Street", zip_code="12345",
                     state="NY", country="USA")    
    
    
def test_contact_str():
    """Test formating of contact string."""
    
    person1 = Contact(last_name="Busch", first_name="Maia", 
                     street="123 S 2nd Street", zip_code="12345",
                     state="NY", country="USA")
            
    assert person1.__str__() == 'Busch, Maia: 123 S 2nd Street, NY, 12345, USA'

    
def test_contact_repr(): 
    """Test formating of contact repr."""
    
    person1 = Contact(last_name="Busch", first_name="Maia", 
                     street="123 S 2nd Street", zip_code="12345",
                     state="NY", country="USA")
    
    repr_str = ('<Contact(last_name="Busch", first_name="Maia", '
                'street="123 S 2nd Street", zip_code="12345", '
                'state="NY", country="USA")>')
            
    assert person1.__repr__() == repr_str
    
    
    
def test_book_instantiate(): 
    """Test whether address book can be instantiated without crashing."""
    
    AddressBook() 

    
def test_book_add_contact(): 
    """Test whether contact can be added to address book."""
    
    book = AddressBook()
    
    person1 = Contact(last_name="Busch", first_name="Maia", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    book.add_contact(person1)
    
    assert isinstance(book.contacts, dict)
    assert isinstance(book.contacts["Busch, Maia"], Contact)
    
    
def test_book_print(): 
    """Test whether contact can be added to address book."""
    
    book = AddressBook()
    
    person1 = Contact(last_name="Busch", first_name="Maia", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    book.add_contact(person1)
    
    print_str = "Busch, Maia: 123 S 2nd Street, NY, 12345, USA\n"
    
    assert book.__str__() == print_str


def test_book_get_contact(): 
    """Test whether we can get contact from address book."""
    
    book = AddressBook()
    
    person1 = Contact(last_name="Busch", first_name="Maia", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    book.add_contact(person1)
    
    assert isinstance(book.contacts, dict)
    assert isinstance(book.get_contact("Busch, Maia"), Contact)
    
    
def test_book_add_contact_disambiguation(): 
    """Test whether duplicate contacts are disambiguated."""
    
    book = AddressBook()
    
    person1 = Contact(last_name="Busch", first_name="Maia", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    book.add_contact(person1)
    book.add_contact(person1)
    
    assert isinstance(book.get_contact("Busch, Maia"), Contact)
    assert isinstance(book.get_contact("Busch, Maia #2"), Contact)   
    
    
def test_book_delete_contact(): 
    """Test whether contact can be added to address book."""
    
    book = AddressBook()
    
    person1 = Contact(last_name="Busch", first_name="Maia", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    book.add_contact(person1)
    
    person2 = Contact(last_name="Trump", first_name="Donald", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    book.add_contact(person2)
    
    book.delete_contact("Trump, Donald")
    
    assert "Trump, Donald" not in book.contacts.keys()
    
    
def test_book_update_contact():
    """Test whether we can update a contact."""
    
    book = AddressBook()
    
    person1 = Contact(last_name="Trump", first_name="Donald", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    book.add_contact(person1)
    
    book.update_contact("Trump, Donald", {"zip_code": "666"})
    
    contact_new = book.get_contact("Trump, Donald")
    
    repr_str = ('<Contact(last_name="Trump", first_name="Donald", '
            'street="123 S 2nd Street", zip_code="666", '
            'state="NY", country="USA")>')
    
    assert contact_new.__repr__() == repr_str
    

def test_book_sort_contacts():
    """Sort contacts in two directions."""

    book = AddressBook()

    person1 = Contact(last_name="Trump", first_name="Donald", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    person2 = Contact(last_name="Busch", first_name="Maia", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    book.add_contact(person1)
    book.add_contact(person2)
    
    assert book.sort_contacts("last_name", reverse=False)[0] == person2
    assert book.sort_contacts("last_name", reverse=True)[0] == person1
    
    
    
def test_book_filter_contacts():
    """Test whether we can filter by attribute. More filtering options should be implemented."""

    book = AddressBook()

    person1 = Contact(last_name="Trump", first_name="Donald", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    person2 = Contact(last_name="Busch", first_name="Maia", 
                 street="123 S 2nd Street", zip_code="12345",
                 state="NY", country="USA")
    
    book.add_contact(person1)
    book.add_contact(person2)
    
    assert len(book.filter_contacts("last_name", "startswith('Bu')")) == 1
        
    
    
    
    