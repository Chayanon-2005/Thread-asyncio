import asyncio

async def main():
    """ฟังก์ชันหลัก"""
    base = 2
    exponents = [3, 4, 5]
    tasks = [asyncio.create_task(power(base, exp)) for exp in exponents]
    results = await asyncio.gather(*tasks)
    print("ผลลัพธ์ทั้งหมด:", results)

if __name__ == "__main__":
    asyncio.run(main())