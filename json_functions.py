import time
import flet as ft

from base_class import JsonOpener


# Функции TICKETS BANS 11

def open_json_function_11(e: ft.FilePickerResultEvent):
    from buttons import tickets_bans_11_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_bans_11_buttons["selected_files_11"])
    page.json_checker = json_checker
    json_checker.open_json(e, "json_data_11")


def download_json_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_tickets(11)


def reset_function_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_tickets(11)


def check_bans_11_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 0)


def check_bans_11_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 1)


def check_bans_11_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 2)


def check_bans_11_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 3)


def check_bans_11_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 4)


def check_bans_11_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 5)


def check_bans_11_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 6)


def check_bans_11_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 7)


def check_bans_11_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 8)


def check_bans_11_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 9)


def check_bans_11_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(11, 10)


def check_bans_11_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 11)


def check_bans_11_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 12)


def check_bans_11_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 13)


def check_bans_11_15(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 14)


def check_bans_11_16(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 15)


def check_bans_11_17(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 16)


def check_bans_11_18(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 17)


def check_bans_11_19(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 18)


def check_bans_11_20(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 19)


def check_bans_11_21(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 20)


def check_bans_11_22(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(11, 21)


def check_all_bans_tickets_11(e):
    from buttons import PageManager, tickets_bans_11_buttons
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 23):
        function_name = f"check_bans_11_{i}"
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 23 and k < 22:
        tickets_bans_11_buttons[f'ban_11_{i}'].text = json_checker.json_data_11['global'][k]['_id']
        i += 1
        k += 1
    page.update()


bans_11_functions = {
    "open_json": open_json_function_11,
    "download_json": download_json_11,
    "reset": reset_function_11,
    "function_1": check_bans_11_1,
    "function_2": check_bans_11_2,
    "function_3": check_bans_11_3,
    "function_4": check_bans_11_4,
    "function_5": check_bans_11_5,
    "function_6": check_bans_11_6,
    "function_7": check_bans_11_7,
    "function_8": check_bans_11_8,
    "function_9": check_bans_11_9,
    "function_10": check_bans_11_10,
    "function_11": check_bans_11_11,
    "function_12": check_bans_11_12,
    "function_13": check_bans_11_13,
    "function_14": check_bans_11_14,
    "function_15": check_bans_11_15,
    "function_16": check_bans_11_16,
    "function_17": check_bans_11_17,
    "function_18": check_bans_11_18,
    "function_19": check_bans_11_19,
    "function_20": check_bans_11_20,
    "function_21": check_bans_11_21,
    "function_22": check_bans_11_22,
    "check_all": check_all_bans_tickets_11
}


# Функции TICKETS BANS 10

def open_json_function_10(e: ft.FilePickerResultEvent):
    from buttons import tickets_bans_10_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_bans_10_buttons["selected_files_10"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_10')


def download_json_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_tickets(10)


def reset_function_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_tickets(10)


def check_bans_10_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 0)


def check_bans_10_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 1)


def check_bans_10_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 2)


def check_bans_10_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 3)


def check_bans_10_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 4)


def check_bans_10_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 5)


def check_bans_10_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 6)


def check_bans_10_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 7)


def check_bans_10_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 8)


def check_bans_10_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(10, 9)


def check_bans_10_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 10)


def check_bans_10_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 11)


def check_bans_10_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 12)


def check_bans_10_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 13)


def check_bans_10_15(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 14)


def check_bans_10_16(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 15)


def check_bans_10_17(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 16)


def check_bans_10_18(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 17)


def check_bans_10_19(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 18)


def check_bans_10_20(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(10, 19)


def check_all_bans_tickets_10(e):
    from buttons import PageManager, tickets_bans_10_buttons
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 21):
        function_name = f"check_bans_10_{i}"
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 21 and k < 20:
        tickets_bans_10_buttons[f'ban_10_{i}'].text = json_checker.json_data_10['global'][k]['_id']
        i += 1
        k += 1
    page.update()


bans_10_functions = {
    "open_json": open_json_function_10,
    "download_json": download_json_10,
    "reset": reset_function_10,
    "function_1": check_bans_10_1,
    "function_2": check_bans_10_2,
    "function_3": check_bans_10_3,
    "function_4": check_bans_10_4,
    "function_5": check_bans_10_5,
    "function_6": check_bans_10_6,
    "function_7": check_bans_10_7,
    "function_8": check_bans_10_8,
    "function_9": check_bans_10_9,
    "function_10": check_bans_10_10,
    "function_11": check_bans_10_11,
    "function_12": check_bans_10_12,
    "function_13": check_bans_10_13,
    "function_14": check_bans_10_14,
    "function_15": check_bans_10_15,
    "function_16": check_bans_10_16,
    "function_17": check_bans_10_17,
    "function_18": check_bans_10_18,
    "function_19": check_bans_10_19,
    "function_20": check_bans_10_20,
    "check_all": check_all_bans_tickets_10
}


# Функции TICKETS BANS 9

def open_json_function_9(e: ft.FilePickerResultEvent):
    from buttons import tickets_bans_9_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_bans_9_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_9')


def download_json_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_tickets(9)


def reset_function_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_tickets(9)


def check_bans_9_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(9, 0)


def check_bans_9_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(9, 1)


def check_bans_9_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(9, 2)


def check_bans_9_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(9, 3)


def check_bans_9_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(9, 4)


def check_bans_9_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(9, 5)


def check_bans_9_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(9, 6)


def check_bans_9_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(9, 7)


def check_bans_9_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(9, 8)


def check_bans_9_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(9, 9)


def check_bans_9_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(9, 10)


def check_bans_9_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(9, 11)


def check_bans_9_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(9, 12)


def check_bans_9_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(9, 13)


def check_bans_9_15(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(9, 14)


def check_bans_9_16(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(9, 15)


def check_bans_9_17(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(9, 16)


def check_bans_9_18(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(9, 17)


def check_all_bans_tickets_9(e):
    from buttons import PageManager, tickets_bans_9_buttons
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 19):
        function_name = f"check_bans_9_{i}"
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 19 and k < 18:
        tickets_bans_9_buttons[f'ban_9_{i}'].text = json_checker.json_data_9['global'][k]['_id']
        i += 1
        k += 1
    page.update()


bans_9_functions = {
    "open_json": open_json_function_9,
    "download_json": download_json_9,
    "reset": reset_function_9,
    "function_1": check_bans_9_1,
    "function_2": check_bans_9_2,
    "function_3": check_bans_9_3,
    "function_4": check_bans_9_4,
    "function_5": check_bans_9_5,
    "function_6": check_bans_9_6,
    "function_7": check_bans_9_7,
    "function_8": check_bans_9_8,
    "function_9": check_bans_9_9,
    "function_10": check_bans_9_10,
    "function_11": check_bans_9_11,
    "function_12": check_bans_9_12,
    "function_13": check_bans_9_13,
    "function_14": check_bans_9_14,
    "function_15": check_bans_9_15,
    "function_16": check_bans_9_16,
    "function_17": check_bans_9_17,
    "function_18": check_bans_9_18,
    "check_all": check_all_bans_tickets_9
}


# Функции TICKETS BANS 7

def open_json_function_7(e: ft.FilePickerResultEvent):
    from buttons import tickets_bans_7_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_bans_7_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_7')


def download_json_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_tickets(7)


def reset_function_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_tickets(7)


def check_bans_7_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(7, 0)


def check_bans_7_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(7, 1)


def check_bans_7_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(7, 2)


def check_bans_7_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(7, 3)


def check_bans_7_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(7, 4)


def check_bans_7_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(7, 5)


def check_bans_7_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(7, 6)


def check_bans_7_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(7, 7)


def check_bans_7_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(7, 8)


def check_bans_7_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(7, 9)


def check_bans_7_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(7, 10)


def check_bans_7_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(7, 11)


def check_bans_7_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(7, 12)


def check_bans_7_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(7, 13)


def check_all_bans_tickets_7(e):
    from buttons import PageManager, tickets_bans_7_buttons
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 15):
        function_name = f"check_bans_7_{i}"
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 15 and k < 14:
        tickets_bans_7_buttons[f'ban_7_{i}'].text = json_checker.json_data_7['global'][k]['_id']
        i += 1
        k += 1
    page.update()


bans_7_functions = {
    "open_json": open_json_function_7,
    "download_json": download_json_7,
    "reset": reset_function_7,
    "function_1": check_bans_7_1,
    "function_2": check_bans_7_2,
    "function_3": check_bans_7_3,
    "function_4": check_bans_7_4,
    "function_5": check_bans_7_5,
    "function_6": check_bans_7_6,
    "function_7": check_bans_7_7,
    "function_8": check_bans_7_8,
    "function_9": check_bans_7_9,
    "function_10": check_bans_7_10,
    "function_11": check_bans_7_11,
    "function_12": check_bans_7_12,
    "function_13": check_bans_7_13,
    "function_14": check_bans_7_14,
    "check_all": check_all_bans_tickets_7
}


# Функции TICKETS BANS 3

def open_json_function_3(e: ft.FilePickerResultEvent):
    from buttons import tickets_bans_3_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_bans_3_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_3')


def download_json_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_tickets(3)


def reset_function_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_tickets(3)


def check_bans_3_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(3, 0)


def check_bans_3_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(3, 1)


def check_bans_3_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_lto(3, 2)


def check_bans_3_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(3, 3)


def check_bans_3_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(3, 4)


def check_bans_3_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_oto(3, 5)


def check_all_bans_tickets_3(e):
    from buttons import PageManager, tickets_bans_3_buttons
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 7):
        function_name = f"check_bans_3_{i}"
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 7 and k < 6:
        tickets_bans_3_buttons[f'ban_3_{i}'].text = json_checker.json_data_3['global'][k]['_id']
        i += 1
        k += 1
    page.update()


bans_3_functions = {
    "open_json": open_json_function_3,
    "download_json": download_json_3,
    "reset": reset_function_3,
    "function_1": check_bans_3_1,
    "function_2": check_bans_3_2,
    "function_3": check_bans_3_3,
    "function_4": check_bans_3_4,
    "function_5": check_bans_3_5,
    "function_6": check_bans_3_6,
    "check_all": check_all_bans_tickets_3
}


# Функции TICKETS CRITERIA

def open_json_function_tickets_criteria(e: ft.FilePickerResultEvent):
    from buttons import tickets_criteria_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_criteria_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_criteria')


def download_json_tickets_criteria(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('criteria')


def reset_function_tickets_criteria(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("criteria")


def check_all_tickets_criteria(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_criteria()


tickets_criteria_functions = {
    "open_json": open_json_function_tickets_criteria,
    "download_json": download_json_tickets_criteria,
    "reset": reset_function_tickets_criteria,
    "check_all": check_all_tickets_criteria
}


# Функции NO HINT BANS

def open_json_function_no_hint(e: ft.FilePickerResultEvent):
    from buttons import no_hint_bans_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(no_hint_bans_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_no_hint_bans')


def download_json_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('no_hint_bans')


def reset_function_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("no_hint_bans")


def check_bans_1_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(0)


def check_bans_2_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(1)


def check_bans_3_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(2)


def check_bans_4_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(3)


def check_bans_5_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(4)


def check_bans_6_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(5)


def check_bans_7_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(6)


def check_bans_8_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(7)


def check_bans_9_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(8)


def check_bans_10_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(9)


def check_bans_11_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(10)


def check_bans_12_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(11)


def check_bans_13_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(12)


def check_bans_14_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(13)


def check_bans_15_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(14)


def check_bans_16_no_hint(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bans_no_hint(15)


def check_all_bans_no_hint(e):
    from buttons import PageManager, no_hint_bans_buttons
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 17):
        function_name = f'check_bans_{i}_no_hint'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 17 and k < 16:
        no_hint_bans_buttons[f'button_{i}'].text = json_checker.json_data_no_hint_bans['global'][k]['_id']
        i += 1
        k += 1
    page.update()


no_hint_bans_functions = {
    "open_json": open_json_function_no_hint,
    "download_json": download_json_no_hint,
    "reset": reset_function_no_hint,
    "function_1": check_bans_1_no_hint,
    "function_2": check_bans_2_no_hint,
    "function_3": check_bans_3_no_hint,
    "function_4": check_bans_4_no_hint,
    "function_5": check_bans_5_no_hint,
    "function_6": check_bans_6_no_hint,
    "function_7": check_bans_7_no_hint,
    "function_8": check_bans_8_no_hint,
    "function_9": check_bans_9_no_hint,
    "function_10": check_bans_10_no_hint,
    "function_11": check_bans_11_no_hint,
    "function_12": check_bans_12_no_hint,
    "function_13": check_bans_13_no_hint,
    "function_14": check_bans_14_no_hint,
    "function_15": check_bans_15_no_hint,
    "function_16": check_bans_16_no_hint,
    "check_all": check_all_bans_no_hint
}


# Функции NO HINT BALANCE

def open_json_function_no_hint_balance(e: ft.FilePickerResultEvent):
    from buttons import no_hint_balance_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(no_hint_balance_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_no_hint_balance')


def download_json_no_hint_balance(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('no_hint_balance')


def reset_function_no_hint_balance(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("no_hint_balance")


def check_all_balance(e):
    from buttons import no_hint_balance_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 5):
        function_name = f'check_no_hint_balance_1_{i}'
        func = globals().get(function_name)
        func(e)
    for i in range(1, 5):
        function_name = f'check_no_hint_balance_2_{i}'
        func = globals().get(function_name)
        func(e)
    for i in range(1, 5):
        function_name = f'check_no_hint_balance_3_{i}'
        func = globals().get(function_name)
        func(e)
    for i in range(1, 5):
        function_name = f'check_no_hint_balance_4_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 17 and k < 16:
        no_hint_balance_buttons[f'button_{i}'].text = json_checker.json_data_no_hint_balance['global'][k]['_id']
        i += 1
        k += 1
    page.update()
    print("Буттэ")


def check_no_hint_balance_1_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(0)


def check_no_hint_balance_1_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(1)


def check_no_hint_balance_1_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(2)


def check_no_hint_balance_1_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(3)


def check_no_hint_balance_2_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(4)


def check_no_hint_balance_2_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(5)


def check_no_hint_balance_2_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(6)


def check_no_hint_balance_2_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(7)


def check_no_hint_balance_3_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(8)


def check_no_hint_balance_3_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(9)


def check_no_hint_balance_3_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(10)


def check_no_hint_balance_3_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(11)


def check_no_hint_balance_4_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(12)


def check_no_hint_balance_4_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(13)


def check_no_hint_balance_4_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(14)


def check_no_hint_balance_4_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_balance_no_hint(15)


no_hint_balance_functions = {
    "open_json": open_json_function_no_hint_balance,
    "download_json": download_json_no_hint_balance,
    "reset": reset_function_no_hint_balance,
    "function_1": check_no_hint_balance_1_1,
    "function_2": check_no_hint_balance_1_2,
    "function_3": check_no_hint_balance_1_3,
    "function_4": check_no_hint_balance_1_4,
    "function_5": check_no_hint_balance_2_1,
    "function_6": check_no_hint_balance_2_2,
    "function_7": check_no_hint_balance_2_3,
    "function_8": check_no_hint_balance_2_4,
    "function_9": check_no_hint_balance_3_1,
    "function_10": check_no_hint_balance_3_2,
    "function_11": check_no_hint_balance_3_3,
    "function_12": check_no_hint_balance_3_4,
    "function_13": check_no_hint_balance_4_1,
    "function_14": check_no_hint_balance_4_2,
    "function_15": check_no_hint_balance_4_3,
    "function_16": check_no_hint_balance_4_4,
    "check_all": check_all_balance
}


# Функции BCP json PREVIOUS

def open_json_function_bcp_previous(e: ft.FilePickerResultEvent):
    from buttons import bcp_previous_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(bcp_previous_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_bcp_previous')


def download_json_bcp_previous(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('bcp_previous')


def reset_function_bcp_previous(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("bcp_previous")


def bcp_previous_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_previous(0)


def bcp_previous_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_previous(1)


def bcp_previous_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_previous(2)


def bcp_previous_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_previous(3)


def bcp_previous_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_previous(4)


def bcp_previous_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_previous(5)


def bcp_previous_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_previous(6)


def bcp_previous_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_previous(7)


def bcp_previous_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_previous(8)


def check_all_bcp_previous(e):
    from buttons import bcp_previous_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 10):
        function_name = f'bcp_previous_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 10 and k < 9:
        bcp_previous_buttons[f'button_{i}'].text = json_checker.json_data_bcp_previous['global'][k]['_id']
        i += 1
        k += 1
    page.update()


bcp_previous_functions = {
    "open_json": open_json_function_bcp_previous,
    "download_json": download_json_bcp_previous,
    "reset": reset_function_bcp_previous,
    "function_1": bcp_previous_1,
    "function_2": bcp_previous_2,
    "function_3": bcp_previous_3,
    "function_4": bcp_previous_4,
    "function_5": bcp_previous_5,
    "function_6": bcp_previous_6,
    "function_7": bcp_previous_7,
    "function_8": bcp_previous_8,
    "function_9": bcp_previous_9,
    "check_all": check_all_bcp_previous
}


# Функции BCP json ACTUAL

def open_json_function_bcp_actual(e: ft.FilePickerResultEvent):
    from buttons import bcp_actual_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(bcp_actual_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_bcp_actual')


def download_json_bcp_actual(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('bcp_actual')


def reset_function_bcp_actual(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("bcp_actual")


def bcp_actual_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_actual(0)


def bcp_actual_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_actual(1)


def bcp_actual_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_actual(2)


def bcp_actual_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_actual(3)


def bcp_actual_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_actual(4)


def bcp_actual_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_actual(5)


def bcp_actual_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_actual(6)


def bcp_actual_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_actual(7)


def bcp_actual_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_bcp_actual(8)


def check_all_bcp_actual(e):
    from buttons import bcp_actual_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 10):
        function_name = f'bcp_actual_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 10 and k < 9:
        bcp_actual_buttons[f'button_{i}'].text = json_checker.json_data_bcp_actual['global'][k]['_id']
        i += 1
        k += 1
    page.update()


bcp_actual_functions = {
    "open_json": open_json_function_bcp_actual,
    "download_json": download_json_bcp_actual,
    "reset": reset_function_bcp_actual,
    "function_1": bcp_actual_1,
    "function_2": bcp_actual_2,
    "function_3": bcp_actual_3,
    "function_4": bcp_actual_4,
    "function_5": bcp_actual_5,
    "function_6": bcp_actual_6,
    "function_7": bcp_actual_7,
    "function_8": bcp_actual_8,
    "function_9": bcp_actual_9,
    "check_all": check_all_bcp_actual
}


# Функции CGP json 6

def open_json_function_cgp_6(e: ft.FilePickerResultEvent):
    from buttons import cgp_6_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(cgp_6_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_cgp_6')


def download_json_cgp_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('cgp_6')


def reset_function_cgp_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("cgp_6")


def cgp_6_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_6(0)


def cgp_6_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_6(1)


def cgp_6_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_6(2)


def cgp_6_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_6(3)


def cgp_6_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_6(4)


def cgp_6_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_6(5)


def check_all_cgp_6(e):
    from buttons import cgp_6_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 7):
        function_name = f'cgp_6_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 7 and k < 6:
        cgp_6_buttons[f'button_{i}'].text = json_checker.json_data_cgp_6['global'][k]['_id']
        i += 1
        k += 1
    page.update()


cgp_6_functions = {
    "open_json": open_json_function_cgp_6,
    "download_json": download_json_cgp_6,
    "reset": reset_function_cgp_6,
    "function_1": cgp_6_1,
    "function_2": cgp_6_2,
    "function_3": cgp_6_3,
    "function_4": cgp_6_4,
    "function_5": cgp_6_5,
    "function_6": cgp_6_6,
    "check_all": check_all_cgp_6
}


# Функции CGP json 9

def open_json_function_cgp_9(e: ft.FilePickerResultEvent):
    from buttons import cgp_9_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(cgp_9_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_cgp_9')


def download_json_cgp_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('cgp_9')


def reset_function_cgp_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("cgp_9")


def cgp_9_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_9(0)


def cgp_9_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_9(1)


def cgp_9_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_9(2)


def cgp_9_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_9(3)


def cgp_9_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_9(4)


def cgp_9_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_9(5)


def cgp_9_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_9(6)


def cgp_9_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_9(7)


def cgp_9_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_cgp_9(8)


def check_all_cgp_9(e):
    from buttons import cgp_9_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 10):
        function_name = f'cgp_9_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 10 and k < 9:
        cgp_9_buttons[f'button_{i}'].text = json_checker.json_data_cgp_9['global'][k]['_id']
        i += 1
        k += 1
    page.update()


cgp_9_functions = {
    "open_json": open_json_function_cgp_9,
    "download_json": download_json_cgp_9,
    "reset": reset_function_cgp_9,
    "button_1": cgp_9_1,
    "button_2": cgp_9_2,
    "button_3": cgp_9_3,
    "button_4": cgp_9_4,
    "button_5": cgp_9_5,
    "button_6": cgp_9_6,
    "button_7": cgp_9_7,
    "button_8": cgp_9_8,
    "button_9": cgp_9_9,
    "check_all": check_all_cgp_9
}


# Функции OTHER BANS WO TEXTFIELD

def open_json_function_other_wo_field(e: ft.FilePickerResultEvent):
    from buttons import other_bans_wo_field_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(other_bans_wo_field_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_other_wo_field')


def download_json_other_wo_field(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('other_wo_field')


def reset_function_other_wo_field(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("other_wo_field")


def check_bans_other_wo_field_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(0)


def check_bans_other_wo_field_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(1)


def check_bans_other_wo_field_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(2)


def check_bans_other_wo_field_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(3)


def check_bans_other_wo_field_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(4)


def check_bans_other_wo_field_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(5)


def check_bans_other_wo_field_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(6)


def check_bans_other_wo_field_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(7)


def check_bans_other_wo_field_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(8)


def check_bans_other_wo_field_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(9)


def check_bans_other_wo_field_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_wo_field(10)


def check_all_bans_other_wo_field(e):
    from buttons import other_bans_wo_field_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 12):
        try:
            function_name = f'check_bans_other_wo_field_{i}'
            func = globals().get(function_name)
            func(e)
        except IndexError:
            break
    time.sleep(3)
    i = 1
    k = 0
    while i < 12 and k < 11:
        try:
            other_bans_wo_field_buttons[f'button_{i}'].text = json_checker.json_data_other_wo_field['global'][k]['_id']
            i += 1
            k += 1
        except IndexError:
            break
    page.update()


check_all_bans_other_wo_field_functions = {
    "open_json": open_json_function_other_wo_field,
    "download_json": download_json_other_wo_field,
    "reset": reset_function_other_wo_field,
    "function_1": check_bans_other_wo_field_1,
    "function_2": check_bans_other_wo_field_2,
    "function_3": check_bans_other_wo_field_3,
    "function_4": check_bans_other_wo_field_4,
    "function_5": check_bans_other_wo_field_5,
    "function_6": check_bans_other_wo_field_6,
    "function_7": check_bans_other_wo_field_7,
    "function_8": check_bans_other_wo_field_8,
    "function_9": check_bans_other_wo_field_9,
    "function_10": check_bans_other_wo_field_10,
    "function_11": check_bans_other_wo_field_11,
    "check_all": check_all_bans_other_wo_field
}


# Функции OTHER BANS WITH TEXTFIELD

def open_json_function_with_field(e: ft.FilePickerResultEvent):
    from buttons import other_bans_with_field_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(other_bans_with_field_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_with_field')


def download_json_with_field(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('other_with_field')


def reset_function_with_field(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("other_with_field")


def check_bans_with_field_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(0)


def check_bans_with_field_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(1)


def check_bans_with_field_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(2)


def check_bans_with_field_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(3)


def check_bans_with_field_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(4)


def check_bans_with_field_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(5)


def check_bans_with_field_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(6)


def check_bans_with_field_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(7)


def check_bans_with_field_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(8)


def check_bans_with_field_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(9)


def check_bans_with_field_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_other_with_field(10)


def check_all_bans_with_field(e):
    from buttons import other_bans_with_field_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 12):
        try:
            function_name = f'check_bans_with_field_{i}'
            func = globals().get(function_name)
            func(e)
        except (KeyError, IndexError):
            break
    time.sleep(3)
    i = 1
    k = 0
    while i < 12 and k < 11:
        try:
            other_bans_with_field_buttons[f'button_{i}'].text = json_checker.json_data_with_field['global'][k]['_id']
            i += 1
            k += 1
        except (IndexError, KeyError):
            break
    page.update()


check_all_bans_other_with_field_functions = {
    "open_json": open_json_function_with_field,
    "download_json": download_json_with_field,
    "reset": reset_function_with_field,
    "function_1": check_bans_with_field_1,
    "function_2": check_bans_with_field_2,
    "function_3": check_bans_with_field_3,
    "function_4": check_bans_with_field_4,
    "function_5": check_bans_with_field_5,
    "function_6": check_bans_with_field_6,
    "function_7": check_bans_with_field_7,
    "function_8": check_bans_with_field_8,
    "function_9": check_bans_with_field_9,
    "function_10": check_bans_with_field_10,
    "function_11": check_bans_with_field_11,
    "check_all": check_all_bans_with_field
}


# ФУНКЦИИ OTO2

def open_json_function_oto_2(e: ft.FilePickerResultEvent):
    from buttons import oto_2_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(oto_2_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_oto_2')


def download_json_oto_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('oto_2')


def reset_function_oto_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("oto_2")


def check_oto_2_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(0)


def check_oto_2_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(1)


def check_oto_2_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(2)


def check_oto_2_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(3)


def check_oto_2_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(4)


def check_oto_2_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(5)


def check_oto_2_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(6)


def check_oto_2_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(7)


def check_oto_2_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(8)


def check_oto_2_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(9)


def check_oto_2_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.check_oto_2(10)


def check_all_oto_2(e):
    from buttons import oto_2_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 12):
        try:
            function_name = f'check_oto_2_{i}'
            func = globals().get(function_name)
            func(e)
        except (KeyError, IndexError):
            break
    time.sleep(3)
    i = 1
    k = 0
    while i < 12 and k < 11:
        try:
            oto_2_buttons[f'button_{i}'].text = json_checker.json_data_oto_2['global'][k]['_id']
            i += 1
            k += 1
        except (IndexError, KeyError):
            break
    page.update()


check_oto_2_functions = {
    "open_json": open_json_function_oto_2,
    "download_json": download_json_oto_2,
    "reset": reset_function_oto_2,
    "function_1": check_oto_2_1,
    "function_2": check_oto_2_2,
    "function_3": check_oto_2_3,
    "function_4": check_oto_2_4,
    "function_5": check_oto_2_5,
    "function_6": check_oto_2_6,
    "function_7": check_oto_2_7,
    "function_8": check_oto_2_8,
    "function_9": check_oto_2_9,
    "function_10": check_oto_2_10,
    "function_11": check_oto_2_11,
    "check_all": check_all_oto_2
}


# ФУНКЦИИ COMPARE JSON

def open_json_function_compare(e: ft.FilePickerResultEvent):
    from buttons import json_compare_buttons_1, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(json_compare_buttons_1["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json_compare(e)


def download_json_compare(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('compare')


def reset_function_compare(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("compare")


def check_compare_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(0)


def check_compare_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(1)


def check_compare_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(2)


def check_compare_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(3)


def check_compare_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(4)


def check_compare_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(5)


def check_compare_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(6)


def check_compare_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(7)


def check_compare_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(8)


def check_compare_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(9)


def check_compare_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(10)


def check_compare_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(11)


def check_compare_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(12)


def check_compare_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(13)


def check_compare_15(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(14)


def check_compare_16(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(15)


def check_compare_17(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(16)


def check_compare_18(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(17)


def check_compare_19(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(18)


def check_compare_20(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(19)


def check_compare_21(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(20)


def check_compare_22(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.compare(21)


def check_all_compare(e):
    from buttons import json_compare_buttons_1, json_compare_buttons_2, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 23):
        try:
            function_name = f'check_compare_{i}'
            func = globals().get(function_name)
            func(e)
        except (KeyError, IndexError):
            break
    time.sleep(3)
    i = 1
    k = 0
    while i < 23 and k < 22:
        try:
            json_compare_buttons_1[f'button_{i}'].text = json_checker.json_data_compare_1['global'][k]['_id']
            json_compare_buttons_2[f'button_{i}'].text = json_checker.json_data_compare_2['global'][k]['_id']
            i += 1
            k += 1
        except (IndexError, KeyError):
            break
    page.update()


compare_functions = {
    "open_json": open_json_function_compare,
    "download_json": download_json_compare,
    "reset": reset_function_compare,
    "function_1": check_compare_1,
    "function_2": check_compare_2,
    "function_3": check_compare_3,
    "function_4": check_compare_4,
    "function_5": check_compare_5,
    "function_6": check_compare_6,
    "function_7": check_compare_7,
    "function_8": check_compare_8,
    "function_9": check_compare_9,
    "function_10": check_compare_10,
    "function_11": check_compare_11,
    "check_all": check_all_compare
}


# ФУНКЦИИ AMONG NEW TS BALANCE

def open_json_function_among_new_ts(e: ft.FilePickerResultEvent):
    from buttons import among_balance_new_tc_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(among_balance_new_tc_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_among_new_ts')


def download_json_among_new_ts(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('among_new_ts')


def reset_function_among_new_ts(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("among_new_ts")


def check_among_new_ts_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.among_new_ts(0)


def check_among_new_ts_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.among_new_ts(1)


def check_among_new_ts_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.among_new_ts(2)


def check_all_among_new_ts(e):
    from buttons import among_balance_new_tc_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 4):
        try:
            function_name = f'check_among_new_ts_{i}'
            func = globals().get(function_name)
            func(e)
        except (KeyError, IndexError):
            break
    time.sleep(3)
    i = 1
    k = 0
    while i < 4 and k < 3:
        try:
            among_balance_new_tc_buttons[f'button_{i}'].text = json_checker.json_data_among_new_ts['global'][k]['_id']
            i += 1
            k += 1
        except (IndexError, KeyError):
            break
    page.update()


among_new_ts_functions = {
    "open_json": open_json_function_among_new_ts,
    "download_json": download_json_among_new_ts,
    "reset": reset_function_among_new_ts,
    "function_1": check_among_new_ts_1,
    "function_2": check_among_new_ts_2,
    "function_3": check_among_new_ts_3,
    "check_all": check_all_among_new_ts
}


# ФУНКЦИИ AMONG AVERAGE 10

def open_json_function_among_average(e: ft.FilePickerResultEvent):
    from buttons import among_balance_average_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(among_balance_average_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_among_average')


def download_json_among_average(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('among_average')


def reset_function_among_average(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("among_average")


def check_among_average_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.among_average(0)


def check_among_average_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.among_average(1)


def check_among_average_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.among_average(2)


def check_all_among_average(e):
    from buttons import among_balance_average_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 4):
        try:
            function_name = f'check_among_average_{i}'
            func = globals().get(function_name)
            func(e)
        except (KeyError, IndexError):
            break
    time.sleep(3)
    i = 1
    k = 0
    while i < 4 and k < 3:
        try:
            among_balance_average_buttons[f'button_{i}'].text = json_checker.json_data_among_average['global'][k]['_id']
            i += 1
            k += 1
        except (IndexError, KeyError):
            break
    page.update()


among_average_functions = {
    "open_json": open_json_function_among_average,
    "download_json": download_json_among_average,
    "reset": reset_function_among_average,
    "function_1": check_among_average_1,
    "function_2": check_among_average_2,
    "function_3": check_among_average_3,
    "check_all": check_all_among_average
}


# ФУНКЦИИ LABYRINTH WW

def open_json_function_labyrinth_balance_ww(e: ft.FilePickerResultEvent):
    from buttons import labyrinth_balance_ww_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(labyrinth_balance_ww_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_labyrinth_balance_ww')


def download_json_labyrinth_balance_ww(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('labyrinth_balance_ww')


def reset_function_labyrinth_balance_ww(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("labyrinth_balance_ww")


def check_labyrinth_balance_ww_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.labyrinth_balance('ww', 0)


def check_labyrinth_balance_ww_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.labyrinth_balance('ww', 1)


def check_labyrinth_balance_ww_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.labyrinth_balance('ww', 2)


def check_labyrinth_balance_ww_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.labyrinth_balance('ww', 3)


def check_all_labyrinth_balance_ww(e):
    from buttons import labyrinth_balance_ww_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 5):
        try:
            function_name = f'check_labyrinth_balance_ww_{i}'
            func = globals().get(function_name)
            func(e)
        except (KeyError, IndexError):
            break
    time.sleep(3)
    i = 1
    k = 0
    while i < 5 and k < 4:
        try:
            labyrinth_balance_ww_buttons[f'button_{i}'].text = json_checker.json_data_labyrinth_balance_ww['global'][k]['_id']
            i += 1
            k += 1
        except (IndexError, KeyError):
            break
    page.update()


labyrinth_balance_ww_functions = {
    "open_json": open_json_function_labyrinth_balance_ww,
    "download_json": download_json_labyrinth_balance_ww,
    "reset": reset_function_labyrinth_balance_ww,
    "function_1": check_labyrinth_balance_ww_1,
    "function_2": check_labyrinth_balance_ww_2,
    "function_3": check_labyrinth_balance_ww_3,
    "function_4": check_labyrinth_balance_ww_4,
    "check_all": check_all_labyrinth_balance_ww
}


# ФУНКЦИИ LABYRINTH CN

def open_json_function_labyrinth_balance_cn(e: ft.FilePickerResultEvent):
    from buttons import labyrinth_balance_cn_buttons, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(labyrinth_balance_cn_buttons["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_labyrinth_balance_cn')


def download_json_labyrinth_balance_cn(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('labyrinth_balance_cn')


def reset_function_labyrinth_balance_cn(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("labyrinth_balance_cn")


def check_labyrinth_balance_cn_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.labyrinth_balance('cn', 0)


def check_labyrinth_balance_cn_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.labyrinth_balance('cn', 1)


def check_labyrinth_balance_cn_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.labyrinth_balance('cn', 2)


def check_labyrinth_balance_cn_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.labyrinth_balance('cn', 3)


def check_all_labyrinth_balance_cn(e):
    from buttons import labyrinth_balance_cn_buttons, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 5):
        try:
            function_name = f'check_labyrinth_balance_cn_{i}'
            func = globals().get(function_name)
            func(e)
        except (KeyError, IndexError):
            break
    time.sleep(3)
    i = 1
    k = 0
    while i < 5 and k < 4:
        try:
            labyrinth_balance_cn_buttons[f'button_{i}'].text = json_checker.json_data_labyrinth_balance_cn['global'][k]['_id']
            i += 1
            k += 1
        except (IndexError, KeyError):
            break
    page.update()


labyrinth_balance_cn_functions = {
    "open_json": open_json_function_labyrinth_balance_cn,
    "download_json": download_json_labyrinth_balance_cn,
    "reset": reset_function_labyrinth_balance_cn,
    "function_1": check_labyrinth_balance_cn_1,
    "function_2": check_labyrinth_balance_cn_2,
    "function_3": check_labyrinth_balance_cn_3,
    "function_4": check_labyrinth_balance_cn_4,
    "check_all": check_all_labyrinth_balance_cn
}


# ФУНКЦИИ TICKETS BALANCE CHECKER 11

def open_json_function_tickets_balance_11(e: ft.FilePickerResultEvent):
    from buttons import tickets_balance_checker_buttons_11, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_balance_checker_buttons_11["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_tickets_balance_11')


def download_json_tickets_balance_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('tickets_balance_11')


def reset_function_tickets_balance_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("tickets_balance_11")


def check_tickets_balance_11_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 0)


def check_tickets_balance_11_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 1)


def check_tickets_balance_11_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 2)


def check_tickets_balance_11_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 3)


def check_tickets_balance_11_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 4)


def check_tickets_balance_11_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 5)


def check_tickets_balance_11_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 6)


def check_tickets_balance_11_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 7)


def check_tickets_balance_11_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 8)


def check_tickets_balance_11_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 9)


def check_tickets_balance_11_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 10)


def check_tickets_balance_11_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 11)


def check_tickets_balance_11_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 12)


def check_tickets_balance_11_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 13)


def check_tickets_balance_11_15(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 14)


def check_tickets_balance_11_16(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 15)


def check_tickets_balance_11_17(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 16)


def check_tickets_balance_11_18(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 17)


def check_tickets_balance_11_19(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 18)


def check_tickets_balance_11_20(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 19)


def check_tickets_balance_11_21(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 20)


def check_tickets_balance_11_22(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(22, 21)


def check_all_tickets_balance_11(e):
    from buttons import tickets_balance_checker_buttons_11, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 23):
        function_name = f'check_tickets_balance_11_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 23 and k < 22:
        tickets_balance_checker_buttons_11[f'button_{i}'].text = json_checker.json_data_tickets_balance_11['global'][k]['_id']
        tickets_balance_checker_buttons_11[f'bundle_{i}'].text = json_checker.json_data_tickets_balance_11['global'][k]['event']['product_id']
        i += 1
        k += 1
    page.update()


tickets_balance_functions_11 = {
    "open_json": open_json_function_tickets_balance_11,
    "download_json": download_json_tickets_balance_11,
    "reset": reset_function_tickets_balance_11,
    "function_1": check_tickets_balance_11_1,
    "function_2": check_tickets_balance_11_2,
    "function_3": check_tickets_balance_11_3,
    "function_4": check_tickets_balance_11_4,
    "function_5": check_tickets_balance_11_5,
    "function_6": check_tickets_balance_11_6,
    "function_7": check_tickets_balance_11_7,
    "function_8": check_tickets_balance_11_8,
    "function_9": check_tickets_balance_11_9,
    "function_10": check_tickets_balance_11_10,
    "function_11": check_tickets_balance_11_11,
    "function_12": check_tickets_balance_11_12,
    "function_13": check_tickets_balance_11_13,
    "function_14": check_tickets_balance_11_14,
    "function_15": check_tickets_balance_11_15,
    "function_16": check_tickets_balance_11_16,
    "function_17": check_tickets_balance_11_17,
    "function_18": check_tickets_balance_11_18,
    "function_19": check_tickets_balance_11_19,
    "function_20": check_tickets_balance_11_20,
    "function_21": check_tickets_balance_11_21,
    "function_22": check_tickets_balance_11_22,
    "check_all": check_all_tickets_balance_11
}


# ФУНКЦИИ TICKETS BALANCE CHECKER 10 19+ LVL

def open_json_function_tickets_balance_10(e: ft.FilePickerResultEvent):
    from buttons import tickets_balance_checker_buttons_10, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_balance_checker_buttons_10["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_tickets_balance_10')


def download_json_tickets_balance_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('tickets_balance_10')


def reset_function_tickets_balance_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("tickets_balance_10")


def check_tickets_balance_10_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 0)


def check_tickets_balance_10_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 1)


def check_tickets_balance_10_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 2)


def check_tickets_balance_10_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 3)


def check_tickets_balance_10_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 4)


def check_tickets_balance_10_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 5)


def check_tickets_balance_10_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 6)


def check_tickets_balance_10_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 7)


def check_tickets_balance_10_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 8)


def check_tickets_balance_10_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 9)


def check_tickets_balance_10_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 10)


def check_tickets_balance_10_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 11)


def check_tickets_balance_10_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 12)


def check_tickets_balance_10_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 13)


def check_tickets_balance_10_15(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 14)


def check_tickets_balance_10_16(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 15)


def check_tickets_balance_10_17(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 16)


def check_tickets_balance_10_18(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 17)


def check_tickets_balance_10_19(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 18)


def check_tickets_balance_10_20(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(20, 19)


def check_all_tickets_balance_10(e):
    from buttons import tickets_balance_checker_buttons_10, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 21):
        function_name = f'check_tickets_balance_10_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 21 and k < 20:
        tickets_balance_checker_buttons_10[f'button_{i}'].text = json_checker.json_data_tickets_balance_10['global'][k]['_id']
        tickets_balance_checker_buttons_10[f'bundle_{i}'].text = json_checker.json_data_tickets_balance_10['global'][k]['event']['product_id']
        i += 1
        k += 1
    page.update()


tickets_balance_functions_10 = {
    "open_json": open_json_function_tickets_balance_10,
    "download_json": download_json_tickets_balance_10,
    "reset": reset_function_tickets_balance_10,
    "function_1": check_tickets_balance_10_1,
    "function_2": check_tickets_balance_10_2,
    "function_3": check_tickets_balance_10_3,
    "function_4": check_tickets_balance_10_4,
    "function_5": check_tickets_balance_10_5,
    "function_6": check_tickets_balance_10_6,
    "function_7": check_tickets_balance_10_7,
    "function_8": check_tickets_balance_10_8,
    "function_9": check_tickets_balance_10_9,
    "function_10": check_tickets_balance_10_10,
    "function_11": check_tickets_balance_10_11,
    "function_12": check_tickets_balance_10_12,
    "function_13": check_tickets_balance_10_13,
    "function_14": check_tickets_balance_10_14,
    "function_15": check_tickets_balance_10_15,
    "function_16": check_tickets_balance_10_16,
    "function_17": check_tickets_balance_10_17,
    "function_18": check_tickets_balance_10_18,
    "function_19": check_tickets_balance_10_19,
    "function_20": check_tickets_balance_10_20,
    "check_all": check_all_tickets_balance_10
}


# ФУНКЦИИ TICKETS BALANCE CHECKER 10 7-18 LVL

def open_json_function_tickets_balance_10_extra(e: ft.FilePickerResultEvent):
    from buttons import tickets_balance_checker_buttons_10_extra, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_balance_checker_buttons_10_extra["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_tickets_balance_10_extra')


def download_json_tickets_balance_10_extra(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('tickets_balance_10_extra')


def reset_function_tickets_balance_10_extra(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("tickets_balance_10_extra")


def check_tickets_balance_10_extra_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 0)


def check_tickets_balance_10_extra_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 1)


def check_tickets_balance_10_extra_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 2)


def check_tickets_balance_10_extra_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 3)


def check_tickets_balance_10_extra_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 4)


def check_tickets_balance_10_extra_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 5)


def check_tickets_balance_10_extra_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 6)


def check_tickets_balance_10_extra_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 7)


def check_tickets_balance_10_extra_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 8)


def check_tickets_balance_10_extra_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 9)


def check_tickets_balance_10_extra_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 10)


def check_tickets_balance_10_extra_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 11)


def check_tickets_balance_10_extra_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 12)


def check_tickets_balance_10_extra_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 13)


def check_tickets_balance_10_extra_15(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 14)


def check_tickets_balance_10_extra_16(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 15)


def check_tickets_balance_10_extra_17(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 16)


def check_tickets_balance_10_extra_18(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 17)


def check_tickets_balance_10_extra_19(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 18)


def check_tickets_balance_10_extra_20(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker("20_extra", 19)


def check_all_tickets_balance_10_extra(e):
    from buttons import tickets_balance_checker_buttons_10_extra, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 21):
        function_name = f'check_tickets_balance_10_extra_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 21 and k < 20:
        tickets_balance_checker_buttons_10_extra[f'button_{i}'].text = json_checker.json_data_tickets_balance_10_extra['global'][k]['_id']
        i += 1
        k += 1
    page.update()


tickets_balance_functions_10_extra = {
    "open_json": open_json_function_tickets_balance_10_extra,
    "download_json": download_json_tickets_balance_10_extra,
    "reset": reset_function_tickets_balance_10_extra,
    "function_1": check_tickets_balance_10_extra_1,
    "function_2": check_tickets_balance_10_extra_2,
    "function_3": check_tickets_balance_10_extra_3,
    "function_4": check_tickets_balance_10_extra_4,
    "function_5": check_tickets_balance_10_extra_5,
    "function_6": check_tickets_balance_10_extra_6,
    "function_7": check_tickets_balance_10_extra_7,
    "function_8": check_tickets_balance_10_extra_8,
    "function_9": check_tickets_balance_10_extra_9,
    "function_10": check_tickets_balance_10_extra_10,
    "function_11": check_tickets_balance_10_extra_11,
    "function_12": check_tickets_balance_10_extra_12,
    "function_13": check_tickets_balance_10_extra_13,
    "function_14": check_tickets_balance_10_extra_14,
    "function_15": check_tickets_balance_10_extra_15,
    "function_16": check_tickets_balance_10_extra_16,
    "function_17": check_tickets_balance_10_extra_17,
    "function_18": check_tickets_balance_10_extra_18,
    "function_19": check_tickets_balance_10_extra_19,
    "function_20": check_tickets_balance_10_extra_20,
    "check_all": check_all_tickets_balance_10_extra
}


# ФУНКЦИИ TICKETS BALANCE CHECKER 9

def open_json_function_tickets_balance_9(e: ft.FilePickerResultEvent):
    from buttons import tickets_balance_checker_buttons_9, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_balance_checker_buttons_9["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_tickets_balance_9')


def download_json_tickets_balance_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('tickets_balance_9')


def reset_function_tickets_balance_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("tickets_balance_9")


def check_tickets_balance_9_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 0)


def check_tickets_balance_9_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 1)


def check_tickets_balance_9_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 2)


def check_tickets_balance_9_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 3)


def check_tickets_balance_9_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 4)


def check_tickets_balance_9_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 5)


def check_tickets_balance_9_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 6)


def check_tickets_balance_9_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 7)


def check_tickets_balance_9_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 8)


def check_tickets_balance_9_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 9)


def check_tickets_balance_9_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 10)


def check_tickets_balance_9_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 11)


def check_tickets_balance_9_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 12)


def check_tickets_balance_9_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 13)


def check_tickets_balance_9_15(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 14)


def check_tickets_balance_9_16(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 15)


def check_tickets_balance_9_17(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 16)


def check_tickets_balance_9_18(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(18, 17)


def check_all_tickets_balance_9(e):
    from buttons import tickets_balance_checker_buttons_9, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 19):
        function_name = f'check_tickets_balance_9_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 19 and k < 18:
        tickets_balance_checker_buttons_9[f'button_{i}'].text = json_checker.json_data_tickets_balance_9['global'][k]['_id']
        tickets_balance_checker_buttons_9[f'bundle_{i}'].text = json_checker.json_data_tickets_balance_9['global'][k]['event']['product_id']
        i += 1
        k += 1
    page.update()


tickets_balance_functions_9 = {
    "open_json": open_json_function_tickets_balance_9,
    "download_json": download_json_tickets_balance_9,
    "reset": reset_function_tickets_balance_9,
    "function_1": check_tickets_balance_9_1,
    "function_2": check_tickets_balance_9_2,
    "function_3": check_tickets_balance_9_3,
    "function_4": check_tickets_balance_9_4,
    "function_5": check_tickets_balance_9_5,
    "function_6": check_tickets_balance_9_6,
    "function_7": check_tickets_balance_9_7,
    "function_8": check_tickets_balance_9_8,
    "function_9": check_tickets_balance_9_9,
    "function_10": check_tickets_balance_9_10,
    "function_11": check_tickets_balance_9_11,
    "function_12": check_tickets_balance_9_12,
    "function_13": check_tickets_balance_9_13,
    "function_14": check_tickets_balance_9_14,
    "function_15": check_tickets_balance_9_15,
    "function_16": check_tickets_balance_9_16,
    "function_17": check_tickets_balance_9_17,
    "function_18": check_tickets_balance_9_18,
    "check_all": check_all_tickets_balance_9
}


# ФУНКЦИИ TICKETS BALANCE CHECKER 7

def open_json_function_tickets_balance_7(e: ft.FilePickerResultEvent):
    from buttons import tickets_balance_checker_buttons_7, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_balance_checker_buttons_7["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_tickets_balance_7')


def download_json_tickets_balance_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('tickets_balance_7')


def reset_function_tickets_balance_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("tickets_balance_7")


def check_tickets_balance_7_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 0)


def check_tickets_balance_7_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 1)


def check_tickets_balance_7_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 2)


def check_tickets_balance_7_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 3)


def check_tickets_balance_7_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 4)


def check_tickets_balance_7_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 5)


def check_tickets_balance_7_7(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 6)


def check_tickets_balance_7_8(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 7)


def check_tickets_balance_7_9(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 8)


def check_tickets_balance_7_10(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 9)


def check_tickets_balance_7_11(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 10)


def check_tickets_balance_7_12(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 11)


def check_tickets_balance_7_13(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 12)


def check_tickets_balance_7_14(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(14, 13)


def check_all_tickets_balance_7(e):
    from buttons import tickets_balance_checker_buttons_7, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 15):
        function_name = f'check_tickets_balance_7_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 15 and k < 14:
        tickets_balance_checker_buttons_7[f'button_{i}'].text = json_checker.json_data_tickets_balance_7['global'][k]['_id']
        i += 1
        k += 1
    page.update()


tickets_balance_functions_7 = {
    "open_json": open_json_function_tickets_balance_7,
    "download_json": download_json_tickets_balance_7,
    "reset": reset_function_tickets_balance_7,
    "function_1": check_tickets_balance_7_1,
    "function_2": check_tickets_balance_7_2,
    "function_3": check_tickets_balance_7_3,
    "function_4": check_tickets_balance_7_4,
    "function_5": check_tickets_balance_7_5,
    "function_6": check_tickets_balance_7_6,
    "function_7": check_tickets_balance_7_7,
    "function_8": check_tickets_balance_7_8,
    "function_9": check_tickets_balance_7_9,
    "function_10": check_tickets_balance_7_10,
    "function_11": check_tickets_balance_7_11,
    "function_12": check_tickets_balance_7_12,
    "function_13": check_tickets_balance_7_13,
    "function_14": check_tickets_balance_7_14,
    "check_all": check_all_tickets_balance_7
}


# ФУНКЦИИ TICKETS BALANCE CHECKER 3

def open_json_function_tickets_balance_3(e: ft.FilePickerResultEvent):
    from buttons import tickets_balance_checker_buttons_3, PageManager
    page = PageManager.get_page()
    json_checker = JsonOpener(tickets_balance_checker_buttons_3["selected_files"])
    page.json_checker = json_checker
    json_checker.open_json(e, 'json_data_tickets_balance_3')


def download_json_tickets_balance_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.download_json_other('tickets_balance_3')


def reset_function_tickets_balance_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.reset_other("tickets_balance_3")


def check_tickets_balance_3_1(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(6, 0)


def check_tickets_balance_3_2(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(6, 1)


def check_tickets_balance_3_3(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(6, 2)


def check_tickets_balance_3_4(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(6, 3)


def check_tickets_balance_3_5(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(6, 4)


def check_tickets_balance_3_6(e):
    from buttons import PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    json_checker.tickets_balance_checker(6, 5)


def check_all_tickets_balance_3(e):
    from buttons import tickets_balance_checker_buttons_3, PageManager
    page = PageManager.get_page()
    json_checker = getattr(page, 'json_checker', None)
    for i in range(1, 7):
        function_name = f'check_tickets_balance_3_{i}'
        func = globals().get(function_name)
        func(e)
    time.sleep(3)
    i = 1
    k = 0
    while i < 7 and k < 6:
        tickets_balance_checker_buttons_3[f'button_{i}'].text = json_checker.json_data_tickets_balance_3['global'][k]['_id']
        tickets_balance_checker_buttons_3[f'bundle_{i}'].text = json_checker.json_data_tickets_balance_3['global'][k]['event']['product_id']
        i += 1
        k += 1
    page.update()


tickets_balance_functions_3 = {
    "open_json": open_json_function_tickets_balance_3,
    "download_json": download_json_tickets_balance_3,
    "reset": reset_function_tickets_balance_3,
    "function_1": check_tickets_balance_3_1,
    "function_2": check_tickets_balance_3_2,
    "function_3": check_tickets_balance_3_3,
    "function_4": check_tickets_balance_3_4,
    "function_5": check_tickets_balance_3_5,
    "function_6": check_tickets_balance_3_6,
    "check_all": check_all_tickets_balance_3
}
