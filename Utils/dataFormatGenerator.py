import xml.etree.ElementTree as ET
from openpyxl import Workbook
import os

def generate_dynamic_header_excel(xml_file_path: str, output_script_path: str):
    """
    Creates an Excel file in 'Data/' folder with headers as 'ControlLabel / ControlName'
    and values as the 'Value' field from the XML.
    The Excel filename matches the name of the script file (but with .xlsx extension).
    """
    allowed_types = {"Input", "Real", "SegmentedEntry"}
    
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return

    headers = []
    values = []

    for action in root.findall("UserAction"):
        control_type = action.findtext("ControlType", "").strip()
        if control_type in allowed_types:
            control_label = action.findtext("ControlLabel", "").strip()
            control_name = action.findtext("ControlName", "").strip()
            value = action.findtext("Value", "").strip()

            if control_label or control_name:
                header = f"{control_label}/{control_name}".strip(" /")
                headers.append(header)
                # values.append(value)

    # Ensure Data/ directory exists
    data_folder = "Data"
    os.makedirs(data_folder, exist_ok=True)

    # Get base name of the script file (without extension)
    base_name = os.path.splitext(os.path.basename(output_script_path))[0]
    excel_file_path = os.path.join(data_folder, f"{base_name}_data.xlsx")

    # Write to Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "DynamicFields"
    ws.append(headers)
    ws.append(values)

    wb.save(excel_file_path)
    print(f"Excel saved to {excel_file_path}")
