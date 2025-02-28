import asyncio
from process import process_json_from_zip
from database import save_to_db

async def main():
    zip_path = 'proba.zip'
    db_path = 'hw1.db'

    data_list = await process_json_from_zip(zip_path)
    await save_to_db(data_list, db_path)

if __name__ == "__main__":
    asyncio.run(main())
