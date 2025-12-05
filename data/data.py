class UsersTestData:
    email = 'emil_samigullin_31_123@ya.ru'
    password = 'English!'
    username = 'Emil'
    
    def contains_null_byte(data):
    #Проверка на null bytes в строке или bytes
        if isinstance(data, str):
            return '\x00' in data or '%00' in data
        elif isinstance(data, bytes):
            return b'\x00' in data
        return False

def sanitize_input(data):
   
    if isinstance(data, str):
        return data.replace('\x00', '').replace('%00', '')
    elif isinstance(data, bytes):
        return data.replace(b'\x00', b'')
    return data