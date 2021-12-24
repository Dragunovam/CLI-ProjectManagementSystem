class ProjectManagement:

    def __init__(self):

        self.employee_list = []
        self.manager_list = []
        self.client_list = []

        self.active_project_dict = {}
        self.inactive_project_dict = {}
        self.active_ticket_dict = {}
        self.inactive_ticket_dict = {}

        self.INITIAL_MENU_OPTIONS = ['Projects', 'Personnel', 'Clients']
        self.PROJECT_MENU_OPTIONS = ['Show projects', 'Add project']
        self.PERSONNEL_MENU_OPTIONS = ['Show personnel', 'Add personnel']
        self.CLIENT_MENU_OPTIONS = ['Show clients', 'Add clients']
        self.SHOW_PERSONNEL_MENU_OPTIONS = ['Show managers', 'Show employees']

    def add_employee(self, employee_name):
        while True:
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

    # def numbered_list_print(self, position, item):
    #     print('{}. {}'.format(position + 1, item))
    #
    # def numbered_list_print(self, menu_list):
    #     for position, menu_option in enumerate(menu_list):
    #         print('{}. {}'.format(position + 1, menu_option))

    def initial_menu(self):
        menu_options = {}
        print('Initial menu')
        for position, menu_option in enumerate(self.INITIAL_MENU_OPTIONS):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        choice = input('Choose a menu option')
        if choice == 1:
            self.project_menu()
        elif choice == 2:
            self.personnel_menu()
        elif choice == 3:
            self.client_menu()
        # TODO rework the whole choice section via while loop and or different implementation

    def project_menu(self):
        menu_options = {}
        print('Initial menu->Projects')
        for position, menu_option in enumerate(self.PROJECT_MENU_OPTIONS):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        print('0. Previous menu')
        print('\n' * 10)

    def personnel_menu(self):
        menu_options = {}
        print('Initial menu->Personnel')
        for position, menu_option in enumerate(self.PERSONNEL_MENU_OPTIONS):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        print('0. Previous menu')

    def client_menu(self):
        menu_options = {}
        print('Initial menu->Clients')
        for position, menu_option in enumerate(self.CLIENT_MENU_OPTIONS):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        print('0. Previous menu')

    def show_projects_menu(self):
        menu_options = {}
        print('Initial menu->Projects->Show projects')
        for position, menu_option in enumerate(self.active_project_dict.keys()):
            menu_options[position + 1] = menu_option
            print('{}. {}'.format(position + 1, menu_option))
        print('0. Previous menu')
