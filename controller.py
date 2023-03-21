import manager_
import view



def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                manager_.open_file()
                view.init_flag()
            case 2:
                manager_.save_file()
            case 3:
                pb = manager_.get()
                view.show_contact(pb)
            case 4:
                new = view.new_contact_input()
                manager_.add(new)
            case 5:
                pb = manager_.get()
                view.show_contact(pb)
                index = view.input_id()
                contact = view.new_contact_input()
                manager_.change_contact(index, contact)
            case 6:
                find = view.search_contact()
                result = manager_.find(find)
                view.show_contact(result)
            case 7:
                pb = manager_.get()
                view.show_contact(pb)
                index = view.input_id()
                name = manager_.get_name(index)
                if view.confirm('удалить', name):
                    manager_.delete_contact(index)
            case 8:
                if manager_.check_changes():
                    if view.confirm_changes():
                        manager_.save_file()
                print('Досвидания!')
                break
