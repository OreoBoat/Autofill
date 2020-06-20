#!python3
#country = ("/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div[2]/div[" + str(random.randint(3, 228)) + "]/span") example for using in range string

import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re
import urllib
import random

opts = Options()
#opts.set_headless()
#assert opts.set_headless
driver = Firefox(options=opts)

while True:
    #Looping the website
    Formlink = "https://docs.google.com/forms/d/e/1FAIpQLSdifJL6MJpBjOabcwunIQHJEaxvdDnAZ8L30Of12uwUiSeZ2w/viewform"
    driver.get(Formlink)
    space = " "
    time.sleep(3)

    #What is your gender?
    try : 
        randomgender = ["/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div",
                        "/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div"]
        gender = (random.choice(randomgender))
        print (gender)
        driver.find_element_by_xpath(gender).click()
        time.sleep(1.5)

    except NoSuchElementException:
        print ("First gender input function has failed, using the secodnary one now.")
        superagender = ["/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div",
                        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div"]
        mastergender = (random.choice(superagender))
        print (mastergender)
        driver.find_element_by_xpath(mastergender).click()
        time.sleep(1.5)
    
    #What is your age?
    randomage = (random.randint(20, 50))
    findage = (driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input"))
    findage.send_keys(randomage)
    print("Age is" + space + randomage)
    time.sleep(3)
    
    #Which country are you from?
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[1]/span").click()
    time.sleep(2)
    print ("Processing country")
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div[2]/div[125]/span").click()
    time.sleep(3)
    
    #What city do you reside in?
    print ("Processing city")
    citybox = (driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input"))
    malaysia = ["Batu Pahat",
                "Johor Bahru",
                "Kluang",
                "Kota Tinggi",
                "Kulai",
                "Mersing",
                "Muar",
                "Pontian Kechil",
                "Segamat",
                "Tangkak",
                "Baling",
                "Serdang",
                "Alor Setar",
                "Sungai Petani",
                "Jitra",
                "Kulim",
                "Kuah",
                "Kuala Nerang",
                "Pendang",
                "Pokok Sena",
                "Sik",
                "Yan",
                "Bachok",
                "Gua Musang",
                "Jeli",
                "Kota Bharu",
                "Kuala Krai",
                "Machang",
                "Pasir Mas",
                "Pasir Puteh",
                "Tanah Merah",
                "Tumpat",
                "Alor Gajah",
                "Malacca City",
                "Jasin",
                "Kuala Klawang",
                "Bandar Seri Jempol",
                "Kuala Pilah",
                "Port Dickson",
                "Rembau",
                "Seremban",
                "Tampin",
                "Bentong",
                "Bandar Bera",
                "Tanah Rata",
                "Jerantut",
                "Kuantan",
                "Kuala Lipis",
                "Maran",
                "Pekan",
                "Raub",
                "Kuala Rompin",
                "Temerloh",
                "Bukit Mertajam",
                "Kepala Batas",
                "George Town",
                "Sungai Jawi",
                "Balik Pulau",
                "Tapah",
                "Teluk Intan",
                "Gerik",
                "Kampar",
                "Parit Buntar",
                "Batu Gajah",
                "Kuala Kangsar",
                "Taiping",
                "Seri Manjung",
                "Tanjung Malim",
                "Seri Iskandar",
                "Bagan Datuk",
                "Beaufort",
                "Beluran",
                "Keningau",
                "Kota Kinabatangan",
                "Kota Belud",
                "Kota Kinabalu",
                "Kota Marudu",
                "Kuala Penyu",
                "Kudat",
                "Kunak",
                "Lahad Datu",
                "Nabawan",
                "Papar",
                "Donggongon",
                "Pitas",
                "Putatan",
                "Ranau",
                "Sandakan",
                "Semporna",
                "Sipitang",
                "Tambunan",
                "Tawau",
                "Telupid",
                "Tenom",
                "Tongod",
                "Tuaran",
                "Asajaya",
                "Bau",
                "Belaga",
                "Beluru",
                "Betong",
                "Bintulu",
                "Dalat",
                "Matu",
                "Julau",
                "Kabong",
                "Kanowit",
                "Kapit",
                "Kuching",
                "Lawas",
                "Limbang",
                "Lubok Antu",
                "Lundu",
                "Marudi",
                "Matu",
                "Bintangor",
                "Miri",
                "Mukah",
                "Pakan",
                "Pusa",
                "Kota Samarahan",
                "Saratok",
                "Sarikei",
                "Sebauh",
                "Selangau",
                "Serian",
                "Sibu",
                "Simunjan",
                "Song",
                "Sri Aman",
                "Subis",
                "Belawai",
                "Tatau",
                "Tebedu",
                "Long Lama",
                "Bandar Baru Selayang",
                "Bandar Baru Bangi",
                "Kuala Kubu Bharu",
                "Klang",
                "Teluk Datok",
                "Kuala Selangor",
                "Subang",
                "Sabak",
                "Salak Tinggi",
                "Kampung Raja",
                "Kuala Dungun",
                "Kuala Berang",
                "Chukai",
                "Kuala Nerus",
                "Kuala Terengganu",
                "Marang",
                "Bandar Permaisuri"]
    randomplace = (random.choice(malaysia))
    print (randomplace)
    citybox.send_keys(randomplace)
    time.sleep(2)

    #How many countries have you visited?
    print ("Processing visited countries")
    ranvisit = ["/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]",
                "/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]",
                "/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]",
                "/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]",
                "/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]"]
    visit = (random.choice(ranvisit))
    print (visit)
    driver.find_element_by_xpath(visit).click()
    time.sleep(3)

    #Favourite Country
    print ("Processing favourite country")
    favbox = (driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[1]/input"))
    rfav = ["Cambodia",
            "Taiwan",
            "South Korea",
            "Mongolia",
            "United Arab Emirates",
            "Morocco",
            "Mauritius",
            "Greece",
            "United Kingdom",
            "China",
            "France",
            "United States",
            "Italy",
            "Turkey",
            "Mexico",
            "Thailand",
            "India",
            "Singapore",
            "Japan",
            "Hong Kong",
            "Germany",
            "Russia",
            "Spain",
            "Austria"]

    fav = (random.choice(rfav))
    print (fav)
    favbox.send_keys(fav)
    time.sleep(3)

    #Preferred Mode of Transportation
    print ("Processing transportation mode")
    translol = ["/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div",
                "/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div",
                "/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div"]

    randomtranslol = (random.choice(translol))
    print (randomtranslol)
    driver.find_element_by_xpath(randomtranslol).click()
    time.sleep(3)

    #Ideal Vacation
    print ("Processing ideal vacation")
    mastervacation = ["0", "1", "2"]
    randommaster = (random.choice(mastervacation))
    print (randommaster)

    vacation = ["/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div[1]/div/label/div[2]/div[1]/div[2]",
                "/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div[2]/div/label/div[2]/div[1]/div[2]",
                "/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div[3]/div/label/div[2]/div[1]/div[2]"]

    if randommaster == "0":
        randomvac = (random.choice(vacation))
        driver.find_element_by_xpath(randomvac).click()
        print ("There will be a single vacation choice")
    
    if randommaster == "1":
        randomvac = (random.choice(vacation))
        driver.find_element_by_xpath(randomvac).click()
        print ("There will be two vacation choices")
        
    if randommaster == "2":
        randomvac = (random.choice(vacation))
        driver.find_element_by_xpath(randomvac).click()
        print ("All vacation choices will be selected")
    
    time.sleep(3)
    
    #Travelling abroad
    print ("Processing travelling choice")
    travelchoice = ["/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div[1]/div/label/div[2]/div[1]/div[2]",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div[2]/div/label/div[2]/div[1]/div[2]",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div[3]/div/label/div[2]/div[1]/div[2]",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div[4]/div/label/div[2]/div[1]/div[2]",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div[5]/div/label/div[2]/div[1]/div[2]",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div[6]/div/label/div[2]/div[1]/div[2]",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div[7]/div/label/div[2]/div[1]/div[2]"]
    randomtravel = (random.choice(travelchoice))
    print (randomtravel)
    driver.find_element_by_xpath(randomtravel).click()
    time.sleep(3)

    #Job selection
    print ("Processing job selection")
    travelchance = ["/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div"]

    randomchance = (random.choice(travelchance))
    print (randomchance)
    driver.find_element_by_xpath(randomchance).click()
    time.sleep(3)

    #Longest Vacation
    print ("Processing longest vacation time")
    vacationtime = ["/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[6]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[7]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[8]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[9]/label/div/div[1]/div/div[3]/div"]
    
    randomtime = (random.choice(vacationtime))
    print (randomtime)
    driver.find_element_by_xpath(randomtime).click()
    time.sleep(3)
    
    #Travel Spending
    print ("Processing travel spendings")
    travelsspend = ["/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div/span/div/div[6]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div/span/div/div[7]/label/div/div[1]/div/div[3]/div",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div/span/div/div[8]/label/div/div[1]/div/div[3]/div"]
    
    randomspend = (random.choice(travelsspend))
    print (randomspend)
    driver.find_element_by_xpath(randomspend).click()
    time.sleep(3)
    
    #Next Vacation Plans
    print ("Processing vacation plan")
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[1]/div[1]/div[1]/span").click()
    time.sleep(3)
    vacationplan = ["/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[9]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[11]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[12]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[28]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[36]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[38]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[44]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[45]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[60]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[62]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[71]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[72]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[76]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[87]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[92]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[93]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[94]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[99]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[101]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[107]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[121]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[123]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[132]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[136]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[144]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[145]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[152]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[163]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[165]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[169]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[172]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[186]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[193]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[197]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[198]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[203]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[209]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[216]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[217]/span",
                    "/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[2]/div[218]/span"]
    
    randomplan = (random.choice(vacationplan))
    print (randomplan)
    driver.find_element_by_xpath(randomplan).click()
    time.sleep(3)

    #Submit and quit driver
    googleurl = "https://www.google.com/"
    print("Submitting the form")
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div").click()
    print("Submit completed!")
    print("Sleeping for 3 seconds before continuing the loop and going to" + space + googleurl)
    time.sleep(3)
    driver.get(googleurl)
    print("Redirecting to" + space + Formlink)
    time.sleep(2)