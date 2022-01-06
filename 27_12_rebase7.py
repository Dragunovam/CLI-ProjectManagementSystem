import time


class ProjectManagement:

    def __init__(self):

        self.employee_list = ['Marco']
        self.manager_list = ['Laura']
        self.client_list = ['Coca-cola']
        self.active_project_dict = {}
        self.inactive_project_dict = {}
        self.active_ticket_dict = {}
        self.inactive_ticket_dict = {}
        self.INITIAL_MENU_OPTIONS = {'Projects': self.project_menu,
                                     'Personnel': self.personnel_menu,
                                     'Clients': self.client_menu}
        self.PROJECT_MENU_OPTIONS = {'Show projects': self.show_active_projects_menu,
                                     'Add project': self.add_project}
        self.PROJECT_ITEM_MENU_OPTIONS = {'Show tickets': self.active_project_item_show_ticket_item_menu,
                                          'Show manager': self.active_project_item_show_manager_item_menu,
                                          'Add ticket': self.add_ticket,
                                          'Close project': self.close_project}
        self.PROJECT_TICKET_ITEM_OPTIONS = {'Show employee(s)': None,
                                            'Add employee': None,
                                            'Close ticket': None}
        self.PROJECT_TICKET_EMPLOYEES_OPTIONS = {'Remove employee': self.remove_employee}
        self.PROJECT_TICKET_EMPLOYEES_ITEM_OPTIONS = {}
        self.PROJECT_MANAGER_ITEM_OPTIONS = {}
        self.ADD_PERSONNEL_MENU_OPTIONS = {'Add manager': self.add_manager,
                                           'Add employee': self.add_employee}
        self.PERSONNEL_MENU_OPTIONS = {'Show personnel': self.show_personnel_menu,
                                       'Add personnel': self.add_personnel_menu}
        self.SHOW_EMPLOYEE_ITEM_MENU_OPTIONS = {'Remove employee': self.remove_employee}
        self.SHOW_MANAGER_ITEM_MENU_OPTIONS = {'Remove manager': self.remove_manager}
        self.CLIENT_MENU_OPTIONS = {'Show clients': self.show_clients_menu,
                                    'Add clients': self.add_client}
        self.SHOW_CLIENT_ITEM_MENU_OPTIONS = {'Remove client': self.remove_client}
        self.SHOW_PERSONNEL_MENU_OPTIONS = {'Show managers': self.show_managers_menu,
                                            'Show employees': self.show_employees_menu}
        self.ACTIVE_PROJECT_MENU_OPTIONS = {'Show tickets': None,
                                            'Add tickets': None}

        self.initial_menu()

    def sleep_timer(self):
        time.sleep(3)

    def menu_terminator(self, external_dict):
        if external_dict != self.INITIAL_MENU_OPTIONS:
            print('0. Previous menu')

    def clear_screen(self):
        print('\n' * 40)

    def input_validation_static_dict(self,
                                     external_dict,
                                     previous_menu=None,
                                     location=None,
                                     function_pointer=None,
                                     argument=None,
                                     passthrough=False):
        self.clear_screen()
        if external_dict == self.INITIAL_MENU_OPTIONS:
            self.banner_print()
        print(location)
        menu_options = {}
        for position, menu_option in enumerate(external_dict):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        if passthrough is False:
            self.menu_terminator(external_dict)
        else:
            print('0. Cancel')
        while True:
            choice = input('Choose a menu option: ')
            try:
                choice = int(choice)
                if choice == 0:
                    if external_dict == self.INITIAL_MENU_OPTIONS:
                        print('Thank you for using Project management system, have a good day!')
                        self.sleep_timer()
                        # Export to JSON file
                        break
                    else:
                        previous_menu()
                        break
                elif choice in menu_options:
                    if passthrough is True:
                        return menu_options[choice]
                    elif function_pointer is not None:
                        if argument is None:
                            function_pointer(menu_options[choice])
                            break
                        else:
                            function_pointer(argument)
                            break
                    else:
                        if argument is None:
                            external_dict[menu_options[choice]]()
                            break
                        else:
                            external_dict[menu_options[choice]](argument)
                            break
            except Exception:
                print('\n', '*' * 10, 'You input is not valid, try again', '*' * 10, '\n')
                self.sleep_timer()

    def input_validation_list(self, external_list, previous_menu, passthrough=False):
        self.clear_screen()
        while True:
            name = input('Enter a name, enter "/" to exit: ').lower().capitalize()
            if passthrough is True:
                if name == '/':
                    previous_menu()
                else:
                    return name
            elif name.isalpha():
                if name not in external_list:
                    external_list.append(name)
                    print('{} successfully added'.format(name))
                    print(external_list)
                    self.sleep_timer()
                    previous_menu()
                    break
                else:
                    print('This name is already in the list, enter another name')
                    self.sleep_timer()
            else:
                if name == '/':
                    print('Going back to previous menu')
                    self.sleep_timer()
                    previous_menu()
                    break
                else:
                    print('This input is invalid')
                    self.sleep_timer()

    def add_employee(self):
        self.input_validation_list(self.employee_list, self.add_personnel_menu)

    def add_manager(self):
        self.input_validation_list(self.manager_list, self.add_personnel_menu)

    def remove_employee(self, employee_name):
        for key in self.active_ticket_dict:
            if employee_name in self.active_ticket_dict[key]['workers']:
                print('This employee/manager is working on an active ticket/project, close that ticket/project first.')
                self.sleep_timer()
                self.show_personnel_menu()
                break
        self.employee_list.remove(employee_name)
        print('{} successfully removed'.format(employee_name))
        self.sleep_timer()
        self.show_personnel_menu()

    def remove_manager(self, manager_name):
        for element in self.active_project_dict:
            if manager_name in self.active_project_dict[element]['manager_name']:
                print('This manager is working on an active project, add a second manager first')
                self.sleep_timer()
                self.show_personnel_menu()
                break
        self.manager_list.remove(manager_name)
        print('{} successfully removed'.format(manager_name))
        self.sleep_timer()
        self.show_personnel_menu()

    def add_client(self):
        self.input_validation_list(self.client_list, self.client_menu)

    def remove_client(self, client_name):
        for element in self.active_project_dict:
            if client_name in self.active_project_dict[element]['client_name']:
                print('This client is involved in an active project called "{}", close that project first'.
                      format(element))
                self.sleep_timer()
                self.show_clients_menu()
                break
        self.client_list.remove(client_name)
        print('{} successfully removed'.format(client_name))
        self.sleep_timer()
        self.show_clients_menu()

    def add_project(self):
        client_name = self.input_validation_static_dict(self.client_list,
                                                        self.project_menu,
                                                        'Choose a Client',
                                                        None,
                                                        None,
                                                        True)
        manager_name = self.input_validation_static_dict(self.manager_list,
                                                         self.project_menu,
                                                         'Choose a manager',
                                                         None,
                                                         None,
                                                         True)

        while True:
            project_name = self.input_validation_list(self.active_project_dict, self.project_menu, True)
            if project_name not in self.active_project_dict:
                self.active_project_dict[project_name] = {
                    'client_name': client_name,
                    'manager_name': manager_name,
                    'active_tickets': {},
                    'inactive_tickets': {}
                }
                print('Project "{}" successfully added'.format(project_name))
                self.sleep_timer()
                self.project_menu()
                break
            else:
                print('This project already exists, choose another value or exit.')

    def close_project(self):
        project_name = self.input_validation_static_dict(self.active_project_dict,
                                                         self.project_menu,
                                                         'Choose a project',
                                                         None,
                                                         None,
                                                         True)
        if self.active_project_dict[project_name]['active_tickets'] != {}:
            print('This project can not be closed, it is used in an active ticket')
            self.sleep_timer()
            self.project_item_menu(project_name)
            # TICKET_MENU
        self.active_project_dict[project_name] = self.inactive_project_dict[project_name]
        del self.active_project_dict[project_name]
        print('Project "{}" successfully closed'.format(project_name))
        self.sleep_timer()
        self.project_menu()

    def remove_project(self, project_name):
        for ticket in self.active_ticket_dict:
            if project_name == self.active_ticket_dict[ticket]['project_name']:
                print('This project can not be removed, it is used in an active ticket')
                break
        del self.active_project_dict[project_name]

    def add_ticket(self, project_name):
        employee_name = self.input_validation_static_dict(self.employee_list,
                                                          self.project_menu,
                                                          'Choose an employee',
                                                          None,
                                                          None,
                                                          True)
        manager_name = self.active_project_dict[project_name]['manager_name']
        client_name = self.active_project_dict[project_name]['client_name']
        while True:
            ticket_name = self.input_validation_list(self.active_ticket_dict, self.project_menu, True)
            if ticket_name not in self.active_ticket_dict and ticket_name not in self.inactive_ticket_dict:
                self.active_project_dict[project_name]['tickets'].append(ticket_name)
                self.active_ticket_dict[ticket_name] = {
                    'project_name': project_name,
                    'client_name': client_name,
                    'manager_name': manager_name,
                    'workers': [employee_name]}
                print('Ticket "{}" successfully added'.format(ticket_name))
                self.sleep_timer()
                self.project_item_menu(project_name)
                break
            else:
                print('This ticket already exists, choose another value or exit.')

    def close_ticket(self, ticket_name):
        if self.active_ticket_dict[ticket_name]:
            self.active_ticket_dict[ticket_name] = self.inactive_ticket_dict[ticket_name]
            del self.active_ticket_dict[ticket_name]
            print('The ticket is now closed.')
        else:
            print('The selected ticket does not exist in the active ticket list')

    def remove_ticket(self, ticket_name):
        if self.active_ticket_dict[ticket_name]:
            del self.active_ticket_dict[ticket_name]
            print('The ticket has been removed')
        else:
            print('The selected ticket does not exist')

    def initial_menu(self):
        self.input_validation_static_dict(self.INITIAL_MENU_OPTIONS,
                                          self.initial_menu,
                                          'Initial menu')

    def personnel_menu(self):
        self.input_validation_static_dict(self.PERSONNEL_MENU_OPTIONS,
                                          self.initial_menu,
                                          'Initial menu->Personnel')

    def show_personnel_menu(self):
        self.input_validation_static_dict(self.SHOW_PERSONNEL_MENU_OPTIONS,
                                          self.personnel_menu,
                                          'Initial menu->Personnel->Show personnel')

    def add_personnel_menu(self):
        self.input_validation_static_dict(self.ADD_PERSONNEL_MENU_OPTIONS,
                                          self.personnel_menu,
                                          'Initial menu->Personnel->Add personnel')

    def show_employees_menu(self):
        self.input_validation_static_dict(self.employee_list,
                                          self.show_personnel_menu,
                                          'Initial menu->Personnel->Show personnel->Show employees',
                                          self.show_employee_item_menu)

    def show_employee_item_menu(self, argument):
        self.input_validation_static_dict(self.SHOW_EMPLOYEE_ITEM_MENU_OPTIONS,
                                          self.show_employees_menu,
                                          'Initial menu->Personnel->Show personnel->Show employees->{}'.format(
                                              argument),
                                          None,
                                          argument
                                          )

    def show_managers_menu(self):
        self.input_validation_static_dict(self.manager_list,
                                          self.show_personnel_menu,
                                          'Initial menu->Personnel->Show personnel->Show managers',
                                          self.show_manager_item_menu)

    def show_manager_item_menu(self, argument):
        self.input_validation_static_dict(self.SHOW_MANAGER_ITEM_MENU_OPTIONS,
                                          self.show_employees_menu,
                                          'Initial menu->Personnel->Show personnel->Show managers->{}'.format(argument),
                                          None,
                                          argument
                                          )

    def client_menu(self):
        self.input_validation_static_dict(self.CLIENT_MENU_OPTIONS,
                                          self.initial_menu,
                                          'Initial menu->Clients')

    def show_clients_menu(self):
        self.input_validation_static_dict(self.client_list,
                                          self.client_menu,
                                          'Initial menu->Clients->Show clients',
                                          self.show_client_menu_item)

    def show_client_menu_item(self, argument):
        self.input_validation_static_dict(self.SHOW_CLIENT_ITEM_MENU_OPTIONS,
                                          self.show_clients_menu,
                                          'Initial menu->Clients->Show clients->{}'.format(argument),
                                          None,
                                          argument)

    def project_menu(self):
        self.input_validation_static_dict(self.PROJECT_MENU_OPTIONS,
                                          self.initial_menu,
                                          'Initial menu->Projects')

    def show_active_projects_menu(self):
        self.input_validation_static_dict(self.active_project_dict.keys(),
                                          self.project_menu,
                                          'Initial menu->Projects->Show projects',
                                          self.project_item_menu
                                          )

    def project_item_menu(self, argument):
        self.input_validation_static_dict(self.PROJECT_ITEM_MENU_OPTIONS,
                                          self.show_active_projects_menu,
                                          'Initial menu->Projects->Show projects->{}'.format(argument),
                                          None,
                                          argument)

    def active_project_item_show_ticket_item_menu(self, argument):
        self.input_validation_static_dict(self.active_project_dict[argument]['active_tickets'],
                                          self.project_item_menu(argument),
                                          'Initial menu->Projects->Show projects->{}->Show tickets'.format(argument),
                                          None,
                                          argument)

    def active_project_item_show_manager_item_menu(self, argument):
        self.input_validation_static_dict(self.active_project_dict[argument]['managers'],
                                          self.project_item_menu(argument),
                                          'Initial menu->Projects->Show projects->{}->Show managers'.format(argument),
                                          None,
                                          argument)
        pass

    def banner_print(self):
        print(r"""
        #########################################################################
        ╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐  ┌┬┐┌─┐┌┐┌┌─┐┌─┐┌─┐┌┬┐┌─┐┌┐┌┌┬┐  ┌─┐┬ ┬┌─┐┌┬┐┌─┐┌┬┐
        ╠═╝├┬┘│ │ │├┤ │   │   │││├─┤│││├─┤│ ┬├┤ │││├┤ │││ │   └─┐└┬┘└─┐ │ ├┤ │││
        ╩  ┴└─└─┘└┘└─┘└─┘ ┴   ┴ ┴┴ ┴┘└┘┴ ┴└─┘└─┘┴ ┴└─┘┘└┘ ┴   └─┘ ┴ └─┘ ┴ └─┘┴ ┴
        #########################################################################
        """)


project = ProjectManagement()
