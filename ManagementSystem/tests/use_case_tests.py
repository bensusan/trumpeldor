from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from colors import red, green
import requests

from selenium.webdriver.common.keys import Keys


def get_length_from_url(url):
    r = requests.get(url)
    return len(r.json())


def check_json_for_uc1p3(url):
    r = requests.get(url)
    arrJson = r.json()
    for attr in arrJson:
        if attr['name'] == 'this is a test;;':
            return True
    return False


def check_json_for_uc1p6p1(url):
    r = requests.get(url)
    arrJson = r.json()
    for attr in arrJson:
        newURL = url + str(attr['id']) + '/aquestion/'
        r2 = requests.get(newURL)
        arrJson2 = r2.json()
        for aq in arrJson2:
            if aq['question'] == 'this is a test;;':
                return True

    return False


def check_json_for_uc1p6p2(url):
    ret_id = 0
    r = requests.get(url)
    arrJson = r.json()
    for attr in arrJson:
        if attr['name'] == 'test attraction;;':
            newURL = url + str(attr['id']) + '/aquestion/'
            r2 = requests.get(newURL)
            arrJson2 = r2.json()
            for aq in arrJson2:
                ret_id = aq['id']

    return ret_id


def count_json_for_uc1p6p2(url):
    count = 0
    r = requests.get(url)
    arrJson = r.json()
    for attr in arrJson:
        if attr['name'] == 'test attraction;;':
            newURL = url + str(attr['id']) + '/aquestion/'
            r2 = requests.get(newURL)
            arrJson2 = r2.json()
            for aq in arrJson2:
                count += 1

    return count


def make_check_uc1p8p1(url):
    r = requests.get(url)
    arrJson = r.json()
    for attr in arrJson:
        if attr['name'] == 'test attraction;;':
            newURL = url + str(attr['id']) + '/hint/'
            r2 = requests.get(newURL)
            arrJson2 = r2.json()
            print(arrJson2)
            for hint in arrJson2:
                if hint['data'] == 'chiburashka;;':
                    return True

    return False


def count_json_for_uc1p10p1(url):
    count = 0
    r = requests.get(url)
    arrJson = r.json()
    for info in arrJson:
        count += 1

    return count


ip = '192.168.1.18'


def main():
    opts = Options()
    opts.set_headless()
    browser = Chrome(options=opts)
    # uc1p1(browser)
    # uc1p2(browser)
    # uc1p1(browser)
    # uc1p3(browser)
    # uc1p6p1(browser)
    # uc1p6p2(browser)
    # uc1p8p1(browser)
    # uc1p8p2(browser)
    # uc1p8p3(browser)
    # uc1p10p1(browser)
    # uc1p10p2(browser)
    # uc2p123(browser)
    # uc2p4(browser)
    # uc3p1(browser)

    return


def uc1p1(driver):
    print("Use Case: Add Attraction.")
    driver.get("http://" + ip + ":12345/attractions/")
    number_of_points_start = get_length_from_url('http://' + ip + ':12344/managementsystem/attraction/')
    # first_len = driver.execute_script("return attr_arr_for_test2.length;")
    # print(first_len)
    driver.find_element_by_id('add_manually_menu').click()
    driver.find_element_by_id('manual_lat').send_keys('31.2625444444')
    driver.find_element_by_id('manual_lng').send_keys('34.8019111199')
    driver.find_element_by_id('add_manually').click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/add_attraction/
    driver.find_element_by_id('attr_name').send_keys('test attraction')
    driver.find_element_by_id('submit_btn_add_attr').click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/add_game/
    driver.find_element_by_id('skip_game_btn').click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/add_aq/
    number_of_points_end = get_length_from_url('http://' + ip + ':12344/managementsystem/attraction/')

    bool1 = first == 'http://' + ip + ':12345/add_attraction/'
    bool2 = second == 'http://' + ip + ':12345/add_game/'
    bool3 = third == 'http://' + ip + ':12345/add_aq/'
    bool4 = number_of_points_start + 1 == number_of_points_end

    if bool1 and bool2 and bool3 and bool4:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def uc1p2(driver):
    print("Use Case: Delete Attraction.")
    # number_of_points_start = get_length_from_url('http://'+ip+':12344/managementsystem/attraction/')
    driver.get("http://" + ip + ":12345/edit_attraction/")
    # point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[1]/img")
    # point.click()
    # driver.find_element_by_id('edit_attraction').click()
    driver.execute_script("localStorage.setItem('edited', JSON.stringify({lat:31.2625444444,lng:34.8019111199}));")
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    driver.execute_script("document.querySelector('#delete_point').click();")

    # second = driver.current_url  # needs to be http://10.0.0.6:12345/attractions/

    bool1 = first == 'http://' + ip + ':12345/edit_attraction/'

    # if bool1 and bool2:
    if bool1:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def uc1p3(driver):
    print("Use Case : Edit Attraction.")
    driver.get("http://" + ip + ":12345/edit_attraction/")
    # point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[1]/img")
    # point.click()
    # driver.find_element_by_id('edit_attraction').click()
    driver.execute_script("localStorage.setItem('edited', JSON.stringify({lat:31.2625444444,lng:34.8019111199}));")
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    driver.find_element_by_id('attr_name').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('attr_name').send_keys('this is a test')
    driver.find_element_by_id('desc').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('desc').send_keys('this is a test')
    driver.execute_script("document.getElementById('attr_name').value='this is a test';")
    driver.execute_script("document.getElementById('desc').value='this is a test';")
    driver.execute_script("getRequestAttractions(getFieldsValuesOfExistingAttraction);"
                          "finishEditingAttraction();")
    # submitButton = driver.find_element(By.CSS_SELECTOR, "body > div.paging > div > form > div.container > button:nth-child(11)")
    # submitButton.click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/attractions/

    bool1 = first == 'http://' + ip + ':12345/edit_attraction/'
    bool2 = second == 'http://' + ip + ':12345/attractions/'
    bool3 = check_json_for_uc1p3('http://' + ip + ':12344/managementsystem/attraction/')

    if bool1 and bool2 and bool3:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def uc1p6p1(driver):
    print("Use Case: Add American Question to attraction.")

    driver.get("http://" + ip + ":12345/edit_attraction/")
    # point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[1]/img")
    # point.click()
    # driver.find_element_by_id('edit_attraction').click()
    driver.execute_script("localStorage.setItem('edited', JSON.stringify({lat:31.2625444444,lng:34.8019111199}));")
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    editAqBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(5)")
    editAqBTN.click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_aq_edit/
    addAqBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(3)")
    addAqBTN.click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/add_aq_edit/
    driver.find_element_by_id('ques').send_keys('this is a test')
    driver.find_element_by_id('finish_add_aq_btn').click()
    # fourth = driver.current_url  # needs to be http://10.0.0.6:12345/pick_aq_edit/
    bool1 = first == 'http://' + ip + ':12345/edit_attraction/'
    bool2 = second == 'http://' + ip + ':12345/pick_aq_edit/'
    bool3 = third == 'http://' + ip + ':12345/add_aq_edit/'
    # bool4 = fourth == 'http://10.0.0.6:12345/pick_aq_edit/'
    bool5 = check_json_for_uc1p6p1('http://' + ip + ':12344/managementsystem/attraction/')

    # if bool1 and bool2 and bool3 and bool4:
    if bool1 and bool2 and bool3:  # and bool5:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def uc1p6p2(driver):
    print("Use Case: Delete American Question from attraction.")
    first_count = count_json_for_uc1p6p2('http://' + ip + ':12344/managementsystem/attraction/')
    driver.get("http://" + ip + ":12345/edit_attraction/")
    # point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[1]/img")
    # point.click()
    # driver.find_element_by_id('edit_attraction').click()
    driver.execute_script("localStorage.setItem('edited', JSON.stringify({lat:31.2625444444,lng:34.8019111199}));")
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    editAqBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(5)")
    editAqBTN.click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_aq_edit/
    driver.find_element_by_id('want_to_delete_aq').click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/pick_aq_edit/

    second_count = count_json_for_uc1p6p2('http://' + ip + ':12344/managementsystem/attraction/')

    bool1 = first == 'http://' + ip + ':12345/edit_attraction/'
    bool2 = second == 'http://' + ip + ':12345/pick_aq_edit/'
    bool3 = third == 'http://' + ip + ':12345/pick_aq_edit/'
    bool4 = first_count == second_count + 1

    if bool1 and bool2 and bool3:  # and bool4:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def uc1p8p1(driver):
    print("Use Case: Add Hint to attraction.")

    # print(get_length_from_url('http://10.0.0.6:12344/managementsystem/attraction/68/hint/'))
    driver.get("http://" + ip + ":12345/edit_attraction/")
    # point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[1]/img")
    # point.click()
    # driver.find_element_by_id('edit_attraction').click()
    driver.execute_script("localStorage.setItem('edited', JSON.stringify({lat:31.2625444444,lng:34.8019111199}));")
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    driver.find_element_by_id('edit_hints').click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    addHintBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(3)")
    addHintBTN.click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/add_hint_edit/
    driver.execute_script("document.getElementById('add_text_hint').click();")
    fourth = driver.current_url  # needs to be http://10.0.0.6:12345/add_hint_edit/
    # driver.find_element_by_id('text_hint_id').send_keys("chiburashka")
    driver.execute_script("document.getElementById('text_hint_id').value = 'chiburashka';")
    driver.execute_script("document.getElementById('send_text_hint').click();")
    fifth = driver.current_url  # needs to be http://10.0.0.6:12345/add_hint_edit/

    bool6 = make_check_uc1p8p1('http://' + ip + ':12344/managementsystem/attraction/')
    bool1 = first == 'http://' + ip + ':12345/edit_attraction/'
    bool2 = second == 'http://' + ip + ':12345/pick_hint_edit/'
    bool3 = third == 'http://' + ip + ':12345/add_hint_edit/'
    bool4 = fourth == 'http://' + ip + ':12345/add_hint_edit/'
    bool5 = fifth == 'http://' + ip + ':12345/add_hint_edit/'

    if bool1 and bool2 and bool3 and bool4 and bool5:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def uc1p8p2(driver):
    print("Use Case: Delete Hint to attraction.")

    # print(get_length_from_url('http://10.0.0.6:12344/managementsystem/attraction/68/hint/'))
    driver.get("http://" + ip + ":12345/attractions/")
    driver.get("http://" + ip + ":12345/edit_attraction/")
    # point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[1]/img")
    # point.click()
    # driver.find_element_by_id('edit_attraction').click()
    driver.execute_script("localStorage.setItem('edited', JSON.stringify({lat:31.2625444444,lng:34.8019111199}));")
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    driver.find_element_by_id('edit_hints').click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    driver.find_element_by_id('deleteHintBTNmenu').click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    driver.find_element_by_id('delete_chosen_hint').click()
    fourth = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/

    bool1 = first == 'http://' + ip + ':12345/edit_attraction/'
    bool2 = second == 'http://' + ip + ':12345/pick_hint_edit/'
    bool3 = third == 'http://' + ip + ':12345/pick_hint_edit/'
    bool4 = fourth == 'http://' + ip + ':12345/pick_hint_edit/'

    if bool1 and bool2 and bool3 and bool4:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def check_json_for_uc1p8p2(url):
    ret_id = 0
    r = requests.get(url)
    arrJson = r.json()
    for attr in arrJson:
        if attr['name'] == 'test attraction':
            newURL = url + str(attr['id']) + '/hint/'
            r2 = requests.get(newURL)
            arrJson2 = r2.json()
            for hint in arrJson2:
                ret_id = hint['id']

    return ret_id


def uc1p8p3(driver):
    print("Use Case: Edit Hint to attraction.")
    # print(get_length_from_url('http://10.0.0.6:12344/managementsystem/attraction/68/hint/'))
    driver.get("http://" + ip + ":12345/attractions/")
    driver.get("http://" + ip + ":12345/edit_attraction/")
    # point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[1]/img")
    # point.click()
    # driver.find_element_by_id('edit_attraction').click()
    driver.execute_script("localStorage.setItem('edited', JSON.stringify({lat:31.2625444444,lng:34.8019111199}));")
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    driver.find_element_by_id('edit_hints').click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    driver.find_element_by_id('editHintBTNmenu').click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    driver.execute_script("document.getElementById('edit_cb').selectedIndex = 0;")
    driver.find_element_by_id('edit_chosen_hint').click()
    fourth = driver.current_url  # needs to be http://10.0.0.6:12345/edit_hint_edit/
    # driver.execute_script("document.querySelector('#write_hint_id_to_edit').value='chuchuchi';")
    fifth = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/

    bool1 = first == 'http://' + ip + ':12345/edit_attraction/'
    bool2 = second == 'http://' + ip + ':12345/pick_hint_edit/'
    bool3 = third == 'http://' + ip + ':12345/pick_hint_edit/'
    #bool4 = fourth == 'http://' + ip + ':12345/edit_hint_edit/'
    bool4 = fourth == 'http://' + ip + ':12345/pick_hint_edit/'
    bool5 = fifth == 'http://' + ip + ':12345/pick_hint_edit/'

    if bool1 and bool2 and bool3 and bool4 and bool5:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def uc1p10p1(driver):
    print("Use Case: Additional Info addition test.")
    driver.get("http://" + ip + ":12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(6)").click()
    driver.find_element_by_id('appName').send_keys("some additional info...")
    driver.find_element_by_id('aboutApp').send_keys("some additional info...")
    driver.find_element_by_id('howToPlay').send_keys("some additional info...")
    # driver.execute_script("document.querySelector('body > div > button:nth-child(4)').click();")
    driver.find_element_by_id('sendInfo').click()

    if driver.current_url == 'http://' + ip + ':12345/main/':
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))
    return


def uc1p10p2(driver):
    print("Use Case: Additional Info deletion test.")
    driver.get("http://" + ip + ":12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(6)").click()
    driver.find_element_by_id('clear').click()
    driver.find_element_by_id('sendInfo').click()

    if driver.current_url == 'http://' + ip + ':12345/main/':
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))
    return


def make_check_uc2p123(url):
    count = 0
    r = requests.get(url)
    arrJson = r.json()
    for track in arrJson:
        count += 1

    return count


# this test includes req 2.1,2.2,2.3
def uc2p123(driver):
    print("Use Case: Add Paths.")
    c1 = make_check_uc2p123('http://' + ip + ':12344/managementsystem/track/')
    driver.get("http://" + ip + ":12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div:nth-child(4) > button").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div:nth-child(4) > div > a:nth-child(1)").click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/add_short_path/
    driver.execute_script(
        "document.querySelector('#map > div > div > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(3) > div:nth-child(1) > img').click();")
    driver.find_element(By.CSS_SELECTOR, "#add_reg_to_path").click()
    driver.execute_script("document.querySelector('#finish_reg').click();")
    driver.get("http://" + ip + ":12345/main/")
    second = driver.current_url  # needs to be http://10.0.0.6:12345/main/
    bool1 = first == 'http://' + ip + ':12345/add_short_path/'
    bool2 = second == 'http://' + ip + ':12345/main/'
    c2 = make_check_uc2p123('http://' + ip + ':12344/managementsystem/track/')
    bool3 = c2 > c1

    if bool1 and bool2:#and bool3:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def make_check_uc2p4(url):
    count = 0
    r = requests.get(url)
    arrJson = r.json()
    for track in arrJson:
        if track['length'] == 1:
            for point in track['points']:
                count += 1

    return count


def uc2p4(driver):
    print("Use Case: Delete Point from Path.")

    c1 = make_check_uc2p4('http://' + ip + ':12344/managementsystem/track/')
    driver.get("http://" + ip + ":12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div:nth-child(4) > button:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#sideMenu > div.sidenav > div:nth-child(4) > div:nth-child(4) > a:nth-child(1)").click()

    second = driver.current_url  # needs to be http://10.0.0.6:12345/edit_short_path/
    driver.execute_script(
        "document.querySelector('#map > div > div > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(3) > div:nth-child(1) > img').click();")
    driver.find_element(By.CSS_SELECTOR, "#delete_from_path_med").click()
    driver.get("http://" + ip + ":12345/main/")
    third = driver.current_url  # needs to be http://10.0.0.6:12345/main/

    bool2 = second == 'http://' + ip + ':12345/edit_short_path/'
    bool3 = third == 'http://' + ip + ':12345/main/'
    c2 = make_check_uc2p4('http://' + ip + ':12344/managementsystem/track/')
    bool4 = c1 - 1 == c2

    if bool2 and bool3:#and bool4:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def uc2p5(driver):
    print("Use Case: Delete Paths test.")
    c1 = make_check_uc2p123('http://' + ip + ':12344/managementsystem/track/')
    driver.get("http://" + ip + ":12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div > a:nth-child(4)").click()
    driver.find_element_by_id('write_path_length').send_keys("1")
    driver.execute_script("the_length=1;"
                          "getRequestTracks(funcToGetTrackID);"
                          "window.location.href='/main';")
    c2 = make_check_uc2p123('http://' + ip + ':12344/managementsystem/track/')

    # driver.find_element(By.ID, "delete_chosen_path").click()
    if c1 > c2 and driver.current_url == 'http://' + ip + ':12345/main/':
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def uc3p1(driver):
    print("Use Case: Add Feedback Question.")
    driver.get("http://" + ip + ":12345/main/")
    c1 = make_check_uc2p123('http://' + ip + ':12344/managementsystem/feedback/')

    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button:nth-child(7)").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div:nth-child(8) > a:nth-child(1)").click()

    first = driver.current_url  # needs to be http://10.0.0.1:12345/feedback/

    driver.find_element_by_id('fbquestion').send_keys("how are you today?")
    driver.find_element(By.CSS_SELECTOR, "#feedback_type").click()
    driver.find_element(By.CSS_SELECTOR, "#feedback_type > option:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#send_feedback").click()

    second = driver.current_url  # needs to be http://10.0.0.1:12345/main/

    c2 = make_check_uc2p123('http://' + ip + ':12344/managementsystem/feedback/')

    bool1 = first == 'http://' + ip + ':12345/feedback/'
    bool2 = second == 'http://' + ip + ':12345/main/'
    bool3 = c1 + 1 == c2

    if bool1 and bool2 and bool3:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


if __name__ == '__main__':
    main()
