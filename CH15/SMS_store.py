import testing as t

class SMS_store():
    """" Stores SMS' in a tuple and performs appropiate operations """
    # self.messages = (has_viewed, from_num, arrival, text)


    def __init__(self):
        self.messages = []

    def add_new_arrival(self, num, arrived, text):
        """ Adds a new text message """
        message_tuple = (False, num, arrived, text)
        self.messages.append(message_tuple)

    def message_count(self):
        """ Returns the amount of messages """
        return len(self.messages)

    def get_unread_indexes(self):
        """ Returns a list of the indexes of unread messages """
        xs = []
        for index, content in enumerate(self.messages):
            if content[0] == False:
                xs.append(index)

        return xs

    def get_message(self, msg_index):
        """ Gets a single message and changes the read state to True """
        self.messages[msg_index] = (True, self.messages[msg_index][1],
                                          self.messages[msg_index][2],
                                          self.messages[msg_index][3])

        #self.messages[msg_index] = (True, self.messages[msg_index][1:])
        #return self.messages[msg_index]

        return_tuple = (self.messages[msg_index][1],
                        self.messages[msg_index][2],
                        self.messages[msg_index][3])

        return return_tuple

    def delete(self, del_index):
        """ Deletes an element at index """
        #print("len() == " + str(len(self.messages)))
        del self.messages[del_index]

    def clear(self):
        """ Clears all the elements in the function """
        for i in self.get_unread_indexes():
            self.delete(i-1)

def test_suite():
    # Setup, no tests reqiured
    my_inbox = SMS_store()
    my_inbox.add_new_arrival(12345678, 124512, "Netflix and chill?")
    my_inbox.add_new_arrival(98765432, 123456, "Ey gril wan som fucc?")
    my_inbox.add_new_arrival(13453453, 234643, "Bub u wanna get kebab?")

    # Start tests
    t.test(my_inbox.message_count() == 3)

    t.test(my_inbox.get_unread_indexes() == [0, 1, 2])

    t.test(my_inbox.get_message(1) == (98765432, 123456, "Ey gril wan som fucc?"))
    t.test(my_inbox.get_unread_indexes() == [0, 2])

    my_inbox.delete(1)
    my_inbox.clear()

    t.test(my_inbox.message_count() == 0)

test_suite()
