import asyncio

async def power(base, exponent):
    """คำนวณเลขยกกำลังแบบอะซิงโครนัส"""
    print(f"กำลังคำนวณ {base}^{exponent}...")
    await asyncio.sleep(1)  # จำลองการทำงานที่ใช้เวลานาน
    result = base ** exponent
    print(f"{base}^{exponent} = {result}")
    return result

async def main():
    """ฟังก์ชันหลัก"""
    base = 2
    exponents = [3, 4, 5]
    tasks = [asyncio.create_task(power(base, exp)) for exp in exponents]
    results = await asyncio.gather(*tasks)
    print("ผลลัพธ์ทั้งหมด:", results)

if __name__ == "__main__":
    asyncio.run(main())