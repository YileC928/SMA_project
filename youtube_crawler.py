
# Reference: https://stackoverflow.com/a/57076690/15164646
from selenium import webdriver
import json, time 

def get_videos(ticker):
    driver = webdriver.Chrome("/Users/miao/Desktop/chromedriver") #add path to webdriver
    driver.get('https://www.youtube.com/results?search_query={}+stock'.format(ticker))

    youtube_data = []

    # scrolling to the end of the page
    while True:
        # end_result = "No more results" string at the bottom of the page
        # this will be used to break out of the while loop
        end_result = driver.find_element_by_css_selector('#message').is_displayed()
        driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        time.sleep(1) # could be removed
        #print(end_result)

        if end_result == True:
            break

    print('Extracting results for {}. It might take a while...'.format(ticker))

    for result in driver.find_elements_by_css_selector('.text-wrapper.style-scope.ytd-video-renderer'):
        title = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer').text
        link = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
        channel_name = result.find_element_by_css_selector('.long-byline').text
        channel_link = result.find_element_by_css_selector('#text > a').get_attribute('href')
        views = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[0]

        try:
            time_published = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[1]
        except:
            time_published = None

        try:
            snippet = result.find_element_by_css_selector('.metadata-snippet-container').text
        except:
            snippet = None

        try:
            if result.find_element_by_css_selector('#channel-name .ytd-badge-supported-renderer') is not None:
                verified_badge = True
            else:
                verified_badge = False
        except:
            verified_badge = None

        try:
            extensions = result.find_element_by_css_selector('#badges .ytd-badge-supported-renderer').text
        except:
            extensions = None
        #print(verified_badge)
        
        #threshold for views above 1000
        if "K" in views or "M" in views:
            youtube_data.append({
                'title': title,
                'link': link,
                'channel': {'channel_name': channel_name, 'channel_link': channel_link},
                'views': views,
                'time_published': time_published,
                'snippet': snippet,
                'verified_badge': verified_badge,
                'extensions': extensions,
            })
        
    print("crawled", len(youtube_data), "videos")
    #print(json.dumps(youtube_data, indent=2, ensure_ascii=False))
    return youtube_data

    driver.quit()

#get_video_results()
