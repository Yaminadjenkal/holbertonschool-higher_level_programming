import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    :param dictionary: A Python dictionary with data
    :param filename: The filename of the output XML file. If the output file already exists, it will be replaced.
    """
    # Créer un élément racine
    root = ET.Element("data")
    
    # Ajouter les éléments enfants à partir du dictionnaire
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)  # Convertir la valeur en chaîne de caractères
        root.append(child)
    
    # Créer l'arbre XML et l'écrire dans le fichier
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    :param filename: The filename of the input XML file
    :return: A Python dictionary with the deserialized XML data from the file or None if an error occurs
    """
    try:
        # Analyser le fichier XML
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstituer le dictionnaire à partir des éléments XML
        dictionary = {}
        for child in root:
            # Convertir la chaîne de caractères en type approprié si nécessaire
            value = child.text
            if value.isdigit():
                value = int(value)
            elif value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass
            dictionary[child.tag] = value
        
        return dictionary
    except File