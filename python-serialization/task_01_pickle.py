import pickle

class CustomObject:
    """
    A custom object class with attributes name, age, and is_student. 
    Provides methods for display, serialization, and deserialization.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a new instance of CustomObject.

        :param name: The name of the individual.
        :param age: The age of the individual.
        :param is_student: Boolean indicating if the individual is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the CustomObject instance.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the CustomObject instance and save it to a file.

        :param filename: The filename of the output file. If the output file already exists, it will be replaced.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file to create an instance of CustomObject.

        :param filename: The filename of the input file.
        :return: An instance of CustomObject with the deserialized data or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Deserialization error: {e}")
            return None

# Exemple d'utilisation :
if __name__ == "__main__":
    obj = CustomObject("John", 25, True)
    obj.serialize("custom_object.pkl")
    loaded_obj = CustomObject.deserialize("custom_object.pkl")
    if loaded_obj:
        loaded_obj.display()
