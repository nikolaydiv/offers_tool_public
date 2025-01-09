import json
import time
import requests
import flet as ft
import re
import gdown

file_id_balance = "12_nH1IBi2SeaZq663ibpuwLmEXVzgxBc"
url_balance = f"https://drive.google.com/uc?id={file_id_balance}"  # скачивание json-заглушки
output_file_balance = "downloaded_balance.json"
gdown.download(url_balance, output_file_balance, quiet=True)
with open(output_file_balance, 'r', encoding='utf-8') as a:
    raw_data = a.read()
clean_content = re.sub(r"//.*", "", raw_data)
data_balance = json.loads(clean_content)


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
        self.ltos_3 = []
        self.otos_3 = []
        self.json_data_11 = None
        self.json_data_10 = None
        self.json_data_9 = None
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
        self.json_data_tickets_balance_9 = None
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
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons,
                             tickets_bans_9_buttons, tickets_bans_3_buttons)
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
        if tickets_number == 10:
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
                             tickets_balance_checker_buttons_9, tickets_balance_checker_buttons_3)
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
            pattern_1 = [50, 75, 100, 125, 150, 200, 250, 275, 300, 400, 500]
            pattern_2 = [75, 100, 150, 175, 200, 225, 250, 275, 300, 400, 500]
            for i, item in enumerate(self.json_data_tickets_balance_11['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_11[button_key].text = item['_id']
                tickets_balance_checker_buttons_11[button_key].disabled = False
                tickets_balance_checker_buttons_11[button_key].update()
            if tickets_balance_checker_buttons_11['pattern'].value == '50,75,100,125,150,200,250,275,300,400,500':
                for i in range(1, 12):
                    tickets_balance_checker_buttons_11[f'field_lto_{i}'].value = pattern_1[i - 1]
                    tickets_balance_checker_buttons_11[f'field_oto_{i + 11}'].value = pattern_1[i - 1] * 2
                    tickets_balance_checker_buttons_11[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_11[f'field_oto_{i + 11}'].update()
            else:
                for i in range(1, 12):
                    tickets_balance_checker_buttons_11[f'field_lto_{i}'].value = pattern_2[i - 1]
                    tickets_balance_checker_buttons_11[f'field_oto_{i + 11}'].value = pattern_2[i - 1] * 2
                    tickets_balance_checker_buttons_11[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_11[f'field_oto_{i + 11}'].update()
            for i, item in enumerate(self.json_data_tickets_balance_11['global'], start=1):
                button_key = f'bundle_{i}'
                tickets_balance_checker_buttons_11[button_key].text = item['event']['product_id']
                tickets_balance_checker_buttons_11[button_key].disabled = False
                tickets_balance_checker_buttons_11[button_key].update()
        elif kind == 'tickets_balance_10':
            pattern_1 = [50, 75, 125, 150, 175, 200, 225, 250, 300, 400]
            pattern_2 = [75, 100, 150, 175, 225, 250, 275, 300, 350, 450]
            pattern_3 = [75, 100, 150, 175, 200, 225, 250, 275, 300, 400]
            pattern_4 = [100, 125, 150, 175, 225, 250, 275, 300, 350, 450]
            pattern_5 = [100, 125, 150, 175, 200, 225, 250, 275, 300, 400]
            pattern_6 = [100, 125, 150, 175, 225, 250, 275, 300, 350, 450]
            for i, item in enumerate(self.json_data_tickets_balance_10['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_10[button_key].text = item['_id']
                tickets_balance_checker_buttons_10[button_key].disabled = False
                tickets_balance_checker_buttons_10[button_key].update()
            if tickets_balance_checker_buttons_10['pattern'].value == '50,75,125,150,175,200,225,250,300,400':
                for i in range(1, 11):
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].value = pattern_1[i - 1]
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].value = pattern_1[i - 1] * 2
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].update()
            elif tickets_balance_checker_buttons_10['pattern'].value == '75,100,150,175,225,250,275,300,350,450':
                for i in range(1, 11):
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].value = pattern_2[i - 1]
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].value = pattern_2[i - 1] * 2
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].update()
            elif tickets_balance_checker_buttons_10['pattern'].value == '75,100,150,175,200,225,250,275,300,400':
                for i in range(1, 11):
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].value = pattern_3[i - 1]
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].value = pattern_3[i - 1] * 2
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].update()
            elif tickets_balance_checker_buttons_10['pattern'].value == '100,125,150,175,225,250,275,300,350,450':
                for i in range(1, 11):
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].value = pattern_4[i - 1]
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].value = pattern_4[i - 1] * 2
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].update()
            elif tickets_balance_checker_buttons_10['pattern'].value == '100,125,150,175,200,225,250,275,300,400':
                for i in range(1, 11):
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].value = pattern_5[i - 1]
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].value = pattern_5[i - 1] * 2
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].update()
            elif tickets_balance_checker_buttons_10['pattern'].value == '100,125,150,175,225,250,275,300,350,450':
                for i in range(1, 11):
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].value = pattern_6[i - 1]
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].value = pattern_6[i - 1] * 2
                    tickets_balance_checker_buttons_10[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_10[f'field_oto_{i + 10}'].update()
            for i, item in enumerate(self.json_data_tickets_balance_10['global'], start=1):
                button_key = f'bundle_{i}'
                tickets_balance_checker_buttons_10[button_key].text = item['event']['product_id']
                tickets_balance_checker_buttons_10[button_key].disabled = False
                tickets_balance_checker_buttons_10[button_key].update()
        elif kind == 'tickets_balance_9':
            pattern_1 = [100, 125, 150, 175, 200, 225, 250, 300, 400]
            pattern_2 = [50, 75, 100, 125, 200, 225, 250, 300, 400]
            pattern_3 = [50, 75, 100, 125, 150, 200, 225, 250, 350]
            for i, item in enumerate(self.json_data_tickets_balance_9['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_9[button_key].text = item['_id']
                tickets_balance_checker_buttons_9[button_key].disabled = False
                tickets_balance_checker_buttons_9[button_key].update()
            if tickets_balance_checker_buttons_9['pattern'].value == '100,125,150,175,200,225,250,300,400':
                for i in range(1, 10):
                    tickets_balance_checker_buttons_9[f'field_lto_{i}'].value = pattern_1[i - 1]
                    tickets_balance_checker_buttons_9[f'field_oto_{i + 9}'].value = pattern_1[i - 1] * 2
                    tickets_balance_checker_buttons_9[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_9[f'field_oto_{i + 9}'].update()
            elif tickets_balance_checker_buttons_9['pattern'].value == '50,75,100,125,200,225,250,300,400':
                for i in range(1, 10):
                    tickets_balance_checker_buttons_9[f'field_lto_{i}'].value = pattern_2[i - 1]
                    tickets_balance_checker_buttons_9[f'field_oto_{i + 9}'].value = pattern_2[i - 1] * 2
                    tickets_balance_checker_buttons_9[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_9[f'field_oto_{i + 9}'].update()
            elif tickets_balance_checker_buttons_9['pattern'].value == '50,75,100,125,150,200,225,250,350':
                for i in range(1, 10):
                    tickets_balance_checker_buttons_9[f'field_lto_{i}'].value = pattern_3[i - 1]
                    tickets_balance_checker_buttons_9[f'field_oto_{i + 9}'].value = pattern_3[i - 1] * 2
                    tickets_balance_checker_buttons_9[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_9[f'field_oto_{i + 9}'].update()
            for i, item in enumerate(self.json_data_tickets_balance_9['global'], start=1):
                button_key = f'bundle_{i}'
                tickets_balance_checker_buttons_9[button_key].text = item['event']['product_id']
                tickets_balance_checker_buttons_9[button_key].disabled = False
                tickets_balance_checker_buttons_9[button_key].update()
        elif kind == 'tickets_balance_3':
            pattern_1 = [100, 150, 350]
            pattern_2 = [100, 150, 250]
            pattern_3 = [100, 150, 200]
            for i, item in enumerate(self.json_data_tickets_balance_3['global'], start=1):
                button_key = f'button_{i}'
                tickets_balance_checker_buttons_3[button_key].text = item['_id']
                tickets_balance_checker_buttons_3[button_key].disabled = False
                tickets_balance_checker_buttons_3[button_key].update()
            if tickets_balance_checker_buttons_3['pattern'].value == '100,150,350':
                for i in range(1, 4):
                    tickets_balance_checker_buttons_3[f'field_lto_{i}'].value = pattern_1[i - 1]
                    tickets_balance_checker_buttons_3[f'field_oto_{i + 3}'].value = pattern_1[i - 1] * 2
                    tickets_balance_checker_buttons_3[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_3[f'field_oto_{i + 3}'].update()
            elif tickets_balance_checker_buttons_3['pattern'].value == '100,150,250':
                for i in range(1, 4):
                    tickets_balance_checker_buttons_3[f'field_lto_{i}'].value = pattern_2[i - 1]
                    tickets_balance_checker_buttons_3[f'field_oto_{i + 3}'].value = pattern_2[i - 1] * 2
                    tickets_balance_checker_buttons_3[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_3[f'field_oto_{i + 3}'].update()
            elif tickets_balance_checker_buttons_3['pattern'].value == '100,150,200':
                for i in range(1, 4):
                    tickets_balance_checker_buttons_3[f'field_lto_{i}'].value = pattern_3[i - 1]
                    tickets_balance_checker_buttons_3[f'field_oto_{i + 3}'].value = pattern_3[i - 1] * 2
                    tickets_balance_checker_buttons_3[f'field_lto_{i}'].update()
                    tickets_balance_checker_buttons_3[f'field_oto_{i + 3}'].update()
            for i, item in enumerate(self.json_data_tickets_balance_3['global'], start=1):
                button_key = f'bundle_{i}'
                tickets_balance_checker_buttons_3[button_key].text = item['event']['product_id']
                tickets_balance_checker_buttons_3[button_key].disabled = False
                tickets_balance_checker_buttons_3[button_key].update()

    def reset_tickets(self, tickets_number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons, tickets_bans_9_buttons,
                             tickets_bans_3_buttons)
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
                             tickets_balance_checker_buttons_9, tickets_balance_checker_buttons_3)
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
            cgp_6_buttons['dynamic_items'].value = ""
            cgp_6_buttons['dynamic_items'].update()
            for item in cgp_6_buttons:
                if re.match(r'^button_\d+$', item):
                    cgp_6_buttons[item].text = "offer id"
                    cgp_6_buttons[item].color = ft.colors.PRIMARY
                    cgp_6_buttons[item].disabled = True
                    cgp_6_buttons[item].update()
        elif kind == 'cgp_9':
            self.json_data_cgp_9 = None
            self._update_button_text("")
            cgp_9_buttons['dynamic_items'].value = ""
            cgp_9_buttons['dynamic_items'].update()
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
            tickets_balance_checker_buttons_11['items_id_lto'].value = ""
            tickets_balance_checker_buttons_11['items_id_lto'].update()
            tickets_balance_checker_buttons_11['items_id_oto'].value = ""
            tickets_balance_checker_buttons_11['items_id_oto'].update()
            tickets_balance_checker_buttons_11['pattern'].value = ""
            tickets_balance_checker_buttons_11['pattern'].update()
            for item in tickets_balance_checker_buttons_11:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_11[item].text = "offer id"
                    tickets_balance_checker_buttons_11[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_11[item].disabled = True
                elif re.match(r'^field_lto_\d+$', item):
                    tickets_balance_checker_buttons_11[item].value = ""
                elif re.match(r'^field_oto_\d+$', item):
                    tickets_balance_checker_buttons_11[item].value = ""
                elif re.match(r'^bundle_\d+$', item):
                    tickets_balance_checker_buttons_11[item].text = "bundle_id"
                    tickets_balance_checker_buttons_11[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_11[item].disabled = True
                tickets_balance_checker_buttons_11[item].update()
        elif kind == 'tickets_balance_10':
            self.json_data_tickets_balance_10 = None
            self._update_button_text("")
            tickets_balance_checker_buttons_10['items_id_lto'].value = ""
            tickets_balance_checker_buttons_10['items_id_lto'].update()
            tickets_balance_checker_buttons_10['items_id_oto'].value = ""
            tickets_balance_checker_buttons_10['items_id_oto'].update()
            tickets_balance_checker_buttons_10['pattern'].value = ""
            tickets_balance_checker_buttons_10['pattern'].update()
            for item in tickets_balance_checker_buttons_10:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_10[item].text = "offer id"
                    tickets_balance_checker_buttons_10[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_10[item].disabled = True
                elif re.match(r'^field_lto_\d+$', item):
                    tickets_balance_checker_buttons_10[item].value = ""
                elif re.match(r'^field_oto_\d+$', item):
                    tickets_balance_checker_buttons_10[item].value = ""
                elif re.match(r'^bundle_\d+$', item):
                    tickets_balance_checker_buttons_10[item].text = "bundle_id"
                    tickets_balance_checker_buttons_10[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_10[item].disabled = True
                tickets_balance_checker_buttons_10[item].update()
        elif kind == 'tickets_balance_9':
            self.json_data_tickets_balance_9 = None
            self._update_button_text("")
            tickets_balance_checker_buttons_9['items_id_lto'].value = ""
            tickets_balance_checker_buttons_9['items_id_lto'].update()
            tickets_balance_checker_buttons_9['items_id_oto'].value = ""
            tickets_balance_checker_buttons_9['items_id_oto'].update()
            tickets_balance_checker_buttons_9['pattern'].value = ""
            tickets_balance_checker_buttons_9['pattern'].update()
            for item in tickets_balance_checker_buttons_9:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_9[item].text = "offer id"
                    tickets_balance_checker_buttons_9[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_9[item].disabled = True
                elif re.match(r'^field_lto_\d+$', item):
                    tickets_balance_checker_buttons_9[item].value = ""
                elif re.match(r'^field_oto_\d+$', item):
                    tickets_balance_checker_buttons_9[item].value = ""
                elif re.match(r'^bundle_\d+$', item):
                    tickets_balance_checker_buttons_9[item].text = "bundle_id"
                    tickets_balance_checker_buttons_9[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_9[item].disabled = True
                tickets_balance_checker_buttons_9[item].update()
        elif kind == 'tickets_balance_3':
            self.json_data_tickets_balance_3 = None
            self._update_button_text("")
            tickets_balance_checker_buttons_3['items_id_lto'].value = ""
            tickets_balance_checker_buttons_3['items_id_lto'].update()
            tickets_balance_checker_buttons_3['items_id_oto'].value = ""
            tickets_balance_checker_buttons_3['items_id_oto'].update()
            tickets_balance_checker_buttons_3['pattern'].value = ""
            tickets_balance_checker_buttons_3['pattern'].update()
            for item in tickets_balance_checker_buttons_3:
                if re.match(r'^button_\d+$', item):
                    tickets_balance_checker_buttons_3[item].text = "offer id"
                    tickets_balance_checker_buttons_3[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_3[item].disabled = True
                elif re.match(r'^field_lto_\d+$', item):
                    tickets_balance_checker_buttons_3[item].value = ""
                elif re.match(r'^field_oto_\d+$', item):
                    tickets_balance_checker_buttons_3[item].value = ""
                elif re.match(r'^bundle_\d+$', item):
                    tickets_balance_checker_buttons_3[item].text = "bundle_id"
                    tickets_balance_checker_buttons_3[item].color = ft.colors.PRIMARY
                    tickets_balance_checker_buttons_3[item].disabled = True
                tickets_balance_checker_buttons_3[item].update()

    def check_bans_lto(self, tickets_number, number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons, tickets_bans_9_buttons,
                             tickets_bans_3_buttons)
        criteria_gp_rf = {
            "criteria_gp_rf": "secret_data"
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
                    bans_in_json) and criteria == criteria_gp_rf:
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
                    bans_in_json) and criteria == criteria_gp_rf:
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
                    bans_in_json) and criteria == criteria_gp_rf:
                update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], True)
            else:
                update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], False)
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
                    bans_in_json) and criteria == criteria_gp_rf:
                update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], True)
            else:
                update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], False)

    def check_bans_oto(self, tickets_number, number):
        from buttons import (tickets_bans_11_buttons, tickets_bans_10_buttons, tickets_bans_9_buttons,
                             tickets_bans_3_buttons)
        criteria_gp_rf = {
            "criteria_gp_rf": "secret_data"
        }

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баны, денаи и критерий корректны'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баны, денаи или критерий некорректны'
                button.color = ft.colors.RED
            button.update()

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
            try:
                try:
                    denies_in_json_1 = self.json_data_11['global'][number]['conditions']['filter']['and'][1]['or'][0][
                        'denyByOneOf']
                    denies_in_json_2 = self.json_data_11['global'][number]['conditions']['filter']['and'][1]['or'][1][
                        'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_11)
                            and len(denies_in_json_1) == len(self.ltos_11)
                            and set(denies_in_json_2) == set(self.ltos_11)
                            and len(denies_in_json_2) == len(self.ltos_11)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], False)
                except KeyError:
                    denies_in_json_1 = self.json_data_11['global'][number]['conditions']['filter']['and'][0]['or'][0][
                        'denyByOneOf']
                    denies_in_json_2 = self.json_data_11['global'][number]['conditions']['filter']['and'][0]['or'][1][
                        'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_11)
                            and len(denies_in_json_1) == len(self.ltos_11)
                            and set(denies_in_json_2) == set(self.ltos_11)
                            and len(denies_in_json_2) == len(self.ltos_11)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], False)
            except (KeyError, IndexError):
                try:
                    try:
                        denies_in_json_1 = self.json_data_11['global'][number]['conditions']['filter']['and'][1][
                            'denyByOneOf']
                    except KeyError:
                        denies_in_json_1 = \
                            self.json_data_11['global'][number]['conditions']['filter']['and'][1]['or'][0][
                                'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_11)
                            and len(denies_in_json_1) == len(self.ltos_11)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], False)
                except (KeyError, IndexError):
                    try:
                        denies_in_json_1 = self.json_data_11['global'][number]['conditions']['filter']['and'][0][
                            'denyByOneOf']
                    except KeyError:
                        denies_in_json_1 = \
                            self.json_data_11['global'][number]['conditions']['filter']['and'][0]['or'][0][
                                'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_11)
                            and len(denies_in_json_1) == len(self.ltos_11)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_11_buttons[f'ban_11_{number + 1}'], False)
        # OTO 10
        elif tickets_number == 10:
            try:
                try:
                    denies_in_json_1 = self.json_data_10['global'][number]['conditions']['filter']['and'][1]['or'][0][
                        'denyByOneOf']
                    denies_in_json_2 = self.json_data_10['global'][number]['conditions']['filter']['and'][1]['or'][1][
                        'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_10)
                            and len(denies_in_json_1) == len(self.ltos_10)
                            and set(denies_in_json_2) == set(self.ltos_10)
                            and len(denies_in_json_2) == len(self.ltos_10)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], False)
                except KeyError:
                    denies_in_json_1 = self.json_data_10['global'][number]['conditions']['filter']['and'][0]['or'][0][
                        'denyByOneOf']
                    denies_in_json_2 = self.json_data_10['global'][number]['conditions']['filter']['and'][0]['or'][1][
                        'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_10)
                            and len(denies_in_json_1) == len(self.ltos_10)
                            and set(denies_in_json_2) == set(self.ltos_10)
                            and len(denies_in_json_2) == len(self.ltos_10)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], False)
            except (KeyError, IndexError):
                try:
                    try:
                        denies_in_json_1 = self.json_data_10['global'][number]['conditions']['filter']['and'][1][
                            'denyByOneOf']
                    except KeyError:
                        denies_in_json_1 = \
                            self.json_data_10['global'][number]['conditions']['filter']['and'][1]['or'][0][
                                'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_10)
                            and len(denies_in_json_1) == len(self.ltos_10)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], False)
                except (KeyError, IndexError):
                    try:
                        denies_in_json_1 = self.json_data_10['global'][number]['conditions']['filter']['and'][0][
                            'denyByOneOf']
                    except KeyError:
                        denies_in_json_1 = \
                            self.json_data_10['global'][number]['conditions']['filter']['and'][0]['or'][0][
                                'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_10)
                            and len(denies_in_json_1) == len(self.ltos_10)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_10_buttons[f'ban_10_{number + 1}'], False)
        # OTO 9
        elif tickets_number == 9:
            try:
                try:
                    denies_in_json_1 = self.json_data_9['global'][number]['conditions']['filter']['and'][1]['or'][0][
                        'denyByOneOf']
                    denies_in_json_2 = self.json_data_9['global'][number]['conditions']['filter']['and'][1]['or'][1][
                        'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_9)
                            and len(denies_in_json_1) == len(self.ltos_9)
                            and set(denies_in_json_2) == set(self.ltos_9)
                            and len(denies_in_json_2) == len(self.ltos_9)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], False)
                except KeyError:
                    denies_in_json_1 = self.json_data_9['global'][number]['conditions']['filter']['and'][0]['or'][0][
                        'denyByOneOf']
                    denies_in_json_2 = self.json_data_9['global'][number]['conditions']['filter']['and'][0]['or'][1][
                        'denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_9)
                            and len(denies_in_json_1) == len(self.ltos_9)
                            and set(denies_in_json_2) == set(self.ltos_9)
                            and len(denies_in_json_2) == len(self.ltos_9)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], False)
            except (KeyError, IndexError):
                try:
                    try:
                        denies_in_json_1 = self.json_data_9['global'][number]['conditions']['filter']['and'][1][
                            'denyByOneOf']
                    except KeyError:
                        denies_in_json_1 = \
                        self.json_data_9['global'][number]['conditions']['filter']['and'][1]['or'][0]['denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_9)
                            and len(denies_in_json_1) == len(self.ltos_9)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], False)
                except (KeyError, IndexError):
                    try:
                        denies_in_json_1 = self.json_data_9['global'][number]['conditions']['filter']['and'][0][
                            'denyByOneOf']
                    except KeyError:
                        denies_in_json_1 = \
                            self.json_data_9['global'][number]['conditions']['filter']['and'][0]['or'][0]['denyByOneOf']
                    if (set(bans_should_be) == set(bans_in_json)
                            and len(bans_should_be) == len(bans_in_json)
                            and set(denies_in_json_1) == set(self.ltos_9)
                            and len(denies_in_json_1) == len(self.ltos_9)
                            and criteria == criteria_gp_rf):
                        update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], True)
                    else:
                        update_button(tickets_bans_9_buttons[f'ban_9_{number + 1}'], False)
        # OTO 3
        elif tickets_number == 3:
            try:
                try:
                    denies_in_json = self.json_data_3['global'][number]['conditions']['filter']['and'][1]['denyByOneOf']
                except KeyError:
                    denies_in_json = self.json_data_3['global'][number]['conditions']['filter']['and'][1]['or'][0][
                        'denyByOneOf']
                if (set(bans_should_be) == set(bans_in_json)
                        and len(bans_should_be) == len(bans_in_json)
                        and set(denies_in_json) == set(self.ltos_3)
                        and len(denies_in_json) == len(self.ltos_3)
                        and criteria == criteria_gp_rf):
                    update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], True)
                else:
                    update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], False)
            except (KeyError, IndexError):
                try:
                    denies_in_json = self.json_data_3['global'][number]['conditions']['filter']['and'][0]['denyByOneOf']
                except KeyError:
                    denies_in_json = self.json_data_3['global'][number]['conditions']['filter']['and'][0]['or'][0][
                        'denyByOneOf']
                if (set(bans_should_be) == set(bans_in_json)
                        and len(bans_should_be) == len(bans_in_json)
                        and set(denies_in_json) == set(self.ltos_3)
                        and len(denies_in_json) == len(self.ltos_3)
                        and criteria == criteria_gp_rf):
                    update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], True)
                else:
                    update_button(tickets_bans_3_buttons[f'ban_3_{number + 1}'], False)

    def check_criteria(self):
        from buttons import tickets_criteria_buttons
        criteria_gp_rf = {
            "criteria_gp_rf": "secret_data"
        }
        for i, item in enumerate(self.json_data_criteria['global'], start=0):
            if self.json_data_criteria['global'][i]['criteria'] == criteria_gp_rf:
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
        criteria_gp_rf = {
            "criteria_gp_rf": "secret_data"
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

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс корректный'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс некорректный'
                button.color = ft.colors.RED
            button.update()

        if number == 0:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[0]
                    and this_trigger == "no_hint" and this_trigger_param == 400006 and this_skin_id == 10078
                    and this_event == event_1_1 and this_criteria == criteria_gp_rf and this_packname == "events1"
                    and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
            no_hint_balance_buttons[f'button_{number + 1}'].update()
        elif number == 1:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[1]
                    and this_trigger == "no_hint" and this_trigger_param == 400006 and this_skin_id == 10078
                    and this_event == event_1_2 and this_criteria == criteria_gp_rf and this_packname == "events1"
                    and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 2:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[2]
                    and this_trigger == "no_hint" and this_trigger_param == 400006 and this_skin_id == 10078
                    and this_event == event_1_3 and this_criteria == criteria_gp_rf and this_packname == "events1"
                    and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 3:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[3]
                    and this_trigger == "no_hint" and this_trigger_param == 400006 and this_skin_id == 10078
                    and this_event == event_1_4 and this_criteria == criteria_gp_rf and this_packname == "events1"
                    and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 4:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[0]
                    and this_trigger == "no_hint" and this_trigger_param == 400008 and this_skin_id == 10078
                    and this_event == event_2_1 and this_delay == 30 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 5:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[1]
                    and this_trigger == "no_hint" and this_trigger_param == 400008 and this_skin_id == 10078
                    and this_event == event_2_2 and this_delay == 30 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 6:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[2]
                    and this_trigger == "no_hint" and this_trigger_param == 400008 and this_skin_id == 10078
                    and this_event == event_2_3 and this_delay == 30 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 7:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[3]
                    and this_trigger == "no_hint" and this_trigger_param == 400008 and this_skin_id == 10078
                    and this_event == event_2_4 and this_delay == 30 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 8:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[0]
                    and this_trigger == "no_hint" and this_trigger_param == 400003 and this_skin_id == 10078
                    and this_event == event_3_1 and this_delay == 60 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 9:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[1]
                    and this_trigger == "no_hint" and this_trigger_param == 400003 and this_skin_id == 10078
                    and this_event == event_3_2 and this_delay == 60 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 10:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[2]
                    and this_trigger == "no_hint" and this_trigger_param == 400003 and this_skin_id == 10078
                    and this_event == event_3_3 and this_delay == 60 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 11:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[3]
                    and this_trigger == "no_hint" and this_trigger_param == 400003 and this_skin_id == 10078
                    and this_event == event_3_4 and this_delay == 60 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 12:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[0]
                    and this_trigger == "no_hint" and this_trigger_param == 400009 and this_skin_id == 10078
                    and this_event == event_4_1 and this_delay == 45 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 13:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[1]
                    and this_trigger == "no_hint" and this_trigger_param == 400009 and this_skin_id == 10078
                    and this_event == event_4_2 and this_delay == 45 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 14:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[2]
                    and this_trigger == "no_hint" and this_trigger_param == 400009 and this_skin_id == 10078
                    and this_event == event_4_3 and this_delay == 45 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)
        elif number == 15:
            if (this_level_start == 7 and this_only_for_buyer is True and this_filter == filters[3]
                    and this_trigger == "no_hint" and this_trigger_param == 400009 and this_skin_id == 10078
                    and this_event == event_4_4 and this_delay == 45 and this_criteria == criteria_gp_rf
                    and this_packname == "events1" and this_platform == []):
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], True)
            else:
                update_button(no_hint_balance_buttons[f'button_{number + 1}'], False)

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
        criteria_gp_rf = {"criteria_gp_rf": "secret_data"}
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
            if (this_conditions == conditions_payer and this_platform == [] and this_criteria == criteria_gp_rf
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
            if (this_conditions == conditions_payer and this_platform == [] and this_criteria == criteria_gp_rf
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
            if (this_conditions == conditions_payer and this_platform == [] and this_criteria == criteria_gp_rf
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
        criteria_gp_rf = {"criteria_gp_rf": "secret_data"}

        this_packname = self.json_data_bcp_actual['global'][number]['conditions']['packName']
        this_level_start = self.json_data_bcp_actual['global'][number]['conditions']['level_start']
        this_only_for_buyer = self.json_data_bcp_actual['global'][number]['conditions']['OnlyForBuyer']
        this_subtype = self.json_data_bcp_actual['global'][number]['conditions']['subtype']
        this_show_in_item_info = self.json_data_bcp_actual['global'][number]['conditions']['show_in_item_info']
        this_platform = self.json_data_bcp_actual['global'][number]['platform']
        this_criteria = self.json_data_bcp_actual['global'][number]['criteria']
        if number == 0 or number == 1 or number == 2 or number == 6:
            this_skin_id = self.json_data_bcp_actual['global'][number]['conditions']['skin_id']
        if number == 2 or number == 5:
            this_event_uwp = self.json_data_bcp_actual['global'][number]['event']

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс корректный'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс некорректный'
                button.color = ft.colors.RED
            button.update()

        if number == 0:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_skin_id == int(bcp_actual_buttons["skin_id_field"].value) and this_subtype == 1002
                    and this_show_in_item_info is True and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_non_default):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 1:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_skin_id == int(bcp_actual_buttons["skin_id_field"].value) and this_subtype == 1000
                    and this_show_in_item_info is True and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_default):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 2:
            event_default = self.json_data_bcp_actual['global'][1]['event']
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_skin_id == int(bcp_actual_buttons["skin_id_field"].value) and this_subtype == 1000
                    and this_show_in_item_info is True and this_platform == platform_win_amazon and this_criteria == criteria
                    and this_event_uwp == event_default):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 3:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_subtype == 1002 and this_show_in_item_info is True
                    and this_platform == platform_ios_android_samsung and this_criteria == criteria_non_default):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 4:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_subtype == 1000 and this_show_in_item_info is True
                    and this_platform == platform_ios_android_samsung and this_criteria == criteria_default):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 5:
            event_default = self.json_data_bcp_actual['global'][4]['event']
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is False
                    and this_subtype == 1000 and this_show_in_item_info is True
                    and this_platform == platform_win_amazon and this_criteria == criteria and this_event_uwp == event_default):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 6:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is True
                    and this_skin_id == int(bcp_actual_buttons["skin_id_field"].value) and this_subtype == 1000
                    and this_show_in_item_info is True and this_platform == [] and this_criteria == criteria_gp_rf):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 7:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is True
                    and this_subtype == 1000 and this_show_in_item_info is True
                    and this_platform == [] and this_criteria == criteria_gp_rf):
                update_button(bcp_actual_buttons[f'button_{number + 1}'], True)
            else:
                update_button(bcp_actual_buttons[f'button_{number + 1}'], False)
        elif number == 8:
            if (this_packname == "events1" and this_level_start == 7 and this_only_for_buyer is True
                    and this_subtype == 1000 and this_show_in_item_info is True
                    and this_platform == [] and this_criteria == criteria_gp_rf):
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
        criteria_cgp_5 = {"criteria_cgp_5": "secret_data"}
        event_0 = {"event_0": "secret_data"}
        event_1_and_2 = {"event_1_and_2": "secret_data"}
        event_3 = {"event_3": "secret_data"}
        event_4 = {"event_4": "secret_data"}
        event_5 = {"event_5": "secret_data"}

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
                    and this_criteria == criteria_cgp_1 and this_event == event_0):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 1:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_2 and this_event == event_1_and_2):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 2:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_win_amazon
                    and this_criteria == criteria_cgp_3 and this_event == event_1_and_2):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 3:
            if (this_conditions == conditions_cgp_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_5 and this_event == event_3):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 4:
            if (this_conditions == conditions_cgp_payer and this_platform == [] and this_criteria == criteria_cgp_4
                    and this_event == event_4):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_6_buttons[f'button_{number + 1}'], False)
        elif number == 5:
            if (this_conditions == conditions_cgp_payer and this_platform == [] and this_criteria == criteria_cgp_4
                    and this_event == event_5):
                update_button(cgp_6_buttons[f'button_{number + 1}'], True)
                cgp_6_buttons['dynamic_items'].value = (
                    self.json_data_cgp_6['global'][number]['event']['rewards'][0]['itemId'],
                    self.json_data_cgp_6['global'][number]['event']['rewards'][0]['count'],
                    self.json_data_cgp_6['global'][number]['event']['rewards'][1]['itemId'],
                    self.json_data_cgp_6['global'][number]['event']['rewards'][1]['count'],
                    self.json_data_cgp_6['global'][number]['event']['rewards'][2]['itemId'],
                    self.json_data_cgp_6['global'][number]['event']['rewards'][2]['count'],
                    self.json_data_cgp_6['global'][number]['event']['rewards'][3]['itemId'],
                    self.json_data_cgp_6['global'][number]['event']['rewards'][3]['count'])
                cgp_6_buttons['dynamic_items'].update()
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
        event_0 = {"event_0": "secret_data"}
        event_1 = {"event_1": "secret_data"}
        event_2_and_3 = {"event_2_and_3": "secret_data"}
        event_4_and_5 = {"event_4_and_5": "secret_data"}
        event_6 = {"event_6": "secret_data"}
        event_7 = {"event_7": "secret_data"}
        event_8 = {"event_8": "secret_data"}

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
                    and this_criteria == criteria_cgp_1 and this_event == event_0):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 1:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_1 and this_event == event_1):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 2:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_2 and this_event == event_2_and_3):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 3:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == platform_win_amazon
                    and this_criteria == criteria_cgp_3 and this_event == event_2_and_3):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 4:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_ios_android_samsung
                    and this_criteria == criteria_cgp_2 and this_event == event_4_and_5):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 5:
            if (this_conditions == conditions_cgp_non_payer and this_platform == platform_win_amazon
                    and this_criteria == criteria_cgp_3 and this_event == event_4_and_5):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 6:
            if (this_conditions == conditions_cgp_payer_lt_25 and this_platform == []
                    and this_criteria == criteria_cgp_4 and this_event == event_6):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 7:
            if (this_conditions == conditions_cgp_payer_gt_25 and this_platform == []
                    and this_criteria == criteria_cgp_4 and this_event == event_7):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
            else:
                update_button(cgp_9_buttons[f'button_{number + 1}'], False)
        elif number == 8:
            if (this_conditions == conditions_cgp_payer_gt_25 and this_platform == []
                    and this_criteria == criteria_cgp_4 and this_event == event_8):
                update_button(cgp_9_buttons[f'button_{number + 1}'], True)
                cgp_9_buttons['dynamic_items'].value = (
                    self.json_data_cgp_9['global'][8]['event']['rewards'][0]['itemId'],
                    self.json_data_cgp_9['global'][8]['event']['rewards'][0]['count'],
                    self.json_data_cgp_9['global'][8]['event']['rewards'][1]['itemId'],
                    self.json_data_cgp_9['global'][8]['event']['rewards'][1]['count'],
                    self.json_data_cgp_9['global'][8]['event']['rewards'][2]['itemId'],
                    self.json_data_cgp_9['global'][8]['event']['rewards'][2]['count'],
                    self.json_data_cgp_9['global'][8]['event']['rewards'][3]['itemId'],
                    self.json_data_cgp_9['global'][8]['event']['rewards'][3]['count'])
                cgp_9_buttons['dynamic_items'].update()
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
            needed_denies_1 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][1]['or'][0][
                'denyByOneOf']
            needed_denies_2 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][1]['or'][1][
                'denyByOneOf']
            needed_allows_1 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][1]['or'][0][
                'allowByOneOf']
            needed_allows_2 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][1]['or'][1][
                'allowByOneOf']
        except (KeyError, IndexError):
            needed_denies_1 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][0]['or'][0][
                'denyByOneOf']
            needed_denies_2 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][0]['or'][1][
                'denyByOneOf']
            needed_allows_1 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][0]['or'][0][
                'allowByOneOf']
            needed_allows_2 = self.json_data_oto_2['global'][number]['conditions']['filter']['and'][0]['or'][1][
                'allowByOneOf']
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
        balance = [
            data_balance[0],
            data_balance[1],
            data_balance[2]
        ]

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс и сегментация корректные'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс или сегментация некорректные'
                button.color = ft.colors.RED
            button.update()

        if this_balance == balance[number] and this_segmentation == segmentation[number]:
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
        balance = [
            data_balance[3],
            data_balance[4],
            data_balance[5]
        ]

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс и сегментация корректные'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс или сегментация некорректные'
                button.color = ft.colors.RED
            button.update()

        if this_balance == balance[number] and this_filter == filter[number]:
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
        balance_ww = [
            data_balance[6],
            data_balance[7],
            data_balance[8],
            data_balance[9]
        ]
        balance_cn = [
            data_balance[10],
            data_balance[11],
            data_balance[12],
            data_balance[13]
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
            if this_filter == filter[number] and this_balance == balance_ww[number]:
                update_button(labyrinth_balance_ww_buttons[f'button_{number + 1}'], True)
            else:
                update_button(labyrinth_balance_ww_buttons[f'button_{number + 1}'], False)
        else:
            this_filter = self.json_data_labyrinth_balance_cn['global'][number]['conditions']['filter']
            this_balance = self.json_data_labyrinth_balance_cn['global'][number]['event']
            if this_filter == filter[number] and this_balance == balance_cn[number]:
                update_button(labyrinth_balance_cn_buttons[f'button_{number + 1}'], True)
            else:
                update_button(labyrinth_balance_cn_buttons[f'button_{number + 1}'], False)

    def tickets_balance_checker(self, amount, number):
        from buttons import (tickets_balance_checker_buttons_11, tickets_balance_checker_buttons_10,
                             tickets_balance_checker_buttons_9, tickets_balance_checker_buttons_3)

        def update_button(button, is_correct):
            if is_correct is True:
                button.text = 'Баланс корректный'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Баланс некорректный'
                button.color = ft.colors.RED
            button.update()

        def update_button_bundle(button, is_correct):
            if is_correct is True:
                button.text = 'Бандл корректный'
                button.color = ft.colors.GREEN
            else:
                button.text = 'Бандл некорректный'
                button.color = ft.colors.RED
            button.update()

        if amount == 22:
            try:
                input_item_id_lto = [int(val) for val in
                                     tickets_balance_checker_buttons_11['items_id_lto'].value.split(",")]
            except AttributeError:
                input_item_id_lto = int(tickets_balance_checker_buttons_11['items_id_lto'].value)
            try:
                input_item_id_oto = [int(val) for val in
                                     tickets_balance_checker_buttons_11['items_id_oto'].value.split(",")]
            except AttributeError:
                input_item_id_oto = int(tickets_balance_checker_buttons_11['items_id_oto'].value)
            try:
                try:
                    input_count_lto = [int(val) for val in
                                       tickets_balance_checker_buttons_11[f'field_lto_{number + 1}'].value.split(",")]
                except AttributeError:
                    input_count_lto = int(tickets_balance_checker_buttons_11[f'field_lto_{number + 1}'].value)
            except (ValueError, KeyError):
                pass
            try:
                try:
                    input_count_oto = [int(val) for val in
                                       tickets_balance_checker_buttons_11[f'field_oto_{number + 1}'].value.split(",")]
                except AttributeError:
                    input_count_oto = int(tickets_balance_checker_buttons_11[f'field_oto_{number + 1}'].value)
            except (ValueError, KeyError):
                pass
            this_item_id = self.json_data_tickets_balance_11['global'][number]['event']['item_id']
            this_count = self.json_data_tickets_balance_11['global'][number]['event']['count']
            this_type = self.json_data_tickets_balance_11['global'][number]['type']
            this_bundle = self.json_data_tickets_balance_11['global'][number]['event']['product_id']
            bundles = [
                'secret_bundle_1',
                'secret_bundle_2',
                'secret_bundle_3',
                'secret_bundle_4',
                'secret_bundle_5',
                'secret_bundle_6',
                'secret_bundle_7',
                'secret_bundle_8',
                'secret_bundle_9',
                'secret_bundle_10',
                'secret_bundle_11',
                'secret_bundle_1',
                'secret_bundle_2',
                'secret_bundle_3',
                'secret_bundle_4',
                'secret_bundle_5',
                'secret_bundle_6',
                'secret_bundle_7',
                'secret_bundle_8',
                'secret_bundle_9',
                'secret_bundle_10',
                'secret_bundle_11'
            ]

            if this_type == 'limited_time_offer':
                if (set(this_item_id) == set(input_item_id_lto) and len(this_item_id) == len(input_item_id_lto)
                        and set(this_count) == set(input_count_lto) and len(this_count) == len(input_count_lto)):
                    update_button(tickets_balance_checker_buttons_11[f'button_{number + 1}'], True)
                else:
                    update_button(tickets_balance_checker_buttons_11[f'button_{number + 1}'], False)
            elif this_type == 'one_time_offer':
                if (set(this_item_id) == set(input_item_id_oto) and len(this_item_id) == len(input_item_id_oto)
                        and set(this_count) == set(input_count_oto) and len(this_count) == len(input_count_oto)):
                    update_button(tickets_balance_checker_buttons_11[f'button_{number + 1}'], True)
                else:
                    update_button(tickets_balance_checker_buttons_11[f'button_{number + 1}'], False)

            if this_bundle == bundles[number]:
                update_button_bundle(tickets_balance_checker_buttons_11[f'bundle_{number + 1}'], True)
            else:
                update_button_bundle(tickets_balance_checker_buttons_11[f'bundle_{number + 1}'], False)
        elif amount == 20:
            try:
                input_item_id_lto = [int(val) for val in
                                     tickets_balance_checker_buttons_10['items_id_lto'].value.split(",")]
            except AttributeError:
                input_item_id_lto = int(tickets_balance_checker_buttons_10['items_id_lto'].value)
            try:
                input_item_id_oto = [int(val) for val in
                                     tickets_balance_checker_buttons_10['items_id_oto'].value.split(",")]
            except AttributeError:
                input_item_id_oto = int(tickets_balance_checker_buttons_10['items_id_oto'].value)
            try:
                try:
                    input_count_lto = [int(val) for val in
                                       tickets_balance_checker_buttons_10[f'field_lto_{number + 1}'].value.split(",")]
                except AttributeError:
                    input_count_lto = int(tickets_balance_checker_buttons_10[f'field_lto_{number + 1}'].value)
            except (ValueError, KeyError):
                pass
            try:
                try:
                    input_count_oto = [int(val) for val in
                                       tickets_balance_checker_buttons_10[f'field_oto_{number + 1}'].value.split(",")]
                except AttributeError:
                    input_count_oto = int(tickets_balance_checker_buttons_10[f'field_oto_{number + 1}'].value)
            except (ValueError, KeyError):
                pass
            this_item_id = self.json_data_tickets_balance_10['global'][number]['event']['item_id']
            this_count = self.json_data_tickets_balance_10['global'][number]['event']['count']
            this_type = self.json_data_tickets_balance_10['global'][number]['type']
            this_bundle = self.json_data_tickets_balance_10['global'][number]['event']['product_id']
            bundles = [
                'secret_bundle_1',
                'secret_bundle_2',
                'secret_bundle_3',
                'secret_bundle_4',
                'secret_bundle_5',
                'secret_bundle_6',
                'secret_bundle_7',
                'secret_bundle_8',
                'secret_bundle_9',
                'secret_bundle_10',
                'secret_bundle_1',
                'secret_bundle_2',
                'secret_bundle_3',
                'secret_bundle_4',
                'secret_bundle_5',
                'secret_bundle_6',
                'secret_bundle_7',
                'secret_bundle_8',
                'secret_bundle_9',
                'secret_bundle_10'
            ]

            if this_type == 'limited_time_offer':
                if (set(this_item_id) == set(input_item_id_lto) and len(this_item_id) == len(input_item_id_lto)
                        and set(this_count) == set(input_count_lto) and len(this_count) == len(input_count_lto)):
                    update_button(tickets_balance_checker_buttons_10[f'button_{number + 1}'], True)
                else:
                    update_button(tickets_balance_checker_buttons_10[f'button_{number + 1}'], False)
            elif this_type == 'one_time_offer':
                if (set(this_item_id) == set(input_item_id_oto) and len(this_item_id) == len(input_item_id_oto)
                        and set(this_count) == set(input_count_oto) and len(this_count) == len(input_count_oto)):
                    update_button(tickets_balance_checker_buttons_10[f'button_{number + 1}'], True)
                else:
                    update_button(tickets_balance_checker_buttons_10[f'button_{number + 1}'], False)

            if this_bundle == bundles[number]:
                update_button_bundle(tickets_balance_checker_buttons_10[f'bundle_{number + 1}'], True)
            else:
                update_button_bundle(tickets_balance_checker_buttons_10[f'bundle_{number + 1}'], False)
        elif amount == 18:
            try:
                input_item_id_lto = [int(val) for val in
                                     tickets_balance_checker_buttons_9['items_id_lto'].value.split(",")]
            except AttributeError:
                input_item_id_lto = int(tickets_balance_checker_buttons_9['items_id_lto'].value)
            try:
                input_item_id_oto = [int(val) for val in
                                     tickets_balance_checker_buttons_9['items_id_oto'].value.split(",")]
            except AttributeError:
                input_item_id_oto = int(tickets_balance_checker_buttons_9['items_id_oto'].value)
            try:
                try:
                    input_count_lto = [int(val) for val in
                                       tickets_balance_checker_buttons_9[f'field_lto_{number + 1}'].value.split(",")]
                except AttributeError:
                    input_count_lto = int(tickets_balance_checker_buttons_9[f'field_lto_{number + 1}'].value)
            except (ValueError, KeyError):
                pass
            try:
                try:
                    input_count_oto = [int(val) for val in
                                       tickets_balance_checker_buttons_9[f'field_oto_{number + 1}'].value.split(",")]
                except AttributeError:
                    input_count_oto = int(tickets_balance_checker_buttons_9[f'field_oto_{number + 1}'].value)
            except (ValueError, KeyError):
                pass
            this_item_id = self.json_data_tickets_balance_9['global'][number]['event']['item_id']
            this_count = self.json_data_tickets_balance_9['global'][number]['event']['count']
            this_type = self.json_data_tickets_balance_9['global'][number]['type']
            this_bundle = self.json_data_tickets_balance_9['global'][number]['event']['product_id']
            bundles = [
                'secret_bundle_1',
                'secret_bundle_2',
                'secret_bundle_3',
                'secret_bundle_4',
                'secret_bundle_5',
                'secret_bundle_6',
                'secret_bundle_7',
                'secret_bundle_8',
                'secret_bundle_9',
                'secret_bundle_1',
                'secret_bundle_2',
                'secret_bundle_3',
                'secret_bundle_4',
                'secret_bundle_5',
                'secret_bundle_6',
                'secret_bundle_7',
                'secret_bundle_8',
                'secret_bundle_9',
            ]

            if this_type == 'limited_time_offer':
                if (set(this_item_id) == set(input_item_id_lto) and len(this_item_id) == len(input_item_id_lto)
                        and set(this_count) == set(input_count_lto) and len(this_count) == len(input_count_lto)):
                    update_button(tickets_balance_checker_buttons_9[f'button_{number + 1}'], True)
                else:
                    update_button(tickets_balance_checker_buttons_9[f'button_{number + 1}'], False)
            elif this_type == 'one_time_offer':
                if (set(this_item_id) == set(input_item_id_oto) and len(this_item_id) == len(input_item_id_oto)
                        and set(this_count) == set(input_count_oto) and len(this_count) == len(input_count_oto)):
                    update_button(tickets_balance_checker_buttons_9[f'button_{number + 1}'], True)
                else:
                    update_button(tickets_balance_checker_buttons_9[f'button_{number + 1}'], False)

            if this_bundle == bundles[number]:
                update_button_bundle(tickets_balance_checker_buttons_9[f'bundle_{number + 1}'], True)
            else:
                update_button_bundle(tickets_balance_checker_buttons_9[f'bundle_{number + 1}'], False)
        elif amount == 6:
            try:
                input_item_id_lto = [int(val) for val in
                                     tickets_balance_checker_buttons_3['items_id_lto'].value.split(",")]
            except AttributeError:
                input_item_id_lto = int(tickets_balance_checker_buttons_3['items_id_lto'].value)
            try:
                input_item_id_oto = [int(val) for val in
                                     tickets_balance_checker_buttons_3['items_id_oto'].value.split(",")]
            except AttributeError:
                input_item_id_oto = int(tickets_balance_checker_buttons_3['items_id_oto'].value)
            try:
                try:
                    input_count_lto = [int(val) for val in
                                       tickets_balance_checker_buttons_3[f'field_lto_{number + 1}'].value.split(",")]
                except AttributeError:
                    input_count_lto = int(tickets_balance_checker_buttons_3[f'field_lto_{number + 1}'].value)
            except (ValueError, KeyError):
                pass
            try:
                try:
                    input_count_oto = [int(val) for val in
                                       tickets_balance_checker_buttons_3[f'field_oto_{number + 1}'].value.split(",")]
                except AttributeError:
                    input_count_oto = int(tickets_balance_checker_buttons_3[f'field_oto_{number + 1}'].value)
            except (ValueError, KeyError):
                pass
            this_item_id = self.json_data_tickets_balance_3['global'][number]['event']['item_id']
            this_count = self.json_data_tickets_balance_3['global'][number]['event']['count']
            this_type = self.json_data_tickets_balance_3['global'][number]['type']
            this_bundle = self.json_data_tickets_balance_3['global'][number]['event']['product_id']
            bundles = [
                'secret_bundle_1',
                'secret_bundle_2',
                'secret_bundle_3',
                'secret_bundle_1',
                'secret_bundle_2',
                'secret_bundle_3',
            ]

            if this_type == 'limited_time_offer':
                if (set(this_item_id) == set(input_item_id_lto) and len(this_item_id) == len(input_item_id_lto)
                        and set(this_count) == set(input_count_lto) and len(this_count) == len(input_count_lto)):
                    update_button(tickets_balance_checker_buttons_3[f'button_{number + 1}'], True)
                else:
                    update_button(tickets_balance_checker_buttons_3[f'button_{number + 1}'], False)
            elif this_type == 'one_time_offer':
                if (set(this_item_id) == set(input_item_id_oto) and len(this_item_id) == len(input_item_id_oto)
                        and set(this_count) == set(input_count_oto) and len(this_count) == len(input_count_oto)):
                    update_button(tickets_balance_checker_buttons_3[f'button_{number + 1}'], True)
                else:
                    update_button(tickets_balance_checker_buttons_3[f'button_{number + 1}'], False)

            if this_bundle == bundles[number]:
                update_button_bundle(tickets_balance_checker_buttons_3[f'bundle_{number + 1}'], True)
            else:
                update_button_bundle(tickets_balance_checker_buttons_3[f'bundle_{number + 1}'], False)


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
