import time


class ProjectManagement:
    import time

    def __init__(self):

        self.employee_list = []
        self.manager_list = []
        self.client_list = []

        self.active_project_dict = {}
        self.inactive_project_dict = {}
        self.active_ticket_dict = {}
        self.inactive_ticket_dict = {}

        self.INITIAL_MENU_OPTIONS = {'Projects': self.project_menu,
                                     'Personnel': self.personnel_menu,
                                     'Clients': self.client_menu}
        self.PROJECT_MENU_OPTIONS = {'Show projects': self.active_project_menu,
                                     'Add project': self.add_project}
        self.PERSONNEL_MENU_OPTIONS = {'Show personnel': self.show_personnel_menu,
                                       'Add personnel': self.add_employee}
        self.CLIENT_MENU_OPTIONS = {'Show clients': self.show_clients_menu,
                                    'Add clients': self.add_client}
        self.SHOW_PERSONNEL_MENU_OPTIONS = {'Show managers': None,
                                            'Show employees': None}
        self.ACTIVE_PROJECT_MENU_OPTIONS = {'Show tickets': None,
                                            'Add tickets': None}

        self.initial_menu()

    def menu_terminator(self, external_dict):
        if external_dict != self.INITIAL_MENU_OPTIONS:
            print('0. Previous menu')

    def clear_screen(self):
        print('\n' * 40)

    def input_validation_dict(self, external_dict, previous_menu):
        self.clear_screen()
        if external_dict == self.INITIAL_MENU_OPTIONS:
            self.banner_print()
        menu_options = {}
        for position, menu_option in enumerate(external_dict):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        self.menu_terminator(external_dict)
        while True:
            choice = input('Choose a menu option: ')
            try:
                choice = int(choice)
                if int(choice) == 0:
                    previous_menu()
                    break
                elif int(choice) in menu_options:
                    external_dict[menu_options[choice]]()
                    break
            except Exception:
                print('\n', '*' * 10, 'You input is not valid, try again', '*' * 10, '\n')
                time.sleep(3)

    def add_employee(self, employee_name):
        while True:
            employee_name = input('Enter an employee name: ')
            if employee_name.isalpha():
                if employee_name.casefold() not in self.employee_list:
                    self.employee_list.append(employee_name)
                    break
                else:
                    print('This employee is already in the list, enter another name')
            else:
                print('This input is invalid')

    def remove_employee(self, employee_name):
        for key in self.active_ticket_dict:
            if employee_name in self.active_ticket_dict[key]['workers'].values() and \
                    len(self.active_ticket_dict[key]['workers'].values()) < 2:
                print('This employee is working on an active ticket, add a second employee first')
                break
        del self.employee_list[employee_name]

    def add_manager(self, manager_name):
        while True:
            if manager_name.isalpha():
                if manager_name.casefold() not in self.manager_list:
                    self.manager_list.append(manager_name)
                    print('Manager successfully added')
                    break
                else:
                    print('This manager is already in the list, enter another name')
            else:
                print('This input is incorrect, try again')

    def remove_manager(self, manager_name):
        for element in self.active_project_dict.values():
            if manager_name in element and len(element) < 3:
                print('This manager is working on an active project, add a second manager first')
                break
        del self.manager_list[manager_name]
        print('Manager successfully removed')

    def add_client(self, client_name):
        while True:
            if client_name.isalpha():
                if client_name.casefold() not in self.client_list:
                    self.client_list.append(client_name)
                    print('Client successfully added')
                    break
                else:
                    print('This client is already in the list')
            else:
                print('This input is incorrect, try again')

    def remove_client(self, client_name):
        for project in self.active_project_dict:
            if client_name == self.active_project_dict[project]['client_name'].values():
                break
        del self.client_list[client_name]

    def add_project(self, project_name, client_name, manager_name, ):
        while True:
            if project_name.isalpha():
                if project_name.casefold() not in self.active_project_dict.keys():
                    self.active_project_dict[project_name] = {
                        'client_name': client_name,
                        'manager_name': manager_name
                    }
                    break
                else:
                    print('This project is already in the list')
            else:
                print('This input is incorrect, try again')

    def close_project(self, project_name):
        for tickets in self.active_ticket_dict:
            if project_name == self.active_ticket_dict['project_name'].values():
                print('This project can not be closed, it is used in an active ticket')
                break
        self.active_project_dict[project_name] = self.inactive_project_dict[project_name]
        del self.inactive_project_dict[project_name]

    def remove_project(self, project_name):
        for ticket in self.active_ticket_dict:
            if project_name == self.active_ticket_dict[ticket]['project_name']:
                print('This project can not be removed, it is used in an active ticket')
                break
        del self.active_project_dict[project_name]

    def add_ticket(self, ticket_name, project_name, employee_name):
        client_name, manager_name = self.active_project_dict[project_name]
        while True:
            if ticket_name.isalpha():
                if ticket_name.casefold() not in self.active_ticket_dict \
                        and self.inactive_ticket_dict:
                    self.active_ticket_dict[ticket_name] = \
                        {'project_name': project_name,
                         'client_name': client_name,
                         'manager_name': manager_name,
                         'workers': [employee_name]}

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
        self.input_validation_dict(self.INITIAL_MENU_OPTIONS, self.initial_menu)

    def project_menu(self):
        print('Initial menu->Projects')
        self.input_validation_dict(self.PROJECT_MENU_OPTIONS, self.initial_menu)

    def personnel_menu(self):
        print('Initial menu->Personnel')
        self.input_validation_dict(self.PERSONNEL_MENU_OPTIONS, self.initial_menu)

    def show_personnel_menu(self):
        print('Initial menu->Personnel->Show personnel')
        self.input_validation_dict(self.SHOW_PERSONNEL_MENU_OPTIONS, self.personnel_menu)

    def client_menu(self):
        print('Initial menu->Clients')
        self.input_validation_dict(self.CLIENT_MENU_OPTIONS, self.initial_menu)

    def show_clients_menu(self):
        menu_options = {}
        print('Initial menu->Clients->Show clients')
        for position, menu_option in enumerate(self.client_list):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        print('0. Previous menu')

    def show_projects_menu(self):
        menu_options = {}
        print('Initial menu->Projects->Show projects')
        for position, menu_option in enumerate(self.active_project_dict):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        print('0. Previous menu')
        while True:
            choice = input()
            if choice == 0:
                self.project_menu()
            if choice in menu_options.keys():
                pass

    def active_project_menu(self):
        menu_options = {}
        print('Initial menu->Projects->Show projects')

    def menu_generator_from_list(self, list):
        menu_options = {}
        for position, menu_option in enumerate(list):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        print('0. Previous menu')

    def menu_generator_from_dict(self, dict):
        menu_options = {}
        for position, menu_option in enumerate(dict.keys):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        print('0. Previous menu')

    def banner_print(self):
        print(r"""
        #########################################################################
        ╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐  ┌┬┐┌─┐┌┐┌┌─┐┌─┐┌─┐┌┬┐┌─┐┌┐┌┌┬┐  ┌─┐┬ ┬┌─┐┌┬┐┌─┐┌┬┐
        ╠═╝├┬┘│ │ │├┤ │   │   │││├─┤│││├─┤│ ┬├┤ │││├┤ │││ │   └─┐└┬┘└─┐ │ ├┤ │││
        ╩  ┴└─└─┘└┘└─┘└─┘ ┴   ┴ ┴┴ ┴┘└┘┴ ┴└─┘└─┘┴ ┴└─┘┘└┘ ┴   └─┘ ┴ └─┘ ┴ └─┘┴ ┴
        #########################################################################
        """)


project = ProjectManagement()
