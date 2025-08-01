import flet as ft
from flet import *
from buttons import (PageManager, get_profile_buttons, update_tags_11_buttons, update_tags_10_buttons,
                                    update_tags_9_buttons, update_tags_3_buttons, no_hint_buttons,
                                    collection_gacha_tags_buttons, weapon_lto_buttons, shiny_buttons, theo_buttons,
                                    lto_oto_gc_buttons, among_buttons, labyrinth_buttons, bogo_buttons,
                                    tickets_bans_11_buttons, choose_json_button_11, tickets_bans_10_buttons,
                                    choose_json_button_10, tickets_bans_9_buttons, choose_json_button_9,
                                    tickets_bans_3_buttons, choose_json_button_3, tickets_criteria_buttons,
                                    choose_json_button_tickets_criteria, no_hint_bans_buttons,
                                    choose_json_button_no_hint, no_hint_balance_buttons,
                                    choose_json_button_no_hint_balance, bcp_previous_buttons,
                                    choose_json_button_bcp_previous, bcp_actual_buttons, choose_json_button_bcp_actual,
                                    cgp_6_buttons, choose_json_button_cgp_6, cgp_9_buttons, choose_json_button_cgp_9,
                                    other_bans_wo_field_buttons, choose_json_button_other_wo_field,
                                    other_bans_with_field_buttons, choose_json_button_with_field, new_shiny_buttons,
                                    new_among_buttons, my_tags_buttons, comeback_buttons, manual_tags_buttons,
                                    oto_2_buttons, choose_json_button_oto_2, json_compare_buttons_1,
                                    json_compare_buttons_2, choose_json_compare_button, among_balance_new_tc_buttons,
                                    choose_json_button_among_balance_new_ts, among_balance_average_buttons,
                                    choose_json_button_among_balance_average, labyrinth_balance_ww_buttons,
                                    choose_json_button_labyrinth_balance_ww, labyrinth_balance_cn_buttons,
                                    choose_json_button_labyrinth_balance_cn, tickets_balance_checker_buttons_11,
                                    choose_json_button_tickets_balance_checker_11, tickets_balance_checker_buttons_10,
                                    choose_json_button_tickets_balance_checker_10, tickets_balance_checker_buttons_9,
                                    choose_json_button_tickets_balance_checker_9, tickets_balance_checker_buttons_3,
                                    choose_json_button_tickets_balance_checker_3,
                                    tickets_balance_checker_buttons_10_extra,
                                    choose_json_button_tickets_balance_checker_10_extra,
                                    update_tags_7_buttons, tickets_bans_7_buttons, tickets_balance_checker_buttons_7,
                                    choose_json_button_7, choose_json_button_tickets_balance_checker_7,
                                    update_tags_10_buttons_raskat, tickets_bans_10_buttons_raskat,
                                    choose_json_button_10_raskat)


def boss_page(page: ft.Page):
    PageManager.set_page(page)

    page.title = "OFFERS TOOL"

    # Подвкладка UPDATE TAGS 11
    update_tags_11_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=update_tags_11_buttons["update_tags_11_1"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_2"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_3"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_4"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_5"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_6"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_7"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_8"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_9"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_10"]
                ),
                Container(
                    content=update_tags_11_buttons["update_tags_11_11"]
                )
            ]
        )
    )

    # Подвкладка UPDATE TAGS 10
    update_tags_10_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=update_tags_10_buttons["update_tags_10_1"]
                ),
                Container(
                    content=update_tags_10_buttons["update_tags_10_2"]
                ),
                Container(
                    content=update_tags_10_buttons["update_tags_10_3"]
                ),
                Container(
                    content=update_tags_10_buttons["update_tags_10_4"]
                ),
                Container(
                    content=update_tags_10_buttons["update_tags_10_5"]
                ),
                Container(
                    content=update_tags_10_buttons["update_tags_10_6"]
                ),
                Container(
                    content=update_tags_10_buttons["update_tags_10_7"]
                ),
                Container(
                    content=update_tags_10_buttons["update_tags_10_8"]
                ),
                Container(
                    content=update_tags_10_buttons["update_tags_10_9"]
                ),
                Container(
                    content=update_tags_10_buttons["update_tags_10_10"]
                )
            ]
        )
    )

    # Подвкладка UPDATE TAGS 10 RASKAT
    update_tags_10_content_raskat = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_1"]
                ),
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_2"]
                ),
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_3"]
                ),
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_4"]
                ),
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_5"]
                ),
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_6"]
                ),
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_7"]
                ),
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_8"]
                ),
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_9"]
                ),
                Container(
                    content=update_tags_10_buttons_raskat["update_tags_10_10"]
                )
            ]
        )
    )

    # Подвкладка UPDATE TAGS 9
    update_tags_9_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=update_tags_9_buttons["update_tags_9_1"]
                ),
                Container(
                    content=update_tags_9_buttons["update_tags_9_2"]
                ),
                Container(
                    content=update_tags_9_buttons["update_tags_9_3"]
                ),
                Container(
                    content=update_tags_9_buttons["update_tags_9_4"]
                ),
                Container(
                    content=update_tags_9_buttons["update_tags_9_5"]
                ),
                Container(
                    content=update_tags_9_buttons["update_tags_9_6"]
                ),
                Container(
                    content=update_tags_9_buttons["update_tags_9_7"]
                ),
                Container(
                    content=update_tags_9_buttons["update_tags_9_8"]
                ),
                Container(
                    content=update_tags_9_buttons["update_tags_9_9"]
                )
            ]
        )
    )

    # Подвкладка UPDATE TAGS 7
    update_tags_7_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=update_tags_7_buttons["update_tags_7_1"]
                ),
                Container(
                    content=update_tags_7_buttons["update_tags_7_2"]
                ),
                Container(
                    content=update_tags_7_buttons["update_tags_7_3"]
                ),
                Container(
                    content=update_tags_7_buttons["update_tags_7_4"]
                ),
                Container(
                    content=update_tags_7_buttons["update_tags_7_5"]
                ),
                Container(
                    content=update_tags_7_buttons["update_tags_7_6"]
                ),
                Container(
                    content=update_tags_7_buttons["update_tags_7_7"]
                )
            ]
        )
    )

    # Подвкладка UPDATE TAGS 3
    update_tags_3_content = Container(
        content=Column(
            controls=[
                Container(
                    content=update_tags_3_buttons["update_tags_3_1"]
                ),
                Container(
                    content=update_tags_3_buttons["update_tags_3_2"]
                ),
                Container(
                    content=update_tags_3_buttons["update_tags_3_3"]
                )
            ]
        )
    )

    # Подвкладка TICKETS BANS 11
    tickets_bans_11_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["reset_button_11"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_bans_11_buttons["open_json_button_11"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_11,
                                             tickets_bans_11_buttons["selected_files_11"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["upload_json_button_11"],
                                             tickets_bans_11_buttons["check_all_bans_button_11"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_1"],
                                             tickets_bans_11_buttons['ban_11_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_2"],
                                             tickets_bans_11_buttons['ban_11_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_3"],
                                             tickets_bans_11_buttons['ban_11_14']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_4"],
                                             tickets_bans_11_buttons['ban_11_15']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_5"],
                                             tickets_bans_11_buttons['ban_11_16']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_6"],
                                             tickets_bans_11_buttons['ban_11_17']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_7"],
                                             tickets_bans_11_buttons['ban_11_18']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_8"],
                                             tickets_bans_11_buttons['ban_11_19']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_9"],
                                             tickets_bans_11_buttons['ban_11_20']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_10"],
                                             tickets_bans_11_buttons['ban_11_21']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_11_buttons["ban_11_11"],
                                             tickets_bans_11_buttons['ban_11_22']])
                ),
                tickets_bans_11_buttons['errors']
            ]
        )
    )

    # Подвкладка TICKETS BANS 10
    tickets_bans_10_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["reset_button_10"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["open_json_button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_10, tickets_bans_10_buttons["selected_files_10"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["upload_json_button_10"],
                                             tickets_bans_10_buttons["check_all_bans_button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_1"],
                                             tickets_bans_10_buttons['ban_10_11']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_2"],
                                             tickets_bans_10_buttons['ban_10_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_3"],
                                             tickets_bans_10_buttons['ban_10_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_4"],
                                             tickets_bans_10_buttons['ban_10_14']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_5"],
                                             tickets_bans_10_buttons['ban_10_15']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_6"],
                                             tickets_bans_10_buttons['ban_10_16']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_7"],
                                             tickets_bans_10_buttons['ban_10_17']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_8"],
                                             tickets_bans_10_buttons['ban_10_18']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_9"],
                                             tickets_bans_10_buttons['ban_10_19']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons["ban_10_10"],
                                             tickets_bans_10_buttons['ban_10_20']])
                ),
                tickets_bans_10_buttons['errors']
            ]
        )
    )

    # Подвкладка TICKETS BANS 10 RASKAT
    tickets_bans_10_content_raskat = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["reset_button_10"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["open_json_button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_10_raskat, tickets_bans_10_buttons_raskat["selected_files_10"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["upload_json_button_10"],
                                             tickets_bans_10_buttons_raskat["check_all_bans_button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_1"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_11']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_2"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_3"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_4"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_14']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_5"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_15']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_6"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_16']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_7"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_17']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_8"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_18']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_9"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_19']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_10_buttons_raskat["ban_10_raskat_10"],
                                             tickets_bans_10_buttons_raskat['ban_10_raskat_20']])
                ),
                tickets_bans_10_buttons_raskat['errors']
            ]
        )
    )

    # Подвкладка TICKETS BANS 9
    tickets_bans_9_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_bans_9_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_9, tickets_bans_9_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["upload_json_button"],
                                             tickets_bans_9_buttons["check_all_bans_button"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["ban_9_1"],
                                             tickets_bans_9_buttons['ban_9_10']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["ban_9_2"],
                                             tickets_bans_9_buttons['ban_9_11']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["ban_9_3"],
                                             tickets_bans_9_buttons['ban_9_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["ban_9_4"],
                                             tickets_bans_9_buttons['ban_9_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["ban_9_5"],
                                             tickets_bans_9_buttons['ban_9_14']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["ban_9_6"],
                                             tickets_bans_9_buttons['ban_9_15']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["ban_9_7"],
                                             tickets_bans_9_buttons['ban_9_16']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["ban_9_8"],
                                             tickets_bans_9_buttons['ban_9_17']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_9_buttons["ban_9_9"],
                                             tickets_bans_9_buttons['ban_9_18']])
                ),
                tickets_bans_9_buttons['errors']
            ]
        )
    )

    # Подвкладка TICKETS BANS 7
    tickets_bans_7_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_bans_7_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_bans_7_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_7, tickets_bans_7_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_7_buttons["upload_json_button"],
                                             tickets_bans_7_buttons["check_all_bans_button"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_7_buttons["ban_7_1"],
                                             tickets_bans_7_buttons['ban_7_8']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_7_buttons["ban_7_2"],
                                             tickets_bans_7_buttons['ban_7_9']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_7_buttons["ban_7_3"],
                                             tickets_bans_7_buttons['ban_7_10']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_7_buttons["ban_7_4"],
                                             tickets_bans_7_buttons['ban_7_11']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_7_buttons["ban_7_5"],
                                             tickets_bans_7_buttons['ban_7_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_7_buttons["ban_7_6"],
                                             tickets_bans_7_buttons['ban_7_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_7_buttons["ban_7_7"],
                                             tickets_bans_7_buttons['ban_7_14']])
                ),
                tickets_bans_7_buttons['errors']
            ]
        )
    )

    # Подвкладка TICKETS BANS 3
    tickets_bans_3_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_bans_3_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_bans_3_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_3, tickets_bans_3_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_3_buttons["upload_json_button"],
                                             tickets_bans_3_buttons["check_all_bans_button"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_3_buttons["ban_3_1"],
                                             tickets_bans_3_buttons['ban_3_4']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_3_buttons["ban_3_2"],
                                             tickets_bans_3_buttons['ban_3_5']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_bans_3_buttons["ban_3_3"],
                                             tickets_bans_3_buttons['ban_3_6']])
                ),
                tickets_bans_3_buttons['errors']
            ]
        )
    )

    # Подвкладка OTO2
    oto_2_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[oto_2_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=oto_2_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_oto_2,
                                             oto_2_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["upload_json_button"],
                                             oto_2_buttons["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_1"],
                                             oto_2_buttons["input_denies_field"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_2"],
                                             oto_2_buttons["input_allows_field"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_7"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_8"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_9"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[oto_2_buttons["button_11"]])
                )
            ]
        )
    )

    # Подвкладка COMPARE
    compare_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[json_compare_buttons_2["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=ft.Row(controls=[choose_json_compare_button,
                                             json_compare_buttons_1["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1['open_json_button']])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["upload_json_button"],
                                             json_compare_buttons_2["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_1"],
                                             json_compare_buttons_2["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_2"],
                                             json_compare_buttons_2["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_3"],
                                             json_compare_buttons_2["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_4"],
                                             json_compare_buttons_2["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_5"],
                                             json_compare_buttons_2["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_6"],
                                             json_compare_buttons_2["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_7"],
                                             json_compare_buttons_2["button_7"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_8"],
                                             json_compare_buttons_2["button_8"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_9"],
                                             json_compare_buttons_2["button_9"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_10"],
                                             json_compare_buttons_2["button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_11"],
                                             json_compare_buttons_2["button_11"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_12"],
                                             json_compare_buttons_2["button_12"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_13"],
                                             json_compare_buttons_2["button_13"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_14"],
                                             json_compare_buttons_2["button_14"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_15"],
                                             json_compare_buttons_2["button_15"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_16"],
                                             json_compare_buttons_2["button_16"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_17"],
                                             json_compare_buttons_2["button_17"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_18"],
                                             json_compare_buttons_2["button_18"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_19"],
                                             json_compare_buttons_2["button_19"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_20"],
                                             json_compare_buttons_2["button_20"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_21"],
                                             json_compare_buttons_2["button_21"]])
                ),
                Container(
                    content=ft.Row(controls=[json_compare_buttons_1["button_22"],
                                             json_compare_buttons_2["button_22"]])
                )
            ]
        )
    )

    # Подвкладка TICKETS CRITERIA
    tickets_criteria_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_criteria_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_tickets_criteria,
                                             tickets_criteria_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["upload_json_button"],
                                             tickets_criteria_buttons["check_all_criteria_button"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_7"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_8"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_9"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_11"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_12"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_13"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_14"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_15"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_16"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_17"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_18"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_19"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_20"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_21"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_criteria_buttons["button_22"]])
                )
            ]
        )
    )

    # Подвкладка TICKETS BALANCE CHECKER 11
    tickets_balance_checker_content_11 = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_balance_checker_buttons_11["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_tickets_balance_checker_11,
                                             tickets_balance_checker_buttons_11["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["upload_json_button"],
                                             tickets_balance_checker_buttons_11["day"],
                                             tickets_balance_checker_buttons_11["check_all"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_1"],
                                             tickets_balance_checker_buttons_11['button_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_2"],
                                             tickets_balance_checker_buttons_11['button_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_3"],
                                             tickets_balance_checker_buttons_11['button_14']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_4"],
                                             tickets_balance_checker_buttons_11['button_15']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_5"],
                                             tickets_balance_checker_buttons_11['button_16']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_6"],
                                             tickets_balance_checker_buttons_11['button_17']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_7"],
                                             tickets_balance_checker_buttons_11['button_18']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_8"],
                                             tickets_balance_checker_buttons_11['button_19']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_9"],
                                             tickets_balance_checker_buttons_11['button_20']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_10"],
                                             tickets_balance_checker_buttons_11['button_21']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_11["button_11"],
                                             tickets_balance_checker_buttons_11['button_22']])
                ),
                tickets_balance_checker_buttons_11['errors']
            ]
        )
    )

    # Подвкладка TICKETS BALANCE CHECKER 10 19+ LVL
    tickets_balance_checker_content_10 = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_balance_checker_buttons_10["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_tickets_balance_checker_10,
                                             tickets_balance_checker_buttons_10["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["upload_json_button"],
                                             tickets_balance_checker_buttons_10['day'],
                                             tickets_balance_checker_buttons_10["check_all"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_1"],
                                             tickets_balance_checker_buttons_10['button_11']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_2"],
                                             tickets_balance_checker_buttons_10['button_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_3"],
                                             tickets_balance_checker_buttons_10['button_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_4"],
                                             tickets_balance_checker_buttons_10['button_14']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_5"],
                                             tickets_balance_checker_buttons_10['button_15']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_6"],
                                             tickets_balance_checker_buttons_10['button_16']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_7"],
                                             tickets_balance_checker_buttons_10['button_17']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_8"],
                                             tickets_balance_checker_buttons_10['button_18']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_9"],
                                             tickets_balance_checker_buttons_10['button_19']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10["button_10"],
                                             tickets_balance_checker_buttons_10['button_20']])
                ),
                tickets_balance_checker_buttons_10['errors']
            ]
        )
    )

    # Подвкладка TICKETS BALANCE CHECKER 10 7-18 LVL
    tickets_balance_checker_content_10_extra = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_balance_checker_buttons_10_extra["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_tickets_balance_checker_10_extra,
                                             tickets_balance_checker_buttons_10_extra["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["upload_json_button"],
                                             tickets_balance_checker_buttons_10_extra['day'],
                                             tickets_balance_checker_buttons_10_extra["check_all"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_1"],
                                             tickets_balance_checker_buttons_10_extra['button_11']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_2"],
                                             tickets_balance_checker_buttons_10_extra['button_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_3"],
                                             tickets_balance_checker_buttons_10_extra['button_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_4"],
                                             tickets_balance_checker_buttons_10_extra['button_14']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_5"],
                                             tickets_balance_checker_buttons_10_extra['button_15']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_6"],
                                             tickets_balance_checker_buttons_10_extra['button_16']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_7"],
                                             tickets_balance_checker_buttons_10_extra['button_17']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_8"],
                                             tickets_balance_checker_buttons_10_extra['button_18']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_9"],
                                             tickets_balance_checker_buttons_10_extra['button_19']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_10_extra["button_10"],
                                             tickets_balance_checker_buttons_10_extra['button_20']])
                ),
                tickets_balance_checker_buttons_10_extra['errors']
            ]
        )
    )

    # Подвкладка TICKETS BALANCE CHECKER 9
    tickets_balance_checker_content_9 = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_balance_checker_buttons_9["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_tickets_balance_checker_9,
                                             tickets_balance_checker_buttons_9["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["upload_json_button"],
                                             tickets_balance_checker_buttons_9['day'],
                                             tickets_balance_checker_buttons_9["check_all"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["button_1"],
                                             tickets_balance_checker_buttons_9['button_10']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["button_2"],
                                             tickets_balance_checker_buttons_9['button_11']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["button_3"],
                                             tickets_balance_checker_buttons_9['button_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["button_4"],
                                             tickets_balance_checker_buttons_9['button_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["button_5"],
                                             tickets_balance_checker_buttons_9['button_14']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["button_6"],
                                             tickets_balance_checker_buttons_9['button_15']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["button_7"],
                                             tickets_balance_checker_buttons_9['button_16']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["button_8"],
                                             tickets_balance_checker_buttons_9['button_17']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_9["button_9"],
                                             tickets_balance_checker_buttons_9['button_18']])
                ),
                tickets_balance_checker_buttons_9['errors']
            ]
        )
    )

    # Подвкладка TICKETS BALANCE CHECKER 7
    tickets_balance_checker_content_7 = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_7["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_balance_checker_buttons_7["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_tickets_balance_checker_7,
                                             tickets_balance_checker_buttons_7["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_7["upload_json_button"],
                                             tickets_balance_checker_buttons_7['day'],
                                             tickets_balance_checker_buttons_7["check_all"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_7["button_1"],
                                             tickets_balance_checker_buttons_7['button_8']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_7["button_2"],
                                             tickets_balance_checker_buttons_7['button_9']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_7["button_3"],
                                             tickets_balance_checker_buttons_7['button_10']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_7["button_4"],
                                             tickets_balance_checker_buttons_7['button_11']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_7["button_5"],
                                             tickets_balance_checker_buttons_7['button_12']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_7["button_6"],
                                             tickets_balance_checker_buttons_7['button_13']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_7["button_7"],
                                             tickets_balance_checker_buttons_7['button_14']])
                ),
                tickets_balance_checker_buttons_7['errors']
            ]
        )
    )

    # Подвкладка TICKETS BALANCE CHECKER 3
    tickets_balance_checker_content_3 = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_3["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=tickets_balance_checker_buttons_3["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_tickets_balance_checker_3,
                                             tickets_balance_checker_buttons_3["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_3["upload_json_button"],
                                             tickets_balance_checker_buttons_3['day'],
                                             tickets_balance_checker_buttons_3["check_all"]])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_3["button_1"],
                                             tickets_balance_checker_buttons_3['button_4']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_3["button_2"],
                                             tickets_balance_checker_buttons_3['button_5']])
                ),
                Container(
                    content=ft.Row(controls=[tickets_balance_checker_buttons_3["button_3"],
                                             tickets_balance_checker_buttons_3['button_6']])
                ),
                tickets_balance_checker_buttons_3['errors']
            ]
        )
    )


    # Вкладка 11
    tab_11 = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text='tags',
                icon=ft.icons.UPDATE,
                content=update_tags_11_content
            ),
            ft.Tab(
                text='bans, denies',
                icon=ft.icons.COMPARE,
                content=tickets_bans_11_content
            ),
            ft.Tab(
                text='balance',
                icon=ft.icons.CHECK,
                content=tickets_balance_checker_content_11
            )
        ],
        expand=1
    )

    # Вкладка 10
    tab_10 = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text='tags',
                icon=ft.icons.UPDATE,
                content=update_tags_10_content
            ),
            ft.Tab(
                text='tags raskat',
                icon=ft.icons.UPDATE,
                content=update_tags_10_content_raskat
            ),
            ft.Tab(
                text='bans, denies 19+ lvl',
                icon=ft.icons.COMPARE,
                content=tickets_bans_10_content
            ),
            ft.Tab(
                text='balance 19+ lvl',
                icon=ft.icons.CHECK,
                content=tickets_balance_checker_content_10
            ),
            ft.Tab(
                text='bans, denies 7-18 lvl',
                icon=ft.icons.COMPARE,
                content=tickets_bans_10_content_raskat
            ),
            ft.Tab(
                text='balance 7-18 lvl',
                icon=ft.icons.CHECK,
                content=tickets_balance_checker_content_10_extra
            )
        ],
        expand=1
    )

    # Вкладка 9
    tab_9 = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text='tags',
                icon=ft.icons.UPDATE,
                content=update_tags_9_content
            ),
            ft.Tab(
                text='bans, denies',
                icon=ft.icons.COMPARE,
                content=tickets_bans_9_content
            ),
            ft.Tab(
                text='balance',
                icon=ft.icons.CHECK,
                content=tickets_balance_checker_content_9
            )
        ],
        expand=1
    )

    # Вкладка 3
    tab_3 = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text='tags',
                icon=ft.icons.UPDATE,
                content=update_tags_3_content
            ),
            ft.Tab(
                text='bans, denies',
                icon=ft.icons.COMPARE,
                content=tickets_bans_3_content
            ),
            ft.Tab(
                text='balance',
                icon=ft.icons.CHECK,
                content=tickets_balance_checker_content_3
            )
        ],
        expand=1
    )

    # Вкладка B
    tab_b = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text='tags',
                icon=ft.icons.UPDATE,
                content=update_tags_7_content
            ),
            ft.Tab(
                text='bans, denies',
                icon=ft.icons.COMPARE,
                content=tickets_bans_7_content
            ),
            ft.Tab(
                text='balance',
                icon=ft.icons.CHECK,
                content=tickets_balance_checker_content_7
            )
        ],
        expand=1
    )

    # Вкладка PROFILE TAGS
    tab_profile_tags = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="11",
                icon=ft.icons.ELEVEN_MP,
                content=tab_11
            ),
            ft.Tab(
                text="10",
                icon=ft.icons.TEN_MP,
                content=tab_10
            ),
            ft.Tab(
                text="9",
                icon=ft.icons.NINE_MP,
                content=tab_9
            ),
            ft.Tab(
                text="3",
                icon=ft.icons.THREE_MP,
                content=tab_3
            ),
            ft.Tab(
                text="notIn РФ/РБ" + "\n" + "и в GP/iOS РФ, iOS РБ criteria",
                icon=ft.icons.ADMIN_PANEL_SETTINGS,
                content=tickets_criteria_content
            ),
            ft.Tab(
                text="OTO 2",
                icon=ft.icons.LIBRARY_ADD,
                content=oto_2_content
            ),
            ft.Tab(
                text="COMPARE",
                icon=ft.icons.COMPARE,
                content=compare_content
            ),
            ft.Tab(
                text='GROUP B',
                icon=ft.icons.ABC,
                content=tab_b
            )
        ],
        expand=1
    )

    # Подвкладка NO HINT TAGS
    no_hint_content = Container(
        content=Column(
            controls=[
                Container(
                    content=no_hint_buttons["no_hint_1"]
                ),
                Container(
                    content=no_hint_buttons["no_hint_2"]
                ),
                Container(
                    content=no_hint_buttons["no_hint_3"]
                ),
                Container(
                    content=no_hint_buttons["no_hint_4"]
                )
            ]
        )
    )

    # Подвкладка NO HINT BANS
    no_hint_bans_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=no_hint_bans_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_no_hint,
                                             no_hint_bans_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["upload_json_button"],
                                             no_hint_bans_buttons["check_all_bans_button"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_7"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_8"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_9"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_11"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_12"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_13"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_14"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_15"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_bans_buttons["button_16"]])
                )
            ]
        )
    )

    # Подвкладка NO HINT BALANCE
    no_hint_balance_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["description"]],
                                   alignment=ft.MainAxisAlignment.CENTER)
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=no_hint_balance_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_no_hint_balance,
                                             no_hint_balance_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["upload_json_button"],
                                             no_hint_balance_buttons["check_all_balance_button"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_7"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_8"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_9"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_11"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_12"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_13"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_14"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_15"]])
                ),
                Container(
                    content=ft.Row(controls=[no_hint_balance_buttons["button_16"]])
                )
            ]
        )
    )

    # Вкладка NO HINT
    tab_no_hint = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="NO HINT",
                icon=ft.icons.NO_CELL,
                content=no_hint_content
            ),
            ft.Tab(
                text="NO HINT BANS",
                icon=ft.icons.COMPARE,
                content=no_hint_bans_content
            ),
            ft.Tab(
                text="NO HINT BALANCE",
                icon=ft.icons.BALANCE,
                content=no_hint_balance_content
            )
        ],
        expand=1
    )

    # Подкладка CGP TAGS
    collection_gacha_content = Container(
        content=Column(
            controls=[
                Container(
                    content=collection_gacha_tags_buttons["collection_gacha_1"]
                ),
                Container(
                    content=collection_gacha_tags_buttons["collection_gacha_2"]
                )
            ]
        )
    )

    # Подкладка BCP JSON PREVIOUS
    bcp_content_previous = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["description"]],
                                   alignment=ft.MainAxisAlignment.CENTER)
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=bcp_previous_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_bcp_previous,
                                             bcp_previous_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["upload_json_button"],
                                             bcp_previous_buttons["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["button_7"],
                                             bcp_previous_buttons['dynamic_items_1']])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["button_8"],
                                             bcp_previous_buttons['dynamic_items_2']])
                ),
                Container(
                    content=ft.Row(controls=[bcp_previous_buttons["button_9"],
                                             bcp_previous_buttons['dynamic_items_3']])
                )
            ]
        )
    )

    # Подкладка BCP JSON ACTUAL
    bcp_content_actual = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["description"]],
                                   alignment=ft.MainAxisAlignment.CENTER)
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=bcp_actual_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_bcp_actual,
                                             bcp_actual_buttons["selected_files"]]),
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["skin_id_field"],
                                             bcp_actual_buttons["day"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["upload_json_button"],
                                             bcp_actual_buttons["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["button_7"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["button_8"]])
                ),
                Container(
                    content=ft.Row(controls=[bcp_actual_buttons["button_9"]])
                )
            ]
        )
    )

    # Подкладка CGP JSON 9
    cgp_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["description"]],
                                   alignment=ft.MainAxisAlignment.CENTER)
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=cgp_9_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_cgp_9,
                                             cgp_9_buttons["selected_files"]]),
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["upload_json_button"],
                                             cgp_9_buttons["day"],
                                             cgp_9_buttons["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["button_7"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["button_8"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_9_buttons["button_9"]])
                )
            ]
        )
    )

    # Подкладка CGP JSON 6
    cgp_content_6 = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[cgp_6_buttons["description"]],
                                   alignment=ft.MainAxisAlignment.CENTER)
                ),
                Container(
                    content=ft.Row(controls=[cgp_6_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=cgp_6_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_cgp_6,
                                             cgp_6_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_6_buttons["upload_json_button"],
                                             cgp_6_buttons['day'],
                                             cgp_6_buttons["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_6_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_6_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_6_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_6_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_6_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[cgp_6_buttons["button_6"]])
                )
            ]
        )
    )

    # Вкладка BCP/CGP

    tab_bcp_cgp = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="CGP TAGS",
                icon=ft.icons.UPDATE,
                content=collection_gacha_content
            ),
            ft.Tab(
                text="BCP" + "\n" + "PREVIOUS",
                icon=ft.icons.CONTENT_COPY,
                content=bcp_content_previous
            ),
            ft.Tab(
                text="BCP" + "\n" + "ACTUAL",
                icon=ft.icons.CONTENT_PASTE,
                content=bcp_content_actual
            ),
            ft.Tab(
                text="CGP 6",
                icon=ft.icons.CONTENT_COPY,
                content=cgp_content_6
            ),
            ft.Tab(
                text="CGP 9",
                icon=ft.icons.CONTENT_PASTE,
                content=cgp_content
            )
        ],
        expand=1
    )

    # Вкладка WEAPON LTO
    weapon_lto_content = Container(
        content=Column(
            controls=[
                Container(
                    content=weapon_lto_buttons["weapon_lto_1"]
                ),
                Container(
                    content=weapon_lto_buttons["weapon_lto_2"]
                ),
                Container(
                    content=weapon_lto_buttons["weapon_lto_3"]
                ),
                Container(
                    content=weapon_lto_buttons["weapon_lto_4"]
                )
            ]
        )
    )

    # Подвкладка SHINY
    shiny_content = Container(
        content=Column(
            controls=[
                Container(
                    content=shiny_buttons["shiny_1"]
                ),
                Container(
                    content=shiny_buttons["shiny_2"]
                ),
                Container(
                    content=shiny_buttons["shiny_3"]
                ),
                Container(
                    content=shiny_buttons["shiny_4"]
                ),
                Container(
                    content=shiny_buttons["shiny_5"]
                )
            ]
        )
    )

    # Подвкладка NEW SHINY
    new_shiny_content = Container(
        content=Column(
            controls=[
                Container(
                    content=new_shiny_buttons["shiny_1"]
                ),
                Container(
                    content=new_shiny_buttons["shiny_2"]
                ),
                Container(
                    content=new_shiny_buttons["shiny_3"]
                ),
                Container(
                    content=new_shiny_buttons["shiny_4"]
                ),
                Container(
                    content=new_shiny_buttons["shiny_5"]
                )
            ]
        )
    )

    # Подвкладка THEO
    theo_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=theo_buttons["theo_1"]
                ),
                Container(
                    content=theo_buttons["theo_2"]
                ),
                Container(
                    content=theo_buttons["theo_3"]
                ),
                Container(
                    content=theo_buttons["theo_4"]
                ),
                Container(
                    content=theo_buttons["theo_5"]
                ),
                Container(
                    content=theo_buttons["theo_6"]
                ),
                Container(
                    content=theo_buttons["theo_7"]
                )
            ]
        )
    )

    # Вкладка PIGGY BANK
    tab_piggy = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="SHINY totalSpent28",
                content=shiny_content
            ),
            ft.Tab(
                text="SHINY new_totalSpent28",
                content=new_shiny_content
            ),
            ft.Tab(
                text="THEO",
                content=theo_content
            )
        ],
        expand=1
    )

    # Вкладка LTO_OTO_GC
    lto_oto_gc_content = Container(
        content=Column(
            controls=[
                Container(
                    content=lto_oto_gc_buttons["lto_oto_gc_1"]
                ),
                Container(
                    content=lto_oto_gc_buttons["lto_oto_gc_2"]
                ),
                Container(
                    content=lto_oto_gc_buttons["lto_oto_gc_3"]
                ),
                Container(
                    content=lto_oto_gc_buttons["lto_oto_gc_4"]
                )
            ]
        )
    )

    # Подвкладка AMONG NEW TS TAGS
    among_new_ts_tags = Container(
        content=Column(
            controls=[
                Container(
                    content=among_buttons["among_1"]
                ),
                Container(
                    content=among_buttons["among_2"]
                ),
                Container(
                    content=among_buttons["among_3"]
                )
            ]
        )
    )

    # Подкладка AMONG NEW TS BALANCE
    among_new_ts_balance = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[among_balance_new_tc_buttons['description']],
                                   alignment=ft.MainAxisAlignment.CENTER)
                ),
                Container(
                    content=ft.Row(controls=[among_balance_new_tc_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=among_balance_new_tc_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_among_balance_new_ts,
                                             among_balance_new_tc_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[among_balance_new_tc_buttons["upload_json_button"],
                                             among_balance_new_tc_buttons["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[among_balance_new_tc_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[among_balance_new_tc_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[among_balance_new_tc_buttons["button_3"]])
                )
            ]
        )
    )

    # ПОДВКЛАДКА AMONG NEW TS TAGS AND BALANCE

    tab_among_1 = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="TAGS",
                content=among_new_ts_tags
            ),
            ft.Tab(
                text="JSON CHECK",
                content=among_new_ts_balance
            )
        ],
        expand=1
    )

    # Подкладка AMONG AVERAGE BALANCE
    among_average_balance = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[among_balance_average_buttons['description']],
                                   alignment=ft.MainAxisAlignment.CENTER)
                ),
                Container(
                    content=ft.Row(controls=[among_balance_average_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=among_balance_average_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_among_balance_average,
                                             among_balance_average_buttons["selected_files"]])
                ),
                Container(
                    content=among_balance_average_buttons['upload_json_button']
                ),
                Container(
                    content=ft.Row(controls=[among_balance_average_buttons["me_field"],
                                             among_balance_average_buttons["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[among_balance_average_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[among_balance_average_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[among_balance_average_buttons["button_3"]])
                )
            ]
        )
    )

    # Подвкладка AMONG AVERAGE TAGS
    among_average_tags = Container(
        content=Column(
            controls=[
                Container(
                    content=new_among_buttons["among_1"]
                ),
                Container(
                    content=new_among_buttons["among_2"]
                ),
                Container(
                    content=new_among_buttons["among_3"]
                )
            ]
        )
    )

    # ПОДВКЛАДКА AMONG AVERAGE TAGS AND BALANCE

    tab_among_2 = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="TAGS",
                content=among_average_tags
            ),
            ft.Tab(
                text="JSON CHECK",
                content=among_average_balance
            )
        ],
        expand=1
    )

    # Вкладка AMONG
    tab_among = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="new_totalSpent28",
                content=tab_among_1
            ),
            ft.Tab(
                text="average10",
                content=tab_among_2
            )
        ],
        expand=1
    )

    # Подкладка LABYRINTH TAGS
    labyrinth_tags = Container(
        content=Column(
            controls=[
                Container(
                    content=labyrinth_buttons["labyrinth_1"]
                ),
                Container(
                    content=labyrinth_buttons["labyrinth_2"]
                ),
                Container(
                    content=labyrinth_buttons["labyrinth_3"]
                ),
                Container(
                    content=labyrinth_buttons["labyrinth_4"]
                )
            ]
        )
    )

    # Подкладка LABYRINTH BALANCE WW
    labyrinth_balance_ww = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[labyrinth_balance_ww_buttons['description']],
                                   alignment=ft.MainAxisAlignment.CENTER)
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_ww_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=labyrinth_balance_ww_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_labyrinth_balance_ww,
                                             labyrinth_balance_ww_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_ww_buttons['upload_json_button'],
                                             labyrinth_balance_ww_buttons['check_all_button']])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_ww_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_ww_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_ww_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_ww_buttons["button_4"]])
                )
            ]
        )
    )

    # Подкладка LABYRINTH BALANCE CN
    labyrinth_balance_cn = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[labyrinth_balance_cn_buttons['description']],
                                   alignment=ft.MainAxisAlignment.CENTER)
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_cn_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=labyrinth_balance_cn_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_labyrinth_balance_cn,
                                             labyrinth_balance_cn_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_cn_buttons['upload_json_button'],
                                             labyrinth_balance_cn_buttons['check_all_button']])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_cn_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_cn_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_cn_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[labyrinth_balance_cn_buttons["button_4"]])
                )
            ]
        )
    )

    # Вкладка LABYRINTH
    tab_labyrinth = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="tags",
                content=labyrinth_tags
            ),
            ft.Tab(
                text="JSON WW",
                content=labyrinth_balance_ww
            ),
            ft.Tab(
                text='JSON CN',
                content=labyrinth_balance_cn
            )
        ],
        expand=1
    )

    # Вкладка BOGO
    bogo_content = Container(
        content=Column(
            controls=[
                Container(
                    content=bogo_buttons["bogo_1"]
                ),
                Container(
                    content=bogo_buttons["bogo_2"]
                ),
                Container(
                    content=bogo_buttons["bogo_3"]
                ),
                Container(
                    content=bogo_buttons["bogo_4"]
                )
            ]
        )
    )

    # Вкладка COMEBACK
    comeback_content = Container(
        content=Column(
            controls=[
                Container(
                    content=comeback_buttons["comeback_1"]
                ),
                Container(
                    content=comeback_buttons["comeback_2"]
                ),
                Container(
                    content=comeback_buttons["comeback_3"]
                ),
                Container(
                    content=comeback_buttons["comeback_4"]
                )
            ]
        )
    )

    # Подвкладка OTHER BANS WO FIELD
    other_wo_field_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=other_bans_wo_field_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_other_wo_field,
                                             other_bans_wo_field_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["upload_json_button"],
                                             other_bans_wo_field_buttons["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_1"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_7"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_8"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_9"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_wo_field_buttons["button_11"]])
                )
            ]
        )
    )

    # Подвкладка OTHER BANS WITH FIELD
    other_with_field_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["reset_button"]],
                                   alignment=ft.MainAxisAlignment.END)
                ),
                Container(
                    content=other_bans_with_field_buttons["open_json_button"]
                ),
                Container(
                    content=ft.Row(controls=[choose_json_button_with_field,
                                             other_bans_with_field_buttons["selected_files"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["upload_json_button"],
                                             other_bans_with_field_buttons["check_all_button"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_1"],
                                             other_bans_with_field_buttons["input_bans_field"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_2"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_3"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_4"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_5"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_6"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_7"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_8"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_9"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_10"]])
                ),
                Container(
                    content=ft.Row(controls=[other_bans_with_field_buttons["button_11"]])
                )
            ]
        )
    )

    # Вкладка OTHER BANS

    tab_bans = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="W/O FIELD",
                icon=ft.icons.CONNECT_WITHOUT_CONTACT,
                content=other_wo_field_content
            ),
            ft.Tab(
                text="WITH FIELD",
                icon=ft.icons.TEXT_FIELDS,
                content=other_with_field_content
            )
        ],
        expand=1
    )

    my_tags_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=my_tags_buttons["my_tags"]
                ),
                Container(
                    content=my_tags_buttons["tags_field"]
                )
            ]
        )
    )

    manual_tags_content = Container(
        content=Column(
            scroll=True,
            controls=[
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_1"],
                                             manual_tags_buttons["some_tag_1"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_2"],
                                             manual_tags_buttons["some_tag_2"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_3"],
                                             manual_tags_buttons["some_tag_3"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_4"],
                                             manual_tags_buttons["some_tag_4"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_5"],
                                             manual_tags_buttons["some_tag_5"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_6"],
                                             manual_tags_buttons["some_tag_6"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_7"],
                                             manual_tags_buttons["some_tag_7"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_8"],
                                             manual_tags_buttons["some_tag_8"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_9"],
                                             manual_tags_buttons["some_tag_9"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_10"],
                                             manual_tags_buttons["some_tag_10"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_11"],
                                             manual_tags_buttons["some_tag_11"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_12"],
                                             manual_tags_buttons["some_tag_12"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_13"],
                                             manual_tags_buttons["some_tag_13"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_14"],
                                             manual_tags_buttons["some_tag_14"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_15"],
                                             manual_tags_buttons["some_tag_15"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_16"],
                                             manual_tags_buttons["some_tag_16"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_17"],
                                             manual_tags_buttons["some_tag_17"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_18"],
                                             manual_tags_buttons["some_tag_18"]])
                ),
                Container(
                    content=ft.Row(controls=[manual_tags_buttons["some_tag_text_19"],
                                             manual_tags_buttons["some_tag_19"]])
                ),
                Container(
                    content=manual_tags_buttons["submit"]
                )
            ]
        )
    )

    tags_tab = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="MY TAGS",
                icon=ft.icons.TAG,
                content=my_tags_content
            ),
            ft.Tab(
                text="MANUAL TAGS",
                icon=ft.icons.FIBER_MANUAL_RECORD_SHARP,
                content=manual_tags_content
            )
        ],
        expand=1
    )

    # Основное окно
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="EVENT TICKETS",
                icon=ft.icons.AIRPLANE_TICKET,
                content=tab_profile_tags
            ),
            ft.Tab(
                text="NO HINT",
                icon=ft.icons.NO_CELL,
                content=tab_no_hint
            ),
            ft.Tab(
                text="BCP/CGP",
                icon=ft.icons.COLLECTIONS,
                content=tab_bcp_cgp
            ),
            ft.Tab(
                text="Weapon LTO, def" + "\n" + "LTO with pack&joker",
                icon=ft.icons.LOCAL_OFFER,
                content=weapon_lto_content
            ),
            ft.Tab(
                text="PIGGY",
                icon=ft.icons.SHOP,
                content=tab_piggy
            ),
            ft.Tab(
                text="LTO/OTO GC",
                icon=ft.icons.ALBUM,
                content=lto_oto_gc_content
            ),
            ft.Tab(
                text="AMONG",
                icon=ft.icons.CARD_GIFTCARD,
                content=tab_among
            ),
            ft.Tab(
                text="LABYRINTH",
                icon=ft.icons.DIRECTIONS,
                content=tab_labyrinth
            ),
            ft.Tab(
                text="BOGO",
                icon=ft.icons.WALLET,
                content=bogo_content
            ),
            ft.Tab(
                text="COMEBACK",
                icon=ft.icons.BACK_HAND,
                content=comeback_content
            ),
            ft.Tab(
                text="OTHER BANS",
                icon=ft.icons.DEVICES_OTHER,
                content=tab_bans
            ),
            ft.Tab(
                text="TAGS",
                icon=ft.icons.TAG,
                content=tags_tab
            )
        ],
        expand=1
    )
    page.add(get_profile_buttons["get_profile_line"], get_profile_buttons["submit_button"], t)


ft.app(target=boss_page)
