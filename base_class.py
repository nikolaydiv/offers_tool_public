import json
import time
import requests
import flet as ft
import re
import gdown
import copy

file_id_balance = "1SuldKadbX43vbuQTs_5IsIuqoUHLOLKs"
url_balance = f"https://drive.google.com/uc?id={file_id_balance}"  # скачивание json-заглушки 1 (проверка баланса 1)
output_file_balance = "downloaded_balance.json"
gdown.download(url_balance, output_file_balance, quiet=True)
with open(output_file_balance, 'r', encoding='utf-8') as a:
    raw_data = a.read()
clean_content = re.sub(r"//.*", "", raw_data)
data_balance = json.loads(clean_content)

file_id_balance_1 = "1eW3La1zKU7cyPfZnjq-yCVG-gClTInmV"
url_bcp_balance = f"https://drive.google.com/uc?id={file_id_balance_1}"  # скачивание json-заглушки 2 (проверка баланса 2)
output_file_bcp_balance = "bcp_balance.json"
gdown.download(url_bcp_balance, output_file_bcp_balance, quiet=True)
with open(output_file_bcp_balance, 'r', encoding='utf-8') as a:
    raw_data = a.read()
clean_content_bcp = re.sub(r"//.*", "", raw_data)
bcp_balance = json.loads(clean_content_bcp)


class ProfileFetcher:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.support_id = None

    def get_profile(self, entered_support_id):
        url_endpoint = "?isSupportId=true"
        get_url = f"{self.base_url}{entered_support_id}{url_endpoint}"
        response = requests.get(get_url, headers=self.headers)

        if response.status_code == 200:
            get_json = response.json()
            self.support_id = get_json['profile']['_id']
            return True
        else:
            return False

    def update_button_text(self, button, text, duration=3):
        button.text = text
        button.update()
        time.sleep(duration)
        button.text = "SEND"
        button.update()


class TagsUpdater:

    def __init__(self, put_url, headers_put):
        self.put_url = put_url
        self.headers_put = headers_put

    def update_tags_tickets(self, value_1, value_2,
                            value_3):  # здесь и далее будут использоваться json-заглушки с secret_tag_N вместо реального названия тега
        payload = json.dumps({
            profile_fetcher.support_id: {
                "nicknameLowercase": "skip",
                "secret_tag_1": value_1,
                "secret_tag_2": 0.99,
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
                "secret_tag_12": value_2,
                "secret_tag_13": 0.99,
                "secret_tag_14": 0.99,
                "secret_tag_15": 0.99,
                "secret_tag_16": 0.99,
                "secret_tag_17": 0.99,
                "secret_tag_18": 0.99,
                "secret_tag_19": 0.99,
                "secret_tag_20": 0.99,
                "secret_tag_21": 0.99,
                "secret_tag_22": 0.99,
                "secret_tag_23": 1,
                "secret_tag_24": 1,
                "secret_tag_25": 1,
                "secret_tag_26": 0.99,
                "secret_tag_27": 0.99,
                "secret_tag_28": 0.99,
                "secret_tag_29": 0.99,
                "secret_tag_30": 0.99,
                "secret_tag_31": 0.99,
                "secret_tag_32": 0,
                "secret_tag_33": 0.99,
                "secret_tag_34": 0.99,
                "secret_tag_35": 0.99,
                "secret_tag_36": 0,
                "secret_tag_37": 0.99,
                "secret_tag_38": 0.99,
                "secret_tag_39": value_3
            }
        })
        requests.request("PUT", self.put_url, headers=self.headers_put, data=payload)

    def update_tags_total_spent(self, value_1):
        payload = json.dumps({
            profile_fetcher.support_id: {
                "nicknameLowercase": "skip",
                "secret_tag_1": 0.99,
                "secret_tag_2": 0.99,
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
                "secret_tag_12": 0.99,
                "secret_tag_13": 0.99,
                "secret_tag_14": 0.99,
                "secret_tag_15": 0.99,
                "secret_tag_16": 0.99,
                "secret_tag_17": 0.99,
                "secret_tag_18": 0.99,
                "secret_tag_19": 0.99,
                "secret_tag_20": 0.99,
                "secret_tag_21": 0.99,
                "secret_tag_22": 0.99,
                "secret_tag_23": 1,
                "secret_tag_24": 1,
                "secret_tag_25": 1,
                "secret_tag_26": 0.99,
                "secret_tag_27": 0.99,
                "secret_tag_28": 0.99,
                "secret_tag_29": 0.99,
                "secret_tag_30": 0.99,
                "secret_tag_31": 0.99,
                "secret_tag_32": 0,
                "secret_tag_33": 0.99,
                "secret_tag_34": 0.99,
                "secret_tag_35": 0.99,
                "secret_tag_36": 0,
                "secret_tag_37": 0.99,
                "secret_tag_38": 0.99,
                "secret_tag_39": value_1
            }
        })
        requests.request("PUT", self.put_url, headers=self.headers_put, data=payload)

    def update_tags_new_total_spent(self, value_1):
        payload = json.dumps({
            profile_fetcher.support_id: {
                "nicknameLowercase": "skip",
                "secret_tag_1": 0.99,
                "secret_tag_2": 0.99,
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
                "secret_tag_12": 0.99,
                "secret_tag_13": 0.99,
                "secret_tag_14": 0.99,
                "secret_tag_15": 0.99,
                "secret_tag_16": 0.99,
                "secret_tag_17": 0.99,
                "secret_tag_18": 0.99,
                "secret_tag_19": 0.99,
                "secret_tag_20": 0.99,
                "secret_tag_21": 0.99,
                "secret_tag_22": 0.99,
                "secret_tag_23": 1,
                "secret_tag_24": 1,
                "secret_tag_25": 1,
                "secret_tag_26": 0.99,
                "secret_tag_27": 0.99,
                "secret_tag_28": 0.99,
                "secret_tag_29": 0.99,
                "secret_tag_30": 0.99,
                "secret_tag_31": 0.99,
                "secret_tag_32": 0,
                "secret_tag_33": 0.99,
                "secret_tag_34": 0.99,
                "secret_tag_35": value_1,
                "secret_tag_36": 0,
                "secret_tag_37": 0.99,
                "secret_tag_38": 0.99,
                "secret_tag_39": 0.99
            }
        })
        requests.request("PUT", self.put_url, headers=self.headers_put, data=payload)

    def update_tags_theo(self, value_1, value_2):
        payload = json.dumps({
            profile_fetcher.support_id: {
                "nicknameLowercase": "skip",
                "secret_tag_1": 0.99,
                "secret_tag_2": 0.99,
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
                "secret_tag_12": 0.99,
                "secret_tag_13": 0.99,
                "secret_tag_14": 0.99,
                "secret_tag_15": 0.99,
                "secret_tag_16": 0.99,
                "secret_tag_17": 0.99,
                "secret_tag_18": 0.99,
                "secret_tag_19": 0.99,
                "secret_tag_20": 0.99,
                "secret_tag_21": 0.99,
                "secret_tag_22": 0.99,
                "secret_tag_23": 1,
                "secret_tag_24": 1,
                "secret_tag_25": 1,
                "secret_tag_26": 0.99,
                "secret_tag_27": 0.99,
                "secret_tag_28": value_2,
                "secret_tag_29": 0.99,
                "secret_tag_30": 0.99,
                "secret_tag_31": 0.99,
                "secret_tag_32": 0,
                "secret_tag_33": 0.99,
                "secret_tag_34": 0.99,
                "secret_tag_35": value_1,
                "secret_tag_36": 0,
                "secret_tag_37": 0.99,
                "secret_tag_38": 0.99,
                "secret_tag_39": 0.99
            }
        })
        requests.request("PUT", self.put_url, headers=self.headers_put, data=payload)

    def update_tags_average_10(self, value_1):
        payload = json.dumps({
            profile_fetcher.support_id: {
                "nicknameLowercase": "skip",
                "secret_tag_1": value_1,
                "secret_tag_2": 0.99,
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
                "secret_tag_12": 0.99,
                "secret_tag_13": 0.99,
                "secret_tag_14": 0.99,
                "secret_tag_15": 0.99,
                "secret_tag_16": 0.99,
                "secret_tag_17": 0.99,
                "secret_tag_18": 0.99,
                "secret_tag_19": 0.99,
                "secret_tag_20": 0.99,
                "secret_tag_21": 0.99,
                "secret_tag_22": 0.99,
                "secret_tag_23": 1,
                "secret_tag_24": 1,
                "secret_tag_25": 1,
                "secret_tag_26": 0.99,
                "secret_tag_27": 0.99,
                "secret_tag_28": 0.99,
                "secret_tag_29": 0.99,
                "secret_tag_30": 0.99,
                "secret_tag_31": 0.99,
                "secret_tag_32": 0,
                "secret_tag_33": 0.99,
                "secret_tag_34": 0.99,
                "secret_tag_35": 0.99,
                "secret_tag_36": 0,
                "secret_tag_37": 0.99,
                "secret_tag_38": 0.99,
                "secret_tag_39": 0.99
            }
        })
        requests.request("PUT", self.put_url, headers=self.headers_put, data=payload)


class ButtonUpdater:
    def __init__(self, buttons):
        self.buttons = buttons
        self.initial_texts = {key: button.content.value for key, button in buttons.items()}

    def update_buttons(self, button_key_to_update):
        i = 1
        for key, button in self.buttons.items():
            if key == button_key_to_update:
                if profile_fetcher.support_id is None:
                    button.content.value = 'supid не введен'
                else:
                    button.content.value = "Теги обновлены!"
            else:
                button.content.value = f"Update tags {str(i)}"
            button.update()
            i += 1

    def update_buttons_other(self, button_key_to_update):
        for key, button in self.buttons.items():
            if key == button_key_to_update:
                button.content.value = "Теги обновлены!"
                button.update()
                button.content.value = self.initial_texts[key]
            else:
                button.content.value = self.initial_texts[key]
                button.update()

class JsonOpener:

    def __init__(self, button):
        self.button = button
        self.json_data = None
        self.ltos_list = []
        self.otos_list = []
        self.json_data_other_wo_field = None
        self.all_ids_other_wo_field = None
        self.json_data_with_field = None
        self.compare_reference_with_field = None
        self.json_data_oto_2 = None
        self.all_ids_oto_2 = None
        self.json_data_compare_1 = None
        self.json_data_compare_2 = None

    @staticmethod
    def add_error(errors, name, expected, actual):
        if expected != actual:
            errors.append(f"{name}:\nER: {expected}\nAR: {actual}")

    @staticmethod
    def add_bans(ltos_list, this_id, bans_should_be):
        for item in ltos_list:
            if item != this_id:
                bans_should_be.append(item)
            elif item == this_id:
                pass

    @staticmethod
    def errors_output(result_text, buttons):
        for line in result_text:
            buttons['errors'].controls.append(
                ft.Column([
                    ft.Icon(name=ft.icons.ERROR_OUTLINE, color=ft.colors.RED),
                    ft.Text(line, no_wrap=False)
                ])
            )
        buttons['errors'].update()

    def update_button(self, button, is_correct, text):
        self.button = button

        if is_correct is True:
            button.text = text
            button.color = ft.colors.GREEN
        else:
            button.text = text
            button.color = ft.colors.RED
        button.update()

    def json_check_end_other(self, errors, buttons, number, result_text, this_id):
        if not errors:
            self.update_button(buttons[f'button_{number + 1}'], True, 'УСПЕШНО')
        else:
            self.update_button(buttons[f'button_{number + 1}'], False, 'ОШИБКА')
            result_text.append(f"{this_id}:\n" + "\n".join(errors))
        self.errors_output(result_text, buttons)

    def json_check_end_tickets(self, errors, buttons, tickets_number, number, result_text, this_id):
        if not errors:
            self.update_button(buttons[f'ban_{tickets_number}_{number + 1}'], True, 'УСПЕШНО')
        else:
            self.update_button(buttons[f'ban_{tickets_number}_{number + 1}'], False, 'ОШИБКА')
            result_text.append(f"{this_id}:\n" + "\n".join(errors))
        self.errors_output(result_text, buttons)

    def normalize_conditions(self, data, ignore_keys):
        if isinstance(data, dict):
            return {
                k: self.normalize_conditions(v, ignore_keys)
                for k, v in data.items()
                if k not in ignore_keys
            }
        elif isinstance(data, list):
            return [self.normalize_conditions(i, ignore_keys) for i in data]
        else:
            return data

    def equal_ignore(self, d1, d2, ignore_keys):
        return self.normalize_conditions(copy.deepcopy(d1), ignore_keys) == self.normalize_conditions(copy.deepcopy(d2), ignore_keys)

    def open_json(self, e: ft.FilePickerResultEvent, target_attr="json_data"):
        if e.files:
            file = e.files[0]
            self._update_button_text(file.name)
            self._load_json(file.path, target_attr=target_attr)
        else:
            self._update_button_text("JSON не выбран")

    def open_json_compare(self, e: ft.FilePickerResultEvent):
        if e.files and len(e.files) >= 2:
            file1, file2 = e.files[:2]
            self.json_data_compare_1 = self._load_json_compare(file1.path)
            self.json_data_compare_2 = self._load_json_compare(file2.path)
            self._update_button_text(f'{file1.name}, {file2.name}')
        else:
            self._update_button_text("Выберите 2 JSON файла")

    def _update_button_text(self, text):
        self.button.value = text
        self.button.update()

    def _load_json(self, file_path, target_attr="json_data"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            setattr(self, target_attr, data)
        except TypeError:
            self._update_button_text("Ошибка загрузки JSON")

    def _load_json_compare(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def download_json_tickets(self, tickets_number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons,
                                            tickets_bans_9_buttons, tickets_bans_3_buttons, tickets_bans_7_buttons,
                                            tickets_bans_10_buttons_raskat)

        buttons_dict = {
            11: tickets_bans_11_buttons,
            10: tickets_bans_10_buttons,
            9: tickets_bans_9_buttons,
            3: tickets_bans_3_buttons,
            7: tickets_bans_7_buttons,
            '10_raskat': tickets_bans_10_buttons_raskat
        }
        buttons = buttons_dict[tickets_number]

        for item in self.json_data['global']:
            if item['type'] == 'limited_time_offer':
                self.ltos_list.append(item['_id'])
            elif item['type'] == 'one_time_offer':
                self.otos_list.append(item['_id'])
        for i, item in enumerate(self.json_data['global'], start=1):
            button_key = f'ban_{tickets_number}_{i}'
            button = buttons.get(button_key)
            if button:
                button.text = item['_id']
                button.disabled = False
                button.update()

    def download_json_other(self, kind):
        from buttons import (tickets_criteria_buttons, no_hint_bans_buttons, no_hint_balance_buttons,
                                            bcp_previous_buttons, bcp_actual_buttons, cgp_6_buttons, cgp_9_buttons,
                                            other_bans_wo_field_buttons, other_bans_with_field_buttons, oto_2_buttons_7_18,
                                            json_compare_buttons_1, json_compare_buttons_2,
                                            among_balance_new_tc_buttons, among_balance_average_buttons,
                                            labyrinth_balance_ww_buttons, labyrinth_balance_cn_buttons,
                                            tickets_balance_checker_buttons_11, tickets_balance_checker_buttons_10,
                                            tickets_balance_checker_buttons_9, tickets_balance_checker_buttons_3,
                                            tickets_balance_checker_buttons_10_extra,
                                            tickets_balance_checker_buttons_7, usual_theo_json_buttons,
                                            add_theo_json_buttons, oto_2_buttons_19, comeback_json_buttons,
                                            gf_real_json_buttons)

        def update_button(type_, buttons):
            for i, item in enumerate(self.json_data['global'], start=1):
                button_key = f'button_{i}'
                buttons[button_key].text = item['_id']
                buttons[button_key].disabled = False
                buttons[button_key].update()

        kinds = {
            'criteria': tickets_criteria_buttons,
            'no_hint_bans': no_hint_bans_buttons,
            'no_hint_balance': no_hint_balance_buttons,
            'bcp_previous': bcp_previous_buttons,
            'bcp_actual': bcp_actual_buttons,
            'cgp_6': cgp_6_buttons,
            'cgp_9': cgp_9_buttons,
            'with_field': other_bans_with_field_buttons,
            'among_new_ts': among_balance_new_tc_buttons,
            'among_average': among_balance_average_buttons,
            'labyrinth_balance_ww': labyrinth_balance_ww_buttons,
            'labyrinth_balance_cn': labyrinth_balance_cn_buttons,
            'tickets_balance_11': tickets_balance_checker_buttons_11,
            'tickets_balance_10': tickets_balance_checker_buttons_10,
            'tickets_balance_9': tickets_balance_checker_buttons_9,
            'tickets_balance_3': tickets_balance_checker_buttons_3,
            'tickets_balance_10_extra': tickets_balance_checker_buttons_10_extra,
            'tickets_balance_7': tickets_balance_checker_buttons_7,
            'usual_theo': usual_theo_json_buttons,
            'add_theo': add_theo_json_buttons,
            'comeback': comeback_json_buttons,
            'gf_real': gf_real_json_buttons
        }

        json_type = kinds.get(kind)
        if json_type:
            update_button(kind, json_type)
            if kind in ('usual_theo', 'add_theo', 'comeback', 'gf_real'):
                for item in self.json_data['global']:
                    self.ltos_list.append(item['_id'])
            else:
                if kind == 'other_wo_field':
                    self.all_ids_other_wo_field = [item['_id'] for item in self.json_data_other_wo_field['global']]
                    for i, item in enumerate(self.all_ids_other_wo_field, start=1):
                        button_key = f'button_{i}'
                        other_bans_wo_field_buttons[button_key].text = item
                        other_bans_wo_field_buttons[button_key].disabled = False
                        other_bans_wo_field_buttons[button_key].update()
                elif kind == 'oto_2_7_18':
                    self.all_ids_oto_2 = [item['_id'] for item in self.json_data_oto_2['global']]
                    for i, item in enumerate(self.all_ids_oto_2, start=1):
                        button_key = f'button_{i}'
                        oto_2_buttons_7_18[button_key].text = item
                        oto_2_buttons_7_18[button_key].disabled = False
                        oto_2_buttons_7_18[button_key].update()
                elif kind == 'oto_2_19':
                    self.all_ids_oto_2 = [item['_id'] for item in self.json_data_oto_2['global']]
                    for i, item in enumerate(self.all_ids_oto_2, start=1):
                        button_key = f'button_{i}'
                        oto_2_buttons_19[button_key].text = item
                        oto_2_buttons_19[button_key].disabled = False
                        oto_2_buttons_19[button_key].update()
                elif kind == "compare":
                    for i, item in enumerate(self.json_data_compare_1['global'], start=1):
                        button_key = f'button_{i}'
                        json_compare_buttons_1[button_key].text = item['_id']
                        json_compare_buttons_1[button_key].disabled = False
                        json_compare_buttons_1[button_key].update()
                    for i, item in enumerate(self.json_data_compare_2['global'], start=1):
                        button_key = f'button_{i}'
                        json_compare_buttons_2[button_key].text = item['_id']
                        json_compare_buttons_2[button_key].disabled = False
                        json_compare_buttons_2[button_key].update()

    def reset_tickets(self, tickets_number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons,
                                            tickets_bans_9_buttons, tickets_bans_3_buttons, tickets_bans_7_buttons,
                                            tickets_bans_10_buttons_raskat)

        buttons_disct = {
            11: tickets_bans_11_buttons,
            10: tickets_bans_10_buttons,
            9: tickets_bans_9_buttons,
            3: tickets_bans_3_buttons,
            7: tickets_bans_7_buttons,
            '10_raskat': tickets_bans_10_buttons_raskat
        }
        buttons = buttons_disct[tickets_number]

        self.json_data = None
        self.ltos_list = []
        self.otos_list = []
        self._update_button_text("")
        buttons['errors'].controls.clear()
        buttons['errors'].update()
        for item in buttons:
            if re.match(fr'^ban_{tickets_number}_\d+$', item):
                buttons[item].text = 'offer id'
                buttons[item].color = ft.colors.PRIMARY
                buttons[item].disabled = True
                buttons[item].update()

    def reset_other(self, kind):
        from buttons import (tickets_criteria_buttons, no_hint_bans_buttons, no_hint_balance_buttons,
                                            bcp_previous_buttons, bcp_actual_buttons, cgp_6_buttons, cgp_9_buttons,
                                            other_bans_wo_field_buttons, other_bans_with_field_buttons, oto_2_buttons_7_18,
                                            json_compare_buttons_1, json_compare_buttons_2,
                                            among_balance_new_tc_buttons, among_balance_average_buttons,
                                            labyrinth_balance_ww_buttons, labyrinth_balance_cn_buttons,
                                            tickets_balance_checker_buttons_11, tickets_balance_checker_buttons_10,
                                            tickets_balance_checker_buttons_9, tickets_balance_checker_buttons_3,
                                            tickets_balance_checker_buttons_10_extra, tickets_balance_checker_buttons_7,
                                            usual_theo_json_buttons, add_theo_json_buttons, oto_2_buttons_19,
                                            comeback_json_buttons, gf_real_json_buttons)

        def reset_data(buttons):
            self.json_data = None
            self._update_button_text("")
            for item in buttons:
                if re.match(r'^button_\d+$', item):
                    buttons[item].text = 'offer id'
                    buttons[item].color = ft.colors.PRIMARY
                    buttons[item].disabled = True
                    buttons[item].update()
                    if kind == 'oto_2_7_18' or kind == 'oto_2_19':
                        self.json_data_oto_2 = None
                        self.all_ids_oto_2 = None
                        buttons['input_denies_field'].value = ""
                        buttons['input_denies_field'].update()
                        buttons['input_allows_field'].value = ""
                        buttons['input_allows_field'].update()
                    elif kind == 'among_average':
                        buttons['me_field'].value = ""
                        buttons['me_field'].update()
            if 'errors' in buttons:
                buttons['errors'].controls.clear()
                buttons['errors'].update()


        kinds = {
            'criteria': tickets_criteria_buttons,
            'no_hint_bans': no_hint_bans_buttons,
            'no_hint_balance': no_hint_balance_buttons,
            'bcp_previous': bcp_previous_buttons,
            'bcp_actual': bcp_actual_buttons,
            'cgp_6': cgp_6_buttons,
            'cgp_9': cgp_9_buttons,
            'with_field': other_bans_with_field_buttons,
            'among_new_ts': among_balance_new_tc_buttons,
            'among_average': among_balance_average_buttons,
            'labyrinth_balance_ww': labyrinth_balance_ww_buttons,
            'labyrinth_balance_cn': labyrinth_balance_cn_buttons,
            'tickets_balance_11': tickets_balance_checker_buttons_11,
            'tickets_balance_10': tickets_balance_checker_buttons_10,
            'tickets_balance_9': tickets_balance_checker_buttons_9,
            'tickets_balance_3': tickets_balance_checker_buttons_3,
            'tickets_balance_10_extra': tickets_balance_checker_buttons_10_extra,
            'tickets_balance_7': tickets_balance_checker_buttons_7,
            'oto_2_7_18': oto_2_buttons_7_18,
            'oto_2_19': oto_2_buttons_19,
            'usual_theo': usual_theo_json_buttons,
            'add_theo': add_theo_json_buttons,
            'comeback': comeback_json_buttons,
            'gf_real': gf_real_json_buttons
        }

        json_type = kinds.get(kind)
        if json_type:
            reset_data(json_type)
            if kind in ('usual_theo', 'add_theo', 'comeback', 'gf_real'):
                self.ltos_list = []
        elif kind == 'compare':
            self.json_data_compare_1 = None
            self.json_data_compare_2 = None
            self._update_button_text("")
            for item in json_compare_buttons_1:
                if re.match(r'^button_\d+$', item):
                    json_compare_buttons_1[item].text = "offer id"
                    json_compare_buttons_1[item].color = ft.colors.PRIMARY
                    json_compare_buttons_1[item].disabled = True
                    json_compare_buttons_1[item].update()
            for item in json_compare_buttons_2:
                if re.match(r'^button_\d+$', item):
                    json_compare_buttons_2[item].text = "offer id"
                    json_compare_buttons_2[item].color = ft.colors.PRIMARY
                    json_compare_buttons_2[item].disabled = True
                    json_compare_buttons_2[item].update()
        elif kind == 'other_wo_field':
            self.json_data_other_wo_field = None
            self._update_button_text("")
            for item in other_bans_wo_field_buttons:
                if re.match(r'^button_\d+$', item):
                    other_bans_wo_field_buttons[item].text = "offer id"
                    other_bans_wo_field_buttons[item].color = ft.colors.PRIMARY
                    other_bans_wo_field_buttons[item].disabled = True
                    other_bans_wo_field_buttons[item].update()

    def check_bans_lto(self, tickets_number, number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons,
                                            tickets_bans_9_buttons, tickets_bans_3_buttons, tickets_bans_7_buttons,
                                            tickets_bans_10_buttons_raskat)

        criteria_raskat = bcp_balance['lto_criteria'][0]
        criteria_b = bcp_balance['lto_criteria'][1]
        criteria_daily = bcp_balance['lto_criteria'][2]
        group_b_checks = {
            'lvl_start': bcp_balance['raskat_b'][0],
            'lvl_end': bcp_balance['raskat_b'][1],
            'trigger': bcp_balance['raskat_b'][2],
            'trigger_param': bcp_balance['raskat_b'][3]
        }

        buttons_disct = {
            11: tickets_bans_11_buttons,
            10: tickets_bans_10_buttons,
            9: tickets_bans_9_buttons,
            3: tickets_bans_3_buttons,
            7: tickets_bans_7_buttons,
            '10_raskat': tickets_bans_10_buttons_raskat
        }
        buttons = buttons_disct[tickets_number]
        errors, result_text, bans_should_be = [], [], []

        this_id = self.json_data['global'][number]['_id']
        bans_in_json = self.json_data['global'][number]['conditions']['banOffers']
        this_criteria = self.json_data['global'][number]['criteria']
        this_conditions = self.json_data['global'][number]['conditions']

        self.add_bans(self.ltos_list, this_id, bans_should_be)

        if set(bans_should_be) != set(bans_in_json):
            self.add_error(errors, 'bans', bans_should_be, bans_in_json)
        if tickets_number == '10_raskat':
            if tickets_bans_10_buttons_raskat['group_b'].value is True:
                self.add_error(errors, "criteria", criteria_b, this_criteria)
                for name, conditions in group_b_checks.items():
                    if all(this_conditions.get(k) != v for k, v in conditions.items()):
                        self.add_error(errors, name, conditions, this_conditions)
            else:
                self.add_error(errors, "criteria", criteria_raskat, this_criteria)
        elif tickets_number == 7:
            self.add_error(errors, "criteria", criteria_b, this_criteria)
        else:
            self.add_error(errors, "criteria", criteria_daily, this_criteria)

        self.json_check_end_tickets(errors, buttons, tickets_number, number, result_text, this_id)

    def check_bans_oto(self, tickets_number, number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons,
                                            tickets_bans_9_buttons, tickets_bans_3_buttons, tickets_bans_7_buttons,
                                            tickets_bans_10_buttons_raskat)

        criteria_raskat = bcp_balance['lto_criteria'][0]
        criteria_b = bcp_balance['lto_criteria'][1]
        criteria_daily = bcp_balance['lto_criteria'][2]
        group_b_checks = {
            'lvl_start': bcp_balance['raskat_b'][0],
            'lvl_end': bcp_balance['raskat_b'][1],
            'trigger': bcp_balance['raskat_b'][6],
            'trigger_param': bcp_balance['raskat_b'][4],
            "delay": bcp_balance['raskat_b'][5]
        }

        buttons_disct = {
            11: tickets_bans_11_buttons,
            10: tickets_bans_10_buttons,
            9: tickets_bans_9_buttons,
            3: tickets_bans_3_buttons,
            7: tickets_bans_7_buttons,
            '10_raskat': tickets_bans_10_buttons_raskat
        }
        buttons = buttons_disct[tickets_number]
        errors, result_text, bans_should_be = [], [], []

        def get_denies(json_data, number, paths):
            """Находим denyByOneOf"""
            for path in paths:
                try:
                    node = json_data
                    for key in path:
                        node = node[key]
                    return node
                except (KeyError, IndexError):
                    continue
            return []  # если ничего не найдено

        deny_paths_1 = [
            ['global', number, 'conditions', 'filter', 'and', 1, 'or', 0, 'denyByOneOf'],
            ['global', number, 'conditions', 'filter', 'and', 0, 'or', 0, 'denyByOneOf'],
            ['global', number, 'conditions', 'filter', 'and', 1, 'denyByOneOf'],
            ['global', number, 'conditions', 'filter', 'and', 0, 'denyByOneOf']
        ]
        deny_paths_2 = [
            ['global', number, 'conditions', 'filter', 'and', 1, 'or', 1, 'denyByOneOf'],
            ['global', number, 'conditions', 'filter', 'and', 0, 'or', 1, 'denyByOneOf']
        ]
        deny_paths_3 = [
            ['global', number, 'conditions', 'filter', 'and', 1, 'denyByOneOf']
        ]

        this_id = self.json_data['global'][number]['_id']
        bans_in_json = self.json_data['global'][number]['conditions']['banOffers']
        criteria = self.json_data['global'][number]['criteria']
        this_conditions = self.json_data['global'][number]['conditions']
        self.add_bans(self.otos_list, this_id, bans_should_be)

        if set(bans_in_json) != set(bans_should_be):
            self.add_error(errors, 'bans', bans_should_be, bans_in_json)
        if tickets_number == 3:
            denies_in_json = get_denies(self.json_data, number, deny_paths_3)
            self.add_error(errors, 'denies', self.ltos_list, denies_in_json)
            self.add_error(errors, "criteria", criteria_daily, criteria)
        else:
            denies_in_json_1 = get_denies(self.json_data, number, deny_paths_1)
            denies_in_json_2 = get_denies(self.json_data, number, deny_paths_2)
            if set(denies_in_json_1) != set(self.ltos_list):
                errors.append(f"denies 1: \nER: {self.ltos_list}\nAR: {denies_in_json_1}")
            if set(denies_in_json_2) != set(self.ltos_list):
                errors.append(f"denies 2: \nER: {self.ltos_list}\nAR: {denies_in_json_2}")
            if tickets_number == '10_raskat':
                if tickets_bans_10_buttons_raskat['group_b'].value is True:
                    self.add_error(errors, 'criteria', criteria_b, criteria)
                    for name, conditions in group_b_checks.items():
                        if all(this_conditions.get(k) != v for k, v in conditions.items()):
                            self.add_error(errors, name, conditions, this_conditions)
                else:
                    self.add_error(errors, 'criteria', criteria_raskat, criteria)
            elif tickets_number == 7:
                self.add_error(errors, 'criteria', criteria_b, criteria)
            else:
                self.add_error(errors, 'criteria', criteria_daily, criteria)

        self.json_check_end_tickets(errors, buttons, tickets_number, number, result_text, this_id)

    def check_criteria(self):
        from buttons import tickets_criteria_buttons

        criteria_new_264 = bcp_balance['lto_criteria'][0]

        for i, item in enumerate(self.json_data['global'], start=0):
            if self.json_data['global'][i]['criteria'] == criteria_new_264:
                self.update_button(tickets_criteria_buttons[f'button_{i + 1}'], True, "Критерий корректный")
            else:
                self.update_button(tickets_criteria_buttons[f'button_{i + 1}'], False, "Критерий некорректный")
        time.sleep(3)
        for i, item in enumerate(self.json_data['global'], start=0):
            tickets_criteria_buttons[f'button_{i + 1}'].text = self.json_data['global'][i]['_id']
            tickets_criteria_buttons[f'button_{i + 1}'].update()

    def check_bans_no_hint(self, number):
        from buttons import no_hint_bans_buttons
        errors, result_text, bans_should_be = [], [], []
        bans_in_json = self.json_data['global'][number]['conditions']['banOffers']
        this_product_id = self.json_data['global'][number]['event']['product_id']
        all_ids = self.json_data['global']
        this_id = self.json_data['global'][number]['_id']

        for item in all_ids:
            if this_product_id != item['event']['product_id']:
                bans_should_be.append(item['_id'])
            elif this_product_id == item['event']['product_id']:
                pass

        if set(bans_should_be) != set(bans_in_json):
            self.add_error(errors, 'bans', bans_should_be, bans_in_json)

        self.json_check_end_other(errors, no_hint_bans_buttons, number, result_text, this_id)

    def check_balance_no_hint(self, number):
        from buttons import no_hint_balance_buttons
        criteria = bcp_balance['lto_criteria'][2]
        conditions = bcp_balance['no_hint_conditions']
        event = bcp_balance['no_hint_event']
        errors, result_text = [], []
        ignore_keys = {"banOffers"}
        this_id = self.json_data['global'][number]['_id']
        this_conditions = self.json_data['global'][number]['conditions']
        this_event = self.json_data['global'][number]['event']
        this_criteria = self.json_data['global'][number]['criteria']

        if not self.equal_ignore(conditions[number], this_conditions, ignore_keys):
            self.add_error(errors, 'conditions', conditions[number], this_conditions)
        self.add_error(errors, 'event', event[number], this_event)
        self.add_error(errors, 'criteria', criteria, this_criteria)

        self.json_check_end_other(errors, no_hint_balance_buttons, number, result_text, this_id)

    def check_bcp_previous(self, number):
        from buttons import bcp_previous_buttons
        platform_ios_android_samsung = [
            "ios",
            "android",
            "samsung"
        ]
        criteria_non_default = bcp_balance['bcp_criteria'][0]
        criteria_default = bcp_balance['bcp_criteria'][1]
        criteria = bcp_balance['bcp_criteria'][2]
        platform_win_amazon = [
            "win",
            "amazon"
        ]
        criteria_rb_rf = bcp_balance['bcp_criteria'][3]
        conditions_non_payer_t_3 = {"conditions_non_payer_t_3": "secret_data"}
        conditions_non_payer_default = {"conditions_non_payer_default": "secret_data"}
        conditions_payer = {"conditions_payer": "secret_data"}
        event_non_payer_t_3 = [
            {"event_non_payer_t_3"},
            {"secret_data"}
        ]
        event_non_payer_default = [
            {"event_non_payer_default"},
            {"secret_data"}
        ]
        event_payer = [
            {"event_payer"},
            {"secret_data"}
        ]

        this_conditions = self.json_data['global'][number]['conditions']
        this_event = self.json_data['global'][number]['event']
        this_platform = self.json_data['global'][number]['platform']
        this_criteria = self.json_data['global'][number]['criteria']

        if number == 0:
            if (this_conditions == conditions_non_payer_t_3 and this_platform == platform_ios_android_samsung and
                    this_criteria == criteria_non_default and this_event == event_non_payer_t_3[0]):
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], False, 'Баланс и conditions некорректные')
        elif number == 1:
            if (this_conditions == conditions_non_payer_default and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_default and this_event == event_non_payer_default[0]):
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], False, 'Баланс и conditions некорректные')
        elif number == 2:
            if (this_conditions == conditions_non_payer_default and this_platform == platform_win_amazon
                    and this_criteria == criteria and this_event == event_non_payer_default[0]):
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], False, 'Баланс и conditions некорректные')
        elif number == 3:
            if (this_conditions == conditions_non_payer_t_3 and this_platform == platform_ios_android_samsung and
                    this_criteria == criteria_non_default and this_event == event_non_payer_t_3[1]):
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], False, 'Баланс и conditions некорректные')
        elif number == 4:
            if (this_conditions == conditions_non_payer_default and this_platform == platform_ios_android_samsung and
                    this_criteria == criteria_default and this_event == event_non_payer_default[1]):
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], False, 'Баланс и conditions некорректные')
        elif number == 5:
            if (this_conditions == conditions_non_payer_default and this_platform == platform_win_amazon
                    and this_criteria == criteria and this_event == event_non_payer_default[1]):
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], False, 'Баланс и conditions некорректные')
        elif number == 6:
            if (this_conditions == conditions_payer and this_platform == [] and this_criteria == criteria_rb_rf
                    and this_event == event_payer[0]):
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
                bcp_previous_buttons['dynamic_items_1'].value = (
                    self.json_data['global'][6]['event']['rewards'][0]['itemId'],
                    self.json_data['global'][6]['event']['rewards'][0]['count'],
                    self.json_data['global'][6]['event']['rewards'][1]['itemId'],
                    self.json_data['global'][6]['event']['rewards'][1]['count'],
                    self.json_data['global'][6]['event']['rewards'][2]['itemId'],
                    self.json_data['global'][6]['event']['rewards'][2]['count'],
                    self.json_data['global'][6]['event']['rewards'][3]['itemId'],
                    self.json_data['global'][6]['event']['rewards'][3]['count']
                )
                bcp_previous_buttons['dynamic_items_1'].update()
            else:
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], False, 'Баланс и conditions некорректные')
        elif number == 7:
            if (this_conditions == conditions_payer and this_platform == [] and this_criteria == criteria_rb_rf
                    and this_event == event_payer[1]):
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
                bcp_previous_buttons['dynamic_items_2'].value = (
                    self.json_data['global'][7]['event']['rewards'][0]['itemId'],
                    self.json_data['global'][7]['event']['rewards'][0]['count'],
                    self.json_data['global'][7]['event']['rewards'][1]['itemId'],
                    self.json_data['global'][7]['event']['rewards'][1]['count'],
                    self.json_data['global'][7]['event']['rewards'][2]['itemId'],
                    self.json_data['global'][7]['event']['rewards'][2]['count'],
                    self.json_data['global'][7]['event']['rewards'][3]['itemId'],
                    self.json_data['global'][7]['event']['rewards'][3]['count']
                )
                bcp_previous_buttons['dynamic_items_2'].update()
            else:
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], False, 'Баланс и conditions некорректные')
        elif number == 8:
            if (this_conditions == conditions_payer and this_platform == [] and this_criteria == criteria_rb_rf
                    and this_event == event_payer[2]):
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
                bcp_previous_buttons['dynamic_items_3'].value = (
                    self.json_data['global'][8]['event']['rewards'][0]['itemId'],
                    self.json_data['global'][8]['event']['rewards'][0]['count'],
                    self.json_data['global'][8]['event']['rewards'][1]['itemId'],
                    self.json_data['global'][8]['event']['rewards'][1]['count'],
                    self.json_data['global'][8]['event']['rewards'][2]['itemId'],
                    self.json_data['global'][8]['event']['rewards'][2]['count'],
                    self.json_data['global'][8]['event']['rewards'][3]['itemId'],
                    self.json_data['global'][8]['event']['rewards'][3]['count']
                )
                bcp_previous_buttons['dynamic_items_3'].update()
            else:
                self.update_button(bcp_previous_buttons[f'button_{number + 1}'], False, 'Баланс и conditions некорректные')

    def check_bcp_actual(self, number):
        from buttons import bcp_actual_buttons
        errors, result_text = [], []

        ignore_keys = {"banOffers", "skin_id"}

        platform_ios_android_samsung = [
            "ios",
            "android",
            "samsung"
        ]
        platform_win_amazon = [
            "win",
            "amazon"
        ]
        criteria_non_default = bcp_balance['bcp_criteria'][0]
        criteria_default = bcp_balance['bcp_criteria'][1]
        criteria = bcp_balance['bcp_criteria'][2]
        criteria_rb_rf = bcp_balance['bcp_criteria'][3]
        conditions = bcp_balance['bcp_actual_conditions']
        this = self.json_data['global'][number]

        if number in {0, 1, 2, 6}:
            this_skin_id = self.json_data['global'][number]['conditions']['skin_id']

        if int(bcp_actual_buttons['day'].value) in range(0, 24):
            double = "bcp_0-23_fixed"
        else:
            double = "bcp_24-27_double"

        if not self.equal_ignore(conditions[number], this['conditions'], ignore_keys):
            self.add_error(errors, 'conditions', conditions[number], this['conditions'])
        if number in {0, 1, 2, 3, 4, 5}:
            self.add_error(errors, 'event', bcp_balance[double][number], this['event'])
        elif number in {6, 7, 8}:
            self.add_error(errors, 'event', bcp_balance["bcp_dynamic"][int(bcp_actual_buttons['day'].value)][number - 6],this['event'])
        if number in {0, 1, 2, 6}:
            self.add_error(errors, 'skin_id', int(bcp_actual_buttons["skin_id_field"].value), this_skin_id)
        if number in {0, 1, 3, 4}:
            self.add_error(errors, 'platform', platform_ios_android_samsung, this['platform'])
        if number in {2, 5}:
            self.add_error(errors, 'platform', platform_win_amazon, this['platform'])
        if number in {0, 3}:
            self.add_error(errors, 'criteria', criteria_non_default, this['criteria'])
        if number in {1, 4}:
            self.add_error(errors, 'criteria', criteria_default, this['criteria'])
        if number in {2, 5}:
            self.add_error(errors, 'criteria', criteria, this['criteria'])
        if number in {6, 7, 8}:
            self.add_error(errors, 'criteria', criteria_rb_rf, this['criteria'])

        self.json_check_end_other(errors, bcp_actual_buttons, number, result_text, this['_id'])

    def check_usual_theo(self, number):
        from buttons import usual_theo_json_buttons
        if usual_theo_json_buttons['group_b'].value is True:
            criteria_all = bcp_balance['lto_criteria'][1]
            conditions_1 = bcp_balance['usual_theo_conditions_b_1']
            conditions_2 = bcp_balance['usual_theo_conditions_b_2']
        else:
            criteria_all = bcp_balance['lto_criteria'][0]
            conditions_1 = bcp_balance['usual_theo_conditions_1']
            conditions_2 = bcp_balance['usual_theo_conditions_2']
        events_1 = bcp_balance['usual_theo_event_1']
        events_2 = bcp_balance['usual_theo_event_2']
        errors, result_text, bans_should_be = [], [], []
        ignore_keys = {"banOffers", "skin_id", "aura"}

        this_skin_id = self.json_data['global'][number]['conditions']['skin_id']
        this_event = self.json_data['global'][number]['event']
        this_criteria = self.json_data['global'][number]['criteria']
        this_conditions = self.json_data['global'][number]['conditions']
        this_id = self.json_data['global'][number]['_id']
        bans_in_json = self.json_data['global'][number]['conditions']['banOffers']

        self.add_bans(self.ltos_list, this_id, bans_should_be)

        if int(usual_theo_json_buttons['launch'].value) == 1:
            conditions = conditions_1
            events = events_1
        else:
            conditions = conditions_2
            events = events_2

        if set(bans_should_be) != set(bans_in_json):
            self.add_error(errors, 'bans', bans_should_be, bans_in_json)
        if not self.equal_ignore(this_conditions, conditions[number], ignore_keys):
            self.add_error(errors, 'conditions', conditions[number], this_conditions)
        if not self.equal_ignore(this_event, events[number], ignore_keys):
            self.add_error(errors, 'event', events[number], this_event)
        self.add_error(errors, 'skin_id', int(usual_theo_json_buttons['skin_id_field'].value), this_skin_id)
        self.add_error(errors, 'criteria', criteria_all, this_criteria)

        self.json_check_end_other(errors, usual_theo_json_buttons, number, result_text, this_id)

    def check_add_theo(self, number):
        from buttons import add_theo_json_buttons
        criteria_all = bcp_balance['lto_criteria'][2]
        criteria_1 = bcp_balance['bcp_criteria'][0]
        criteria_2 = bcp_balance['bcp_criteria'][1]
        conditions = bcp_balance['add_theo_conditions']
        events = bcp_balance['add_theo_event']
        input_denies = [int(val) for val in add_theo_json_buttons["input_denies_field"].value.split(",")]
        errors, result_text, bans_should_be = [], [], []
        ignore_keys = {"banOffers", "skin_id", "denyByOneOf", "itemIdLT"}

        this_skin_id = self.json_data['global'][number]['conditions']['skin_id']
        this_event = self.json_data['global'][number]['event']
        this_criteria = self.json_data['global'][number]['criteria']
        this_conditions = self.json_data['global'][number]['conditions']
        this_id = self.json_data['global'][number]['_id']
        this_item_id = self.json_data['global'][number]['conditions']['filter']['itemIdLT'][0]
        bans_in_json = self.json_data['global'][number]['conditions']['banOffers']
        denies_in_json = self.json_data['global'][number]['conditions']['filter']['denyByOneOf']

        self.add_bans(self.ltos_list, this_id, bans_should_be)

        if set(bans_should_be) != set(bans_in_json):
            self.add_error(errors, 'bans', bans_should_be, bans_in_json)
        if set(input_denies) != set(denies_in_json):
            self.add_error(errors, 'denies', input_denies, denies_in_json)
        if not self.equal_ignore(this_conditions, conditions[number], ignore_keys):
            self.add_error(errors, 'conditions', conditions[number], this_conditions)
        self.add_error(errors, 'event', events[number], this_event)
        self.add_error(errors, 'itemId', int(add_theo_json_buttons['item_id_field'].value), this_item_id)
        self.add_error(errors, 'skin_id', int(add_theo_json_buttons['skin_id_field'].value), this_skin_id)
        if number == 0:
            self.add_error(errors, 'criteria', criteria_1, this_criteria)
        elif number == 1:
            self.add_error(errors, 'criteria', criteria_2, this_criteria)
        else:
            self.add_error(errors, 'criteria', criteria_all, this_criteria)

        self.json_check_end_other(errors, add_theo_json_buttons, number, result_text, this_id)

    def check_cgp_6(self, number):
        from buttons import cgp_6_buttons
        platform_ios_android_samsung = [
            "ios",
            "android",
            "samsung"
        ]
        platform_win_amazon = [
            "win",
            "amazon"
        ]
        conditions_cgp_non_payer = {"conditions_cgp_non_payer": "secret_data"}
        conditions_cgp_payer = {"conditions_cgp_payer": "secret_data"}
        criteria_cgp_1 = bcp_balance['cgp_criteria'][0]
        criteria_cgp_2 = bcp_balance['cgp_criteria'][1]
        criteria_cgp_3 = bcp_balance['cgp_criteria'][2]
        criteria_cgp_4 = bcp_balance['cgp_criteria'][3]

        this_conditions = self.json_data['global'][number]['conditions']
        this_platform = self.json_data['global'][number]['platform']
        this_criteria = self.json_data['global'][number]['criteria']
        this_event = self.json_data['global'][number]['event']

        if number == 0:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_1 and this_event == bcp_balance["cgp_6_fixed"][number]):
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 1:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_2 and this_event == bcp_balance["cgp_6_fixed"][number]):
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 2:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_win_amazon
                    and this_criteria == criteria_cgp_3 and this_event == bcp_balance["cgp_6_fixed"][number]):
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 3:
            if (this_conditions == conditions_cgp_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_1 and this_event == bcp_balance["cgp_6_fixed"][number]):
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 4:
            if (this_conditions == conditions_cgp_payer and this_platform == [] and this_criteria == criteria_cgp_4
                    and this_event == bcp_balance["cgp_6_fixed"][number]):
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 5:
            if (this_conditions == conditions_cgp_payer and this_platform == [] and this_criteria == criteria_cgp_4
                    and this_event == bcp_balance["cgp_6_9_dynamic"][int(cgp_6_buttons['day'].value)]):
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_6_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')

    def check_cgp_9(self, number):
        from buttons import cgp_9_buttons
        conditions_cgp_payer_lt_25 = {"conditions_cgp_payer_lt_25": "secret_data"}
        conditions_cgp_payer_gt_25 = {"conditions_cgp_payer_gt_25": "secret_data"}
        conditions_cgp_non_payer = {"conditions_cgp_non_payer": "secret_data"}
        platform_ios_android_samsung = [
            "ios",
            "android",
            "samsung"
        ]
        platform_win_amazon = [
            "win",
            "amazon"
        ]
        criteria_cgp_1 = bcp_balance['cgp_criteria'][0]
        criteria_cgp_2 = bcp_balance['cgp_criteria'][1]
        criteria_cgp_3 = bcp_balance['cgp_criteria'][2]
        criteria_cgp_4 = bcp_balance['cgp_criteria'][3]

        this_conditions = self.json_data['global'][number]['conditions']
        this_platform = self.json_data['global'][number]['platform']
        this_criteria = self.json_data['global'][number]['criteria']
        this_event = self.json_data['global'][number]['event']

        if number == 0:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_1 and this_event == bcp_balance["cgp_9_fixed"][number]):
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 1:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_1 and this_event == bcp_balance["cgp_9_fixed"][number]):
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 2:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_2 and this_event == bcp_balance["cgp_9_fixed"][number]):
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 3:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == platform_win_amazon
                    and this_criteria == criteria_cgp_3 and this_event == bcp_balance["cgp_9_fixed"][number]):
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 4:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_2 and this_event == bcp_balance["cgp_9_fixed"][number]):
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 5:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_win_amazon
                    and this_criteria == criteria_cgp_3 and this_event == bcp_balance["cgp_9_fixed"][number]):
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 6:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == []
                    and this_criteria == criteria_cgp_4 and this_event == bcp_balance["cgp_9_fixed"][number]):
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 7:
            if (this_conditions == conditions_cgp_payer_gt_25 and this_platform == []
                    and this_criteria == criteria_cgp_4 and this_event == bcp_balance["cgp_9_fixed"][number]):
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')
        elif number == 8:
            if (this_conditions == conditions_cgp_payer_gt_25 and this_platform == []
                    and this_criteria == criteria_cgp_4 and
                    this_event == bcp_balance["cgp_6_9_dynamic"][int(cgp_9_buttons['day'].value)]):
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], True, 'Баланс и conditions корректные')
            else:
                self.update_button(cgp_9_buttons[f'button_{number + 1}'], False, 'Баланс или conditions некорректные')

    def check_other_wo_field(self, number):
        from buttons import other_bans_wo_field_buttons
        this_id = self.json_data_other_wo_field['global'][number]['_id']
        check_bans_should_be = []
        check_bans_in_json = self.json_data_other_wo_field['global'][number]['conditions']['banOffers']

        for item in self.all_ids_other_wo_field:
            if item != this_id:
                check_bans_should_be.append(item)
            else:
                pass
        if set(check_bans_should_be) == set(check_bans_in_json) and len(check_bans_should_be) == len(
                check_bans_in_json):
            self.update_button(other_bans_wo_field_buttons[f'button_{number + 1}'], True, 'Баны корректны')
        else:
            self.update_button(other_bans_wo_field_buttons[f'button_{number + 1}'], False, 'Баны некорректны')

    def check_other_with_field(self, number):
        from buttons import other_bans_with_field_buttons
        needed_bans = self.json_data_with_field['global'][number]['conditions']['banOffers']
        input_value = [int(val) for val in other_bans_with_field_buttons["input_bans_field"].value.split(",")]
        self.compare_reference_with_field = input_value

        if number == 0:
            if set(input_value) == set(needed_bans) and len(input_value) == len(needed_bans):
                self.update_button(other_bans_with_field_buttons[f'button_{number + 1}'], True, 'Баны корректны')
            else:
                self.update_button(other_bans_with_field_buttons[f'button_{number + 1}'], False, 'Баны некорректны')
        else:
            compare = self.compare_reference_with_field
            for item in compare:
                if item == other_bans_with_field_buttons[f'button_{number + 1}'].text:
                    compare.remove(item)
                    compare.append(self.json_data_with_field['global'][0]['_id'])
            if set(compare) == set(needed_bans) and len(compare) == len(needed_bans):
                self.update_button(other_bans_with_field_buttons[f'button_{number + 1}'], True, 'Баны корректны')
            else:
                self.update_button(other_bans_with_field_buttons[f'button_{number + 1}'], False, 'Баны некорректны')

    def check_oto_2(self, buttons, level, number):
        from buttons import oto_2_buttons_7_18, oto_2_buttons_19
        this_id = self.json_data_oto_2['global'][number]['_id']
        errors, result_text, bans_should_be = [], [], []
        bans_in_json = self.json_data_oto_2['global'][number]['conditions']['banOffers']
        this_conditions = self.json_data_oto_2['global'][number]['conditions']
        this_event = self.json_data_oto_2['global'][number]['event']
        this_criteria = self.json_data_oto_2['global'][number]['criteria']
        ignore_keys = {"banOffers", "allowByOneOf", "denyByOneOf"}

        if level == 7:
            if oto_2_buttons_7_18['launch'].value == "1":
                conditions = bcp_balance['oto_2_conditions_7_18_1']
                event = bcp_balance['oto_2_event_all_1']
            elif oto_2_buttons_7_18['launch'].value == "2":
                conditions = bcp_balance['oto_2_conditions_7_18_2']
                event= bcp_balance['oto_2_event_7_18_2']
        elif level == 19:
            if oto_2_buttons_19['launch'].value == "1":
                conditions = bcp_balance['oto_2_conditions_19_1']
                event = bcp_balance['oto_2_event_all_1']
            elif oto_2_buttons_19['launch'].value == "2":
                conditions = bcp_balance['oto_2_conditions_19_2']
                event= bcp_balance['oto_2_event_19_2']
        criteria = bcp_balance['lto_criteria'][2]

        try:
            needed_denies_1 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][1]['or'][0]['denyByOneOf']
            needed_denies_2 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][1]['or'][1]['denyByOneOf']
            needed_allows_1 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][1]['or'][0]['allowByOneOf']
            needed_allows_2 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][1]['or'][1]['allowByOneOf']
        except (KeyError, IndexError):
            needed_denies_1 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][0]['or'][0]['denyByOneOf']
            needed_denies_2 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][0]['or'][1]['denyByOneOf']
            needed_allows_1 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][0]['or'][0]['allowByOneOf']
            needed_allows_2 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][0]['or'][1]['allowByOneOf']
        input_denies = [int(val) for val in buttons["input_denies_field"].value.split(",")]
        input_allows = [int(val) for val in buttons["input_allows_field"].value.split(",")]

        self.add_bans(self.all_ids_oto_2, this_id, bans_should_be)

        if set(input_denies) != set(needed_denies_1):
            self.add_error(errors, 'denies 1', input_denies, needed_denies_1)
        if set(input_denies) != set(needed_denies_2):
            self.add_error(errors, 'denies 2', input_denies, needed_denies_2)
        if set(input_allows) != set(needed_allows_1):
            self.add_error(errors, 'allows 1', input_allows, needed_allows_1)
        if set(input_allows) != set(needed_allows_2):
            self.add_error(errors, 'allows 2', input_allows, needed_allows_2)
        if set(bans_should_be) != set(bans_in_json):
            self.add_error(errors, 'bans', bans_should_be, bans_in_json)
        if not self.equal_ignore(this_conditions, conditions[number], ignore_keys):
            self.add_error(errors, 'conditions', conditions[number], this_conditions)
        self.add_error(errors, 'event', event[number], this_event)
        self.add_error(errors, 'criteria', criteria, this_criteria)

        self.json_check_end_other(errors, buttons, number, result_text, this_id)

    def compare(self, number):
        from buttons import json_compare_buttons_1, json_compare_buttons_2
        balance_1 = self.json_data_compare_1['global'][number]['event']
        balance_2 = self.json_data_compare_2['global'][number]['event']

        if balance_1 == balance_2:
            self.update_button(json_compare_buttons_1[f'button_{number + 1}'], True, 'Баланс совпадает')
            self.update_button(json_compare_buttons_2[f'button_{number + 1}'], True, 'Баланс совпадает')
        else:
            self.update_button(json_compare_buttons_1[f'button_{number + 1}'], False, 'Баланс не совпадает')
            self.update_button(json_compare_buttons_2[f'button_{number + 1}'], False, 'Баланс не совпадает')

    def among_new_ts(self, number):
        from buttons import among_balance_new_tc_buttons
        this_balance = self.json_data['global'][number]['event']
        this_segmentation = self.json_data['global'][number]['conditions']['filter']
        segmentation = [
            {
                "segment_1": "secret_data"
            },
            {
                "segment_2": "secret_data"
            },
            {
                "segment_3": "secret_data"
            }
        ]

        if this_balance == data_balance['among_new_ts'][number] and this_segmentation == segmentation[number]:
            self.update_button(among_balance_new_tc_buttons[f'button_{number + 1}'], True, 'Баланс и сегментация корректные')
        else:
            self.update_button(among_balance_new_tc_buttons[f'button_{number + 1}'], False, 'Баланс или сегментация некорректные')

    def among_average(self, number):
        from buttons import among_balance_average_buttons
        this_balance = self.json_data_among_average['global'][number]['event']
        this_filter = self.json_data_among_average['global'][number]['conditions']['filter']
        filter = [
            {"filter_1": "secret_data"},
            {"filter_2": "secret_data"},
            {"filter_3": "secret_data"}
        ]

        if this_balance == data_balance['among_me'][number] and this_filter == filter[number]:
            self.update_button(among_balance_average_buttons[f'button_{number + 1}'], True, 'Баланс и сегментация корректные')
        else:
            self.update_button(among_balance_average_buttons[f'button_{number + 1}'], False, 'Баланс или сегментация некорректные')

    def labyrinth_balance(self, country, number):
        from buttons import labyrinth_balance_ww_buttons, labyrinth_balance_cn_buttons
        filter = [
            {
                "segment_1": "secret_data"
            },
            {
                "segment_2": "secret_data"
            },
            {
                "segment_3": "secret_data"
            },
            {
                "segment_4": "secret_data"
            }
        ]

        if country == 'ww':
            this_filter = self.json_data['global'][number]['conditions']['filter']
            this_balance = self.json_data['global'][number]['event']
            if this_filter == filter[number] and this_balance == data_balance['labyrinth_ww'][number]:
                self.update_button(labyrinth_balance_ww_buttons[f'button_{number + 1}'], True, 'Баланс и сегментация корректные')
            else:
                self.update_button(labyrinth_balance_ww_buttons[f'button_{number + 1}'], False, 'Баланс или сегментация некорректные')
        elif country == 'cn':
            this_filter = self.json_data['global'][number]['conditions']['filter']
            this_balance = self.json_data['global'][number]['event']
            if this_filter == filter[number] and this_balance == data_balance['labyrinth_cn'][number]:
                self.update_button(labyrinth_balance_cn_buttons[f'button_{number + 1}'], True, 'Баланс и сегментация корректные')
            else:
                self. update_button(labyrinth_balance_cn_buttons[f'button_{number + 1}'], False, 'Баланс или сегментация некорректные')

    def tickets_balance_checker(self, amount, number, minus_day):
        from buttons import (tickets_balance_checker_buttons_11, tickets_balance_checker_buttons_10,
                             tickets_balance_checker_buttons_9, tickets_balance_checker_buttons_3,
                             tickets_balance_checker_buttons_10_extra, tickets_balance_checker_buttons_7)

        buttons_dict = {
            11: tickets_balance_checker_buttons_11,
            10: tickets_balance_checker_buttons_10,
            9: tickets_balance_checker_buttons_9,
            3: tickets_balance_checker_buttons_3,
            7: tickets_balance_checker_buttons_7,
            "10_extra": tickets_balance_checker_buttons_10_extra
        }
        buttons = buttons_dict[amount]

        this_id = self.json_data['global'][number]['_id']
        this_event = self.json_data['global'][number]['event']
        result_text = []
        event_should_be = bcp_balance[f'tickets_{amount}'][int(buttons['day'].value) - minus_day][number]
        if this_event == event_should_be:
            self.update_button(buttons[f'button_{number + 1}'], True, 'Баланс корректный')
        else:
            self.update_button(buttons[f'button_{number + 1}'], False, 'Баланс некорректный')
            result_text.append(f'{this_id}:\n ER: {event_should_be}\n AR: {this_event}')

        self.errors_output(result_text, buttons)

    def check_comeback(self, number):
        from buttons import comeback_json_buttons
        errors, result_text, bans_should_be = [], [], []
        criteria = bcp_balance['lto_criteria'][2]
        conditions = bcp_balance['comeback_conditions']
        ignore_keys = {"banOffers"}
        if comeback_json_buttons['launch'].value == '1':
            event = bcp_balance['comeback_event_1']
        elif comeback_json_buttons['launch'].value == '2':
            event = bcp_balance['comeback_event_2']

        this_event = self.json_data['global'][number]['event']
        this_criteria = self.json_data['global'][number]['criteria']
        this_conditions = self.json_data['global'][number]['conditions']
        this_id = self.json_data['global'][number]['_id']
        bans_in_json = self.json_data['global'][number]['conditions']['banOffers']

        self.add_bans(self.ltos_list, this_id, bans_should_be)

        if set(bans_should_be) != set(bans_in_json):
            self.add_error(errors, 'bans', bans_should_be, bans_in_json)
        if not self.equal_ignore(this_conditions, conditions[number], ignore_keys):
            self.add_error(errors, 'conditions', conditions[number], this_conditions)
        self.add_error(errors, 'criteria', criteria, this_criteria)
        self.add_error(errors, 'event', event[number], this_event)

        self.json_check_end_other(errors, comeback_json_buttons, number, result_text, this_id)

    def check_gf_real(self, number):
        from buttons import gf_real_json_buttons
        conditions = bcp_balance['gf_real_conditions']
        event = bcp_balance['gf_real_event']
        ignore_keys = {"banOffers", "compatibleEvents"}
        errors, result_text, bans_should_be = [], [], []

        if gf_real_json_buttons['day'].value == '9':
            conditions = bcp_balance['gf_real_conditions_9']
        elif gf_real_json_buttons['day'].value == '23':
            conditions = bcp_balance['gf_real_conditions_23']
        if gf_real_json_buttons['launch'].value == 'ww':
            criteria = bcp_balance['lto_criteria'][2]
            this_compatible_events = self.json_data['global'][number]['conditions']['compatibleEvents'][0]
        elif gf_real_json_buttons['launch'].value == 'cn':
            criteria = bcp_balance['cn_criteria'][0]
            this_compatible_events = self.json_data['global'][number]['conditions']['compatibleEvents'][0]
        elif gf_real_json_buttons['launch'].value == 'ruby':
            criteria = {}
            event = bcp_balance['gf_ruby_event']
            if gf_real_json_buttons['day'].value == '9':
                conditions = bcp_balance['gf_ruby_conditions_9']
            elif gf_real_json_buttons['day'].value == '23':
                conditions = bcp_balance['gf_ruby_conditions_23']

        this_event = self.json_data['global'][number]['event']
        this_criteria = self.json_data['global'][number]['criteria']
        this_conditions = self.json_data['global'][number]['conditions']
        this_id = self.json_data['global'][number]['_id']
        bans_in_json = self.json_data['global'][number]['conditions']['banOffers']

        self.add_bans(self.ltos_list, this_id, bans_should_be)

        if set(bans_should_be) != set(bans_in_json):
            errors.append(f"bans: \nER: {bans_should_be}\nAR: {bans_in_json}")
        if not self.equal_ignore(this_conditions, conditions[number], ignore_keys):
            self.add_error(errors, 'conditions', conditions[number], this_conditions)
        self.add_error(errors, "criteria", criteria, this_criteria)
        self.add_error(errors, "event", event[number], this_event)
        if gf_real_json_buttons['launch'].value != 'ruby':
            self.add_error(errors, "compatibleEvents", int(gf_real_json_buttons['compatible_events_field'].value),this_compatible_events)
        else:
            pass

        self.json_check_end_other(errors, gf_real_json_buttons, number, result_text, this_id)


headers_get = {
    'X-Application-Key': 'secret_key'
}
get_url = "secret_get_url"
profile_fetcher = ProfileFetcher(get_url, headers_get)

put_url = "secret_put_url"
headers_put = {
    'X-Application-Key': 'secret_key',
    'Content-Type': 'application/json'
}
tags_updater = TagsUpdater(put_url, headers_put)
