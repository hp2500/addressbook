class Contact: 
    """
    Instance represents an individual contact. 
    """
    
    def __init__(self, last_name, first_name, 
                 street=None, zip_code=None, state=None, 
                 country=None):
         
        self.last_name = last_name
        self.first_name = first_name
        self.street = street
        self.zip_code = zip_code
        self.state = state
        self.country = country
        
    def __str__(self):
        
        str_str = (f"{self.last_name}, {self.first_name}: "
                   f"{self.street}, {self.state}, {self.zip_code}, {self.country}")
        
        return str_str
        
        
    def __repr__(self):
        
        repr_str = (f'<Contact(last_name="{self.last_name}", first_name="{self.first_name}", '
                    f'street="{self.street}", zip_code="{self.zip_code}", '
                    f'state="{self.state}", country="{self.country}")>')

        return repr_str
        


class AddressBook:
    """
    Instance represents an address book with multiple contacts.
    """
    
    def __init__(self): 
        
        self.contacts = {}
        
        
    def __str__(self):
        
        str_str = ""
        
        for i in self.contacts.values(): 
            
            str_str = str_str+i.__str__()+"\n"
        
        return str_str
    
    
    def add_contact(self, contact):
        """Add contact to address book."""
        
        key = contact.last_name+", "+contact.first_name
        
        disambiguator = 2
        
        while key in self.contacts.keys():
            
            key = key.split(" #")[0]
            
            key = key+" #"+str(disambiguator)
                        
            disambiguator+=1
        
        self.contacts[key] = contact
        
        
    def get_contact(self, full_name):
        """Return contact by full name identifier."""
        
        return self.contacts[full_name]
        
        
    def delete_contact(self, full_name):
        """Delete contact from address book."""
        
        del self.contacts[full_name]
        
        
    def update_contact(self, full_name, update_dict):
        """Update information of a contact."""
        
        contact_updated = self.contacts[full_name]
        
        for i in update_dict:
            
            setattr(contact_updated, i, update_dict[i])
            
        self.contacts[full_name] = contact_updated
        
     
    def sort_contacts(self, key, reverse=False):
        """"Sort contacts by chosen key."""
                
        return sorted(self.contacts.values(), key=lambda x: getattr(x, key), reverse=reverse)
    
        
    def filter_contacts(self, key, condition):
        """Filter contacts by string condition. Only tested this for startswith(). Will break in other cases."""
        
        condition_str = f'getattr(i, "{key}").{condition}'
                        
        return [i for i in self.contacts.values() if eval(condition_str)]
        