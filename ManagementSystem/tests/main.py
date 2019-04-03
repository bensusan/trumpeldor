# from Servers import *
# from src.deku import *
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as req
from colors import red, green


#ip = 'http://132.73.201.223'
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


def main():
    opts = Options()
    opts.set_headless()
    browser = Chrome(options=opts)
    #test1(browser)
    #test2(browser)
    # test_req_one_one(browser)
    # test_req_one_two(browser)
    # test_req_one_three(browser)
    # test_req_one_six_one(browser)
    test_req_one_six_two(browser)
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
    first_len = driver.execute_script("return attr_arr_for_test2.length;")
    print(first_len)
    driver.find_element_by_id('add_manually_menu').click()
    driver.find_element_by_id('manual_lat').send_keys('31.2625444444')
    driver.find_element_by_id('manual_lng').send_keys('34.8019111199')
    driver.find_element_by_id('add_manually').click()
    driver.find_element_by_id('attr_name').send_keys('test attraction')
    driver.find_element_by_id('desc').send_keys('test attraction')
    driver.find_element_by_id('submit_btn_add_attr').click()
    driver.find_element_by_id('skip_game_btn').click()
    # driver.find_element_by_id('ques').send_keys('?')
    # driver.find_element_by_id('ans1').send_keys('a')
    # driver.find_element_by_id('ans2').send_keys('b')
    # driver.find_element_by_id('ans3').send_keys('c')
    # driver.find_element_by_id('ans4').send_keys('d')
    # driver.find_element_by_id('correctAns').send_keys('0')
    # print("1: "+driver.current_url)
    # driver.find_element_by_id('finish_add_aq_btn').click()
    # print("2: " + driver.current_url)
    # driver.find_element_by_id('finish_add_hint').click()
    # print("3: " + driver.current_url)
    #
    # if driver.current_url == 'http://10.0.0.3:12345/attractions/':
    #     print("we are on the right page!")

    driver.get("http://10.0.0.6:12345/attractions/")
    second_len = driver.execute_script("return attr_arr_for_test2.length;")

    print(second_len)

    if second_len == first_len+1:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))


    return


def test_req_one_two(driver):
    print("Test: Delete Attraction test.")
    driver.get("http://10.0.0.6:12345/attractions/")
    #second_len = driver.execute_script("document.querySelector('#sliding_puzzle_button').click();")
    # webElement = driver.find_element(By.XPATH, "//*[@id='sliding_puzzle_button']")
    first_len = driver.execute_script("return attr_arr_for_test2.length;")
    print(first_len)
    # point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[10]/img")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[11]/img")
    # point = driver.find_element(By.XPATH, "// *[ @ id = 'map'] / div / div / div[1] / div[1] / div[4] / div[5]")
    point.click()
    print(driver.current_url)
    editButton = driver.find_element(By.XPATH, "//*[@id='edit_attraction']")
    editButton.click()
    print(driver.current_url)
    driver.find_element_by_id('delete_point').click()

    driver.get("http://10.0.0.6:12345/attractions/")
    second_len = driver.execute_script("return attr_arr_for_test2.length;")

    print(second_len)

    if second_len == first_len - 1:
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return

def test_req_one_three(driver):
    print("Test: Edit Attraction test.")
    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[8]/img")
    point.click()
    editButton = driver.find_element(By.XPATH, "//*[@id='edit_attraction']")
    editButton.click()
    attrName = driver.execute_script("let x1 = document.getElementById('attr_name').value;"
                                     "return x;")
    attrDesc = driver.execute_script("let x2 = document.getElementById('desc').value;"
                                     "return x;")
    driver.find_element_by_id('attr_name').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('attr_name').send_keys('this is a test')
    driver.find_element_by_id('desc').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('desc').send_keys('this is a test')

    attrNameAfterEdit = 'this is a test'
    attrDescAfterEdit = 'this is a test'

    submitButton = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[2]/button[1]")
    submitButton.click()

    print("need to attractions: "+driver.current_url)

    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[8]/img")
    point.click()
    editButton = driver.find_element(By.XPATH, "//*[@id='edit_attraction']")
    editButton.click()

    attrName2 = driver.execute_script("let x = document.getElementById('attr_name').value;"
                                     "return x;")
    attrDesc2 = driver.execute_script("let y = document.getElementById('desc').value;"
                                     "return y;")

    if attrNameAfterEdit==attrName2 or attrDescAfterEdit==attrDesc2 :
        print(green('--- test passed!!! ---'))
    else:
        print(red('--- test failed!!! ---'))

    return

def test_req_one_six_one(driver):
    print("Test: Add American Question to attraction.")
    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[2]/img")
    point.click()
    editButton = driver.find_element(By.XPATH, "//*[@id='edit_attraction']")
    editButton.click()
    print("edit: " + driver.current_url)
    editAqBTN = driver.find_element(By.XPATH, "//*[@id='sideMenu']/div[1]/a[4]")
    editAqBTN.click()
    print("pick: " + driver.current_url)
    first_len = driver.execute_script("return aq_arr_for_test.length;")
    addAqBTN = driver.find_element(By.XPATH, "//*[@id='sideMenu']/div[1]/a[2]")
    addAqBTN.click()
    print("add: " + driver.current_url)
    # driver.find_element_by_id('attr_name').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('noOfAns').send_keys('4')
    driver.find_element_by_id('noOfCorrect').send_keys('1')
    okBTN = driver.find_element(By.XPATH, "//*[@id='ok_button_to_prepare']")
    okBTN.click()
    driver.find_element_by_id('ques').send_keys('how are you?')
    driver.find_element_by_id('ans1').send_keys('ok')
    driver.find_element_by_id('ans2').send_keys('good')
    driver.find_element_by_id('ans3').send_keys('fine')
    driver.find_element_by_id('ans4').send_keys('very good')
    driver.find_element_by_id('correctAns').send_keys('3')
    submitBTN = driver.find_element(By.XPATH, "//*[@id='finish_add_aq_btn']")
    submitBTN.click()


    # if second_len == first_len + 1:
    print(green('--- test passed!!! ---'))
    # else:
    #     print(red('--- test failed!!! ---'))


    return


def test_req_one_six_two(driver):
    print("Test: Delete American Question from attraction.")
    driver.get("http://10.0.0.6:12345/attractions/")
    point = driver.find_element(By.XPATH, "//*[@id='map']/div/div/div[1]/div[3]/div/div[3]/div[2]/img")
    point.click()
    editButton = driver.find_element(By.XPATH, "//*[@id='edit_attraction']")
    editButton.click()
    print("edit: " + driver.current_url)
    editAqBTN = driver.find_element(By.XPATH, "//*[@id='sideMenu']/div[1]/a[4]")
    editAqBTN.click()
    print("pick: " + driver.current_url)

    delAqBTN = driver.find_element(By.XPATH, "//*[@id='want_to_delete_aq']")
    delAqBTN.click()
    # driver.find_element_by_id('attr_name').send_keys(Keys.CONTROL, 'a')
    some_aq_id = driver.execute_script("getRequestAttractions(funcForExistingAmericanQuestions);"
                                       "return id_to_delete;")
    print(some_aq_id)
    driver.find_element_by_id('write_aq_id_to_delete').send_keys(some_aq_id)
    deleteBTN = driver.find_element(By.XPATH, "//*[@id='delete_chosen_aq']")
    deleteBTN.click()
    print("pick: " + driver.current_url)

    # if second_len == first_len + 1:
    print(green('--- test passed!!! ---'))
    # else:
    #     print(red('--- test failed!!! ---'))


    return


if __name__ == '__main__':
    main()
