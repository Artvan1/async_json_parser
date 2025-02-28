import aiosqlite

async def save_to_db(data_list, db_path):
    async with aiosqlite.connect(db_path) as conn:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS telecom_companies (
                name TEXT,
                kod_okved TEXT,
                inn TEXT,
                full_name TEXT,
                ogrn TEXT,
                naim_okved TEXT
            )
        ''')

        await conn.executemany('''
            INSERT INTO telecom_companies (name, kod_okved, inn, full_name, ogrn, naim_okved)
            VALUES (:name, :kod_okved, :inn, :full_name, :ogrn, :naim_okved)
        ''', data_list)

        await conn.commit()
