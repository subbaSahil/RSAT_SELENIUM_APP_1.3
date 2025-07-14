def generate_xpath_from_control(control_type, control_name, control_label, description,value,second_word):
    grid_value = value
    
    control_type = control_type.lower()
#filter manager/quick filter
    if control_type in ["commandbutton", "menuitembutton","dropdialogbutton","button","togglebutton"]:
        return [f"//button[@name='{control_name}']",
                f"//button[@data-dyn-controlname='{control_name}']",
                f"//button[@aria-label='{control_label}']",
                f"//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='{control_name}']",
                f"//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='{control_label}']"
                ]

    elif control_type in ["menubutton", "menuitem"]:
        return [f"//button[@name='{control_name}']", f"//span[text()='{control_label}']/ancestor::button"]
    # elif control_type in ["combobox"]:
    #     return f"//div[@data-dyn-controlname='{control_name}']"
    elif control_type == "combobox":
        if control_label in ["Main account type"]:
            value = int(value)+2
        return [f"//input[@name='{control_name}']/following-sibling::div",
                f"//ul[contains(@aria-labelledby, '{control_name}')]//li[@data-dyn-index='{grid_value}']",
                f"//ul[contains(@aria-labelledby, '{control_name}')]",
                f"//input[@aria-label='{control_label}']/following-sibling::div",
                f"//ul[contains(@id,'{control_name}')]//li[{grid_value}]",
                f"//ul[contains(@id, '{control_name}')]",
                f"//input[@name='{control_name}']/parent::div/following-sibling::div/div"
            ]
    elif control_type == "sectionpage":
        return f"//button[contains(text(),'{control_label}')]"
    elif control_type == "checkbox":
        return [
            f"//label[contains(text(),'{control_label}')]/following-sibling::div/span[1]",
            f"//span[contains(@id, '{control_name}') and (@class='toggle-box' or @class='checkBox')]",
            f"//div[@aria-label='{control_label}']//span"
            ]
    elif control_type == "pivotitem":
        return f"//li[contains(@data-dyn-controlname,'{control_name}')]"
    elif control_type in ["input", "real", "referencegroup","date","radiobutton", "quickfilter","filtermanager", "datetime"]:
        return [
            f"//input[contains(@name,'{control_name.strip()}')]",
            f"//input[contains(@aria-label,'{control_label.strip()}')]"
        ]
    elif control_type == "appbartab":
        return f"//button/parent::div[@data-dyn-controlname='{control_name}']"
    elif control_type == "multilineinput":
        return f"//textarea[@name='{control_name}']"
    elif control_type == "formrunpersonalizationtoolbarcontrol":
        if second_word:
            return f"(//span[contains(text(),'{second_word}')]/parent::div/parent::button)[2]"
        return f"(//span[contains(text(),'Personalize')]/parent::div/parent::button)[2]"
    elif control_type == "grid":
        if grid_value == "": 
            return f"//div[contains(@class,'fixedDataTableRowLayout_')]"
        elif grid_value == "true" or grid_value == "false":
            return f"//div[contains(@class,'fixedDataTableRowLayout_')]/div[@aria-rowindex='1']"
        #if value !='' or value != "true" or value != "false":
        elif value=="SelectForAdd":
            return f"//button[@aria-label='Insert columns...']"
        else:
            return f"//div[contains(@class,'fixedDataTableRowLayout_')]/div[@aria-rowindex='{str(int(grid_value) + 1) }']"
    elif control_name == "No Control Name":
        return
    elif control_type == "segmentedentry":
        return [
            f"//input[contains(@name,'{control_name.strip()}')]",
            f"//input[contains(@aria-label,'{control_label.strip()}') and contains(@id,'{control_name.strip()}')]",
            f"//input[@title='{control_label.strip()}']",
            f"//input[contains(@id,'{control_name.strip()}')]"
        ]
    elif control_type=="filterpane":
        return ["//span[text()='Apply']//ancestor::button" ,
                "//span[text()='Reset']//ancestor::button",
                "//span[text()='Add']//ancestor::button"
        ]
    elif control_type == "listbox":
        return f"//ul[contains(@id,'{control_name}')]//li[@data-dyn-index='{grid_value}']"  
    elif control_type == "integer":
        return f"//div[@name='{control_name}']"
    elif control_type == "anchorbutton":
        return f"//span[text() = '{control_label}']/ancestor::a"
    
    
