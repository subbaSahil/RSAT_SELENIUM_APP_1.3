import xml.etree.ElementTree as ET
 
def extract_user_actions(input_xml):
    tree = ET.parse(input_xml)
    root = tree.getroot()
 
    namespaces = {
        '': 'http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.Client.ServerForm.TaskRecording',
        'd2p1': 'http://schemas.microsoft.com/2003/10/Serialization/Arrays',
        'd7p1': 'http://schemas.microsoft.com/2003/10/Serialization/Arrays',
        'i': 'http://www.w3.org/2001/XMLSchema-instance',
        'z': 'http://schemas.microsoft.com/2003/10/Serialization/'
    }
 
    user_actions_with_details = ET.Element("UserActionsWithDetails")
    user_actions = root.findall(".//UserActions//d2p1:anyType", namespaces=namespaces)
 
    actions_dict = {}
    first_occurrence_of_navigtion = None
    for index, action in enumerate(user_actions):
        ref = action.attrib.get("{http://schemas.microsoft.com/2003/10/Serialization/}Ref")
        node = root.find(f".//Node[@z:Id='{ref}']", namespaces=namespaces)
 
        description = ''
        control_label = ''
        control_type = ''
        control_names = []
        value = ''
        navigation_path = []
        annotations_elem = None  # To store annotations if "Close the page."
        command_name = ''
 
        if node is not None:
            desc_elem = node.find(".//Description", namespaces=namespaces)
            if desc_elem is not None and desc_elem.text:
                # if desc_elem.text.startswith("Go to"):
                #     first_occurrence_of_navigtion = True
                # if first_occurrence_of_navigtion:
                    description = desc_elem.text
 
            # Capture annotations only for "Close the page."
            if description == "Close the page.":
                annotations_elem = node.find(".//Annotations", namespaces=namespaces)
 
            control_label_elem = node.find(".//ControlLabel", namespaces=namespaces)
            if control_label_elem is not None and control_label_elem.text:
                control_label = control_label_elem.text
 
            control_type_elem = node.find(".//ControlType", namespaces=namespaces)
            if control_type_elem is not None and control_type_elem.text:
                control_type = control_type_elem.text
 
            control_name_elem = node.find(".//ControlName", namespaces=namespaces)
            if control_name_elem is not None and control_name_elem.text:
                control_name_text = control_name_elem.text
                # if control_name_text.strip() == "Grid" and control_type.strip() == "GridOverview":
                #     continue   we commented this because we were ignoring grid in the beginning 
                control_names.append(control_name_text)
            
            command_name_elem = node.find(".//CommandName", namespaces=namespaces)
            if command_name_elem is not None and command_name_elem.text:
                command_name = command_name_elem.text
            else:
                nav_path = node.find(".//NavigationPath", namespaces=namespaces)
                if nav_path is not None:
                    path_parts = nav_path.findall(".//d7p1:string", namespaces=namespaces)
                    for part in path_parts:
                        if part.text:
                            navigation_path.append(part.text)
 
            # Check for value in CanonicalUserAction
            annotation_value = node.find(".//Annotations//Annotation//CanonicalUserAction//Value", namespaces=namespaces)
            if annotation_value is not None and annotation_value.text:
                value = annotation_value.text.strip()
            else:
                direct_value = node.find(".//Value", namespaces=namespaces)
                if direct_value is not None and direct_value.text:
                    value = direct_value.text.strip()
 
        # Add to dictionary
        if ref not in actions_dict:
            actions_dict[ref] = {
                "Description": description,
                "ControlNames": set(),
                "ControlLabel": control_label,
                "ControlType": control_type,
                "Value": value,
                "NavigationPath": navigation_path,
                "Annotations": annotations_elem , # store only if it's for "Close the page."
                "command_name": command_name
            }
 
        for control_name in control_names:
            actions_dict[ref]["ControlNames"].add(control_name)
 
    # Build output XML
    for ref, action_data in actions_dict.items():
        user_action = ET.SubElement(user_actions_with_details, "UserAction")
        user_action.set("Ref", ref)
        ET.SubElement(user_action, "Description").text = action_data["Description"]
        ET.SubElement(user_action, "NodeId").text = ref
        ET.SubElement(user_action, "Sequence").text = str(index + 1)
 
        if action_data["NavigationPath"]:
            for nav_item in action_data["NavigationPath"]:
                ET.SubElement(user_action, "Navigation").text = nav_item
 
        if action_data["ControlNames"]:
            for control_name in action_data["ControlNames"]:
                ET.SubElement(user_action, "ControlName").text = control_name
        else:
            ET.SubElement(user_action, "ControlName").text = 'No Control Name'
 
        ET.SubElement(user_action, "ControlLabel").text = action_data["ControlLabel"]
        ET.SubElement(user_action, "ControlType").text = action_data["ControlType"]
        ET.SubElement(user_action, "Value").text = action_data["Value"]
        ET.SubElement(user_action, "CommandName").text = action_data["command_name"]
 
        # Add Annotations only if present
        if action_data["Annotations"] is not None:
            # Deep copy annotations (optional: import copy and use deepcopy)
            annotations_element = ET.SubElement(user_action, "Annotations")
            for child in action_data["Annotations"]:
                annotations_element.append(child)
 
    tree_out = ET.ElementTree(user_actions_with_details)
    tree_out.write('output.xml', encoding='UTF-8', xml_declaration=True)
 
# extract_user_actions("recording.xml")