import zipfile
import asyncio
import pandas as pd

async def process_json_from_zip(zip_path):
    data_list = []

    # Открываем ZIP-архив
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        file_names = zip_file.namelist()

        for file_name in file_names:
            # Читаем JSON-файл в отдельном потоке
            with zip_file.open(file_name) as file:
                json_data = await asyncio.to_thread(pd.read_json, file)

                for _, item in json_data.iterrows():
                    data = item['data']

                    inn = data.get('ИНН', '')
                    svokved_data = data.get('СвОКВЭД', {}).get('СвОКВЭДОсн', {})

                    if isinstance(svokved_data, dict) and svokved_data.get('КодОКВЭД', '').startswith('61'):
                        data_list.append({
                            'name': item['name'],
                            'kod_okved': svokved_data['КодОКВЭД'],
                            'inn': inn,
                            'full_name': item['full_name'],
                            'ogrn': data['ОГРН'],
                            'naim_okved': svokved_data['НаимОКВЭД'],
                        })

    return data_list
