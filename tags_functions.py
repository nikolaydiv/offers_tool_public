import requests
import json
import time

from base_class import profile_fetcher, tags_updater, ButtonUpdater

headers_put = {
    'X-Application-Key': 'secret_key',
    'Content-Type': 'application/json'
}
put_url = "put_url"


def get_profile_button_clicked(e):
    from buttons import get_profile_buttons
    entered_support_id = get_profile_buttons["get_profile_line"].value
    if profile_fetcher.get_profile(entered_support_id):
        profile_fetcher.update_button_text(button=get_profile_buttons["submit_button"], text="Успешно!")
    else:
        profile_fetcher.update_button_text(button=get_profile_buttons["submit_button"], text="Неверный supid")


# Функции обновления тегов 11 TICKETS

def update_tags_11_1_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(0.99, 0.99, 0.99)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_1")


def update_tags_11_2_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(2.5, 4, 0.99)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_2")


def update_tags_11_3_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(3.5, 5, 0.99)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_3")


def update_tags_11_4_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(4.5, 8, 0.99)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_4")


def update_tags_11_5_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(4.5, 8, 18)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_5")


def update_tags_11_6_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(6, 18, 18)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_6")


def update_tags_11_7_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(6, 18, 37)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_7")


def update_tags_11_8_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(10, 30, 37)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_8")


def update_tags_11_9_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(10, 30, 61)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_9")


def update_tags_11_10_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(20, 50, 61)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_10")


def update_tags_11_11_function(e):
    from buttons import update_tags_11_buttons
    tags_updater.update_tags_tickets(20, 50, 121)
    button_updater = ButtonUpdater(update_tags_11_buttons)
    button_updater.update_buttons("update_tags_11_11")


update_tags_11_functions = {
    "function_1": update_tags_11_1_function,
    "function_2": update_tags_11_2_function,
    "function_3": update_tags_11_3_function,
    "function_4": update_tags_11_4_function,
    "function_5": update_tags_11_5_function,
    "function_6": update_tags_11_6_function,
    "function_7": update_tags_11_7_function,
    "function_8": update_tags_11_8_function,
    "function_9": update_tags_11_9_function,
    "function_10": update_tags_11_10_function,
    "function_11": update_tags_11_11_function
}


# Функции обновления тегов 10 TICKETS

def update_tags_10_1_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(0.99, 0.99, 0.99)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_1")


def update_tags_10_2_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(2.5, 4, 0.99)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_2")


def update_tags_10_3_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(3.5, 5, 0.99)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_3")


def update_tags_10_4_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(4.5, 0.99, 17)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_4")


def update_tags_10_5_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(6, 18, 18)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_5")


def update_tags_10_6_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(6, 18, 37)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_6")


def update_tags_10_7_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(10, 30, 37)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_7")


def update_tags_10_8_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(10, 30, 61)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_8")


def update_tags_10_9_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(20, 50, 61)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_9")


def update_tags_10_10_function(e):
    from buttons import update_tags_10_buttons
    tags_updater.update_tags_tickets(20, 50, 121)
    button_updater = ButtonUpdater(update_tags_10_buttons)
    button_updater.update_buttons("update_tags_10_10")


update_tags_10_functions = {
    "function_1": update_tags_10_1_function,
    "function_2": update_tags_10_2_function,
    "function_3": update_tags_10_3_function,
    "function_4": update_tags_10_4_function,
    "function_5": update_tags_10_5_function,
    "function_6": update_tags_10_6_function,
    "function_7": update_tags_10_7_function,
    "function_8": update_tags_10_8_function,
    "function_9": update_tags_10_9_function,
    "function_10": update_tags_10_10_function
}


# Функции обновления тегов 10 TICKETS RASKAT

def update_tags_10_1_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(0.99, 0.99, 0.99)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_1")


def update_tags_10_2_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(2.5, 4, 0.99)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_2")


def update_tags_10_3_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(3.5, 5, 0.99)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_3")


def update_tags_10_4_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(4.5, 8, 0.99)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_4")


def update_tags_10_5_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(4.5, 8, 18)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_5")


def update_tags_10_6_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(6, 18, 18)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_6")


def update_tags_10_7_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(6, 18, 37)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_7")


def update_tags_10_8_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(10, 30, 37)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_8")


def update_tags_10_9_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(10, 30, 61)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_9")


def update_tags_10_10_function_raskat(e):
    from buttons import update_tags_10_buttons_raskat
    tags_updater.update_tags_tickets(20, 50, 121)
    button_updater = ButtonUpdater(update_tags_10_buttons_raskat)
    button_updater.update_buttons("update_tags_10_10")


update_tags_10_functions_raskat = {
    "function_1": update_tags_10_1_function_raskat,
    "function_2": update_tags_10_2_function_raskat,
    "function_3": update_tags_10_3_function_raskat,
    "function_4": update_tags_10_4_function_raskat,
    "function_5": update_tags_10_5_function_raskat,
    "function_6": update_tags_10_6_function_raskat,
    "function_7": update_tags_10_7_function_raskat,
    "function_8": update_tags_10_8_function_raskat,
    "function_9": update_tags_10_9_function_raskat,
    "function_10": update_tags_10_10_function_raskat
}


# Функции обновления тегов 9 TICKETS

def update_tags_9_1_function(e):
    from buttons import update_tags_9_buttons
    tags_updater.update_tags_tickets(0.99, 0.99, 0.99)
    button_updater = ButtonUpdater(update_tags_9_buttons)
    button_updater.update_buttons("update_tags_9_1")


def update_tags_9_2_function(e):
    from buttons import update_tags_9_buttons
    tags_updater.update_tags_tickets(2.5, 4, 0.99)
    button_updater = ButtonUpdater(update_tags_9_buttons)
    button_updater.update_buttons("update_tags_9_2")


def update_tags_9_3_function(e):
    from buttons import update_tags_9_buttons
    tags_updater.update_tags_tickets(3.5, 5, 0.99)
    button_updater = ButtonUpdater(update_tags_9_buttons)
    button_updater.update_buttons("update_tags_9_3")


def update_tags_9_4_function(e):
    from buttons import update_tags_9_buttons
    tags_updater.update_tags_tickets(4.5, 5, 17)
    button_updater = ButtonUpdater(update_tags_9_buttons)
    button_updater.update_buttons("update_tags_9_4")


def update_tags_9_5_function(e):
    from buttons import update_tags_9_buttons
    tags_updater.update_tags_tickets(6, 5, 24)
    button_updater = ButtonUpdater(update_tags_9_buttons)
    button_updater.update_buttons("update_tags_9_5")


def update_tags_9_6_function(e):
    from buttons import update_tags_9_buttons
    tags_updater.update_tags_tickets(10, 30, 24)
    button_updater = ButtonUpdater(update_tags_9_buttons)
    button_updater.update_buttons("update_tags_9_6")


def update_tags_9_7_function(e):
    from buttons import update_tags_9_buttons
    tags_updater.update_tags_tickets(10, 30, 61)
    button_updater = ButtonUpdater(update_tags_9_buttons)
    button_updater.update_buttons("update_tags_9_7")


def update_tags_9_8_function(e):
    from buttons import update_tags_9_buttons
    tags_updater.update_tags_tickets(20, 50, 61)
    button_updater = ButtonUpdater(update_tags_9_buttons)
    button_updater.update_buttons("update_tags_9_8")


def update_tags_9_9_function(e):
    from buttons import update_tags_9_buttons
    tags_updater.update_tags_tickets(20, 50, 121)
    button_updater = ButtonUpdater(update_tags_9_buttons)
    button_updater.update_buttons("update_tags_9_9")


update_tags_9_functions = {
    "function_1": update_tags_9_1_function,
    "function_2": update_tags_9_2_function,
    "function_3": update_tags_9_3_function,
    "function_4": update_tags_9_4_function,
    "function_5": update_tags_9_5_function,
    "function_6": update_tags_9_6_function,
    "function_7": update_tags_9_7_function,
    "function_8": update_tags_9_8_function,
    "function_9": update_tags_9_9_function
}


# Функции обновления тегов 7 TICKETS

def update_tags_7_1_function(e):
    from buttons import update_tags_7_buttons
    tags_updater.update_tags_tickets(0.99, 0.99, 0.99)
    button_updater = ButtonUpdater(update_tags_7_buttons)
    button_updater.update_buttons("update_tags_7_1")


def update_tags_7_2_function(e):
    from buttons import update_tags_7_buttons
    tags_updater.update_tags_tickets(2.5, 4, 0.99)
    button_updater = ButtonUpdater(update_tags_7_buttons)
    button_updater.update_buttons("update_tags_7_2")


def update_tags_7_3_function(e):
    from buttons import update_tags_7_buttons
    tags_updater.update_tags_tickets(3.5, 5, 0.99)
    button_updater = ButtonUpdater(update_tags_7_buttons)
    button_updater.update_buttons("update_tags_7_3")


def update_tags_7_4_function(e):
    from buttons import update_tags_7_buttons
    tags_updater.update_tags_tickets(4.5, 8, 17)
    button_updater = ButtonUpdater(update_tags_7_buttons)
    button_updater.update_buttons("update_tags_7_4")


def update_tags_7_5_function(e):
    from buttons import update_tags_7_buttons
    tags_updater.update_tags_tickets(6, 18, 37)
    button_updater = ButtonUpdater(update_tags_7_buttons)
    button_updater.update_buttons("update_tags_7_5")


def update_tags_7_6_function(e):
    from buttons import update_tags_7_buttons
    tags_updater.update_tags_tickets(10, 30, 61)
    button_updater = ButtonUpdater(update_tags_7_buttons)
    button_updater.update_buttons("update_tags_7_6")


def update_tags_7_7_function(e):
    from buttons import update_tags_7_buttons
    tags_updater.update_tags_tickets(20, 50, 121)
    button_updater = ButtonUpdater(update_tags_7_buttons)
    button_updater.update_buttons("update_tags_7_7")


update_tags_7_functions = {
    "function_1": update_tags_7_1_function,
    "function_2": update_tags_7_2_function,
    "function_3": update_tags_7_3_function,
    "function_4": update_tags_7_4_function,
    "function_5": update_tags_7_5_function,
    "function_6": update_tags_7_6_function,
    "function_7": update_tags_7_7_function
}


# Функции обновления тегов 3 TICKETS

def update_tags_3_1_function(e):
    from buttons import update_tags_3_buttons
    tags_updater.update_tags_tickets(0.99, 0.99, 0.99)
    button_updater = ButtonUpdater(update_tags_3_buttons)
    button_updater.update_buttons("update_tags_3_1")


def update_tags_3_2_function(e):
    from buttons import update_tags_3_buttons
    tags_updater.update_tags_tickets(5, 0.99, 0.99)
    button_updater = ButtonUpdater(update_tags_3_buttons)
    button_updater.update_buttons("update_tags_3_2")
    i = 1
    for key, button in update_tags_3_buttons.items():
        if button == update_tags_3_buttons["update_tags_3_2"]:
            button.content.value = "Теги обновлены!"
            button.update()
            i += 1
            continue
        button.content.value = "Update tags " + str(i)
        i += 1
        button.update()


def update_tags_3_3_function(e):
    from buttons import update_tags_3_buttons
    tags_updater.update_tags_tickets(10, 0.99, 0.99)
    button_updater = ButtonUpdater(update_tags_3_buttons)
    button_updater.update_buttons("update_tags_3_3")


update_tags_3_functions = {
    "function_1": update_tags_3_1_function,
    "function_2": update_tags_3_2_function,
    "function_3": update_tags_3_3_function
}


# Функции обновления тегов NO HINT

def no_hint_1_function(e):
    from buttons import no_hint_buttons
    tags_updater.update_tags_total_spent(0.99)
    button_updater = ButtonUpdater(no_hint_buttons)
    button_updater.update_buttons_other("no_hint_1")


def no_hint_2_function(e):
    from buttons import no_hint_buttons
    tags_updater.update_tags_total_spent(50)
    button_updater = ButtonUpdater(no_hint_buttons)
    button_updater.update_buttons_other("no_hint_2")


def no_hint_3_function(e):
    from buttons import no_hint_buttons
    tags_updater.update_tags_total_spent(200)
    button_updater = ButtonUpdater(no_hint_buttons)
    button_updater.update_buttons_other("no_hint_3")


def no_hint_4_function(e):
    from buttons import no_hint_buttons
    tags_updater.update_tags_total_spent(351)
    button_updater = ButtonUpdater(no_hint_buttons)
    button_updater.update_buttons_other("no_hint_4")


no_hint_functions = {
    "function_1": no_hint_1_function,
    "function_2": no_hint_2_function,
    "function_3": no_hint_3_function,
    "function_4": no_hint_4_function
}


# Функции обновления тегов COLLECTION GACHA

def collection_gacha_tags_function_1(e):
    from buttons import collection_gacha_tags_buttons
    tags_updater.update_tags_total_spent(0.99)
    button_updater = ButtonUpdater(collection_gacha_tags_buttons)
    button_updater.update_buttons_other("collection_gacha_1")


def collection_gacha_tags_function_2(e):
    from buttons import collection_gacha_tags_buttons
    tags_updater.update_tags_total_spent(26)
    button_updater = ButtonUpdater(collection_gacha_tags_buttons)
    button_updater.update_buttons_other("collection_gacha_2")


collection_gacha_tags_functions = {
    "function_1": collection_gacha_tags_function_1,
    "function_2": collection_gacha_tags_function_2
}


# Функции обновления тегов WEAPON LTO

def weapon_lto_function_1(e):
    from buttons import weapon_lto_buttons
    tags_updater.update_tags_total_spent(0.99)
    button_updater = ButtonUpdater(weapon_lto_buttons)
    button_updater.update_buttons_other("weapon_lto_1")


def weapon_lto_function_2(e):
    from buttons import weapon_lto_buttons
    tags_updater.update_tags_total_spent(50)
    button_updater = ButtonUpdater(weapon_lto_buttons)
    button_updater.update_buttons_other("weapon_lto_2")


def weapon_lto_function_3(e):
    from buttons import weapon_lto_buttons
    tags_updater.update_tags_total_spent(100)
    button_updater = ButtonUpdater(weapon_lto_buttons)
    button_updater.update_buttons_other("weapon_lto_3")


def weapon_lto_function_4(e):
    from buttons import weapon_lto_buttons
    tags_updater.update_tags_total_spent(151)
    button_updater = ButtonUpdater(weapon_lto_buttons)
    button_updater.update_buttons_other("weapon_lto_4")


weapon_lto_functions = {
    "function_1": weapon_lto_function_1,
    "function_2": weapon_lto_function_2,
    "function_3": weapon_lto_function_3,
    "function_4": weapon_lto_function_4
}


# Функции обновления тегов SHINY

def shiny_function_1(e):
    from buttons import shiny_buttons
    tags_updater.update_tags_total_spent(0.99)
    button_updater = ButtonUpdater(shiny_buttons)
    button_updater.update_buttons_other("shiny_1")


def shiny_function_2(e):
    from buttons import shiny_buttons
    tags_updater.update_tags_total_spent(50)
    button_updater = ButtonUpdater(shiny_buttons)
    button_updater.update_buttons_other("shiny_2")


def shiny_function_3(e):
    from buttons import shiny_buttons
    tags_updater.update_tags_total_spent(65)
    button_updater = ButtonUpdater(shiny_buttons)
    button_updater.update_buttons_other("shiny_3")


def shiny_function_4(e):
    from buttons import shiny_buttons
    tags_updater.update_tags_total_spent(100)
    button_updater = ButtonUpdater(shiny_buttons)
    button_updater.update_buttons_other("shiny_4")


def shiny_function_5(e):
    from buttons import shiny_buttons
    tags_updater.update_tags_total_spent(151)
    button_updater = ButtonUpdater(shiny_buttons)
    button_updater.update_buttons_other("shiny_5")


shiny_functions = {
    "function_1": shiny_function_1,
    "function_2": shiny_function_2,
    "function_3": shiny_function_3,
    "function_4": shiny_function_4,
    "function_5": shiny_function_5
}


# Функции обновления тегов NEW SHINY

def new_shiny_function_1(e):
    from buttons import new_shiny_buttons
    tags_updater.update_tags_new_total_spent(0.99)
    button_updater = ButtonUpdater(new_shiny_buttons)
    button_updater.update_buttons_other("shiny_1")


def new_shiny_function_2(e):
    from buttons import new_shiny_buttons
    tags_updater.update_tags_new_total_spent(45)
    button_updater = ButtonUpdater(new_shiny_buttons)
    button_updater.update_buttons_other("shiny_2")


def new_shiny_function_3(e):
    from buttons import new_shiny_buttons
    tags_updater.update_tags_new_total_spent(75)
    button_updater = ButtonUpdater(new_shiny_buttons)
    button_updater.update_buttons_other("shiny_3")


def new_shiny_function_4(e):
    from buttons import new_shiny_buttons
    tags_updater.update_tags_new_total_spent(120)
    button_updater = ButtonUpdater(new_shiny_buttons)
    button_updater.update_buttons_other("shiny_4")


def new_shiny_function_5(e):
    from buttons import new_shiny_buttons
    tags_updater.update_tags_new_total_spent(151)
    button_updater = ButtonUpdater(new_shiny_buttons)
    button_updater.update_buttons_other("shiny_5")


new_shiny_functions = {
    "function_1": new_shiny_function_1,
    "function_2": new_shiny_function_2,
    "function_3": new_shiny_function_3,
    "function_4": new_shiny_function_4,
    "function_5": new_shiny_function_5
}


# Функции обновления тегов THEO

def theo_function_1(e):
    from buttons import usual_theo_tags_buttons
    tags_updater.update_tags_theo(0.99, 0.99)
    button_updater = ButtonUpdater(usual_theo_tags_buttons)
    button_updater.update_buttons_other("theo_1")


def theo_function_2(e):
    from buttons import usual_theo_tags_buttons
    tags_updater.update_tags_theo(0.99, 30)
    button_updater = ButtonUpdater(usual_theo_tags_buttons)
    button_updater.update_buttons_other("theo_2")


def theo_function_3(e):
    from buttons import usual_theo_tags_buttons
    tags_updater.update_tags_theo(0.99, 80)
    button_updater = ButtonUpdater(usual_theo_tags_buttons)
    button_updater.update_buttons_other("theo_3")


def theo_function_4(e):
    from buttons import usual_theo_tags_buttons
    tags_updater.update_tags_theo(16, 80)
    button_updater = ButtonUpdater(usual_theo_tags_buttons)
    button_updater.update_buttons_other("theo_4")


def theo_function_5(e):
    from buttons import usual_theo_tags_buttons
    tags_updater.update_tags_theo(16, 200)
    button_updater = ButtonUpdater(usual_theo_tags_buttons)
    button_updater.update_buttons_other("theo_5")


def theo_function_6(e):
    from buttons import usual_theo_tags_buttons
    tags_updater.update_tags_theo(20, 200)
    button_updater = ButtonUpdater(usual_theo_tags_buttons)
    button_updater.update_buttons_other("theo_6")


def theo_function_7(e):
    from buttons import usual_theo_tags_buttons
    tags_updater.update_tags_theo(20, 600)
    button_updater = ButtonUpdater(usual_theo_tags_buttons)
    button_updater.update_buttons_other("theo_7")


theo_functions = {
    "function_1": theo_function_1,
    "function_2": theo_function_2,
    "function_3": theo_function_3,
    "function_4": theo_function_4,
    "function_5": theo_function_5,
    "function_6": theo_function_6,
    "function_7": theo_function_7
}


# Функции обновления тегов ADD THEO

def add_theo_function_1(e):
    from buttons import add_theo_tags_buttons
    tags_updater.update_tags_theo(0.99, 0.99)
    button_updater = ButtonUpdater(add_theo_tags_buttons)
    button_updater.update_buttons_other("theo_1")


def add_theo_function_2(e):
    from buttons import add_theo_tags_buttons
    tags_updater.update_tags_theo(0.99, 30)
    button_updater = ButtonUpdater(add_theo_tags_buttons)
    button_updater.update_buttons_other("theo_2")


def add_theo_function_3(e):
    from buttons import add_theo_tags_buttons
    tags_updater.update_tags_theo(15, 80)
    button_updater = ButtonUpdater(add_theo_tags_buttons)
    button_updater.update_buttons_other("theo_3")


def add_theo_function_4(e):
    from buttons import add_theo_tags_buttons
    tags_updater.update_tags_theo(17, 80)
    button_updater = ButtonUpdater(add_theo_tags_buttons)
    button_updater.update_buttons_other("theo_4")


def add_theo_function_5(e):
    from buttons import add_theo_tags_buttons
    tags_updater.update_tags_theo(20, 200)
    button_updater = ButtonUpdater(add_theo_tags_buttons)
    button_updater.update_buttons_other("theo_5")


def add_theo_function_6(e):
    from buttons import add_theo_tags_buttons
    tags_updater.update_tags_theo(0.99, 200)
    button_updater = ButtonUpdater(add_theo_tags_buttons)
    button_updater.update_buttons_other("theo_6")


add_theo_functions = {
    "function_1": add_theo_function_1,
    "function_2": add_theo_function_2,
    "function_3": add_theo_function_3,
    "function_4": add_theo_function_4,
    "function_5": add_theo_function_5,
    "function_6": add_theo_function_6
}


# Функции обновления тегов LTO_OTO_GC

def lto_oto_gc_function_1(e):
    from buttons import lto_oto_gc_buttons
    tags_updater.update_tags_new_total_spent(0.99)
    button_updater = ButtonUpdater(lto_oto_gc_buttons)
    button_updater.update_buttons_other("lto_oto_gc_1")


def lto_oto_gc_function_2(e):
    from buttons import lto_oto_gc_buttons
    tags_updater.update_tags_new_total_spent(50)
    button_updater = ButtonUpdater(lto_oto_gc_buttons)
    button_updater.update_buttons_other("lto_oto_gc_2")


def lto_oto_gc_function_3(e):
    from buttons import lto_oto_gc_buttons
    tags_updater.update_tags_new_total_spent(100)
    button_updater = ButtonUpdater(lto_oto_gc_buttons)
    button_updater.update_buttons_other("lto_oto_gc_3")


def lto_oto_gc_function_4(e):
    from buttons import lto_oto_gc_buttons
    tags_updater.update_tags_new_total_spent(170)
    button_updater = ButtonUpdater(lto_oto_gc_buttons)
    button_updater.update_buttons_other("lto_oto_gc_4")


lto_oto_gc_functions = {
    "function_1": lto_oto_gc_function_1,
    "function_2": lto_oto_gc_function_2,
    "function_3": lto_oto_gc_function_3,
    "function_4": lto_oto_gc_function_4
}


# Функции обновления тегов AMONG

def among_function_1(e):
    from buttons import among_buttons
    tags_updater.update_tags_new_total_spent(0.99)
    button_updater = ButtonUpdater(among_buttons)
    button_updater.update_buttons_other("among_1")


def among_function_2(e):
    from buttons import among_buttons
    tags_updater.update_tags_new_total_spent(200)
    button_updater = ButtonUpdater(among_buttons)
    button_updater.update_buttons_other("among_2")


def among_function_3(e):
    from buttons import among_buttons
    tags_updater.update_tags_new_total_spent(301)
    button_updater = ButtonUpdater(among_buttons)
    button_updater.update_buttons_other("among_3")


among_functions = {
    "function_1": among_function_1,
    "function_2": among_function_2,
    "function_3": among_function_3
}


# Функции обновления тегов NEW AMONG

def new_among_function_1(e):
    from buttons import new_among_buttons
    tags_updater.update_tags_average_10(0.99)
    button_updater = ButtonUpdater(new_among_buttons)
    button_updater.update_buttons_other("among_1")


def new_among_function_2(e):
    from buttons import new_among_buttons
    tags_updater.update_tags_average_10(5)
    button_updater = ButtonUpdater(new_among_buttons)
    button_updater.update_buttons_other("among_2")


def new_among_function_3(e):
    from buttons import new_among_buttons
    tags_updater.update_tags_average_10(10)
    button_updater = ButtonUpdater(new_among_buttons)
    button_updater.update_buttons_other("among_3")


new_among_functions = {
    "function_1": new_among_function_1,
    "function_2": new_among_function_2,
    "function_3": new_among_function_3
}


# Функции обновления тегов LABYRINTH

def labyrinth_function_1(e):
    from buttons import labyrinth_buttons
    tags_updater.update_tags_new_total_spent(0.99)
    button_updater = ButtonUpdater(labyrinth_buttons)
    button_updater.update_buttons_other("labyrinth_1")


def labyrinth_function_2(e):
    from buttons import labyrinth_buttons
    tags_updater.update_tags_new_total_spent(50)
    button_updater = ButtonUpdater(labyrinth_buttons)
    button_updater.update_buttons_other("labyrinth_2")


def labyrinth_function_3(e):
    from buttons import labyrinth_buttons
    tags_updater.update_tags_new_total_spent(200)
    button_updater = ButtonUpdater(labyrinth_buttons)
    button_updater.update_buttons_other("labyrinth_3")


def labyrinth_function_4(e):
    from buttons import labyrinth_buttons
    tags_updater.update_tags_new_total_spent(301)
    button_updater = ButtonUpdater(labyrinth_buttons)
    button_updater.update_buttons_other("labyrinth_4")


labyrinth_functions = {
    "function_1": labyrinth_function_1,
    "function_2": labyrinth_function_2,
    "function_3": labyrinth_function_3,
    "function_4": labyrinth_function_4
}


# Функции обновления тегов BOGO

def bogo_function_1(e):
    from buttons import bogo_buttons
    tags_updater.update_tags_total_spent(0.99)
    button_updater = ButtonUpdater(bogo_buttons)
    button_updater.update_buttons_other("bogo_1")


def bogo_function_2(e):
    from buttons import bogo_buttons
    tags_updater.update_tags_total_spent(60)
    button_updater = ButtonUpdater(bogo_buttons)
    button_updater.update_buttons_other("bogo_2")


def bogo_function_3(e):
    from buttons import bogo_buttons
    tags_updater.update_tags_total_spent(151)
    button_updater = ButtonUpdater(bogo_buttons)
    button_updater.update_buttons_other("bogo_3")


def bogo_function_4(e):
    from buttons import bogo_buttons
    tags_updater.update_tags_total_spent(501)
    button_updater = ButtonUpdater(bogo_buttons)
    button_updater.update_buttons_other("bogo_4")


bogo_functions = {
    "function_1": bogo_function_1,
    "function_2": bogo_function_2,
    "function_3": bogo_function_3,
    "function_4": bogo_function_4
}


# Функции обновления тегов COMEBACK

def comeback_function_1(e):
    from buttons import comeback_buttons
    tags_updater.update_tags_average_10(0.99)
    button_updater = ButtonUpdater(comeback_buttons)
    button_updater.update_buttons_other("comeback_1")


def comeback_function_2(e):
    from buttons import comeback_buttons
    tags_updater.update_tags_average_10(12)
    button_updater = ButtonUpdater(comeback_buttons)
    button_updater.update_buttons_other("comeback_2")


def comeback_function_3(e):
    from buttons import comeback_buttons
    tags_updater.update_tags_average_10(17)
    button_updater = ButtonUpdater(comeback_buttons)
    button_updater.update_buttons_other("comeback_3")


def comeback_function_4(e):
    from buttons import comeback_buttons
    tags_updater.update_tags_average_10(21)
    button_updater = ButtonUpdater(comeback_buttons)
    button_updater.update_buttons_other("comeback_4")


comeback_functions = {
    "function_1": comeback_function_1,
    "function_2": comeback_function_2,
    "function_3": comeback_function_3,
    "function_4": comeback_function_4
}


# Функции MY TAGS

def my_tags(e):
    from buttons import my_tags_buttons, PageManager
    page = PageManager.get_page()
    headers = {
        'X-Application-Key': 'secret_key'
    }
    url = put_url + f'?playerIds={profile_fetcher.support_id}'
    response = requests.request("GET", url, headers=headers, data="")
    response_1 = json.loads(response.text)
    my_tags_buttons["tags_field"].value = json.dumps(response_1, indent=4, ensure_ascii=False)
    page.update()


my_tags_functions = {
    "function_1": my_tags
}


def manual_tags(e):
    from buttons import manual_tags_buttons
    payload = json.dumps({
        profile_fetcher.support_id: {
            "nicknameLowercase": "skip",
            "secret_tag_1": float(manual_tags_buttons["some_tag_1"].value),
            "secret_tag_2": float(manual_tags_buttons["some_tag_2"].value),
            "secret_tag_3": 0.99,
            "secret_tag_4": 0.99,
            "secret_tag_5": 0.99,
            "secret_tag_6": 0.99,
            "secret_tag_7": 0.99,
            "secret_tag_8": 0.99,
            "secret_value": 1710309974,
            "secret_tag_9": 1,
            "secret_tag_10": 1,
            "secret_tag_11": 1,
            "secret_tag_12": float(manual_tags_buttons["some_tag_3"].value),
            "secret_tag_13": float(manual_tags_buttons["some_tag_4"].value),
            "secret_tag_14": float(manual_tags_buttons["some_tag_5"].value),
            "secret_tag_15": float(manual_tags_buttons["some_tag_6"].value),
            "secret_tag_16": 0.99,
            "secret_tag_17": 0.99,
            "secret_tag_18": 0.99,
            "secret_tag_19": float(manual_tags_buttons["some_tag_7"].value),
            "secret_tag_20": float(manual_tags_buttons["some_tag_8"].value),
            "secret_tag_21": float(manual_tags_buttons["some_tag_9"].value),
            "secret_tag_22": float(manual_tags_buttons["some_tag_10"].value),
            "secret_tag_23": 1,
            "secret_tag_24": 1,
            "secret_tag_25": 1,
            "secret_tag_26": float(manual_tags_buttons["some_tag_11"].value),
            "secret_tag_27": float(manual_tags_buttons["some_tag_12"].value),
            "secret_tag_28": float(manual_tags_buttons["some_tag_13"].value),
            "secret_tag_29": 0.99,
            "secret_tag_30": 0.99,
            "secret_tag_31": 0.99,
            "secret_tag_32": 0,
            "secret_tag_33": float(manual_tags_buttons["some_tag_14"].value),
            "secret_tag_34": float(manual_tags_buttons["some_tag_15"].value),
            "secret_tag_35": float(manual_tags_buttons["some_tag_16"].value),
            "secret_tag_36": 0,
            "secret_tag_37": float(manual_tags_buttons["some_tag_17"].value),
            "secret_tag_38": float(manual_tags_buttons["some_tag_18"].value),
            "secret_tag_39": float(manual_tags_buttons["some_tag_19"].value)
        }
    })
    requests.request("PUT", put_url, headers=headers_put, data=payload)
    manual_tags_buttons['submit'].content.value = "Done"
    manual_tags_buttons['submit'].update()
    time.sleep(3)
    manual_tags_buttons['submit'].content.value = "Submit"
    manual_tags_buttons['submit'].update()
