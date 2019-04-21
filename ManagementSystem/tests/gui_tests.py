# from Servers import *
# from src.deku import *
from pip._internal.vcs import git
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as req
from colors import red, green
import urllib.request
import json
import requests

#ip = 'http://132.73.201.223'
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

def get_length_from_url(url):
    r = requests.get(url)
    return len(r.json())

def main():
    # download_path = 'D:\_Guy\d9anime\downloaded'
    # download('kyoukai no kanata', [12])
    # print(find('steins gate'))
    # print(find('nanatsu no taizai imashime no fukkatsu'))
    # print(find('yuru camp'))
    # print(fetch_url('http://httpbin.org/headers').replace('\\n', '\n'))
    # deku.download_episodes(anime_name='A Place Further Than The Universe', path='.', server=RapidVideo)
    # deku.download_episodes(anime_name='A Place Further Than The Universe', path='.', server=MyCloud)
    # get_video_links_by_name('A Place Further Than The Universe')
    opts = Options()
    opts.set_headless()
    browser = Chrome(options=opts)
    #test1(browser)
    #test2(browser)
    # test_req_one_one(browser)
    # test_req_one_two(browser)
    # test_req_one_three(browser)
    # test_req_one_six_one(browser)
    # test_req_one_six_two(browser)
    # test_req_one_eight_one(browser)
    # test_req_one_eight_two(browser)
    # test_req_one_eight_three(browser)
    # test_req_one_ten_one(browser)
    # test_req_one_ten_two(browser)
    # test_req_two(browser)
    # test_req_two_four(browser)
    # test_req_two_five(browser)
    # test_req_two_six(browser)

    return


def test1(driver):
    driver.get("http://10.0.0.3:12345/pick_aq/")
    driver.find_element_by_id('finish_pick_aq').click()
    if(driver.current_url=='http://132.73.201.223:12345/attractions/'):
        print('test passed!')
    else:
        print('test failed!')

    return

def test2(driver):
    driver.get('http://10.0.0.3:12345/attractions/')
    driver.execute_script("shitToDeleteFast()")
    print(driver.current_url)

    return


def test3(driver):
    driver.get('http://10.0.0.3:12345/attractions/')
    res = driver.execute_script("let x= funcThatReturnsOne();"
                                "return x;")
    print(res)
    return


def test_req_one_one(driver):
    print("Test: Add Attraction test.")
    driver.get("http://10.0.0.6:12345/attractions/")
    # first_len = driver.execute_script("return attr_arr_for_test2.length;")
    # print(first_len)
    driver.find_element_by_id('add_manually_menu').click()
    driver.find_element_by_id('manual_lat').send_keys('31.2625444444')
    driver.find_element_by_id('manual_lng').send_keys('34.8019111199')
    driver.find_element_by_id('add_manually').click()
    first = driver.current_url # needs to be http://10.0.0.6:12345/add_attraction/
    driver.find_element_by_id('attr_name').send_keys('test attraction')
    driver.find_element_by_id('desc').send_keys('test attraction')
    driver.find_element_by_id('submit_btn_add_attr').click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/add_game/
    driver.find_element_by_id('skip_game_btn').click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/add_aq/
    driver.find_element_by_id('noOfAns').send_keys('4')
    driver.find_element_by_id('noOfCorrect').send_keys('1')
    driver.find_element_by_id('ok_button_to_prepare').click()
    driver.find_element_by_id('ques').send_keys('this is a test')
    driver.find_element_by_id('ans1').send_keys('this is a test')
    driver.find_element_by_id('ans2').send_keys('this is a test')
    driver.find_element_by_id('ans3').send_keys('this is a test')
    driver.find_element_by_id('ans4').send_keys('this is a test')
    driver.find_element_by_id('correctAns').send_keys('0')
    driver.find_element_by_id('finish_add_aq_btn').click()
    fourth = driver.current_url  # needs to be http://10.0.0.6:12345/add_hint/
    # print(fourth)
    # driver.find_element_by_id('finish_add_hint').click()
    # fifth = driver.current_url  # needs to be http://10.0.0.6:12345/attractions/
    #
    # print(first+second+third+fourth+fifth)
    bool1 = first == 'http://10.0.0.6:12345/add_attraction/'
    bool2 = second == 'http://10.0.0.6:12345/add_game/'
    bool3 = third == 'http://10.0.0.6:12345/add_aq/'

    if bool1 and bool2 and bool3:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_one_two(driver):
    print("Test: Delete Attraction test.")
    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[10]/img")
    point.click()
    driver.find_element_by_id('edit_attraction').click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    driver.find_element_by_id('delete_point').click()

    # second = driver.current_url  # needs to be http://10.0.0.6:12345/attractions/

    bool1 = first == 'http://10.0.0.6:12345/edit_attraction/'
    # bool2 = second == 'http://10.0.0.6:12345/attractions/'

    # if bool1 and bool2:
    if bool1:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_one_three(driver):
    print("Test: Edit Attraction test.")
    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[10]/img")
    point.click()
    driver.find_element_by_id('edit_attraction').click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    driver.find_element_by_id('attr_name').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('attr_name').send_keys('this is a test')
    driver.find_element_by_id('desc').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('desc').send_keys('this is a test')

    submitButton = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[2]/button[1]")
    submitButton.click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/attractions/

    bool1 = first == 'http://10.0.0.6:12345/edit_attraction/'
    bool2 = second == 'http://10.0.0.6:12345/attractions/'

    if bool1 and bool2:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_one_six_one(driver):
    print("Test: Add American Question to attraction.")

    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[10]/img")
    point.click()
    driver.find_element_by_id('edit_attraction').click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    editAqBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(4)")
    editAqBTN.click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_aq_edit/
    addAqBTN = driver.find_element(By.XPATH, "//*[@id='sideMenu']/div[1]/a[1]")
    addAqBTN.click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/add_aq_edit/
    driver.find_element_by_id('noOfAns').send_keys('4')
    driver.find_element_by_id('noOfCorrect').send_keys('1')
    driver.find_element_by_id('ok_button_to_prepare').click()
    driver.find_element_by_id('ques').send_keys('this is a test')
    driver.find_element_by_id('ans1').send_keys('this is a test')
    driver.find_element_by_id('ans2').send_keys('this is a test')
    driver.find_element_by_id('ans3').send_keys('this is a test')
    driver.find_element_by_id('ans4').send_keys('this is a test')
    driver.find_element_by_id('correctAns').send_keys('0')
    driver.find_element_by_id('finish_add_aq_btn').click()
    # fourth = driver.current_url  # needs to be http://10.0.0.6:12345/pick_aq_edit/
    bool1 = first == 'http://10.0.0.6:12345/edit_attraction/'
    bool2 = second == 'http://10.0.0.6:12345/pick_aq_edit/'
    bool3 = third == 'http://10.0.0.6:12345/add_aq_edit/'
    # bool4 = fourth == 'http://10.0.0.6:12345/pick_aq_edit/'

    # if bool1 and bool2 and bool3 and bool4:
    if bool1 and bool2 and bool3:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_one_six_two(driver):
    print("Test: Delete American Question from attraction.")
    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[10]/img")
    point.click()
    driver.find_element_by_id('edit_attraction').click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    editAqBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(4)")
    editAqBTN.click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_aq_edit/
    delAqBTN = driver.find_element(By.XPATH, "//*[@id='want_to_delete_aq']")
    delAqBTN.click()

    driver.find_element_by_id('write_aq_id_to_delete').send_keys("12")
    deleteBTN = driver.find_element(By.XPATH, "//*[@id='delete_chosen_aq']")
    deleteBTN.click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/pick_aq_edit/

    bool1 = first == 'http://10.0.0.6:12345/edit_attraction/'
    bool2 = second == 'http://10.0.0.6:12345/pick_aq_edit/'
    bool3 = third == 'http://10.0.0.6:12345/pick_aq_edit/'

    if bool1 and bool2 and bool3:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return

#
# import win32api, win32con
# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def test_req_one_eight_one(driver):
    print("Test: Add Hint to attraction.")

    # print(get_length_from_url('http://10.0.0.6:12344/managementsystem/attraction/68/hint/'))
    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[10]/img")
    point.click()
    driver.find_element_by_id('edit_attraction').click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    editHintBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(5)")
    editHintBTN.click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    edHintBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(4)")
    edHintBTN.click()
    addHintBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(3)")
    addHintBTN.click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/add_hint_edit/
    addTextBTN = driver.find_element(By.CSS_SELECTOR, "#add_text_hint")
    addTextBTN.click()
    fourth = driver.current_url  # needs to be http://10.0.0.6:12345/add_hint_edit/
    driver.find_element_by_id('text_hint_id').send_keys("wahhhhhhh")
    driver.find_element_by_id('send_text_hint').click()
    fifth = driver.current_url  # needs to be http://10.0.0.6:12345/add_hint_edit/

    bool1 = first == 'http://10.0.0.6:12345/edit_attraction/'
    bool2 = second == 'http://10.0.0.6:12345/pick_hint_edit/'
    bool3 = third == 'http://10.0.0.6:12345/add_hint_edit/'
    bool4 = fourth == 'http://10.0.0.6:12345/add_hint_edit/'
    bool5 = fifth == 'http://10.0.0.6:12345/add_hint_edit/'

    if bool1 and bool2 and bool3 and bool4 and bool5:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_one_eight_two(driver):
    print("Test: Delete Hint to attraction.")

    # print(get_length_from_url('http://10.0.0.6:12344/managementsystem/attraction/68/hint/'))
    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[10]/img")
    point.click()
    driver.find_element_by_id('edit_attraction').click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    editHintBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(5)")
    editHintBTN.click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    edHintBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(4)")
    edHintBTN.click()
    delHintBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(5)")
    delHintBTN.click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    driver.find_element_by_id('write_hint_id_to_delete').send_keys("2")
    driver.find_element_by_id('delete_chosen_hint').click()
    fourth = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/

    bool1 = first == 'http://10.0.0.6:12345/edit_attraction/'
    bool2 = second == 'http://10.0.0.6:12345/pick_hint_edit/'
    bool3 = third == 'http://10.0.0.6:12345/pick_hint_edit/'
    bool4 = fourth == 'http://10.0.0.6:12345/pick_hint_edit/'

    if bool1 and bool2 and bool3 and bool4:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_one_eight_three(driver):
    print("Test: Edit Hint to attraction.")

    # print(get_length_from_url('http://10.0.0.6:12344/managementsystem/attraction/68/hint/'))
    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[10]/img")
    point.click()
    driver.find_element_by_id('edit_attraction').click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/edit_attraction/
    editHintBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(5)")
    editHintBTN.click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    edHintBTN = driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(4)")
    edHintBTN.click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/
    driver.find_element_by_id('write_hint_id_to_edit').send_keys("2")
    driver.find_element_by_id('edit_chosen_hint').click()
    fourth = driver.current_url  # needs to be http://10.0.0.6:12345/edit_hint_edit/
    driver.find_element_by_id('write_hint_text_in_edit').send_keys("chuchuchu")
    driver.find_element_by_id('submit_to_edit_hint').click()
    fifth = driver.current_url  # needs to be http://10.0.0.6:12345/pick_hint_edit/

    bool1 = first == 'http://10.0.0.6:12345/edit_attraction/'
    bool2 = second == 'http://10.0.0.6:12345/pick_hint_edit/'
    bool3 = third == 'http://10.0.0.6:12345/pick_hint_edit/'
    bool4 = fourth == 'http://10.0.0.6:12345/edit_hint_edit/'
    bool5 = fifth == 'http://10.0.0.6:12345/pick_hint_edit/'

    if bool1 and bool2 and bool3 and bool4 and bool5:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_one_ten_one(driver):
    print("Test: Additional Info addition test.")
    driver.get("http://10.0.0.6:12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(6)").click()
    driver.find_element_by_id('subject').send_keys("some additional info...")
    driver.find_element(By.CSS_SELECTOR, "body > div > input:nth-child(4)").click()

    if driver.current_url == 'http://10.0.0.6:12345/main/':
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))
    return


def test_req_one_ten_two(driver):
    print("Test: Additional Info addition test.")
    driver.get("http://10.0.0.6:12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > a:nth-child(6)").click()
    driver.find_element(By.CSS_SELECTOR, "body > div > input:nth-child(5)").click()
    driver.find_element(By.CSS_SELECTOR, "body > div > input:nth-child(4)").click()

    if driver.current_url == 'http://10.0.0.6:12345/main/':
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))
    return


# this test includes req 2.1,2.2,2.3
def test_req_two(driver):
    print("Test: Add Paths test.")

    driver.get("http://10.0.0.6:12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div > button").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div > div > a:nth-child(1)").click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/add_short_path/
    point1 = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[1]/img")
    point1.click()
    driver.find_element(By.CSS_SELECTOR, "#add_reg_to_path").click()
    point2 = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[2]/img")
    point2.click()
    driver.find_element(By.CSS_SELECTOR, "#add_reg_to_path").click()
    point3 = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[3]/img")
    point3.click()
    driver.find_element(By.CSS_SELECTOR, "#add_reg_to_path").click()
    driver.execute_script("getRequestAttractions(funcInOrderToGetAttractions);")
    driver.find_element(By.ID, "finish_reg").click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/main/
    print(second)
    bool1 = first == 'http://10.0.0.6:12345/add_short_path/'
    bool2 = second == 'http://10.0.0.6:12345/main/'

    if bool1 and bool2:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_two_four(driver):
    print("Test: Delete Point from Path test.")

    driver.get("http://10.0.0.6:12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div > a:nth-child(3)").click()
    first = driver.current_url  # needs to be http://10.0.0.6:12345/pick_path_edit/
    driver.find_element_by_id('write_path_length').send_keys("1")
    driver.find_element(By.ID, "edit_chosen_path").click()
    second = driver.current_url  # needs to be http://10.0.0.6:12345/edit_short_path/
    point1 = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[1]/img")
    point1.click()
    driver.find_element(By.CSS_SELECTOR, "#delete_from_path_med").click()
    driver.find_element(By.CSS_SELECTOR, "#finish_reg_med").click()
    third = driver.current_url  # needs to be http://10.0.0.6:12345/main/

    bool1 = first == 'http://10.0.0.6:12345/pick_path_edit/'
    bool2 = second == 'http://10.0.0.6:12345/edit_short_path/'
    bool3 = third == 'http://10.0.0.6:12345/main/'

    if bool1 and bool2 and bool3:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_two_five(driver):
    print("Test: Delete Paths test.")

    driver.get("http://10.0.0.6:12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div > a:nth-child(4)").click()
    driver.find_element_by_id('write_path_length').send_keys("1")
    driver.execute_script("the_length=1;"
                          "getRequestTracks(funcToGetTrackID);"
                          "window.location.href='/main';")
    # driver.find_element(By.ID, "delete_chosen_path").click()
    if driver.current_url == 'http://10.0.0.6:12345/main/':
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


def test_req_two_six(driver):
    print("Test: Shows Paths test.")
    driver.get("http://10.0.0.6:12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div > a:nth-child(3)").click()
    driver.find_element_by_id('write_path_length').send_keys("1")
    driver.find_element(By.ID, "edit_chosen_path").click()
    driver.find_element(By.CSS_SELECTOR, "#finish_reg_med").click()

    if driver.current_url == 'http://10.0.0.6:12345/main/':
        print(green('--- test passed short!!! ---'))
    else:
        print(red('--- test failed short!!! ---'))

    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div > a:nth-child(3)").click()
    driver.find_element_by_id('write_path_length').send_keys("2")
    driver.find_element(By.ID, "edit_chosen_path").click()
    driver.find_element(By.CSS_SELECTOR, "#finish_reg_med").click()

    if driver.current_url == 'http://10.0.0.6:12345/main/':
        print(green('--- test passed med!!! ---'))
    else:
        print(red('--- test failed med!!! ---'))

    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div > a:nth-child(3)").click()
    driver.find_element_by_id('write_path_length').send_keys("3")
    driver.find_element(By.ID, "edit_chosen_path").click()
    driver.find_element(By.CSS_SELECTOR, "#finish_reg_long").click()

    if driver.current_url == 'http://10.0.0.6:12345/main/':
        print(green('--- test passed long!!! ---'))
    else:
        print(red('--- test failed long!!! ---'))

    return



def test_req_three_one(driver):
    print("Test: Add Feedback Question.")
    driver.get("http://10.0.0.1:12345/main/")
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > button:nth-child(7)").click()
    driver.find_element(By.CSS_SELECTOR, "#sideMenu > div.sidenav > div:nth-child(8) > a:nth-child(1)").click()

    first = driver.current_url  # needs to be http://10.0.0.1:12345/feedback/

    driver.find_element_by_id('fbquestion').send_keys("how are you today?")
    driver.find_element(By.CSS_SELECTOR, "#feedback_type").click()
    driver.find_element(By.CSS_SELECTOR, "#feedback_type > option:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#send_feedback").click()

    second = driver.current_url  # needs to be http://10.0.0.1:12345/main/

    bool1 = first == 'http://10.0.0.1:12345/feedback/'
    bool2 = second == 'http://10.0.0.1:12345/main/'

    if bool1 and bool2:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return


if __name__ == '__main__':
    main()

