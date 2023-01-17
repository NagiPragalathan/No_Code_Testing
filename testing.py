from olx import get_stack
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from Tools import SetupTools

def action(element,action):
    if action == 'click':
        element.click()

def Make_test(path):
    get_ids = ['id','name','class','xpath']
    list_data = ['ls_id_clk','ls_name_clk','ls_xpath_clk']

    orginal = get_stack(path)
    stack = get_stack(path)[1:]
    try :
        if orginal[0].get("auto_install") == "true":
            driver = SetupTools.install_selenium_tool(orginal[0].get("browser"))
        else:
            path = orginal[0].get('driver_path')
            driver : webdriver = webdriver.Chrome(path)
            driver.get(orginal[0].get('get'))
            if orginal[0].get('window') == 'maximize':
                driver.maximize_window()
    except:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(orginal[0].get('get'))
        if orginal[0].get('window') == 'maximize':
            driver.maximize_window()
            
    for i in stack:
        time.sleep(1)
        for j in i.keys():
            if j in list_data:
                if j == 'ls_id_clk': # list id's excution line
                    for k in i.get(j):
                        Element = driver.find_element('id', k)
                        action(Element,'click')

                elif j == 'ls_name_clk':
                    for k in i.get(j):
                        Element = driver.find_element('name', k)
                        action(Element,'click')

                elif j == 'ls_xpath_clk':
                    for k in i.get(j):
                        Element = driver.find_element('name', k)
                        action(Element,'click')

            if j in get_ids:
                print(j,i.get(j),':' in i.get(j))
                if ':' in i.get(j):
                    values = i.get(j).split(':')
                    at_splited = values[1].split('@')
                    element_id = values[0]
                    print(element_id)
                    # find element
                    Element = driver.find_element(j, element_id)
                            # Select DropDown Methods
                    for k in range(1,len(values)):
                        if at_splited[0] == 'select_by_index':
                            if 'data' in i.keys():
                                Select(Element).select_by_index(int(i.get('data')))
                            else :
                                Select(Element).select_by_index(int(at_splited[1]))
                        elif at_splited[0] == 'select_by_value':
                            if 'data' in i.keys():
                                Select(Element).select_by_value(int(i.get('data')))
                            else :
                                
                                Select(Element).select_by_value(int(at_splited[1]))
                        elif at_splited[0] == 'select_by_visible_text':
                            if 'data' in i.keys():
                                Select(Element).select_by_visible_text(int(i.get('data')))
                            else :
                                Select(Element).select_by_visible_text(int(at_splited[1]))

                                    # DeSelectDropSown Methods
                        elif at_splited[0] == 'deselect_all':
                            Select(Element).deselect_all()
                        elif at_splited[0] == 'deselect_by_index':
                            if 'data' in i.keys():
                                Select(Element).deselect_by_index(int(i.get('data')))
                            else :
                                Select(Element).deselect_by_index(int(at_splited[1]))
                        elif at_splited[0] == 'deselect_by_value':
                            if 'data' in i.keys():
                                Select(Element).deselect_by_value(int(i.get('data')))
                            else :
                                Select(Element).deselect_by_value(int(at_splited[1]))
                        elif at_splited[0] == 'deselect_by_visible_text':
                            if 'data' in i.keys():
                                Select(Element).deselect_by_visible_text(int(i.get('data')))
                            else :
                                Select(Element).deselect_by_visible_text(int(at_splited[1]))

                                    # Input Filed Methods
                        # input box types...
                        if values[k] == 'sk':
                            if 'data' in i.keys():
                                print(i.get('data'))
                                Element.send_keys(i.get('data'))
                        elif values[k] == 'c&sk':
                            if 'data' in i.keys():
                                print(i.get('data'))
                                Element.clear()
                                Element.send_keys(i.get('data'))
                        elif values[k] == 'click':
                            action(Element,'click')

                                    # window's oprating methods
                        if values[k] == 'maximize' or i.get('window') == 'maximize':
                            driver.maximize_window()
                        elif values[k] == 'minimize' or i.get('window') == 'minimize':
                            driver.minimize_window()
                        
                        if type(i.get('set_window_position')) == list :
                            pos = i.get('set_window_position')
                            driver.set_window_position(pos[0],pos[1])
    input()


Make_test('olx.json')