from selenium import webdriver


browser = webdriver.Chrome('/Users/burakkorkmaz/Desktop/4 - 1/cs 461 - ai/project/implementation/chromedriver')
browser.get('https://www.nytimes.com/crosswords/game/mini')
browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div[2]/div[2]/article/div[2]/button/div')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/button')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/ul/li[3]/a')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[2]/article/div[2]/button[2]/div/span')[0].click()
browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[2]/span')[0].click()

clues_across = []
clues_down = []

clues_across.append(browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/article/section[2]/div[1]/ol')[0].text.split('\n'))
clues_down.append(browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div/article/section[2]/div[2]/ol')[0].text.split('\n'))

print(clues_across)
print(clues_down)

solutions = []

#print("Audio bakalım",browser.find_elements_by_tag_name("audio"))

for i in range(25):
    css_link = '#xwd-board > g:nth-child(5) > g:nth-child('+str(i+1)+')'
    #print(css_link)
    if not browser.find_elements_by_css_selector(css_link):
        solutions.append('')
    else:
        solutions.append(browser.find_elements_by_css_selector(css_link)[0].text.split("\n"))

print(solutions)  # Solutions are listed as increasing order from left to right and top to down                                                      
browser.quit()

