import logging
logging.basicConfig(filename='test1.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s  %(message)s')

class Extract_Strings:

    """
    This class is for strings problem statments given in assignment .
    """
    def string_jump(self,string):

        """
                TASK-1's task
                extract string from index one to index 300 with a jump of 3
                :param string: input string
                :return: slices the string s with a step of 3 and starting point of 1, ending point of 300

        """
        try:
            logging.info("The given string for this operation is %s", string)
            if len(string) == 0:
                raise ValueError("Empty String")
                logging.error("empty string")
            else:
                output = string[::3]
                logging.info("Extracted string is %s: " , output)
                return output
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def string_rev(self,string):
        logging.info("We are about to reverse the string")
        try:
            logging.info("The given string for this operation is %s", string)
            if len(string) == 0:
                raise  ValueError("Empty String ")
                logging.error("empty string ")
            else:
                output = string[::-1]
                logging.info("Extracted string is %s: " , output)
                return  output
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def string_lower(self,string):
        logging.info("We are about to lower the string")
        try:
            logging.info("The given string for this operation is %s", string)
            if len(string) == 0:
                raise  ValueError("Empty String ")
            else:
                output = string.lower()
                logging.info("Extracted string is %s: " , output)
                return  output
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def string_Capitalize(self,string):
        logging.info("We are about to capitalize the string")
        try:
            logging.info("The given string for this operation is %s", string)
            if len(string) == 0:
                raise  ValueError("Empty String ")
            else:
                output = string.title()
                logging.info("Extracted string is %s: " , output)
                return  output
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def Split_Uppercase_(self,string):
        logging.info("We are about to split uppercae string ")
        try:
            logging.info("The given string for this operation is %s",string)
            if len(string) == 0:
                raise  ValueError("Empty String!!!")
                logging.error("Empty String!!!")

            else:
                output = string.upper().split(' ')
                logging.info("Extracted string is %s: ", output)
                return output

        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def Expand_string(self,string):
        logging.info("We are about to expand string ")
        try:
            logging.info("The given string for this operation is %s",string)
            if len(string) == 0:
                raise  ValueError("Empty String!!!")
                logging.error("Empty String!!!")

            else:
                output = string.expandtabs()
                logging.info("Extracted string is %s: ", output)
                return output

        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def strip_the_given_string(self, string):
        """
        TASK-1's task
        8.(i) Give an example of strip
        :param s: input string
        :return: returns the given string with stripping the extra spaces present on its left and right side
        """
        try:
            logging.info("The given string for this operation is %s", string)
            if len(string) == 0:
                raise  ValueError("Empty String!!!")
                logging.error("Empty String!!!")
            else:
                output = string.strip()
                logging.info("The output of the operation is %s", output)
                return output
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))

    def Replace_string(self,string,a,b):
        logging.info("We are about to replace the string ")
        try:
            logging.info("The given string is %s",string)
            if len(string) == 0:
                raise  ValueError("Empty String!!!")
                logging.error("Empty String!!!")
            else:
                output = string.replace(a,b)
                logging.info("The output of the operation is %s", output)
                return output
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))


    def string_center(self,string,spaces,symbol):
        logging.info("We are about to center the string ")
        try:
            logging.info("The given string is %s", string)
            if len(string) == 0:
                raise ValueError("Empty String!!!")
                logging.error("Empty String!!!")
            else:
                output = string.center(spaces,symbol)
                logging.info("The output of the operation is %s", output)
                return output
        except Exception as e:
            logging.exception("The exception is:" + "\n" + str(e))




obj1 = Extract_Strings()
obj1.string_jump("this is My First Python programming class and i am learNING python string and its function")
obj1.string_rev("this is My First Python programming class and i am learNING python string and its function")

obj1.string_lower("THIS IS MY FIRST PROGGRAM OF BASIC STRUCTURE WHICH I AM FOLLOWING !")
obj1.string_Capitalize("THIS IS MY FIRST PROGGRAM OF BASIC STRUCTURE WHICH I AM FOLLOWING !")
obj1.Split_Uppercase_("this is My First Python programming class and i am learNING python string and its function")
obj1.Expand_string("xyz\t12345\tabc")
obj1.strip_the_given_string("   hey boy what are you doing ?   ")
obj1.Replace_string("This is girish guys ,  how are you doing ","r","c")
obj1.string_center("Girish Mahamuni",20,"_")
