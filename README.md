<p align="center">
    <img src="https://appmaster.io/images/no-code-preview.png" height="200">
</p>

<div align="center">
  <h3 align="center">
     NCTP-No Code Automation Testing in Python using Selenium  
  </h3>
</div>

![GitHub](https://img.shields.io/github/license/NagiPragalathan/No_Code_Testing?style=flat-square&logo=github)
![GitHub contributors](https://img.shields.io/github/contributors/NagiPragalathan/No_Code_Testing?logo=github&style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/NagiPragalathan/No_Code_Testing?style=flat-square)
[![Telegram](https://img.shields.io/badge/telegram-nagipragalathan-yellow.svg?logo=telegram)](https://t.me/nagipragalathan)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![Read FAQ](https://img.shields.io/badge/Ask%20Question-Read%20FAQ-000000)](https://www.newton.so/view?tags=nctp)
![GitHub Repo stars](https://img.shields.io/github/stars/NagiPragalathan/No_Code_Testing?style=social)
[![Twitter Follow](https://img.shields.io/twitter/follow/nagipragalathan?style=social)](https://twitter.com/NagiPragalathan)

<div align="center">

**NCTP** is an No Code Automation Testing in Python using
  Selenium. It helps the testers to automate their testcases 
  using a json file. It limits the scalability and less complexity 
  to test the application.! 
  Why? Because `It's over 9000!!!!!`.

It is a work in progress, and it is not ready for production.

[Getting started](#getting-started) • [Supported opcodes](#supported-opcodes) •
[Build](#build) • [Test](#test) •
[Report a bug](https://github.com/)
• [Questions](https://www.newton.so/view?tags=nctp)

</div>

<div align="center">
<img src="https://media3.giphy.com/media/9MbgJKNugBIi6QDwEf/200w.webp?cid=ecf05e474m3sg50anfj1rfi5m8628lnk3tqkd77089nsi4y8&rid=200w.webp&ct=g" height="400" />
</div>

<div align="center">
<h2> Fear of coding the testing files use the NCTP to releive your complexity and upgrade your automation using NCTP for your application. </h2>
</div>

# Setup:
## 1. Installation:
install using the command: `pip install nctp`

## 2. Usage:
<hr/>
<pre>
{ <br/>
    "setup":{<br/>
        "driver_path" : "C:/Users/nagip/Desktop/New_folder/chromedriver.exe", <br/>
        "auto_install":"true", <br/>
        "browser":"Opera", <br/>
        "get":"https://www.saucedemo.com/", <br/>
        "window" : "maximize" <br/>
        "screen_recorder":"true",
        "run_amd_wait":"true"
    }<br/>
}<br/>
</pre>
<hr/>
It is the keyword mandatory to use in the NCTP.

1. `driver_path`: give the location of the selenium chrome driver path.
2. `auto_install`: This key is used to download the chrome driver automatically and install it.
3. `browser`: The browser that you recommend for the auto install.
4. `get`: The URL of the landing page.
5. `window`: Always recommended to use the maximize one. Minimize also can be used if needed.
6. `screen_recorder`: It records the testing from beginning to end.
7. `run_and_wait`: It waits  the window of the browser to run the program.
8. Auto_install can run the folowing browsers:
<pre>
        1. Chrome
        2. ChromeService
        3. Brave
        4. BraveService
        5. Firefox
        6. FirefoxService
        7. IE
        8. IEService
        9. Edge
        10. EdgeService
        11. Opera
</pre>
## 3. Get Elements  
### get_ids = ['id','name','class','xpath']
<pre>
'id': It get the id elements using this keyword. 
'name': It get the name elements using this keyword.
'class': It get the class elements using this keyword.
'xpath': It get the xpath elements using this keyword.
</pre>

### Examples:
<pre>


{   
    "setup":{
        "driver_path" : "C:/Users/nagip/Desktop/New_folder/chromedriver.exe",
        "auto_install":"true",
        "browser":"Opera",  //
        "get":"https://www.saucedemo.com/", //
        "window" : "maximize" //
    },
    "login_testing":{
        "fill_user_name" : {
            "id" : "user-name:sk:minimize",
            "data" : "standard_user"
        },
        "fill_password":{
            "id":"password:sk",
            "data":"secret_sauce"
        },
        "click_login_btn":{
            "id":"login-button:click"
        }
    },
 }
</pre>

### Click the list of Elements line by line at a time
list_data = ['ls_id_clk','ls_name_clk','ls_xpath_clk']

<pre>
{   
    "setup":{
        "driver_path" : "C:/Users/nagip/Desktop/New_folder/chromedriver.exe",
        "auto_install":"true",
        "browser":"Opera",  //
        "get":"https://www.saucedemo.com/", //
        "window" : "maximize" //
    },
    "login_testing":{
        "fill_user_name" : {
            "id" : "user-name:sk:minimize",
            "data" : "standard_user"
        },
        "fill_password":{
            "id":"password:sk",
            "data":"secret_sauce"
        },
        "click_login_btn":{
            "id":"login-button:click"
        }
    },
    "home_page":{
        "ls_id_clk" : ["add-to-cart-sauce-labs-backpack","add-to-cart-sauce-labs-bike-light","add-to-cart-sauce-labs-fleece-jacket"],
        "ls_name_clk" : ["add-to-cart-test.allthethings()-t-shirt-(red)","add-to-cart-sauce-labs-bolt-t-shirt","add-to-cart-sauce-labs-onesie"]
    },
    "view_cart":{
        "select_select_box":{
            "xpath":"//*[@id='header_container']/div[2]/div[2]/span/select:select_by_index@2"   
        },
        "nav_to_view_cart":{
            "xpath": "//*[@id='shopping_cart_container']/a:click:minimize",
            "window":  "maximize"
        }
    }
}
</pre>


    
