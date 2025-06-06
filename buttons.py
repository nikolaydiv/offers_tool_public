import flet as ft
from flet import *
from tags_functions import (get_profile_button_clicked, update_tags_11_functions,
                                           update_tags_10_functions, update_tags_9_functions, update_tags_3_functions,
                                           no_hint_functions, collection_gacha_tags_functions, weapon_lto_functions,
                                           shiny_functions, theo_functions, lto_oto_gc_functions, among_functions,
                                           labyrinth_functions, bogo_functions, new_shiny_functions,
                                           new_among_functions, my_tags_functions, comeback_functions, manual_tags,
                                           update_tags_7_functions, update_tags_10_functions_raskat)
from json_functions import (bans_11_functions, bans_10_functions, bans_9_functions, bans_3_functions,
                                           tickets_criteria_functions, no_hint_bans_functions,
                                           no_hint_balance_functions, bcp_previous_functions, bcp_actual_functions,
                                           cgp_6_functions, cgp_9_functions, check_all_bans_other_wo_field_functions,
                                           check_all_bans_other_with_field_functions, check_oto_2_functions,
                                           compare_functions, among_new_ts_functions, among_average_functions,
                                           labyrinth_balance_ww_functions, labyrinth_balance_cn_functions,
                                           tickets_balance_functions_11, tickets_balance_functions_10,
                                           tickets_balance_functions_9, tickets_balance_functions_3,
                                           tickets_balance_functions_10_extra, bans_7_functions,
                                           tickets_balance_functions_7)


class PageManager:
    _page = None

    @classmethod
    def set_page(cls, page):
        cls._page = page

    @classmethod
    def get_page(cls):
        return cls._page


# Конструкторы кнопок

class GetProfileLine(ft.TextField):
    def __init__(self, label, hint_text, icon):
        super().__init__()
        self.label = label
        self.hint_text = hint_text
        self.icon = icon


class SendRequestButton(ft.CupertinoButton):
    def __init__(self, content, bgcolor, on_click, alignment=ft.alignment.top_left,
                 border_radius=ft.border_radius.all(15),
                 opacity_on_click=0.5):
        super().__init__()
        self.content = content
        self.bgcolor = bgcolor
        self.on_click = on_click


class SubmitButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.text = text
        self.on_click = on_click


class BanButton(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.text = "offer id"
        self.icon = ft.icons.LOCAL_OFFER
        self.disabled = True


class BundleButton(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.text = 'bundle id'
        self.icon = ft.icons.LOCAL_OFFER
        self.disabled = True


class ManualTags(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.icon = ft.icons.LOCAL_OFFER
        self.width = 200


class InputBansField(ft.TextField):
    def __init__(self):
        super().__init__()
        self.width = 600
        self.label = "banOffers"
        self.hint_text = "Введи баны через запятую"


get_profile_buttons = {
    "get_profile_line": GetProfileLine("Support id", "Put your supid here", icons.SEARCH),
    "submit_button": SubmitButton("SEND", get_profile_button_clicked)
}

update_tags_11_buttons = {
    "update_tags_11_1": SendRequestButton(ft.Text("Update tags 1", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_11_functions["function_1"]),
    "update_tags_11_2": SendRequestButton(ft.Text("Update tags 2", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_11_functions["function_2"]),
    "update_tags_11_3": SendRequestButton(ft.Text("Update tags 3", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_11_functions["function_3"]),
    "update_tags_11_4": SendRequestButton(ft.Text("Update tags 4", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_11_functions["function_4"]),
    "update_tags_11_5": SendRequestButton(ft.Text("Update tags 5", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_11_functions["function_5"]),
    "update_tags_11_6": SendRequestButton(ft.Text("Update tags 6", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_11_functions["function_6"]),
    "update_tags_11_7": SendRequestButton(ft.Text("Update tags 7", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_11_functions["function_7"]),
    "update_tags_11_8": SendRequestButton(ft.Text("Update tags 8", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_11_functions["function_8"]),
    "update_tags_11_9": SendRequestButton(ft.Text("Update tags 9", color=ft.colors.WHITE), ft.colors.RED,
                                          update_tags_11_functions["function_9"]),
    "update_tags_11_10": SendRequestButton(ft.Text("Update tags 10", color=ft.colors.WHITE), ft.colors.RED,
                                           update_tags_11_functions["function_10"]),
    "update_tags_11_11": SendRequestButton(ft.Text("Update tags 11", color=ft.colors.WHITE), ft.colors.RED,
                                           update_tags_11_functions["function_11"])}

update_tags_10_buttons = {
    "update_tags_10_1": SendRequestButton(ft.Text("Update tags 1", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_10_functions["function_1"]),
    "update_tags_10_2": SendRequestButton(ft.Text("Update tags 2", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_10_functions["function_2"]),
    "update_tags_10_3": SendRequestButton(ft.Text("Update tags 3", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_10_functions["function_3"]),
    "update_tags_10_4": SendRequestButton(ft.Text("Update tags 4", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_10_functions["function_4"]),
    "update_tags_10_5": SendRequestButton(ft.Text("Update tags 5", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_10_functions["function_5"]),
    "update_tags_10_6": SendRequestButton(ft.Text("Update tags 6", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_10_functions["function_6"]),
    "update_tags_10_7": SendRequestButton(ft.Text("Update tags 7", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_10_functions["function_7"]),
    "update_tags_10_8": SendRequestButton(ft.Text("Update tags 8", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_10_functions["function_8"]),
    "update_tags_10_9": SendRequestButton(ft.Text("Update tags 9", color=ft.colors.WHITE), ft.colors.RED,
                                          update_tags_10_functions["function_9"]),
    "update_tags_10_10": SendRequestButton(ft.Text("Update tags 10", color=ft.colors.WHITE), ft.colors.RED,
                                           update_tags_10_functions["function_10"])}

update_tags_10_buttons_raskat = {
    "update_tags_10_1": SendRequestButton(ft.Text("Update tags 1", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_10_functions_raskat["function_1"]),
    "update_tags_10_2": SendRequestButton(ft.Text("Update tags 2", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_10_functions_raskat["function_2"]),
    "update_tags_10_3": SendRequestButton(ft.Text("Update tags 3", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_10_functions_raskat["function_3"]),
    "update_tags_10_4": SendRequestButton(ft.Text("Update tags 4", color=ft.colors.WHITE), ft.colors.GREEN,
                                          update_tags_10_functions_raskat["function_4"]),
    "update_tags_10_5": SendRequestButton(ft.Text("Update tags 5", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_10_functions_raskat["function_5"]),
    "update_tags_10_6": SendRequestButton(ft.Text("Update tags 6", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_10_functions_raskat["function_6"]),
    "update_tags_10_7": SendRequestButton(ft.Text("Update tags 7", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_10_functions_raskat["function_7"]),
    "update_tags_10_8": SendRequestButton(ft.Text("Update tags 8", color=ft.colors.WHITE), ft.colors.ORANGE,
                                          update_tags_10_functions_raskat["function_8"]),
    "update_tags_10_9": SendRequestButton(ft.Text("Update tags 9", color=ft.colors.WHITE), ft.colors.RED,
                                          update_tags_10_functions_raskat["function_9"]),
    "update_tags_10_10": SendRequestButton(ft.Text("Update tags 10", color=ft.colors.WHITE), ft.colors.RED,
                                           update_tags_10_functions_raskat["function_10"])}

update_tags_9_buttons = {
    "update_tags_9_1": SendRequestButton(ft.Text("Update tags 1", color=ft.colors.WHITE), ft.colors.GREEN,
                                         update_tags_9_functions["function_1"]),
    "update_tags_9_2": SendRequestButton(ft.Text("Update tags 2", color=ft.colors.WHITE), ft.colors.GREEN,
                                         update_tags_9_functions["function_2"]),
    "update_tags_9_3": SendRequestButton(ft.Text("Update tags 3", color=ft.colors.WHITE), ft.colors.GREEN,
                                         update_tags_9_functions["function_3"]),
    "update_tags_9_4": SendRequestButton(ft.Text("Update tags 4", color=ft.colors.WHITE), ft.colors.ORANGE,
                                         update_tags_9_functions["function_4"]),
    "update_tags_9_5": SendRequestButton(ft.Text("Update tags 5", color=ft.colors.WHITE), ft.colors.ORANGE,
                                         update_tags_9_functions["function_5"]),
    "update_tags_9_6": SendRequestButton(ft.Text("Update tags 6", color=ft.colors.WHITE), ft.colors.ORANGE,
                                         update_tags_9_functions["function_6"]),
    "update_tags_9_7": SendRequestButton(ft.Text("Update tags 7", color=ft.colors.WHITE), ft.colors.RED,
                                         update_tags_9_functions["function_7"]),
    "update_tags_9_8": SendRequestButton(ft.Text("Update tags 8", color=ft.colors.WHITE), ft.colors.RED,
                                         update_tags_9_functions["function_8"]),
    "update_tags_9_9": SendRequestButton(ft.Text("Update tags 9", color=ft.colors.WHITE), ft.colors.RED,
                                         update_tags_9_functions["function_9"])}

update_tags_7_buttons = {
    "update_tags_7_1": SendRequestButton(ft.Text("Update tags 1", color=ft.colors.WHITE), ft.colors.GREEN,
                                         update_tags_7_functions["function_1"]),
    "update_tags_7_2": SendRequestButton(ft.Text("Update tags 2", color=ft.colors.WHITE), ft.colors.GREEN,
                                         update_tags_7_functions["function_2"]),
    "update_tags_7_3": SendRequestButton(ft.Text("Update tags 3", color=ft.colors.WHITE), ft.colors.GREEN,
                                         update_tags_7_functions["function_3"]),
    "update_tags_7_4": SendRequestButton(ft.Text("Update tags 4", color=ft.colors.WHITE), ft.colors.ORANGE,
                                         update_tags_7_functions["function_4"]),
    "update_tags_7_5": SendRequestButton(ft.Text("Update tags 5", color=ft.colors.WHITE), ft.colors.ORANGE,
                                         update_tags_7_functions["function_5"]),
    "update_tags_7_6": SendRequestButton(ft.Text("Update tags 6", color=ft.colors.WHITE), ft.colors.ORANGE,
                                         update_tags_7_functions["function_6"]),
    "update_tags_7_7": SendRequestButton(ft.Text("Update tags 7", color=ft.colors.WHITE), ft.colors.RED,
                                         update_tags_7_functions["function_7"])}

update_tags_3_buttons = {
    "update_tags_3_1": SendRequestButton(ft.Text("Update tags 1", color=ft.colors.WHITE), ft.colors.GREEN,
                                         update_tags_3_functions["function_1"]),
    "update_tags_3_2": SendRequestButton(ft.Text("Update tags 2", color=ft.colors.WHITE), ft.colors.ORANGE,
                                         update_tags_3_functions["function_2"]),
    "update_tags_3_3": SendRequestButton(ft.Text("Update tags 3", color=ft.colors.WHITE), ft.colors.RED,
                                         update_tags_3_functions["function_3"])}

no_hint_buttons = {
    "no_hint_1": SendRequestButton(ft.Text("Update tags 1, someTag<25", color=ft.colors.WHITE),
                                   ft.colors.GREEN, no_hint_functions["function_1"]),
    "no_hint_2": SendRequestButton(ft.Text("Update tags 2, someTag(25-150)", color=ft.colors.WHITE),
                                   ft.colors.GREEN, no_hint_functions["function_2"]),
    "no_hint_3": SendRequestButton(ft.Text("Update tags 3, someTag(150-350)", color=ft.colors.WHITE),
                                   ft.colors.ORANGE, no_hint_functions["function_3"]),
    "no_hint_4": SendRequestButton(ft.Text("Update tags 4, someTag>350", color=ft.colors.WHITE),
                                   ft.colors.RED, no_hint_functions["function_4"])}

collection_gacha_tags_buttons = {
    "collection_gacha_1": SendRequestButton(ft.Text("Update tags 1, someTag<25", color=ft.colors.WHITE),
                                            ft.colors.GREEN, collection_gacha_tags_functions["function_1"]),
    "collection_gacha_2": SendRequestButton(ft.Text("Update tags 2, someTag>25", color=ft.colors.WHITE),
                                            ft.colors.ORANGE, collection_gacha_tags_functions["function_2"])
}

weapon_lto_buttons = {
    "weapon_lto_1": SendRequestButton(ft.Text("Update tags 1, someTag<30", color=ft.colors.WHITE),
                                      ft.colors.GREEN, weapon_lto_functions["function_1"]),
    "weapon_lto_2": SendRequestButton(ft.Text("Update tags 2, someTag(30-85)", color=ft.colors.WHITE),
                                      ft.colors.ORANGE, weapon_lto_functions["function_2"]),
    "weapon_lto_3": SendRequestButton(ft.Text("Update tags 3, someTag(85-150)", color=ft.colors.WHITE),
                                      ft.colors.ORANGE, weapon_lto_functions["function_3"]),
    "weapon_lto_4": SendRequestButton(ft.Text("Update tags 4, someTag>150", color=ft.colors.WHITE),
                                      ft.colors.RED, weapon_lto_functions["function_4"])}

shiny_buttons = {
    "shiny_1": SendRequestButton(ft.Text("Update tags 1, someTag<30", color=ft.colors.WHITE),
                                 ft.colors.GREEN, shiny_functions["function_1"]),
    "shiny_2": SendRequestButton(ft.Text("Update tags 2, someTag(30-60)", color=ft.colors.WHITE),
                                 ft.colors.GREEN, shiny_functions["function_2"]),
    "shiny_3": SendRequestButton(ft.Text("Update tags 3, someTag(60-85)", color=ft.colors.WHITE),
                                 ft.colors.ORANGE, shiny_functions["function_3"]),
    "shiny_4": SendRequestButton(ft.Text("Update tags 4, someTag(85-150)", color=ft.colors.WHITE),
                                 ft.colors.ORANGE, shiny_functions["function_4"]),
    "shiny_5": SendRequestButton(ft.Text("Update tags 5, someTag>150", color=ft.colors.WHITE),
                                 ft.colors.RED, shiny_functions["function_5"])}

new_shiny_buttons = {
    "shiny_1": SendRequestButton(ft.Text("Update tags 1, someTag<30", color=ft.colors.WHITE),
                                 ft.colors.GREEN, new_shiny_functions["function_1"]),
    "shiny_2": SendRequestButton(ft.Text("Update tags 2, someTag(30-60)", color=ft.colors.WHITE),
                                 ft.colors.GREEN, new_shiny_functions["function_2"]),
    "shiny_3": SendRequestButton(ft.Text("Update tags 3, someTag(60-90)", color=ft.colors.WHITE),
                                 ft.colors.ORANGE, new_shiny_functions["function_3"]),
    "shiny_4": SendRequestButton(ft.Text("Update tags 4, someTag(90-150)", color=ft.colors.WHITE),
                                 ft.colors.ORANGE, new_shiny_functions["function_4"]),
    "shiny_5": SendRequestButton(ft.Text("Update tags 5, someTag>150", color=ft.colors.WHITE),
                                 ft.colors.RED, new_shiny_functions["function_5"])}

theo_buttons = {
    "theo_1": SendRequestButton(ft.Text("Update tags 1, someTag<15", color=ft.colors.WHITE),
                                ft.colors.GREEN, theo_functions["function_1"]),
    "theo_2": SendRequestButton(ft.Text("Update tags 2, someTag(15-45)", color=ft.colors.WHITE),
                                ft.colors.GREEN, theo_functions["function_2"]),
    "theo_3": SendRequestButton(ft.Text("Update tags 3, someTag(45-100)/someTag(<14)",
                                        color=ft.colors.WHITE), ft.colors.GREEN, theo_functions["function_3"]),
    "theo_4": SendRequestButton(ft.Text("Update tags 4, someTag(45-100)/someTag(>14)",
                                        color=ft.colors.WHITE), ft.colors.ORANGE, theo_functions["function_4"]),
    "theo_5": SendRequestButton(ft.Text("Update tags 5, someTag(100-500)/someTag(<18)",
                                        color=ft.colors.WHITE), ft.colors.ORANGE, theo_functions["function_5"]),
    "theo_6": SendRequestButton(ft.Text("Update tags 6, someTag(100-500)/someTag(>18)",
                                        color=ft.colors.WHITE), ft.colors.ORANGE, theo_functions["function_6"]),
    "theo_7": SendRequestButton(ft.Text("Update tags 7, someTag>500", color=ft.colors.WHITE),
                                ft.colors.RED, theo_functions["function_7"])}

lto_oto_gc_buttons = {
    "lto_oto_gc_1": SendRequestButton(ft.Text("Update tags 1, someTag<20", color=ft.colors.WHITE),
                                      ft.colors.GREEN, lto_oto_gc_functions["function_1"]),
    "lto_oto_gc_2": SendRequestButton(ft.Text("Update tags 2, someTag(20-85)", color=ft.colors.WHITE),
                                      ft.colors.GREEN, lto_oto_gc_functions["function_2"]),
    "lto_oto_gc_3": SendRequestButton(ft.Text("Update tags 3, someTag(85-150)", color=ft.colors.WHITE),
                                      ft.colors.ORANGE, lto_oto_gc_functions["function_3"]),
    "lto_oto_gc_4": SendRequestButton(ft.Text("Update tags 4, someTag>150", color=ft.colors.WHITE),
                                      ft.colors.RED, lto_oto_gc_functions["function_4"])
}

among_buttons = {
    "among_1": SendRequestButton(ft.Text("Update tags 1, someTag<150", color=ft.colors.WHITE),
                                 ft.colors.GREEN, among_functions["function_1"]),
    "among_2": SendRequestButton(ft.Text("Update tags 2, someTag(150-300)", color=ft.colors.WHITE),
                                 ft.colors.ORANGE, among_functions["function_2"]),
    "among_3": SendRequestButton(ft.Text("Update tags 3, someTag>300", color=ft.colors.WHITE),
                                 ft.colors.RED, among_functions["function_3"])
}

new_among_buttons = {
    "among_1": SendRequestButton(ft.Text("Update tags 1, someTag<4", color=ft.colors.WHITE),
                                 ft.colors.GREEN, new_among_functions["function_1"]),
    "among_2": SendRequestButton(ft.Text("Update tags 2, someTag(4-8)", color=ft.colors.WHITE),
                                 ft.colors.ORANGE, new_among_functions["function_2"]),
    "among_3": SendRequestButton(ft.Text("Update tags 3, someTag>8", color=ft.colors.WHITE),
                                 ft.colors.RED, new_among_functions["function_3"])
}

labyrinth_buttons = {
    "labyrinth_1": SendRequestButton(ft.Text("Update tags 1, someTag<25", color=ft.colors.WHITE),
                                     ft.colors.GREEN, labyrinth_functions["function_1"]),
    "labyrinth_2": SendRequestButton(ft.Text("Update tags 2, someTag(25-150)", color=ft.colors.WHITE),
                                     ft.colors.ORANGE, labyrinth_functions["function_2"]),
    "labyrinth_3": SendRequestButton(ft.Text("Update tags 3, someTag(150-300)", color=ft.colors.WHITE),
                                     ft.colors.ORANGE, labyrinth_functions["function_3"]),
    "labyrinth_4": SendRequestButton(ft.Text("Update tags 4, someTag>300", color=ft.colors.WHITE),
                                     ft.colors.RED, labyrinth_functions["function_4"])
}

bogo_buttons = {
    "bogo_1": SendRequestButton(ft.Text("Update tags 1, someTag<50", color=ft.colors.WHITE),
                                ft.colors.GREEN, bogo_functions["function_1"]),
    "bogo_2": SendRequestButton(ft.Text("Update tags 2, someTag(50-150)", color=ft.colors.WHITE),
                                ft.colors.ORANGE, bogo_functions["function_2"]),
    "bogo_3": SendRequestButton(ft.Text("Update tags 3, someTag(150-500)", color=ft.colors.WHITE),
                                ft.colors.ORANGE, bogo_functions["function_3"]),
    "bogo_4": SendRequestButton(ft.Text("Update tags 4, someTag>500", color=ft.colors.WHITE),
                                ft.colors.RED, bogo_functions["function_4"])
}

comeback_buttons = {
    "comeback_1": SendRequestButton(ft.Text("Update tags 1, someTag<8", color=ft.colors.WHITE),
                                    ft.colors.GREEN, comeback_functions["function_1"]),
    "comeback_2": SendRequestButton(ft.Text("Update tags 2, someTag(8-15)", color=ft.colors.WHITE),
                                    ft.colors.ORANGE, comeback_functions["function_2"]),
    "comeback_3": SendRequestButton(ft.Text("Update tags 3, someTag(15-20)", color=ft.colors.WHITE),
                                    ft.colors.ORANGE, comeback_functions["function_3"]),
    "comeback_4": SendRequestButton(ft.Text("Update tags 4, someTag>20", color=ft.colors.WHITE),
                                    ft.colors.RED, comeback_functions["function_4"])
}

tickets_bans_11_buttons = {
    "ban_11_1": BanButton(),
    "ban_11_2": BanButton(),
    "ban_11_3": BanButton(),
    "ban_11_4": BanButton(),
    "ban_11_5": BanButton(),
    "ban_11_6": BanButton(),
    "ban_11_7": BanButton(),
    "ban_11_8": BanButton(),
    "ban_11_9": BanButton(),
    "ban_11_10": BanButton(),
    "ban_11_11": BanButton(),
    "ban_11_12": BanButton(),
    "ban_11_13": BanButton(),
    "ban_11_14": BanButton(),
    "ban_11_15": BanButton(),
    "ban_11_16": BanButton(),
    "ban_11_17": BanButton(),
    "ban_11_18": BanButton(),
    "ban_11_19": BanButton(),
    "ban_11_20": BanButton(),
    "ban_11_21": BanButton(),
    "ban_11_22": BanButton(),
    "check_all_bans_button_11": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                                  on_click=bans_11_functions["check_all"]),
    "open_json_button_11": ft.FilePicker(on_result=bans_11_functions["open_json"]),
    "selected_files_11": ft.Text(),
    "upload_json_button_11": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=bans_11_functions["download_json"]
    ),
    "reset_button_11": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET, on_click=bans_11_functions["reset"])
}

choose_json_button_11 = ft.Row(
    [
        ft.ElevatedButton(
            text="Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_bans_11_buttons["open_json_button_11"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_bans_11_buttons["selected_files_11"]
    ]
)

tickets_bans_10_buttons = {
    "open_json_button_10": ft.FilePicker(on_result=bans_10_functions["open_json"]),
    "selected_files_10": ft.Text(),
    "upload_json_button_10": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=bans_10_functions["download_json"]
    ),
    "reset_button_10": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET,
                                         on_click=bans_10_functions["reset"]),
    "check_all_bans_button_10": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                                  on_click=bans_10_functions["check_all"]),
    "ban_10_1": BanButton(),
    "ban_10_2": BanButton(),
    "ban_10_3": BanButton(),
    "ban_10_4": BanButton(),
    "ban_10_5": BanButton(),
    "ban_10_6": BanButton(),
    "ban_10_7": BanButton(),
    "ban_10_8": BanButton(),
    "ban_10_9": BanButton(),
    "ban_10_10": BanButton(),
    "ban_10_11": BanButton(),
    "ban_10_12": BanButton(),
    "ban_10_13": BanButton(),
    "ban_10_14": BanButton(),
    "ban_10_15": BanButton(),
    "ban_10_16": BanButton(),
    "ban_10_17": BanButton(),
    "ban_10_18": BanButton(),
    "ban_10_19": BanButton(),
    "ban_10_20": BanButton()
}

choose_json_button_10 = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_bans_10_buttons["open_json_button_10"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_bans_10_buttons["selected_files_10"]
    ]
)

tickets_bans_9_buttons = {
    "open_json_button": ft.FilePicker(on_result=bans_9_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=bans_9_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET, on_click=bans_9_functions["reset"]),
    "ban_9_1": BanButton(),
    "ban_9_2": BanButton(),
    "ban_9_3": BanButton(),
    "ban_9_4": BanButton(),
    "ban_9_5": BanButton(),
    "ban_9_6": BanButton(),
    "ban_9_7": BanButton(),
    "ban_9_8": BanButton(),
    "ban_9_9": BanButton(),
    "ban_9_10": BanButton(),
    "ban_9_11": BanButton(),
    "ban_9_12": BanButton(),
    "ban_9_13": BanButton(),
    "ban_9_14": BanButton(),
    "ban_9_15": BanButton(),
    "ban_9_16": BanButton(),
    "ban_9_17": BanButton(),
    "ban_9_18": BanButton(),
    "check_all_bans_button": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                               on_click=bans_9_functions["check_all"])
}

choose_json_button_9 = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_bans_9_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_bans_9_buttons["selected_files"]
    ]
)

tickets_bans_7_buttons = {
    "open_json_button": ft.FilePicker(on_result=bans_7_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=bans_7_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET, on_click=bans_7_functions["reset"]),
    "ban_7_1": BanButton(),
    "ban_7_2": BanButton(),
    "ban_7_3": BanButton(),
    "ban_7_4": BanButton(),
    "ban_7_5": BanButton(),
    "ban_7_6": BanButton(),
    "ban_7_7": BanButton(),
    "ban_7_8": BanButton(),
    "ban_7_9": BanButton(),
    "ban_7_10": BanButton(),
    "ban_7_11": BanButton(),
    "ban_7_12": BanButton(),
    "ban_7_13": BanButton(),
    "ban_7_14": BanButton(),
    "check_all_bans_button": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                               on_click=bans_7_functions["check_all"])
}

choose_json_button_7 = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_bans_7_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_bans_7_buttons["selected_files"]
    ]
)

tickets_bans_3_buttons = {
    "open_json_button": ft.FilePicker(on_result=bans_3_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=bans_3_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET, on_click=bans_3_functions["reset"]),
    "check_all_bans_button": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                               on_click=bans_3_functions["check_all"]),
    "ban_3_1": BanButton(),
    "ban_3_2": BanButton(),
    "ban_3_3": BanButton(),
    "ban_3_4": BanButton(),
    "ban_3_5": BanButton(),
    "ban_3_6": BanButton()
}

choose_json_button_3 = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_bans_3_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_bans_3_buttons["selected_files"]
    ]
)

tickets_criteria_buttons = {
    "open_json_button": ft.FilePicker(on_result=tickets_criteria_functions["open_json"]),
    "selected_files": ft.Text(),
    "description": ft.Text("Здесь можно закидывать на проверку любые офферы, у которых критерий " +
                           "notIn РБ и РФ и доступен в ГП РФ, кроме bcp и cgp."),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=tickets_criteria_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=tickets_criteria_functions["reset"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "button_15": BanButton(),
    "button_16": BanButton(),
    "button_17": BanButton(),
    "button_18": BanButton(),
    "button_19": BanButton(),
    "button_20": BanButton(),
    "button_21": BanButton(),
    "button_22": BanButton(),
    "check_all_criteria_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                                   on_click=tickets_criteria_functions["check_all"])
}

choose_json_button_tickets_criteria = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_criteria_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_criteria_buttons["selected_files"]
    ]
)

no_hint_bans_buttons = {
    "open_json_button": ft.FilePicker(on_result=no_hint_bans_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=no_hint_bans_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET, on_click=no_hint_bans_functions["reset"]),
    "check_all_bans_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                               on_click=no_hint_bans_functions["check_all"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "button_15": BanButton(),
    "button_16": BanButton()
}

choose_json_button_no_hint = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: no_hint_bans_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        no_hint_bans_buttons["selected_files"]
    ]
)

no_hint_balance_buttons = {
    "open_json_button": ft.FilePicker(on_result=no_hint_balance_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=no_hint_balance_functions["download_json"]
    ),
    "description": ft.Text(
        "Здесь у офферов типа no_hint проверяются lvl start, only_for_buyer, теги, trigger, trigger_param, " +
        "skin_id, наполнение, criteria, packname и platform." + "\n" +
        "Вручную проверить на дашборде name, type, ver begin, date_begin, date_finish." + "\n" +
        "В начале апдейта словить все офферы в игре, чтобы убедиться, что ни один из энергетиков " +
        "не добавили в store.json"),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=no_hint_balance_functions["reset"]),
    "check_all_balance_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                                  on_click=no_hint_balance_functions["check_all"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "button_15": BanButton(),
    "button_16": BanButton()
}

choose_json_button_no_hint_balance = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: no_hint_balance_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        no_hint_balance_buttons["selected_files"]
    ]
)

bcp_previous_buttons = {
    "description": ft.Text(
        f"Здесь проверяются только BCP пред. апдейта; проверяется все, кроме дат."
        + "\n" +
        "На даше проверить date_begin и date_finish, ловить в игре необязательно."),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=bcp_previous_functions["reset"]),
    "open_json_button": ft.FilePicker(on_result=bcp_previous_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=bcp_previous_functions["download_json"]
    ),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=bcp_previous_functions["check_all"]),
    'dynamic_items_1': ft.Text(),
    'dynamic_items_2': ft.Text(),
    'dynamic_items_3': ft.Text()
}

choose_json_button_bcp_previous = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: bcp_previous_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        bcp_previous_buttons["selected_files"]
    ]
)

bcp_actual_buttons = {
    "description": ft.Text(f"Здесь проверяются только BCP текущего апдейта; проверяется все, кроме " +
                           "дат и версий." + "\n" + "Перед нажатием на Check all в строку skin_id вставить " +
                           "скин айди актуального bcp, а в day выбрать день апдейта (смотри в таблице офферов)." + "\n" +
                           "На даше проверить date_begin, date_finish и версии. В игре ловить необязательно."),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET, on_click=bcp_actual_functions["reset"]),
    "open_json_button": ft.FilePicker(on_result=bcp_actual_functions["open_json"]),
    "selected_files": ft.Text(),
    "skin_id_field": ft.TextField(width=300, label="skin id", hint_text="Введи skin_id. Пример: 1094"),
    "day": ft.Dropdown(
        width=100,
        label='day',
        options=[
            ft.dropdown.Option('0'),
            ft.dropdown.Option('1'),
            ft.dropdown.Option('2'),
            ft.dropdown.Option('3'),
            ft.dropdown.Option('4'),
            ft.dropdown.Option('5'),
            ft.dropdown.Option('6'),
            ft.dropdown.Option('7'),
            ft.dropdown.Option('8'),
            ft.dropdown.Option('9'),
            ft.dropdown.Option('10'),
            ft.dropdown.Option('11'),
            ft.dropdown.Option('12'),
            ft.dropdown.Option('13'),
            ft.dropdown.Option('14'),
            ft.dropdown.Option('15'),
            ft.dropdown.Option('16'),
            ft.dropdown.Option('17'),
            ft.dropdown.Option('18'),
            ft.dropdown.Option('19'),
            ft.dropdown.Option('20'),
            ft.dropdown.Option('21'),
            ft.dropdown.Option('22'),
            ft.dropdown.Option('23'),
            ft.dropdown.Option('24'),
            ft.dropdown.Option('25'),
            ft.dropdown.Option('26'),
            ft.dropdown.Option('27')
        ],
    ),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=bcp_actual_functions["download_json"]
    ),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=bcp_actual_functions["check_all"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton()
}

choose_json_button_bcp_actual = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: bcp_actual_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        bcp_actual_buttons["selected_files"]
    ]
)

cgp_6_buttons = {
    "description": ft.Text(
        "Здесь проверяются CGP в кол-ве 6 штук (запускаются в начале апдейта): проверяется всё, кроме дат и " +
        "версий." + "\n" + "На даше проверить даты и версии, в игре ловить необязательно."),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET, on_click=cgp_6_functions["reset"]),
    "open_json_button": ft.FilePicker(on_result=cgp_6_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=cgp_6_functions["download_json"]
    ),
    "day": ft.Dropdown(
        width=100,
        label='day',
        options=[
            ft.dropdown.Option('0'),
            ft.dropdown.Option('1'),
            ft.dropdown.Option('2'),
            ft.dropdown.Option('3')
        ],
    ),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=cgp_6_functions["check_all"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton()
}

choose_json_button_cgp_6 = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: cgp_6_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        cgp_6_buttons["selected_files"]
    ]
)

cgp_9_buttons = {
    "open_json_button": ft.FilePicker(on_result=cgp_9_functions["open_json"]),
    "selected_files": ft.Text(),
    "description": ft.Text(
        "Здесь проверяются CGP в кол-ве 9 штук: проверяется всё, кроме дат и версий."
        + "\n" + "На даше проверить даты и версии, в игре ловить необязательно."),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=cgp_9_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET, on_click=cgp_9_functions["reset"]),
    "day": ft.Dropdown(
        width=100,
        label='day',
        options=[
            ft.dropdown.Option('4'),
            ft.dropdown.Option('5'),
            ft.dropdown.Option('6'),
            ft.dropdown.Option('7'),
            ft.dropdown.Option('8'),
            ft.dropdown.Option('9'),
            ft.dropdown.Option('10'),
            ft.dropdown.Option('11'),
            ft.dropdown.Option('12'),
            ft.dropdown.Option('13'),
            ft.dropdown.Option('14'),
            ft.dropdown.Option('15'),
            ft.dropdown.Option('16'),
            ft.dropdown.Option('17'),
            ft.dropdown.Option('18'),
            ft.dropdown.Option('19'),
            ft.dropdown.Option('20'),
            ft.dropdown.Option('21'),
            ft.dropdown.Option('22'),
            ft.dropdown.Option('23'),
            ft.dropdown.Option('24'),
            ft.dropdown.Option('25'),
            ft.dropdown.Option('26'),
            ft.dropdown.Option('27')
        ],
    ),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=cgp_9_functions["check_all"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton()
}

choose_json_button_cgp_9 = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: cgp_9_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        cgp_9_buttons["selected_files"]
    ]
)

other_bans_wo_field_buttons = {
    "open_json_button": ft.FilePicker(on_result=check_all_bans_other_wo_field_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=check_all_bans_other_wo_field_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=check_all_bans_other_wo_field_functions["reset"]),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=check_all_bans_other_wo_field_functions["check_all"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton()
}

choose_json_button_other_wo_field = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: other_bans_wo_field_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        other_bans_wo_field_buttons["selected_files"]
    ]
)

other_bans_with_field_buttons = {
    "open_json_button": ft.FilePicker(on_result=check_all_bans_other_with_field_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=check_all_bans_other_with_field_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=check_all_bans_other_with_field_functions["reset"]),
    "button_1": BanButton(),
    "input_bans_field": ft.TextField(width=600, label="banOffers", hint_text="Введи баны через запятую"),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=check_all_bans_other_with_field_functions["check_all"])
}

choose_json_button_with_field = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: other_bans_with_field_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        other_bans_with_field_buttons["selected_files"]
    ]
)

oto_2_buttons = {
    "open_json_button": ft.FilePicker(on_result=check_oto_2_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=check_oto_2_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=check_oto_2_functions["reset"]),
    "button_1": BanButton(),
    "input_denies_field": ft.TextField(width=600, label="denies", hint_text="Введи denies через запятую"),
    "input_allows_field": ft.TextField(width=600, label="allows", hint_text="Введи allows через запятую"),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=check_oto_2_functions["check_all"])
}

choose_json_button_oto_2 = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: oto_2_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        oto_2_buttons["selected_files"]
    ]
)

my_tags_buttons = {
    "my_tags": SendRequestButton(ft.Text("What are my tags?", color=ft.colors.WHITE),
                                 ft.colors.BLUE, my_tags_functions["function_1"]),
    "tags_field": ft.Text("")
}

manual_tags_buttons = {
    "some_tag_text_1": ManualTags("some_tag_text_1"),
    "some_tag_1": ft.TextField(width=100, value="0.99"),
    "some_tag_text_2": ManualTags("some_tag_text_2"),
    "some_tag_2": ft.TextField(width=100, value="0.99"),
    "some_tag_text_3": ManualTags("some_tag_text_3"),
    "some_tag_3": ft.TextField(width=100, value="0.99"),
    "some_tag_text_4": ManualTags("some_tag_text_4"),
    "some_tag_4": ft.TextField(width=100, value="0.99"),
    "some_tag_text_5": ManualTags("some_tag_text_5"),
    "some_tag_5": ft.TextField(width=100, value="0.99"),
    "some_tag_text_6": ManualTags("some_tag_text_6"),
    "some_tag_6": ft.TextField(width=100, value="0.99"),
    "some_tag_text_7": ManualTags("some_tag_text_7"),
    "some_tag_7": ft.TextField(width=100, value="0.99"),
    "some_tag_text_8": ManualTags("some_tag_text_8"),
    "some_tag_8": ft.TextField(width=100, value="0.99"),
    "some_tag_text_9": ManualTags("some_tag_text_9"),
    "some_tag_9": ft.TextField(width=100, value="0.99"),
    "some_tag_text_10": ManualTags("some_tag_text_10"),
    "some_tag_10": ft.TextField(width=100, value="0.99"),
    "some_tag_text_11": ManualTags("some_tag_text_11"),
    "some_tag_11": ft.TextField(width=100, value="0.99"),
    "some_tag_text_12": ManualTags("some_tag_text_12"),
    "some_tag_12": ft.TextField(width=100, value="0.99"),
    "some_tag_text_13": ManualTags("some_tag_text_13"),
    "some_tag_13": ft.TextField(width=100, value="0.99"),
    "some_tag_text_14": ManualTags("some_tag_text_14"),
    "some_tag_14": ft.TextField(width=100, value="0.99"),
    "some_tag_text_15": ManualTags("some_tag_text_15"),
    "some_tag_15": ft.TextField(width=100, value="0.99"),
    "some_tag_text_16": ManualTags("some_tag_text_16"),
    "some_tag_16": ft.TextField(width=100, value="0.99"),
    "some_tag_text_17": ManualTags("some_tag_text_17"),
    "some_tag_17": ft.TextField(width=100, value="0.99"),
    "some_tag_text_18": ManualTags("some_tag_text_18"),
    "some_tag_18": ft.TextField(width=100, value="0.99"),
    "some_tag_text_19": ManualTags("some_tag_text_19"),
    "some_tag_19": ft.TextField(width=100, value="0.99"),
    "submit": SendRequestButton(ft.Text("Submit", color=ft.colors.WHITE),
                                ft.colors.BLUE, manual_tags)
}

json_compare_buttons_1 = {
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "button_15": BanButton(),
    "button_16": BanButton(),
    "button_17": BanButton(),
    "button_18": BanButton(),
    "button_19": BanButton(),
    "button_20": BanButton(),
    "button_21": BanButton(),
    "button_22": BanButton(),
    "open_json_button": ft.FilePicker(on_result=compare_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON'ы",
        icon=ft.icons.UPLOAD,
        on_click=compare_functions["download_json"]
    )
}

choose_json_compare_button = ft.Row(
    [
        ft.ElevatedButton(
            text="Выбрать JSON'ы",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: json_compare_buttons_1["open_json_button"].pick_files(
                allow_multiple=True,
                allowed_extensions=["json"]
            ),
        ),
        json_compare_buttons_1["selected_files"]
    ]
)

json_compare_buttons_2 = {
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "button_15": BanButton(),
    "button_16": BanButton(),
    "button_17": BanButton(),
    "button_18": BanButton(),
    "button_19": BanButton(),
    "button_20": BanButton(),
    "button_21": BanButton(),
    "button_22": BanButton(),
    "check_all_button": ft.ElevatedButton(text="Compare all", icon=ft.icons.ALL_INBOX,
                                          on_click=compare_functions["check_all"]),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET, on_click=compare_functions["reset"])
}

among_balance_new_tc_buttons = {
    "description": ft.Text('Проверяются блоки event и filter. Вручную проверить скин, ауру, баны и т.д.'),
    "open_json_button": ft.FilePicker(on_result=among_new_ts_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=among_new_ts_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=among_new_ts_functions["reset"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=among_new_ts_functions["check_all"]),
    'type': ft.Dropdown(
        width=300,
        label='type',
        options=[
            ft.dropdown.Option('hanami'),
            ft.dropdown.Option('songkran')
        ],
    )
}

choose_json_button_among_balance_new_ts = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: among_balance_new_tc_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        among_balance_new_tc_buttons["selected_files"]
    ]
)

among_balance_average_buttons = {
    "description": ft.Text('Проверяются блоки event и filter. Вручную проверить скин, ауру, баны и т.д.'),
    "open_json_button": ft.FilePicker(on_result=among_average_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=among_average_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=among_average_functions["reset"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=among_average_functions["check_all"]),
    "me_field": ft.TextField(width=300, label="ME id", hint_text="Введи id ME. Пример: 100822"),
}

choose_json_button_among_balance_average = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: among_balance_average_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        among_balance_average_buttons["selected_files"]
    ]
)

labyrinth_balance_ww_buttons = {
    "description": ft.Text('Проверяются блоки event и filter. Вручную проверить скин, ауру, баны и т.д.'),
    "open_json_button": ft.FilePicker(on_result=labyrinth_balance_ww_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=labyrinth_balance_ww_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=labyrinth_balance_ww_functions["reset"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=labyrinth_balance_ww_functions["check_all"]),
    'type': ft.Dropdown(
        width=300,
        label='type',
        options=[
            ft.dropdown.Option('summer day'),
            ft.dropdown.Option("father's day")
        ]
    )
}

choose_json_button_labyrinth_balance_ww = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: labyrinth_balance_ww_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        labyrinth_balance_ww_buttons["selected_files"]
    ]
)

labyrinth_balance_cn_buttons = {
    "description": ft.Text('Проверяются блоки event и filter. Вручную проверить скин, ауру, баны и т.д.'),
    "open_json_button": ft.FilePicker(on_result=labyrinth_balance_cn_functions["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        "Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=labyrinth_balance_cn_functions["download_json"]
    ),
    "reset_button": ft.ElevatedButton("Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=labyrinth_balance_cn_functions["reset"]),
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "check_all_button": ft.ElevatedButton("Check all", icon=ft.icons.ALL_INBOX,
                                          on_click=labyrinth_balance_cn_functions["check_all"]),
    'type': ft.Dropdown(
        width=300,
        label='type',
        options=[
            ft.dropdown.Option('summer day'),
            ft.dropdown.Option("father's day")
        ]
    )
}

choose_json_button_labyrinth_balance_cn = ft.Row(
    [
        ft.ElevatedButton(
            "Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: labyrinth_balance_cn_buttons["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        labyrinth_balance_cn_buttons["selected_files"]
    ]
)

tickets_balance_checker_buttons_11 = {
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "button_15": BanButton(),
    "button_16": BanButton(),
    "button_17": BanButton(),
    "button_18": BanButton(),
    "button_19": BanButton(),
    "button_20": BanButton(),
    "button_21": BanButton(),
    "button_22": BanButton(),
    "check_all": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                   on_click=tickets_balance_functions_11["check_all"]),
    "open_json_button": ft.FilePicker(on_result=tickets_balance_functions_11["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=tickets_balance_functions_11["download_json"]
    ),
    "day": ft.Dropdown(
        width=100,
        label='day',
        options=[
            ft.dropdown.Option('0'),
            ft.dropdown.Option('1'),
            ft.dropdown.Option('2'),
            ft.dropdown.Option('3'),
            ft.dropdown.Option('4'),
            ft.dropdown.Option('5'),
            ft.dropdown.Option('6'),
            ft.dropdown.Option('7')
        ]
    ),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=tickets_balance_functions_11["reset"])
}

choose_json_button_tickets_balance_checker_11 = ft.Row(
    [
        ft.ElevatedButton(
            text="Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_balance_checker_buttons_11["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_balance_checker_buttons_11["selected_files"]
    ]
)

tickets_balance_checker_buttons_10 = {
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "button_15": BanButton(),
    "button_16": BanButton(),
    "button_17": BanButton(),
    "button_18": BanButton(),
    "button_19": BanButton(),
    "button_20": BanButton(),
    "check_all": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                   on_click=tickets_balance_functions_10["check_all"]),
    "open_json_button": ft.FilePicker(on_result=tickets_balance_functions_10["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=tickets_balance_functions_10["download_json"]
    ),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=tickets_balance_functions_10["reset"]),
    "day": ft.Dropdown(
        width=100,
        label='day',
        options=[
            ft.dropdown.Option('8'),
            ft.dropdown.Option('9'),
            ft.dropdown.Option('10'),
            ft.dropdown.Option('11'),
            ft.dropdown.Option('12'),
            ft.dropdown.Option('13'),
            ft.dropdown.Option('14'),
            ft.dropdown.Option('15'),
            ft.dropdown.Option('16'),
            ft.dropdown.Option('17'),
            ft.dropdown.Option('18')
        ]
    )
}

choose_json_button_tickets_balance_checker_10 = ft.Row(
    [
        ft.ElevatedButton(
            text="Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_balance_checker_buttons_10["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_balance_checker_buttons_10["selected_files"]
    ]
)

tickets_balance_checker_buttons_10_extra = {
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "button_15": BanButton(),
    "button_16": BanButton(),
    "button_17": BanButton(),
    "button_18": BanButton(),
    "button_19": BanButton(),
    "button_20": BanButton(),
    "check_all": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                   on_click=tickets_balance_functions_10_extra["check_all"]),
    "open_json_button": ft.FilePicker(on_result=tickets_balance_functions_10_extra["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=tickets_balance_functions_10_extra["download_json"]
    ),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=tickets_balance_functions_10_extra["reset"]),
    "day": ft.Dropdown(
        width=100,
        label='day',
        options=[
            ft.dropdown.Option('0'),
            ft.dropdown.Option('1'),
            ft.dropdown.Option('2'),
            ft.dropdown.Option('3'),
            ft.dropdown.Option('4'),
            ft.dropdown.Option('5'),
            ft.dropdown.Option('6'),
            ft.dropdown.Option('7'),
            ft.dropdown.Option('8'),
            ft.dropdown.Option('9'),
            ft.dropdown.Option('10'),
            ft.dropdown.Option('11'),
            ft.dropdown.Option('12'),
            ft.dropdown.Option('13'),
            ft.dropdown.Option('14'),
            ft.dropdown.Option('15'),
            ft.dropdown.Option('16'),
            ft.dropdown.Option('17'),
            ft.dropdown.Option('18'),
            ft.dropdown.Option('19'),
            ft.dropdown.Option('20'),
            ft.dropdown.Option('21'),
            ft.dropdown.Option('22'),
            ft.dropdown.Option('23'),
            ft.dropdown.Option('24'),
            ft.dropdown.Option('25'),
            ft.dropdown.Option('26'),
            ft.dropdown.Option('27')
        ]
    )
}

choose_json_button_tickets_balance_checker_10_extra = ft.Row(
    [
        ft.ElevatedButton(
            text="Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_balance_checker_buttons_10_extra["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_balance_checker_buttons_10_extra["selected_files"]
    ]
)

tickets_balance_checker_buttons_9 = {
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "button_15": BanButton(),
    "button_16": BanButton(),
    "button_17": BanButton(),
    "button_18": BanButton(),
    "check_all": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                   on_click=tickets_balance_functions_9["check_all"]),
    "open_json_button": ft.FilePicker(on_result=tickets_balance_functions_9["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=tickets_balance_functions_9["download_json"]
    ),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=tickets_balance_functions_9["reset"]),
    "day": ft.Dropdown(
        width=100,
        label='day',
        options=[
            ft.dropdown.Option('19'),
            ft.dropdown.Option('20'),
            ft.dropdown.Option('21'),
            ft.dropdown.Option('22'),
            ft.dropdown.Option('23'),
            ft.dropdown.Option('24')
        ]
    )
}

choose_json_button_tickets_balance_checker_9 = ft.Row(
    [
        ft.ElevatedButton(
            text="Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_balance_checker_buttons_9["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_balance_checker_buttons_9["selected_files"]
    ]
)

tickets_balance_checker_buttons_7 = {
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "button_7": BanButton(),
    "button_8": BanButton(),
    "button_9": BanButton(),
    "button_10": BanButton(),
    "button_11": BanButton(),
    "button_12": BanButton(),
    "button_13": BanButton(),
    "button_14": BanButton(),
    "check_all": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                   on_click=tickets_balance_functions_7["check_all"]),
    "open_json_button": ft.FilePicker(on_result=tickets_balance_functions_7["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=tickets_balance_functions_7["download_json"]
    ),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=tickets_balance_functions_7["reset"]),
    "day": ft.Dropdown(
        width=100,
        label='day',
        options=[
            ft.dropdown.Option('0'),
            ft.dropdown.Option('1'),
            ft.dropdown.Option('2'),
            ft.dropdown.Option('3'),
            ft.dropdown.Option('4'),
            ft.dropdown.Option('5'),
            ft.dropdown.Option('6'),
            ft.dropdown.Option('7'),
            ft.dropdown.Option('8'),
            ft.dropdown.Option('9'),
            ft.dropdown.Option('10'),
            ft.dropdown.Option('11'),
            ft.dropdown.Option('12'),
            ft.dropdown.Option('13'),
            ft.dropdown.Option('14'),
            ft.dropdown.Option('15'),
            ft.dropdown.Option('16'),
            ft.dropdown.Option('17'),
            ft.dropdown.Option('18'),
            ft.dropdown.Option('19'),
            ft.dropdown.Option('20'),
            ft.dropdown.Option('21'),
            ft.dropdown.Option('22'),
            ft.dropdown.Option('23'),
            ft.dropdown.Option('24'),
            ft.dropdown.Option('25'),
            ft.dropdown.Option('26'),
            ft.dropdown.Option('27')
        ]
    )
}

choose_json_button_tickets_balance_checker_7 = ft.Row(
    [
        ft.ElevatedButton(
            text="Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_balance_checker_buttons_7["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_balance_checker_buttons_7["selected_files"]
    ]
)

tickets_balance_checker_buttons_3 = {
    "button_1": BanButton(),
    "button_2": BanButton(),
    "button_3": BanButton(),
    "button_4": BanButton(),
    "button_5": BanButton(),
    "button_6": BanButton(),
    "check_all": ft.ElevatedButton(text="Check all", icon=ft.icons.ALL_INBOX,
                                   on_click=tickets_balance_functions_3["check_all"]),
    "open_json_button": ft.FilePicker(on_result=tickets_balance_functions_3["open_json"]),
    "selected_files": ft.Text(),
    "upload_json_button": ft.ElevatedButton(
        text="Загрузить JSON",
        icon=ft.icons.UPLOAD,
        on_click=tickets_balance_functions_3["download_json"]
    ),
    "reset_button": ft.ElevatedButton(text="Reset", icon=ft.icons.LOCK_RESET,
                                      on_click=tickets_balance_functions_3["reset"]),
    "day": ft.Dropdown(
        width=100,
        label='day',
        options=[
            ft.dropdown.Option('25'),
            ft.dropdown.Option('26'),
            ft.dropdown.Option('27')
        ]
    )
}

choose_json_button_tickets_balance_checker_3 = ft.Row(
    [
        ft.ElevatedButton(
            text="Выбрать JSON",
            icon=ft.icons.FILE_OPEN,
            on_click=lambda _: tickets_balance_checker_buttons_3["open_json_button"].pick_files(
                allow_multiple=False,
                allowed_extensions=["json"]
            ),
        ),
        tickets_balance_checker_buttons_3["selected_files"]
    ]
)
