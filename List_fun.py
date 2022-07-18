import logging

logging.basicConfig(filename="test2.log",level=logging.INFO ,format= '%(asctime)s %(levelname)s %(name)s %(message)s')

class Try_List:

    """
    This class is on List examples we will try diffferent examples on the List as per given in Assignments.
    """

    def sep_list(self,l):
        """
        We are extracting only list  from the given list
        :param l: list
        :return: seprate list
        """

        try:
            logging.info("The given list for this operation is %s", l)
            extracted_list = []
            for element in l:
                if type(element) == list:
                    extracted_list.append(element)
            logging.info("List from list  : %s",extracted_list)
            return extracted_list
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def sep_dict(self,l):
        """
        We are extracting only list  from the given list
        :param l: list
        :return: seprate dict
        """

        try:
            logging.info("The given list for this operation is %s", l)
            extracted_list = []
            for element in l:
                if type(element) == dict:
                    extracted_list.append(element)
            logging.info("Dictinoary from list : %s",extracted_list)
            return extracted_list
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def sep_tuple(self,l):
        """
        We are extracting only tuple  from the given list
        :param l: list
        :return: seprate tuple
        """

        try:
            logging.info("The given list for this operation is %s", l)
            extracted_list = []
            for element in l:
                if type(element) == tuple :
                    extracted_list.append(element)
            logging.info("extracting only tuple  from the given list: %s",extracted_list)
            return extracted_list
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def extract_number(self,l):
        """
        Try to extract all numerical values from given list

        :param l: input list
        :return: all numeriacal values present in each entity
        """
        try:
            logging.info("The given list for this operation is %s",l)
            output_list = []
            for element in l:
                if type(element) == list or type(element) == tuple or type(element) == set:
                    for inner in element:
                        if type(inner) == int:
                            output_list.append(inner)
                elif type(element) == dict:
                    for j,k in element.items():
                        if type(j) == int:
                            output_list.append(j)
                        if type(k) == int:
                            output_list.append(k)


            logging.info("all numeriacal values : %s",output_list)
            return  output_list


        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def summation_of_all_num(self,l):
        """
        We are try to give summation of all numeric data present in the list .
        :param l: the input list
        :return: will return summation of all numeric data
        """
        try:
            logging.info("The given list for this operation is %s",l)
            output_list = []
            sum = 0
            for element in l:
                if type(element) == list or type(element) == tuple or type(element) == set:
                    for inner in element:
                        if type(inner) == int:
                            output_list.append(inner)
                elif type(element) == dict:
                    for j,k in element.items():
                        if type(j) == int:
                            output_list.append(j)
                        if type(k) == int:
                            output_list.append(k)

            for element in output_list:
                sum = sum + element


            logging.info("summation of all numeric data : %s",sum)
            return  sum


        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))


    def list_filter_odd_num(self,l):
        """
        We are extracting only list  from the given list
        :param l: list
        :return: will filter odd values form all list
        """

        try:
            logging.info("The given list for this operation is %s", l)
            extracted_list = []
            for element in l:
                if type(element) == list:
                    for inner in element:
                        if type(inner) == int and inner%2 != 0:
                            extracted_list.append(inner)

            logging.info("odd values form all list  : %s",extracted_list)
            return extracted_list
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def filter_word(self,l,word):
        """
        We are trying to search the input word from list..
        :param l: the input list
        :param m: the word want to filter
        :return: will filter out  given word from all list
        """
        try:
            logging.info("The given list for this operation is %s",l)
            logging.info("The given word to filter out is %s", word)
            output_list = []
            for element in l:
                if type(element) == list or type(element) == tuple or type(element) == set:
                    for inner in element:
                        if type(inner) == str and inner == word:
                            output_list.append(inner)
                elif type(element) == dict:
                    for j,k in element.items():
                        if type(j) == str and j == word:
                            output_list.append(j)
                        if type(k) == str and k == word:
                            output_list.append(k)


            logging.info("filter %s from list : %s and count is %s",word,output_list,len(output_list))
            return  output_list


        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def no_of_keys_dict(self,l):
        """
        We are extracting number of key present in dictionaries
        :param l: list
        :return: no of keys in dict
        """

        try:
            logging.info("The given list for this operation is %s", l)
            extracted_list = []
            for element in l:
                if type(element) == dict:
                    for inner in element:
                        extracted_list.append(inner)
            logging.info("The no of keys  : %s",len(extracted_list))
            return extracted_list
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def extrac_strings(self, l):
        """
        Try to extract all strings values from given list

        :param l: input list
        :return: all strings values present in each entity
        """
        try:
            logging.info("The given list for this operation is %s", l)
            output_list = []
            for element in l:
                if type(element) == list or type(element) == tuple or type(element) == set:
                    for inner in element:
                        if type(inner) == str:
                            output_list.append(inner)
                elif type(element) == dict:
                    for j, k in element.items():
                        if type(j) == str:
                            output_list.append(j)
                        if type(k) == str:
                            output_list.append(k)

            logging.info("all strings values : %s", output_list)
            return output_list


        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def extrac_alphanum(self, l):
        """
        Try to extract all alphanum values from given list

        :param l: input list
        :return: all alphanum values present in each entity
        """
        try:
            logging.info("The given list for this operation is %s", l)
            output_list = []
            for element in l:
                if type(element) == list or type(element) == tuple or type(element) == set:
                    for inner in element:
                        if type(inner) == str and inner.isalnum():
                            output_list.append(inner)
                elif type(element) == dict:
                    for j, k in element.items():
                        if type(j) == str and j.isalnum():
                            output_list.append(j)
                        if type(k) == str and k.isalnum():
                            output_list.append(k)

            logging.info("all alphanum values : %s", output_list)
            return output_list


        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def unwrap(self,l):
        """
        We are try to gunwrap all data present in the list .
        :param l: the input list
        :return: will return list of all elements
        """
        try:
            logging.info("The given list for this operation is %s",l)
            output_list = []

            for element in l:
                if type(element) == list or type(element) == tuple or type(element) == set:
                    for inner in element:
                        output_list.append(inner)
                elif type(element) == dict:
                    for j,k in element.items():
                        output_list.append(j)
                        output_list.append(k)


            logging.info("unwrap all elements : %s",output_list)
            return  sum


        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def occurence_of_numbers(self,l):
        """
        We are try to count occurence of every element in list
        :param l: the input list
        :return: will return occurence of elements
        """
        try:
            logging.info("The given list for this operation is %s",l)
            output_list = []

            for element in l:
                if type(element) == list or type(element) == tuple or type(element) == set:
                    for inner in element:
                        output_list.append(inner)
                elif type(element) == dict:
                    for j,k in element.items():
                        output_list.append(j)
                        output_list.append(k)

            for item in set(output_list):
                logging.info("The element :" + str(item) + "  comes  " + str(output_list.count(item)))


        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))






obj1 = Try_List()
l = [[1,2,3,4],(11,12,13,14),("a","b","c"),set([2,3,44,5,6,44,7,8,44,5,44,6,44]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","datascience"]]
'''
obj1.sep_list(l)
obj1.sep_dict(l)
obj1.sep_tuple(l)
obj1.extract_number(l)
obj1.summation_of_all_num(l)
obj1.list_filter_odd_num(l)
obj1.filter_word(l,"ineuron")
obj1.no_of_keys_dict(l)
obj1.extrac_strings(l)
obj1.extrac_alphanum(l)
obj1.unwrap(l)
obj1.occurence_of_numbers(l)
'''




