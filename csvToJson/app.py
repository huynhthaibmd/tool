#!/usr/bin/env python3
"""Chuyển file CSV sang JSON. Chỉ dùng thư viện chuẩn."""

import csv
import json
import sys
from pathlib import Path

city = [    {
        "no": "1",
        "code": "1",
        "name": "Thành phố Hà Nội"
    },
    {
        "no": "2",
        "code": "4",
        "name": "Cao Bằng"
    },
    {
        "no": "3",
        "code": "8",
        "name": "Tuyên Quang"
    },
    {
        "no": "4",
        "code": "11",
        "name": "Điện Biên"
    },
    {
        "no": "5",
        "code": "12",
        "name": "Lai Châu"
    },
    {
        "no": "6",
        "code": "14",
        "name": "Sơn La"
    },
    {
        "no": "7",
        "code": "15",
        "name": "Lào Cai"
    },
    {
        "no": "8",
        "code": "19",
        "name": "Thái Nguyên"
    },
    {
        "no": "9",
        "code": "20",
        "name": "Lạng Sơn"
    },
    {
        "no": "10",
        "code": "22",
        "name": "Quảng Ninh"
    },
    {
        "no": "11",
        "code": "24",
        "name": "Bắc Ninh"
    },
    {
        "no": "12",
        "code": "25",
        "name": "Phú Thọ"
    },
    {
        "no": "13",
        "code": "31",
        "name": "Thành phố Hải Phòng"
    },
    {
        "no": "14",
        "code": "33",
        "name": "Hưng Yên"
    },
    {
        "no": "15",
        "code": "37",
        "name": "Ninh Bình"
    },
    {
        "no": "16",
        "code": "38",
        "name": "Thanh Hóa"
    },
    {
        "no": "17",
        "code": "40",
        "name": "Nghệ An"
    },
    {
        "no": "18",
        "code": "42",
        "name": "Hà Tĩnh"
    },
    {
        "no": "19",
        "code": "44",
        "name": "Quảng Trị"
    },
    {
        "no": "20",
        "code": "46",
        "name": "Thành phố Huế"
    },
    {
        "no": "21",
        "code": "48",
        "name": "Thành phố Đà Nẵng"
    },
    {
        "no": "22",
        "code": "51",
        "name": "Quảng Ngãi"
    },
    {
        "no": "23",
        "code": "52",
        "name": "Gia Lai"
    },
    {
        "no": "24",
        "code": "56",
        "name": "Khánh Hòa"
    },
    {
        "no": "25",
        "code": "66",
        "name": "Đắk Lắk"
    },
    {
        "no": "26",
        "code": "68",
        "name": "Lâm Đồng"
    },
    {
        "no": "27",
        "code": "75",
        "name": "Đồng Nai"
    },
    {
        "no": "28",
        "code": "79",
        "name": "Thành phố Hồ Chí Minh"
    },
    {
        "no": "29",
        "code": "80",
        "name": "Tây Ninh"
    },
    {
        "no": "30",
        "code": "82",
        "name": "Đồng Tháp"
    },
    {
        "no": "31",
        "code": "86",
        "name": "Vĩnh Long"
    },
    {
        "no": "32",
        "code": "91",
        "name": "An Giang"
    },
    {
        "no": "33",
        "code": "92",
        "name": "Thành phố Cần Thơ"
    },
    {
        "no": "34",
        "code": "96",
        "name": "Cà Mau"
    }
]

def csv_to_json(
    input_path: str,
    output_path: str,
    delimiter: str = ",",
    encoding: str = "utf-8",
) -> list[dict]:
    """
    Đọc CSV: hàng 1 = header, các hàng sau = data.
    Trả về list dict với key từ header.
    """
    with open(input_path, "r", encoding=encoding, newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        data = list(reader)

    # Đọc dữ liệu city (tỉnh/thành) để lấy parentCode
    with open(Path(__file__).parent / "city.json", "r", encoding="utf-8") as city_file:
        cities = json.load(city_file)
        city_name_to_code = {city["name"]: city["code"] for city in cities}

    data = [x for x in data if x["no"] != ""]
    # Đảm bảo luôn có trường parentCode, nếu không thì để giá trị là None
    data = [
        {
            "no": int(x["no"]),
            "code": x["code"],
            "name": x["name"],
            "district": x["district"],
            # Xử lý một số tên tỉnh/thành có thể có "Tỉnh " hoặc "Thành phố " ở đầu
            "parentCode": (
                city_name_to_code.get(x["district"])
                or city_name_to_code.get(x["district"].replace("Tỉnh ", ""))
                or city_name_to_code.get(x["district"].replace("Thành phố ", ""))
                or city_name_to_code.get(x["district"].replace("Tp ", ""))
                or None
            )
        }
        for x in data
    ]
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return data


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "data.csv"
    output_file = script_dir / "data.json"

    if len(sys.argv) >= 2:
        input_file = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])

    if not input_file.exists():
        print(f"File không tồn tại: {input_file}", file=sys.stderr)
        sys.exit(1)

    try:
        data = csv_to_json(str(input_file), str(output_file))
        print(f"Đã chuyển {len(data)} dòng → {output_file}")
    except Exception as e:
        print(f"Lỗi: {e}", file=sys.stderr)
        sys.exit(1)
