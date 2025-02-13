import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
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
            dictionary[child.tag] = value
        
        return dictionary
    except FileNotFoundError:
        print(f"Erreur : le fichier {filename} n'a pas été trouvé.")
        return None
    except ET.ParseError:
        print(f"Erreur : le fichier {filename} est mal formé.")
        return None

# Exemple d'utilisation :
if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
