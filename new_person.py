import telephone_book as tb
import view

t_book = {}



def writing_down(t_book: dict):
    name = view.get_name()
    phone = view.get_number()
    action = view. what_to_do()
    if action == 'новый контакт':
        if name[0] not in t_book:
            tb.create_new_list(name, t_book, phone)
        tb.create_new_note(name, t_book[name[0]], phone)
    elif action == 'смена номера':
        tb.update_note(name, t_book[name[0]], phone)
    elif action == 'дополнительный номер':
        tb.append_number(name, phone, t_book[name[0]])
    elif action == 'удалить номер':
        tb.delete_note(name, t_book[name[0]])
    return t_book