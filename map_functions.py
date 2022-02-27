from selenium import webdriver
import folium
from folium import plugins
import os
import warnings

def sukurti_zemelapi(koordinates):
    mapobj = folium.Map(location=(55.1694, 23.8813), zoom_start=8)

    if not koordinates == []:
        count = 1
        for i in koordinates:
            folium.Marker(location=[i[0], i[1]],
                          icon=plugins.BeautifyIcon(number=count,
                                                    border_color='blue',
                                                    border_width=1,
                                                    text_color='red',
                                                    inner_icon_style='margin-top:0px;')).add_to(mapobj)
            count += 1

        folium.PolyLine(koordinates,
                            color="blue",
                            weight=2,
                            fill=False,
                            fill_opacity=0.5).add_to(mapobj)
    else:
        pass
    mapobj.save('zemelapis.html')
    warnings.filterwarnings("ignore")
    class MyBot:
        def __init__(self):
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
            self.options = webdriver.ChromeOptions()
            self.options.headless = True
            self.options.add_argument(f'user-agent={user_agent}')
            self.options.add_argument(f"--window-size=1920,1080")
            self.options.add_argument('--ignore-certificate-errors')
            self.options.add_argument('--allow-running-insecure-content')
            self.options.add_argument("--disable-extensions")
            self.options.add_argument("--proxy-server='direct://'")
            self.options.add_argument("--proxy-bypass-list=*")
            self.options.add_argument("--start-maximized")
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('--no-sandbox')
            self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=self.options)
            self.mapUrl = 'file://{0}/{1}'.format(os.getcwd(), 'zemelapis.html')
            self.driver.get(self.mapUrl)
            self.driver.set_window_size(1150, 900)
            self.driver.get_screenshot_as_file('zemelapis.png')
            self.driver.quit()
    MyBot()