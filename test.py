import sys
import time
import urllib.request

REQUESTS_COUNT = 10
TIMEOUT = 30  # секунд


def main():
    if len(sys.argv) != 2:
        print('Использование: python test.py "<ссылка>"')
        sys.exit(1)

    url = sys.argv[1]

    total_bytes = 0
    total_time = 0.0
    success = 0

    for i in range(1, REQUESTS_COUNT + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "speedtest-script/1.0"})
            start = time.perf_counter()
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                data = response.read()
            end = time.perf_counter()
        except Exception as e:
            print(f"Запрос {i}: ошибка - {e}")
            continue

        elapsed = end - start
        size = len(data)

        total_bytes += size
        total_time += elapsed
        success += 1

        print(f"Запрос {i}: {elapsed:.2f} с, {size / 1_000_000:.2f} МБ")

    if success == 0:
        print("Все запросы завершились ошибкой")
        sys.exit(1)

    avg_time = total_time / success
    speed_mbit = total_bytes * 8 / total_time / 1_000_000

    print()
    print(f"Успешных запросов: {success} из {REQUESTS_COUNT}")
    print(f"Среднее время запроса: {avg_time:.2f} с")
    print(f"Всего скачано: {total_bytes / 1_000_000:.2f} МБ")
    print(f"Скорость скачивания: {speed_mbit:.2f} Мбит/с")


if __name__ == "__main__":
    main()