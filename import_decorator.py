from initialiser import add_procedure


def procedure(name):
    ''' Creating a procedure decorator '''
    def procedure_decorator(given_procedure):
        '''
        Adding a new procedure to the procedure dictionary

        :param given_procedure: Procedure function
        :return: Procedure function
        '''
        add_procedure(name, given_procedure)
        return given_procedure

    return procedure_decorator
