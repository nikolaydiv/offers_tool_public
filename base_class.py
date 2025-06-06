import json
import time
import requests
import flet as ft
import re
import gdown

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

    def update_tags_tickets(self, value_1, value_2, value_3):  # здесь и далее будут использоваться json-заглушки с secret_tag_N вместо реального названия тега
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
        self.ltos_11 = []
        self.otos_11 = []
        self.ltos_10 = []
        self.otos_10 = []
        self.ltos_9 = []
        self.otos_9 = []
        self.ltos_8 = []
        self.otos_8 = []
        self.ltos_7 = []
        self.otos_7 = []
        self.ltos_3 = []
        self.otos_3 = []
        self.json_data_11 = None
        self.json_data_10 = None
        self.json_data_9 = None
        self.json_data_8 = None
        self.json_data_7 = None
        self.json_data_3 = None
        self.json_data_criteria = None
        self.json_data_no_hint_bans = None
        self.json_data_no_hint_balance = None
        self.json_data_bcp_previous = None
        self.json_data_bcp_actual = None
        self.json_data_cgp_6 = None
        self.json_data_cgp_9 = None
        self.json_data_other_wo_field = None
        self.all_ids_other_wo_field = None
        self.json_data_with_field = None
        self.compare_reference_with_field = None
        self.json_data_oto_2 = None
        self.all_ids_oto_2 = None
        self.json_data_compare_1 = None
        self.json_data_compare_2 = None
        self.json_data_among_new_ts = None
        self.json_data_among_average = None
        self.json_data_labyrinth_balance_ww = None
        self.json_data_labyrinth_balance_cn = None
        self.json_data_tickets_balance_11 = None
        self.json_data_tickets_balance_10 = None
        self.json_data_tickets_balance_10_extra = None
        self.json_data_tickets_balance_9 = None
        self.json_data_tickets_balance_7 = None
        self.json_data_tickets_balance_3 = None

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
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons, tickets_bans_9_buttons,
                             tickets_bans_3_buttons, tickets_bans_7_buttons)
        if tickets_number == 11:
            for item in self.json_data_11['global']:
                if item['type'] == 'limited_time_offer':
                    self.ltos_11.append(item['_id'])
                elif item['type'] == 'one_time_offer':
                    self.otos_11.append(item['_id'])
            for i, item in enumerate(self.json_data_11['global'], start=1):
                button_key = f'ban_11_{i}'
                tickets_bans_11_buttons[button_key].text = item['_id']
                tickets_bans_11_buttons[button_key].disabled = False
                tickets_bans_11_buttons[button_key].update()
        elif tickets_number == 10:
            for item in self.json_data_10['global']:
                if item['type'] == 'limited_time_offer':
                    self.ltos_10.append(item['_id'])
                elif item['type'] == 'one_time_offer':
                    self.otos_10.append(item['_id'])
            for i, item in enumerate(self.json_data_10['global'], start=1):
                button_key = f'ban_10_{i}'
                tickets_bans_10_buttons[button_key].text = item['_id']
                tickets_bans_10_buttons[button_key].disabled = False
                tickets_bans_10_buttons[button_key].update()
        elif tickets_number == 9:
            for item in self.json_data_9['global']:
                if item['type'] == 'limited_time_offer':
                    self.ltos_9.append(item['_id'])
                elif item['type'] == 'one_time_offer':
                    self.otos_9.append(item['_id'])
            for i, item in enumerate(self.json_data_9['global'], start=1):
                button_key = f'ban_9_{i}'
                tickets_bans_9_buttons[button_key].text = item['_id']
                tickets_bans_9_buttons[button_key].disabled = False
                tickets_bans_9_buttons[button_key].update()
        elif tickets_number == 7:
            for item in self.json_data_7['global']:
                if item['type'] == 'limited_time_offer':
                    self.ltos_7.append(item['_id'])
                elif item['type'] == 'one_time_offer':
                    self.otos_7.append(item['_id'])
            for i, item in enumerate(self.json_data_7['global'], start=1):
                button_key = f'ban_7_{i}'
                tickets_bans_7_buttons[button_key].text = item['_id']
                tickets_bans_7_buttons[button_key].disabled = False
                tickets_bans_7_buttons[button_key].update()
        elif tickets_number == 3:
            for item in self.json_data_3['global']:
                if item['type'] == 'limited_time_offer':
                    self.ltos_3.append(item['_id'])
                elif item['type'] == 'one_time_offer':
                    self.otos_3.append(item['_id'])
            for i, item in enumerate(self.json_data_3['global'], start=1):
                button_key = f'ban_3_{i}'
                tickets_bans_3_buttons[button_key].text = item['_id']
                tickets_bans_3_buttons[button_key].disabled = False
                tickets_bans_3_buttons[button_key].update()

    def download_json_other(self, kind):
        from buttons import (tickets_criteria_buttons, no_hint_bans_buttons, no_hint_balance_buttons,
                                            bcp_previous_buttons, bcp_actual_buttons, cgp_6_buttons, cgp_9_buttons,
                                            other_bans_wo_field_buttons, other_bans_with_field_buttons, oto_2_buttons,
                                            json_compare_buttons_1, json_compare_buttons_2,
                                            among_balance_new_tc_buttons, among_balance_average_buttons,
                                            labyrinth_balance_ww_buttons, labyrinth_balance_cn_buttons,
                                            tickets_balance_checker_buttons_11, tickets_balance_checker_buttons_10,
                                            tickets_balance_checker_buttons_9, tickets_balance_checker_buttons_3,
                                            tickets_balance_checker_buttons_10_extra, tickets_balance_checker_buttons_7)
        if kind == 'criteria':
            for i, item in enumerate(self.json_data_criteria['global'], start=1):
                button_key = f'button_{i}'
                tickets_criteria_buttons[button_key].text = item['_id']
                tickets_criteria_buttons[button_key].disabled = False
                tickets_criteria_buttons[button_key].update()
        elif kind == 'no_hint_bans':
            for i, item in enumerate(self.json_data_no_hint_bans['global'], start=1):
                button_key = f'button_{i}'
                no_hint_bans_buttons[button_key].text = item['_id']
                no_hint_bans_buttons[button_key].disabled = False
                no_hint_bans_buttons[button_key].update()
        elif kind == 'no_hint_balance':
            for i, item in enumerate(self.json_data_no_hint_balance['global'], start=1):
                button_key = f'button_{i}'
                no_hint_balance_buttons[button_key].text = item['_id']
                no_hint_balance_buttons[button_key].disabled = False
                no_hint_balance_buttons[button_key].update()
        elif kind == 'bcp_previous':
            for i, item in enumerate(self.json_data_bcp_previous['global'], start=1):
                button_key = f'button_{i}'
                bcp_previous_buttons[button_key].text = item['_id']
                bcp_previous_buttons[button_key].disabled = False
                bcp_previous_buttons[button_key].update()
        elif kind == 'bcp_actual':
            for i, item in enumerate(self.json_data_bcp_actual['global'], start=1):
                button_key = f'button_{i}'
                bcp_actual_buttons[button_key].text = item['_id']
                bcp_actual_buttons[button_key].disabled = False
                bcp_actual_buttons[button_key].update()
        elif kind == 'cgp_6':
            for i, item in enumerate(self.json_data_cgp_6['global'], start=1):
                button_key = f'button_{i}'
                cgp_6_buttons[button_key].text = item['_id']
                cgp_6_buttons[button_key].disabled = False
                cgp_6_buttons[button_key].update()
        elif kind == 'cgp_9':
            for i, item in enumerate(self.json_data_cgp_9['global'], start=1):
                button_key = f'button_{i}'
                cgp_9_buttons[button_key].text = item['_id']
                cgp_9_buttons[button_key].disabled = False
                cgp_9_buttons[button_key].update()
        elif kind == "other_wo_field":
            self.all_ids_other_wo_field = [item['_id'] for item in self.json_data_other_wo_field['global']]
            for i, item in enumerate(self.all_ids_other_wo_field, start=1):
                button_key = f'button_{i}'
                other_bans_wo_field_buttons[button_key].text = item
                other_bans_wo_field_buttons[button_key].disabled = False
                other_bans_wo_field_buttons[button_key].update()
        elif kind == "other_with_field":
            for i, item in enumerate(self.json_data_with_field['global'], start=1):
                button_key = f'button_{i}'
                other_bans_with_field_buttons[button_key].text = item['_id']
                other_bans_with_field_buttons[button_key].disabled = False
                other_bans_with_field_buttons[button_key].update()
        elif kind == "oto_2":
            self.all_ids_oto_2 = [item['_id'] for item in self.json_data_oto_2['global']]
            for i, item in enumerate(self.all_ids_oto_2, start=1):
                button_key = f'button_{i}'
                oto_2_buttons[button_key].text = item
                oto_2_buttons[button_key].disabled = False
                oto_2_buttons[button_key].update()
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
        elif kind == "among_new_ts":
            for i, item in enumerate(self.json_data_among_new_ts['global'], start=1):
                button_key = f'button_{i}'
                among_balance_new_tc_buttons[button_key].text = item['_id']
                among_balance_new_tc_buttons[button_key].disabled = False
                among_balance_new_tc_buttons[button_key].update()
        elif kind == "among_average":
            for i, item in enumerate(self.json_data_among_average['global'], start=1):
                button_key = f'button_{i}'
                among_balance_average_buttons[button_key].text = item['_id']
                among_balance_average_buttons[button_key].disabled = False
                among_balance_average_buttons[button_key].update()
        elif kind == "labyrinth_balance_ww":
            for i, item in enumerate(self.json_data_labyrinth_balance_ww['global'], start=1):
                button_key = f'button_{i}'
                labyrinth_balance_ww_buttons[button_key].text = item['_id']
                labyrinth_balance_ww_buttons[button_key].disabled = False
                labyrinth_balance_ww_buttons[button_key].update()
        elif kind == "labyrinth_balance_cn":
            for i, item in enumerate(self.json_data_labyrinth_balance_cn['global'], start=1):
                button_key = f'button_{i}'
                labyrinth_balance_cn_buttons[button_key].text = item['_id']
                labyrinth_balance_cn_buttons[button_key].disabled = False
                labyrinth_balance_cn_buttons[button_key].update()
        elif kind == 'tickets_balance_11':
            for i, item in enumerate(self.json_data_tickets_balance_11['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_11[button_key].text = item['_id']
                tickets_balance_checker_buttons_11[button_key].disabled = False
                tickets_balance_checker_buttons_11[button_key].update()
        elif kind == 'tickets_balance_10':
            for i, item in enumerate(self.json_data_tickets_balance_10['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_10[button_key].text = item['_id']
                tickets_balance_checker_buttons_10[button_key].disabled = False
                tickets_balance_checker_buttons_10[button_key].update()
        elif kind == 'tickets_balance_9':
            for i, item in enumerate(self.json_data_tickets_balance_9['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_9[button_key].text = item['_id']
                tickets_balance_checker_buttons_9[button_key].disabled = False
                tickets_balance_checker_buttons_9[button_key].update()
        elif kind == 'tickets_balance_7':
            for i, item in enumerate(self.json_data_tickets_balance_7['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_7[button_key].text = item['_id']
                tickets_balance_checker_buttons_7[button_key].disabled = False
                tickets_balance_checker_buttons_7[button_key].update()
        elif kind == 'tickets_balance_3':
            for i, item in enumerate(self.json_data_tickets_balance_3['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_3[button_key].text = item['_id']
                tickets_balance_checker_buttons_3[button_key].disabled = False
                tickets_balance_checker_buttons_3[button_key].update()
        elif kind == 'tickets_balance_10_extra':
            for i, item in enumerate(self.json_data_tickets_balance_10_extra['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_10_extra[button_key].text = item['_id']
                tickets_balance_checker_buttons_10_extra[button_key].disabled = False
                tickets_balance_checker_buttons_10_extra[button_key].update()

    def reset_tickets(self, tickets_number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons, tickets_bans_9_buttons,
                             tickets_bans_3_buttons, tickets_bans_7_buttons)
        if tickets_number == 11:
            self.ltos_11 = []
            self.otos_11 = []
            self.json_data_11 = None
            self._update_button_text("")
            for item in tickets_bans_11_buttons:
                if re.match(r'^ban_11_\d+$', item):
                    tickets_bans_11_buttons[item].text = "offer id"
                    tickets_bans_11_buttons[item].color = ft.colors.PRIMARY
                    tickets_bans_11_buttons[item].disabled = True
                    tickets_bans_11_buttons[item].update()
        elif tickets_number == 10:
            self.ltos_10 = []
            self.otos_10 = []
            self.json_data_10 = None
            self._update_button_text("")
            for item in tickets_bans_10_buttons:
                if re.match(r'^ban_10_\d+$', item):
                    tickets_bans_10_buttons[item].text = "offer id"
                    tickets_bans_10_buttons[item].color = ft.colors.PRIMARY
                    tickets_bans_10_buttons[item].disabled = True
                    tickets_bans_10_buttons[item].update()
        elif tickets_number == 9:
            self.ltos_9 = []
            self.otos_9 = []
            self.json_data_9 = None
            self._update_button_text("")
            for item in tickets_bans_9_buttons:
                if re.match(r'^ban_9_\d+$', item):
                    tickets_bans_9_buttons[item].text = "offer id"
                    tickets_bans_9_buttons[item].color = ft.colors.PRIMARY
                    tickets_bans_9_buttons[item].disabled = True
                    tickets_bans_9_buttons[item].update()
        elif tickets_number == 7:
            self.ltos_7 = []
            self.otos_7 = []
            self.json_data_7 = None
            self._update_button_text("")
            for item in tickets_bans_7_buttons:
                if re.match(r'^ban_7_\d+$', item):
                    tickets_bans_7_buttons[item].text = "offer id"
                    tickets_bans_7_buttons[item].color = ft.colors.PRIMARY
                    tickets_bans_7_buttons[item].disabled = True
                    tickets_bans_7_buttons[item].update()
        elif tickets_number == 3:
            self.ltos_3 = []
            self.otos_3 = []
            self.json_data_3 = None
            self._update_button_text("")
            for item in tickets_bans_3_buttons:
                if re.match(r'^ban_3_\d+$', item):
                    tickets_bans_3_buttons[item].text = "offer id"
                    tickets_bans_3_buttons[item].color = ft.colors.PRIMARY
                    tickets_bans_3_buttons[item].disabled = True
                    tickets_bans_3_buttons[item].update()

    def reset_other(self, kind):
        from buttons import (tickets_criteria_buttons, no_hint_bans_buttons, no_hint_balance_buttons,
                                            bcp_previous_buttons, bcp_actual_buttons, cgp_6_buttons, cgp_9_buttons,
                                            other_bans_wo_field_buttons, other_bans_with_field_buttons, oto_2_buttons,
                                            json_compare_buttons_1, json_compare_buttons_2,
                                            among_balance_new_tc_buttons, among_balance_average_buttons,
                                            labyrinth_balance_ww_buttons, labyrinth_balance_cn_buttons,
                                            tickets_balance_checker_buttons_11, tickets_balance_checker_buttons_10,
                                            tickets_balance_checker_buttons_9, tickets_balance_checker_buttons_3,
                                            tickets_balance_checker_buttons_10_extra, tickets_balance_checker_buttons_7)
        if kind == 'criteria':
            self.json_data_criteria = None
            self._update_button_text("")
            for item in tickets_criteria_buttons:
                if re.match(r'^button_\d+$', item):
                    tickets_criteria_buttons[item].text = "offer id"
                    tickets_criteria_buttons[item].color = ft.colors.PRIMARY
                    tickets_criteria_buttons[item].disabled = True
                    tickets_criteria_buttons[item].update()
        elif kind == 'no_hint_bans':
            self.json_data_no_hint_bans = None
            self._update_button_text("")
            for item in no_hint_bans_buttons:
                if re.match(r'^button_\d+$', item):
                    no_hint_bans_buttons[item].text = "offer id"
                    no_hint_bans_buttons[item].color = ft.colors.PRIMARY
                    no_hint_bans_buttons[item].disabled = True
                    no_hint_bans_buttons[item].update()
        elif kind == 'no_hint_balance':
            self.json_data_no_hint_balance = None
            self._update_button_text("")
            for item in no_hint_balance_buttons:
                if re.match(r'^button_\d+$', item):
                    no_hint_balance_buttons[item].text = "offer id"
                    no_hint_balance_buttons[item].color = ft.colors.PRIMARY
                    no_hint_balance_buttons[item].disabled = True
                    no_hint_balance_buttons[item].update()
        elif kind == 'bcp_previous':
            self.json_data_bcp_previous = None
            self._update_button_text("")
            for item in bcp_previous_buttons:
                if re.match(r'^button_\d+$', item):
                    bcp_previous_buttons[item].text = "offer id"
                    bcp_previous_buttons[item].color = ft.colors.PRIMARY
                    bcp_previous_buttons[item].disabled = True
                    bcp_previous_buttons[item].update()
                if re.match(r'^dynamic_items_\d+$', item):
                    bcp_previous_buttons[item].value = ""
                    bcp_previous_buttons[item].update()
        elif kind == 'bcp_actual':
            self.json_data_bcp_actual = None
            self._update_button_text("")
            for item in bcp_actual_buttons:
                if re.match(r'^button_\d+$', item):
                    bcp_actual_buttons[item].text = "offer id"
                    bcp_actual_buttons[item].color = ft.colors.PRIMARY
                    bcp_actual_buttons[item].disabled = True
                    bcp_actual_buttons[item].update()
        elif kind == 'cgp_6':
            self.json_data_cgp_6 = None
            self._update_button_text("")
            for item in cgp_6_buttons:
                if re.match(r'^button_\d+$', item):
                    cgp_6_buttons[item].text = "offer id"
                    cgp_6_buttons[item].color = ft.colors.PRIMARY
                    cgp_6_buttons[item].disabled = True
                    cgp_6_buttons[item].update()
        elif kind == 'cgp_9':
            self.json_data_cgp_9 = None
            self._update_button_text("")
            for item in cgp_9_buttons:
                if re.match(r'^button_\d+$', item):
                    cgp_9_buttons[item].text = "offer id"
                    cgp_9_buttons[item].color = ft.colors.PRIMARY
                    cgp_9_buttons[item].disabled = True
                    cgp_9_buttons[item].update()
        elif kind == 'other_wo_field':
            self.json_data_other_wo_field = None
            self._update_button_text("")
            for item in other_bans_wo_field_buttons:
                if re.match(r'^button_\d+$', item):
                    other_bans_wo_field_buttons[item].text = "offer id"
                    other_bans_wo_field_buttons[item].color = ft.colors.PRIMARY
                    other_bans_wo_field_buttons[item].disabled = True
                    other_bans_wo_field_buttons[item].update()
        elif kind == 'other_with_field':
            self.json_data_with_field = None
            self._update_button_text("")
            for item in other_bans_with_field_buttons:
                if re.match(r'^button_\d+$', item):
                    other_bans_with_field_buttons[item].text = "offer id"
                    other_bans_with_field_buttons[item].color = ft.colors.PRIMARY
                    other_bans_with_field_buttons[item].disabled = True
                    other_bans_with_field_buttons[item].update()
        elif kind == 'oto_2':
            self.json_data_oto_2 = None
            self._update_button_text("")
            for item in oto_2_buttons:
                if re.match(r'^button_\d+$', item):
                    oto_2_buttons[item].text = "offer id"
                    oto_2_buttons[item].color = ft.colors.PRIMARY
                    oto_2_buttons[item].disabled = True
                    oto_2_buttons[item].update()
                oto_2_buttons['input_denies_field'].value = ""
                oto_2_buttons['input_denies_field'].update()
                oto_2_buttons['input_allows_field'].value = ""
                oto_2_buttons['input_allows_field'].update()
        elif kind == "compare":
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
        elif kind == 'among_new_ts':
            self.json_data_among_new_ts = None
            self._update_button_text("")
            for item in among_balance_new_tc_buttons:
                if re.match(r'^button_\d+$', item):
                    among_balance_new_tc_buttons[item].text = "offer id"
                    among_balance_new_tc_buttons[item].color = ft.colors.PRIMARY
                    among_balance_new_tc_buttons[item].disabled = True
                    among_balance_new_tc_buttons[item].update()
        elif kind == 'among_average':
            self.json_data_among_average = None
            self._update_button_text("")
            among_balance_average_buttons['me_field'].value = ""
            among_balance_average_buttons['me_field'].update()
            for item in among_balance_average_buttons:
                if re.match(r'^button_\d+$', item):
                    among_balance_average_buttons[item].text = "offer id"
                    among_balance_average_buttons[item].color = ft.colors.PRIMARY
                    among_balance_average_buttons[item].disabled = True
                    among_balance_average_buttons[item].update()
        elif kind == 'labyrinth_balance_ww':
            self.json_data_labyrinth_balance_ww = None
            self._update_button_text("")
            for item in labyrinth_balance_ww_buttons:
                if re.match(r'^button_\d+$', item):
                    labyrinth_balance_ww_buttons[item].text = "offer id"
                    labyrinth_balance_ww_buttons[item].color = ft.colors.PRIMARY
                    labyrinth_balance_ww_buttons[item].disabled = True
                    labyrinth_balance_ww_buttons[item].update()
        elif kind == 'labyrinth_balance_cn':
            self.json_data_labyrinth_balance_cn = None
            self._update_button_text("")
            for item in labyrinth_balance_cn_buttons:
                if re.match(r'^button_\d+$', item):
                    labyrinth_balance_cn_buttons[item].text = "offer id"
                    labyrinth_balance_cn_buttons[item].color = ft.colors.PRIMARY
                    labyrinth_balance_cn_buttons[item].disabled = True
                    labyrinth_balance_cn_buttons[item].update()
        elif kind == 'tickets_balance_11':
            self.json_data_tickets_balance_11 = None
            self._update_button_text("")
            for item in tickets_balance_checker_buttons_11:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_11[item].text = "offer id"
                    tickets_balance_checker_buttons_11[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_11[item].disabled = True
                tickets_balance_checker_buttons_11[item].update()
        elif kind == 'tickets_balance_10':
            self.json_data_tickets_balance_10 = None
            self._update_button_text("")
            for item in tickets_balance_checker_buttons_10:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_10[item].text = "offer id"
                    tickets_balance_checker_buttons_10[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_10[item].disabled = True
                tickets_balance_checker_buttons_10[item].update()
        elif kind == 'tickets_balance_9':
            self.json_data_tickets_balance_9 = None
            self._update_button_text("")
            for item in tickets_balance_checker_buttons_9:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_9[item].text = "offer id"
                    tickets_balance_checker_buttons_9[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_9[item].disabled = True
                tickets_balance_checker_buttons_9[item].update()
        elif kind == 'tickets_balance_7':
            self.json_data_tickets_balance_7 = None
            self._update_button_text("")
            for item in tickets_balance_checker_buttons_7:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_7[item].text = "offer id"
                    tickets_balance_checker_buttons_7[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_7[item].disabled = True
                tickets_balance_checker_buttons_7[item].update()
        elif kind == 'tickets_balance_3':
            self.json_data_tickets_balance_3 = None
            self._update_button_text("")
            for item in tickets_balance_checker_buttons_3:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_3[item].text = "offer id"
                    tickets_balance_checker_buttons_3[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_3[item].disabled = True
                tickets_balance_checker_buttons_3[item].update()
        elif kind == 'tickets_balance_10_extra':
            self.json_data_tickets_balance_10_extra = None
            self._update_button_text("")
            for item in tickets_balance_checker_buttons_10_extra:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_10_extra[item].text = "offer id"
                    tickets_balance_checker_buttons_10_extra[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_10_extra[item].disabled = True
                tickets_balance_checker_buttons_10_extra[item].update()

    def check_bans_lto(self, tickets_number, number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons, tickets_bans_9_buttons,
                             tickets_bans_3_buttons, tickets_bans_7_buttons)
        criteria_263_b = {
            "criteria_263_b": "secret_data"
        }
        criteria_263_a_or_not_in = {
            "criteria_263_a_or_not_in": "secret_data"
        }

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баны и критерий корректны'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баны или критерий некорректны'
                button.color = ft.colors.RED
            button.update()

        if tickets_number == 11:
            this_id = self.json_data_11['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_11['global'][number]['conditions']['banOffers']
            criteria = self.json_data_11['global'][number]['criteria']
            for item in self.ltos_11:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
            if set(bans_should_be) == set(bans_in_json) and len(bans_should_be) == len(
                    bans_in_json) and criteria == criteria_263_a_or_not_in:
                update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], True)
            else:
                update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], False)
        elif tickets_number == 10:
            this_id = self.json_data_10['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_10['global'][number]['conditions']['banOffers']
            criteria = self.json_data_10['global'][number]['criteria']
            for item in self.ltos_10:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
            if set(bans_should_be) == set(bans_in_json) and len(bans_should_be) == len(
                    bans_in_json) and criteria == criteria_263_a_or_not_in:
                update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], True)
            else:
                update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], False)
        elif tickets_number == 9:
            this_id = self.json_data_9['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_9['global'][number]['conditions']['banOffers']
            criteria = self.json_data_9['global'][number]['criteria']
            for item in self.ltos_9:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
            if set(bans_should_be) == set(bans_in_json) and len(bans_should_be) == len(
                    bans_in_json) and criteria == criteria_263_a_or_not_in:
                update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], True)
            else:
                update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], False)
        elif tickets_number == 7:
            this_id = self.json_data_7['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_7['global'][number]['conditions']['banOffers']
            criteria = self.json_data_7['global'][number]['criteria']
            for item in self.ltos_7:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
            if set(bans_should_be) == set(bans_in_json) and len(bans_should_be) == len(
                    bans_in_json) and criteria == criteria_263_b:
                update_button(tickets_bans_7_buttons[f'ban_7_{number + 1}'], True)
            else:
                update_button(tickets_bans_7_buttons[f'ban_7_{number + 1}'], False)
        elif tickets_number == 3:
            this_id = self.json_data_3['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_3['global'][number]['conditions']['banOffers']
            criteria = self.json_data_3['global'][number]['criteria']
            for item in self.ltos_3:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
            if set(bans_should_be) == set(bans_in_json) and len(bans_should_be) == len(
                    bans_in_json) and criteria == criteria_263_a_or_not_in:
                update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], True)
            else:
                update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], False)

    def check_bans_oto(self, tickets_number, number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons, tickets_bans_9_buttons,
                             tickets_bans_3_buttons, tickets_bans_7_buttons)
        criteria_263_b = {
            "criteria_263_b": "secret_data"
        }
        criteria_263_a_or_not_in = {
            "criteria_263_a_or_not_in": "secret_data"
        }

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баны, денаи и критерий корректны'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баны, денаи или критерий некорректны'
                button.color = ft.colors.RED
            button.update()

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

        if tickets_number == 11:
            this_id = self.json_data_11['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_11['global'][number]['conditions']['banOffers']
            criteria = self.json_data_11['global'][number]['criteria']
            for item in self.otos_11:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
        elif tickets_number == 10:
            this_id = self.json_data_10['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_10['global'][number]['conditions']['banOffers']
            criteria = self.json_data_10['global'][number]['criteria']
            for item in self.otos_10:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
        elif tickets_number == 9:
            this_id = self.json_data_9['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_9['global'][number]['conditions']['banOffers']
            criteria = self.json_data_9['global'][number]['criteria']
            for item in self.otos_9:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
        elif tickets_number == 7:
            this_id = self.json_data_7['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_7['global'][number]['conditions']['banOffers']
            criteria = self.json_data_7['global'][number]['criteria']
            for item in self.otos_7:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
        elif tickets_number == 3:
            this_id = self.json_data_3['global'][number]['_id']
            bans_should_be = []
            bans_in_json = self.json_data_3['global'][number]['conditions']['banOffers']
            criteria = self.json_data_3['global'][number]['criteria']
            for item in self.otos_3:
                if item != this_id:
                    bans_should_be.append(item)
                elif item == this_id:
                    pass
        # OTO 11
        if tickets_number == 11:
            denies_in_json_1 = get_denies(self.json_data_11, number, deny_paths_1)
            denies_in_json_2 = get_denies(self.json_data_11, number, deny_paths_2)

            if (set(bans_should_be) == set(bans_in_json)
                    and len(bans_should_be) == len(bans_in_json)
                    and set(denies_in_json_1) == set(self.ltos_11)
                    and len(denies_in_json_1) == len(self.ltos_11)
                    and set(denies_in_json_2) == set(self.ltos_11)
                    and len(denies_in_json_2) == len(self.ltos_11)
                    and criteria == criteria_263_a_or_not_in):
                update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], True)
            else:
                update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], False)
        # OTO 10
        elif tickets_number == 10:
            denies_in_json_1 = get_denies(self.json_data_10, number, deny_paths_1)
            denies_in_json_2 = get_denies(self.json_data_10, number, deny_paths_2)

            if (set(bans_should_be) == set(bans_in_json)
                    and len(bans_should_be) == len(bans_in_json)
                    and set(denies_in_json_1) == set(self.ltos_10)
                    and len(denies_in_json_1) == len(self.ltos_10)
                    and set(denies_in_json_2) == set(self.ltos_10)
                    and len(denies_in_json_2) == len(self.ltos_10)
                    and criteria == criteria_263_a_or_not_in):
                update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], True)
            else:
                update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], False)
        # OTO 9
        elif tickets_number == 9:
            denies_in_json_1 = get_denies(self.json_data_9, number, deny_paths_1)
            denies_in_json_2 = get_denies(self.json_data_9, number, deny_paths_2)

            if (set(bans_should_be) == set(bans_in_json)
                    and len(bans_should_be) == len(bans_in_json)
                    and set(denies_in_json_1) == set(self.ltos_9)
                    and len(denies_in_json_1) == len(self.ltos_9)
                    and set(denies_in_json_2) == set(self.ltos_9)
                    and len(denies_in_json_2) == len(self.ltos_9)
                    and criteria == criteria_263_a_or_not_in):
                update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], True)
            else:
                update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], False)
        # OTO 7
        elif tickets_number == 7:
            denies_in_json_1 = get_denies(self.json_data_7, number, deny_paths_1)
            denies_in_json_2 = get_denies(self.json_data_7, number, deny_paths_2)

            if (set(bans_should_be) == set(bans_in_json)
                    and len(bans_should_be) == len(bans_in_json)
                    and set(denies_in_json_1) == set(self.ltos_7)
                    and len(denies_in_json_1) == len(self.ltos_7)
                    and set(denies_in_json_2) == set(self.ltos_7)
                    and len(denies_in_json_2) == len(self.ltos_7)
                    and criteria == criteria_263_b):
                update_button(tickets_bans_7_buttons[f'ban_7_{number + 1}'], True)
            else:
                update_button(tickets_bans_7_buttons[f'ban_7_{number + 1}'], False)
        # OTO 3
        elif tickets_number == 3:
            denies_in_json = get_denies(self.json_data_3, number, deny_paths_3)

            if (set(bans_should_be) == set(bans_in_json)
                    and len(bans_should_be) == len(bans_in_json)
                    and set(denies_in_json) == set(self.ltos_3)
                    and len(denies_in_json) == len(self.ltos_3)
                    and criteria == criteria_263_a_or_not_in):
                update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], True)
            else:
                update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], False)

    def check_criteria(self):
        from buttons import tickets_criteria_buttons
        criteria_new_263 = {
            "criteria_new_263": "secret_data"
        }
        for i, item in enumerate(self.json_data_criteria['global'], start=0):
            if self.json_data_criteria['global'][i]['criteria'] == criteria_new_263:
                tickets_criteria_buttons[f'button_{i + 1}'].text = "Критерий корректный"
                tickets_criteria_buttons[f'button_{i + 1}'].color = ft.colors.GREEN
                tickets_criteria_buttons[f'button_{i + 1}'].update()
            else:
                tickets_criteria_buttons[f'button_{i + 1}'].text = "Критерий некорректный"
                tickets_criteria_buttons[f'button_{i + 1}'].color = ft.colors.RED
                tickets_criteria_buttons[f'button_{i + 1}'].update()
        time.sleep(3)
        for i, item in enumerate(self.json_data_criteria['global'], start=0):
            tickets_criteria_buttons[f'button_{i + 1}'].text = self.json_data_criteria['global'][i]['_id']
            tickets_criteria_buttons[f'button_{i + 1}'].update()

    def check_bans_no_hint(self, number):
        from buttons import no_hint_bans_buttons
        bans_should_be = []
        bans_in_json = self.json_data_no_hint_bans['global'][number]['conditions']['banOffers']
        this_product_id = self.json_data_no_hint_bans['global'][number]['event']['product_id']
        all_ids = self.json_data_no_hint_bans['global']
        for item in all_ids:
            if this_product_id != item['event']['product_id']:
                bans_should_be.append(item['_id'])
            elif this_product_id == item['event']['product_id']:
                pass
        if set(bans_in_json) == set(bans_should_be) and len(bans_in_json) == len(bans_should_be):
            no_hint_bans_buttons[f'button_{number + 1}'].color = ft.colors.GREEN
            no_hint_bans_buttons[f'button_{number + 1}'].text = 'Баны корректны'
            no_hint_bans_buttons[f'button_{number + 1}'].update()
        else:
            no_hint_bans_buttons[f'button_{number + 1}'].color = ft.colors.RED
            no_hint_bans_buttons[f'button_{number + 1}'].text = 'Баны некорректны'
            no_hint_bans_buttons[f'button_{number + 1}'].update()

    def check_balance_no_hint(self, number):
        from buttons import no_hint_balance_buttons
        criteria_new_263 = {
            "criteria_new_263": "secret_data"
        }
        filters = [{'filter_1': "secret_data"},
                   {'filter_2': "secret_data"},
                   {'filter_3': "secret_data"},
                   {'filter_4': "secret_data"}]
        event_1_1 = {"event_1_1": "secret_data"}
        event_1_2 = {"event_1_2": "secret_data"}
        event_1_3 = {"event_1_3": "secret_data"}
        event_1_4 = {"event_1_4": "secret_data"}
        event_2_1 = {"event_2_1": "secret_data"}
        event_2_2 = {"event_2_2": "secret_data"}
        event_2_3 = {"event_2_3": "secret_data"}
        event_2_4 = {"event_2_4": "secret_data"}
        event_3_1 = {"event_3_1": "secret_data"}
        event_3_2 = {"event_3_2": "secret_data"}
        event_3_3 = {"event_3_3": "secret_data"}
        event_3_4 = {"event_3_4": "secret_data"}
        event_4_1 = {"event_4_1": "secret_data"}
        event_4_2 = {"event_4_2": "secret_data"}
        event_4_3 = {"event_4_3": "secret_data"}
        event_4_4 = {"event_4_4": "secret_data"}
        this_level_start = self.json_data_no_hint_balance['global'][number]['conditions']['level_start']
        this_only_for_buyer = self.json_data_no_hint_balance['global'][number]['conditions']['OnlyForBuyer']
        this_filter = self.json_data_no_hint_balance['global'][number]['conditions']['filter']
        this_trigger = self.json_data_no_hint_balance['global'][number]['conditions']['trigger']
        this_trigger_param = self.json_data_no_hint_balance['global'][number]['conditions']['trigger_param']
        this_skin_id = self.json_data_no_hint_balance['global'][number]['conditions']['skin_id']
        this_event = self.json_data_no_hint_balance['global'][number]['event']
        this_criteria = self.json_data_no_hint_balance['global'][number]['criteria']
        this_packname = self.json_data_no_hint_balance['global'][number]['conditions']['packName']
        this_platform = self.json_data_no_hint_balance['global'][number]['platform']
        if number in range(4, 16):
            this_delay = self.json_data_no_hint_balance['global'][number]['conditions']['delay']

        conditions = {
            0: {"filter": filters[0], "event": event_1_1, "trigger_param": 400006},
            1: {"filter": filters[1], "event": event_1_2, "trigger_param": 400006},
            2: {"filter": filters[2], "event": event_1_3, "trigger_param": 400006},
            3: {"filter": filters[3], "event": event_1_4, "trigger_param": 400006},
            4: {"filter": filters[0], "event": event_2_1, "trigger_param": 400008, "delay": 30},
            5: {"filter": filters[1], "event": event_2_2, "trigger_param": 400008, "delay": 30},
            6: {"filter": filters[2], "event": event_2_3, "trigger_param": 400008, "delay": 30},
            7: {"filter": filters[3], "event": event_2_4, "trigger_param": 400008, "delay": 30},
            8: {"filter": filters[0], "event": event_3_1, "trigger_param": 400003, "delay": 60},
            9: {"filter": filters[1], "event": event_3_2, "trigger_param": 400003, "delay": 60},
            10: {"filter": filters[2], "event": event_3_3, "trigger_param": 400003, "delay": 60},
            11: {"filter": filters[3], "event": event_3_4, "trigger_param": 400003, "delay": 60},
            12: {"filter": filters[0], "event": event_4_1, "trigger_param": 400009, "delay": 45},
            13: {"filter": filters[1], "event": event_4_2, "trigger_param": 400009, "delay": 45},
            14: {"filter": filters[2], "event": event_4_3, "trigger_param": 400009, "delay": 45},
            15: {"filter": filters[3], "event": event_4_4, "trigger_param": 400009, "delay": 45},
        }

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс корректный'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс некорректный'
                button.color = ft.colors.RED
            button.update()

        if number in conditions:
            params = conditions[number]

            is_active = (
                    this_level_start == 7 and
                    this_only_for_buyer is True and
                    this_filter == params['filter'] and
                    this_trigger == 'no_hint' and
                    this_trigger_param == params['trigger_param'] and
                    this_skin_id == 10078 and
                    this_event == params['event'] and
                    this_criteria == criteria_new_263 and
                    this_packname == 'events1' and
                    this_platform == []
            )

            if 'delay' in params:
                is_active = is_active and this_delay == params['delay']

            button_key = f'button_{number + 1}'
            update_button(no_hint_balance_buttons[button_key], is_active)

    def check_bcp_previous(self, number):
        from buttons import bcp_previous_buttons
        platform_ios_android_samsung = [
            "ios",
            "android",
            "samsung"
        ]
        criteria_non_default = {"criteria_non_default": "secret_data"}
        criteria_default = {"criteria_default": "secret_data"}
        criteria = {"criteria": "secret_data"}
        platform_win_amazon = [
            "win",
            "amazon"
        ]
        criteria_rb_rf = {"criteria_rb_rf": "secret_data"}
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

        this_conditions = self.json_data_bcp_previous['global'][number]['conditions']
        this_event = self.json_data_bcp_previous['global'][number]['event']
        this_platform = self.json_data_bcp_previous['global'][number]['platform']
        this_criteria = self.json_data_bcp_previous['global'][number]['criteria']

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс и conditions корректные'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс или conditions некорректный'
                button.color = ft.colors.RED
            button.update()

        if number == 0:
            if (this_conditions == conditions_non_payer_t_3 and this_platform == platform_ios_android_samsung and
                    this_criteria == criteria_non_default and this_event == event_non_payer_t_3[0]):
                update_button(bcp_previous_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_previous_buttons[f'button_{number + 1}'], False)
        elif number == 1:
            if (this_conditions == conditions_non_payer_default and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_default and this_event == event_non_payer_default[0]):
                update_button(bcp_previous_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_previous_buttons[f'button_{number + 1}'], False)
        elif number == 2:
            if (this_conditions == conditions_non_payer_default and this_platform == platform_win_amazon
                    and this_criteria == criteria and this_event == event_non_payer_default[0]):
                update_button(bcp_previous_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_previous_buttons[f'button_{number + 1}'], False)
        elif number == 3:
            if (this_conditions == conditions_non_payer_t_3 and this_platform == platform_ios_android_samsung and
                    this_criteria == criteria_non_default and this_event == event_non_payer_t_3[1]):
                update_button(bcp_previous_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_previous_buttons[f'button_{number + 1}'], False)
        elif number == 4:
            if (this_conditions == conditions_non_payer_default and this_platform == platform_ios_android_samsung and
                    this_criteria == criteria_default and this_event == event_non_payer_default[1]):
                update_button(bcp_previous_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_previous_buttons[f'button_{number + 1}'], False)
        elif number == 5:
            if (this_conditions == conditions_non_payer_default and this_platform == platform_win_amazon
                    and this_criteria == criteria and this_event == event_non_payer_default[1]):
                update_button(bcp_previous_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_previous_buttons[f'button_{number + 1}'], False)
        elif number == 6:
            if (this_conditions == conditions_payer and this_platform == [] and this_criteria == criteria_rb_rf
                    and this_event == event_payer[0]):
                update_button(bcp_previous_buttons[f'button_{number + 1}'], True)
                bcp_previous_buttons['dynamic_items_1'].value = (
                    self.json_data_bcp_previous['global'][6]['event']['rewards'][0]['itemId'],
                    self.json_data_bcp_previous['global'][6]['event']['rewards'][0]['count'],
                    self.json_data_bcp_previous['global'][6]['event']['rewards'][1]['itemId'],
                    self.json_data_bcp_previous['global'][6]['event']['rewards'][1]['count'],
                    self.json_data_bcp_previous['global'][6]['event']['rewards'][2]['itemId'],
                    self.json_data_bcp_previous['global'][6]['event']['rewards'][2]['count'],
                    self.json_data_bcp_previous['global'][6]['event']['rewards'][3]['itemId'],
                    self.json_data_bcp_previous['global'][6]['event']['rewards'][3]['count']
                )
                bcp_previous_buttons['dynamic_items_1'].update()
            else:
                update_button(bcp_previous_buttons[f'button_{number + 1}'], False)
        elif number == 7:
            if (this_conditions == conditions_payer and this_platform == [] and this_criteria == criteria_rb_rf
                    and this_event == event_payer[1]):
                update_button(bcp_previous_buttons[f'button_{number + 1}'], True)
                bcp_previous_buttons['dynamic_items_2'].value = (
                    self.json_data_bcp_previous['global'][7]['event']['rewards'][0]['itemId'],
                    self.json_data_bcp_previous['global'][7]['event']['rewards'][0]['count'],
                    self.json_data_bcp_previous['global'][7]['event']['rewards'][1]['itemId'],
                    self.json_data_bcp_previous['global'][7]['event']['rewards'][1]['count'],
                    self.json_data_bcp_previous['global'][7]['event']['rewards'][2]['itemId'],
                    self.json_data_bcp_previous['global'][7]['event']['rewards'][2]['count'],
                    self.json_data_bcp_previous['global'][7]['event']['rewards'][3]['itemId'],
                    self.json_data_bcp_previous['global'][7]['event']['rewards'][3]['count']
                )
                bcp_previous_buttons['dynamic_items_2'].update()
            else:
                update_button(bcp_previous_buttons[f'button_{number + 1}'], False)
        elif number == 8:
            if (this_conditions == conditions_payer and this_platform == [] and this_criteria == criteria_rb_rf
                    and this_event == event_payer[2]):
                update_button(bcp_previous_buttons[f'button_{number + 1}'], True)
                bcp_previous_buttons['dynamic_items_3'].value = (
                    self.json_data_bcp_previous['global'][8]['event']['rewards'][0]['itemId'],
                    self.json_data_bcp_previous['global'][8]['event']['rewards'][0]['count'],
                    self.json_data_bcp_previous['global'][8]['event']['rewards'][1]['itemId'],
                    self.json_data_bcp_previous['global'][8]['event']['rewards'][1]['count'],
                    self.json_data_bcp_previous['global'][8]['event']['rewards'][2]['itemId'],
                    self.json_data_bcp_previous['global'][8]['event']['rewards'][2]['count'],
                    self.json_data_bcp_previous['global'][8]['event']['rewards'][3]['itemId'],
                    self.json_data_bcp_previous['global'][8]['event']['rewards'][3]['count']
                )
                bcp_previous_buttons['dynamic_items_3'].update()
            else:
                update_button(bcp_previous_buttons[f'button_{number + 1}'], False)

    def check_bcp_actual(self, number):
        from buttons import bcp_actual_buttons
        platform_ios_android_samsung = [
            "ios",
            "android",
            "samsung"
        ]
        criteria_non_default = {"criteria_non_default": "secret_data"}
        criteria_default = {"criteria_default": "secret_data"}
        criteria = {"criteria_usual": "secret_data"}
        platform_win_amazon = [
            "win",
            "amazon"
        ]
        criteria_rb_rf = {"criteria_rb_rf": "secret_data"}

        this_packname = self.json_data_bcp_actual['global'][number]['conditions']['packName']
        this_level_start = self.json_data_bcp_actual['global'][number]['conditions']['level_start']
        this_only_for_buyer = self.json_data_bcp_actual['global'][number]['conditions']['OnlyForBuyer']
        this_subtype = self.json_data_bcp_actual['global'][number]['conditions']['subtype']
        this_show_in_item_info = self.json_data_bcp_actual['global'][number]['conditions']['show_in_item_info']
        this_platform = self.json_data_bcp_actual['global'][number]['platform']
        this_criteria = self.json_data_bcp_actual['global'][number]['criteria']
        this_event = self.json_data_bcp_actual['global'][number]['event']
        if number == 0 or number == 1 or number == 2 or number == 6:
            this_skin_id = self.json_data_bcp_actual['global'][number]['conditions']['skin_id']
        if number == 2 or number == 5:
            this_event_uwp = self.json_data_bcp_actual['global'][number]['event']

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Запуск и баланс корректные'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Запуск и баланс некорректные'
                button.color = ft.colors.RED
            button.update()

        if int(bcp_actual_buttons['day'].value) in range(0, 24):
            double = "bcp_0-23_fixed"
        else:
            double = "bcp_24-27_double"

        if number == 0:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_skin_id == int(bcp_actual_buttons["skin_id_field"].value) and this_subtype == 1002
                    and this_show_in_item_info is True and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_non_default and
                    this_event == bcp_balance[double][number]):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 1:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_skin_id == int(bcp_actual_buttons["skin_id_field"].value) and this_subtype == 1000
                    and this_show_in_item_info is True and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_default and
                    this_event == bcp_balance[double][number]):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 2:
            event_default = self.json_data_bcp_actual['global'][1]['event']
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_skin_id == int(bcp_actual_buttons["skin_id_field"].value) and this_subtype == 1000
                    and this_show_in_item_info is True and this_platform == platform_win_amazon and this_criteria == criteria
                    and this_event_uwp == event_default and
                    this_event == bcp_balance[double][number]):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 3:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_subtype == 1002 and this_show_in_item_info is True
                    and this_platform == platform_ios_android_samsung and this_criteria == criteria_non_default
                    and this_event == bcp_balance[double][number]):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 4:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_subtype == 1000 and this_show_in_item_info is True
                    and this_platform == platform_ios_android_samsung and this_criteria == criteria_default
                    and this_event == bcp_balance[double][number]):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 5:
            event_default = self.json_data_bcp_actual['global'][4]['event']
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_subtype == 1000 and this_show_in_item_info is True
                    and this_platform == platform_win_amazon and this_criteria == criteria and this_event_uwp == event_default
                    and this_event == bcp_balance[double][number]):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 6:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is True
                    and this_skin_id == int(bcp_actual_buttons["skin_id_field"].value) and this_subtype == 1000
                    and this_show_in_item_info is True and this_platform == [] and this_criteria == criteria_rb_rf
                    and this_event == bcp_balance["bcp_dynamic"][int(bcp_actual_buttons['day'].value)][0]):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 7:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is True
                    and this_subtype == 1000 and this_show_in_item_info is True
                    and this_platform == [] and this_criteria == criteria_rb_rf
                    and this_event == bcp_balance["bcp_dynamic"][int(bcp_actual_buttons['day'].value)][1]):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 8:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is True
                    and this_subtype == 1000 and this_show_in_item_info is True
                    and this_platform == [] and this_criteria == criteria_rb_rf
                    and this_event == bcp_balance["bcp_dynamic"][int(bcp_actual_buttons['day'].value)][2]):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)

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
        criteria_cgp_1 = {"criteria_cgp_1": "secret_data"}
        criteria_cgp_2 = {"criteria_cgp_2": "secret_data"}
        criteria_cgp_3 = {"criteria_cgp_3": "secret_data"}
        criteria_cgp_4 = {"criteria_cgp_4": "secret_data"}

        this_conditions = self.json_data_cgp_6['global'][number]['conditions']
        this_platform = self.json_data_cgp_6['global'][number]['platform']
        this_criteria = self.json_data_cgp_6['global'][number]['criteria']
        this_event = self.json_data_cgp_6['global'][number]['event']

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс и conditions корректные'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс или conditions некорректные'
                button.color = ft.colors.RED
            button.update()

        if number == 0:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_1 and this_event == bcp_balance["cgp_6_fixed"][number]):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 1:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_2 and this_event == bcp_balance["cgp_6_fixed"][number]):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 2:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_win_amazon
                    and this_criteria == criteria_cgp_3 and this_event == bcp_balance["cgp_6_fixed"][number]):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 3:
            if (this_conditions == conditions_cgp_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_1 and this_event == bcp_balance["cgp_6_fixed"][number]):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 4:
            if (this_conditions == conditions_cgp_payer and this_platform == [] and this_criteria == criteria_cgp_4
                    and this_event == bcp_balance["cgp_6_fixed"][number]):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 5:
            if (this_conditions == conditions_cgp_payer and this_platform == [] and this_criteria == criteria_cgp_4
                    and this_event == bcp_balance["cgp_6_9_dynamic"][int(cgp_6_buttons['day'].value)]):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)

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
        criteria_cgp_1 = {"criteria_cgp_1": "secret_data"}
        criteria_cgp_2 = {"criteria_cgp_2": "secret_data"}
        criteria_cgp_3 = {"criteria_cgp_3": "secret_data"}
        criteria_cgp_4 = {"criteria_cgp_4": "secret_data"}

        this_conditions = self.json_data_cgp_9['global'][number]['conditions']
        this_platform = self.json_data_cgp_9['global'][number]['platform']
        this_criteria = self.json_data_cgp_9['global'][number]['criteria']
        this_event = self.json_data_cgp_9['global'][number]['event']

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс и conditions корректные'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс или conditions некорректные'
                button.color = ft.colors.RED
            button.update()

        if number == 0:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_1 and this_event == bcp_balance["cgp_9_fixed"][number]):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 1:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_1 and this_event == bcp_balance["cgp_9_fixed"][number]):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 2:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_2 and this_event == bcp_balance["cgp_9_fixed"][number]):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 3:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == platform_win_amazon
                    and this_criteria == criteria_cgp_3 and this_event == bcp_balance["cgp_9_fixed"][number]):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 4:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_2 and this_event == bcp_balance["cgp_9_fixed"][number]):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 5:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_win_amazon
                    and this_criteria == criteria_cgp_3 and this_event == bcp_balance["cgp_9_fixed"][number]):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 6:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == []
                    and this_criteria == criteria_cgp_4 and this_event == bcp_balance["cgp_9_fixed"][number]):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 7:
            if (this_conditions == conditions_cgp_payer_gt_25 and this_platform == []
                    and this_criteria == criteria_cgp_4 and this_event == bcp_balance["cgp_9_fixed"][number]):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 8:
            if (this_conditions == conditions_cgp_payer_gt_25 and this_platform == []
                    and this_criteria == criteria_cgp_4 and
                    this_event == bcp_balance["cgp_6_9_dynamic"][int(cgp_9_buttons['day'].value)]):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)

    def check_other_wo_field(self, number):
        from buttons import other_bans_wo_field_buttons
        this_id = self.json_data_other_wo_field['global'][number]['_id']
        check_bans_should_be = []
        check_bans_in_json = self.json_data_other_wo_field['global'][number]['conditions']['banOffers']

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баны корректны'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баны некорректны'
                button.color = ft.colors.RED
            button.update()

        for item in self.all_ids_other_wo_field:
            if item != this_id:
                check_bans_should_be.append(item)
            else:
                pass
        if set(check_bans_should_be) == set(check_bans_in_json) and len(check_bans_should_be) == len(
                check_bans_in_json):
            update_button(other_bans_wo_field_buttons[f'button_{number + 1}'], True)
        else:
            update_button(other_bans_wo_field_buttons[f'button_{number + 1}'], False)

    def check_other_with_field(self, number):
        from buttons import other_bans_with_field_buttons
        needed_bans = self.json_data_with_field['global'][number]['conditions']['banOffers']
        input_value = [int(val) for val in other_bans_with_field_buttons["input_bans_field"].value.split(",")]
        self.compare_reference_with_field = input_value

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баны корректны'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баны некорректны'
                button.color = ft.colors.RED
            button.update()

        if number == 0:
            if set(input_value) == set(needed_bans) and len(input_value) == len(needed_bans):
                update_button(other_bans_with_field_buttons[f'button_{number + 1}'], True)
            else:
                update_button(other_bans_with_field_buttons[f'button_{number + 1}'], False)
        else:
            compare = self.compare_reference_with_field
            for item in compare:
                if item == other_bans_with_field_buttons[f'button_{number + 1}'].text:
                    compare.remove(item)
                    compare.append(self.json_data_with_field['global'][0]['_id'])
            if set(compare) == set(needed_bans) and len(compare) == len(needed_bans):
                update_button(other_bans_with_field_buttons[f'button_{number + 1}'], True)
            else:
                update_button(other_bans_with_field_buttons[f'button_{number + 1}'], False)

    def check_oto_2(self, number):
        from buttons import oto_2_buttons
        this_id = self.json_data_oto_2['global'][number]['_id']
        check_bans_should_be = []
        check_bans_in_json = self.json_data_oto_2['global'][number]['conditions']['banOffers']
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
        input_denies = [int(val) for val in oto_2_buttons["input_denies_field"].value.split(",")]
        input_allows = [int(val) for val in oto_2_buttons["input_allows_field"].value.split(",")]

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баны, denies и allows корректны'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баны, denies или allows некорректны'
                button.color = ft.colors.RED
            button.update()

        for item in self.all_ids_oto_2:
            if item != this_id:
                check_bans_should_be.append(item)
            else:
                pass

        if (set(input_denies) == set(needed_denies_1) and len(input_denies) == len(needed_denies_1)
                and set(input_denies) == set(needed_denies_2) and len(input_denies) == len(needed_denies_2)
                and set(input_allows) == set(needed_allows_1) and len(input_allows) == len(needed_allows_1)
                and set(input_allows) == set(needed_allows_2) and len(input_allows) == len(needed_allows_2)
                and set(check_bans_should_be) == set(check_bans_in_json) and len(check_bans_should_be) == len(
                    check_bans_in_json)):
            update_button(oto_2_buttons[f'button_{number + 1}'], True)
        else:
            update_button(oto_2_buttons[f'button_{number + 1}'], False)

    def compare(self, number):
        from buttons import json_compare_buttons_1, json_compare_buttons_2
        balance_1 = self.json_data_compare_1['global'][number]['event']
        balance_2 = self.json_data_compare_2['global'][number]['event']

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс совпадает'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс не совпадает'
                button.color = ft.colors.RED
            button.update()

        if balance_1 == balance_2:
            update_button(json_compare_buttons_1[f'button_{number + 1}'], True)
            update_button(json_compare_buttons_2[f'button_{number + 1}'], True)
        else:
            update_button(json_compare_buttons_1[f'button_{number + 1}'], False)
            update_button(json_compare_buttons_2[f'button_{number + 1}'], False)

    def among_new_ts(self, number):
        from buttons import among_balance_new_tc_buttons
        this_balance = self.json_data_among_new_ts['global'][number]['event']
        this_segmentation = self.json_data_among_new_ts['global'][number]['conditions']['filter']
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

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс и сегментация корректные'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс или сегментация некорректные'
                button.color = ft.colors.RED
            button.update()

        if this_balance == data_balance['among_new_ts'][number] and this_segmentation == segmentation[number]:
            update_button(among_balance_new_tc_buttons[f'button_{number + 1}'], True)
        else:
            update_button(among_balance_new_tc_buttons[f'button_{number + 1}'], False)

    def among_average(self, number):
        from buttons import among_balance_average_buttons
        this_balance = self.json_data_among_average['global'][number]['event']
        this_filter = self.json_data_among_average['global'][number]['conditions']['filter']
        filter = [
            {"filter_1": "secret_data"},
            {"filter_2": "secret_data"},
            {"filter_3": "secret_data"}
        ]

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс и сегментация корректные'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс или сегментация некорректные'
                button.color = ft.colors.RED
            button.update()

        if this_balance == data_balance['among_me'][number] and this_filter == filter[number]:
            update_button(among_balance_average_buttons[f'button_{number + 1}'], True)
        else:
            update_button(among_balance_average_buttons[f'button_{number + 1}'], False)

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

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс и сегментация корректные'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс или сегментация некорректные'
                button.color = ft.colors.RED
            button.update()

        if country == 'ww':
            this_filter = self.json_data_labyrinth_balance_ww['global'][number]['conditions']['filter']
            this_balance = self.json_data_labyrinth_balance_ww['global'][number]['event']
            if this_filter == filter[number] and this_balance == data_balance['labyrinth_ww'][number]:
                update_button(labyrinth_balance_ww_buttons[f'button_{number + 1}'], True)
            else:
                update_button(labyrinth_balance_ww_buttons[f'button_{number + 1}'], False)
        elif country == 'cn':
            this_filter = self.json_data_labyrinth_balance_cn['global'][number]['conditions']['filter']
            this_balance = self.json_data_labyrinth_balance_cn['global'][number]['event']
            if this_filter == filter[number] and this_balance == data_balance['labyrinth_cn'][number]:
                update_button(labyrinth_balance_cn_buttons[f'button_{number + 1}'], True)
            else:
                update_button(labyrinth_balance_cn_buttons[f'button_{number + 1}'], False)

    def tickets_balance_checker(self, amount, number):
        from buttons import (tickets_balance_checker_buttons_11, tickets_balance_checker_buttons_10,
                                            tickets_balance_checker_buttons_9, tickets_balance_checker_buttons_3,
                                            tickets_balance_checker_buttons_10_extra, tickets_balance_checker_buttons_7)

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс корректный'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс некорректный'
                button.color = ft.colors.RED
            button.update()

        if amount == 22:
            this_event = self.json_data_tickets_balance_11['global'][number]['event']

            if this_event == bcp_balance['tickets_11'][int(tickets_balance_checker_buttons_11['day'].value)][number]:
                update_button(tickets_balance_checker_buttons_11[f'button_{number + 1}'], True)
            else:
                update_button(tickets_balance_checker_buttons_11[f'button_{number + 1}'], False)
        elif amount == 20:
            this_event = self.json_data_tickets_balance_10['global'][number]['event']

            if this_event == bcp_balance['tickets_10'][int(tickets_balance_checker_buttons_10['day'].value) - 8][number]:
                update_button(tickets_balance_checker_buttons_10[f'button_{number + 1}'], True)
            else:
                update_button(tickets_balance_checker_buttons_10[f'button_{number + 1}'], False)
        elif amount == 18:
            this_event = self.json_data_tickets_balance_9['global'][number]['event']

            if this_event == bcp_balance['tickets_9'][int(tickets_balance_checker_buttons_9['day'].value) - 19][number]:
                update_button(tickets_balance_checker_buttons_9[f'button_{number + 1}'], True)
            else:
                update_button(tickets_balance_checker_buttons_9[f'button_{number + 1}'], False)
        elif amount == 14:
            this_event = self.json_data_tickets_balance_7['global'][number]['event']

            if this_event == bcp_balance['tickets_7'][int(tickets_balance_checker_buttons_7['day'].value)][number]:
                update_button(tickets_balance_checker_buttons_7[f'button_{number + 1}'], True)
            else:
                update_button(tickets_balance_checker_buttons_7[f'button_{number + 1}'], False)
        elif amount == 6:
            this_event = self.json_data_tickets_balance_3['global'][number]['event']

            if this_event == bcp_balance['tickets_3'][int(tickets_balance_checker_buttons_3['day'].value) - 25][number]:
                update_button(tickets_balance_checker_buttons_3[f'button_{number + 1}'], True)
            else:
                update_button(tickets_balance_checker_buttons_3[f'button_{number + 1}'], False)
        elif amount == "20_extra":
            this_event = self.json_data_tickets_balance_10_extra['global'][number]['event']

            if this_event == bcp_balance['tickets_10_extra'][int(tickets_balance_checker_buttons_10_extra['day'].value)][number]:
                update_button(tickets_balance_checker_buttons_10_extra[f'button_{number + 1}'], True)
            else:
                update_button(tickets_balance_checker_buttons_10_extra[f'button_{number + 1}'], False)


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
