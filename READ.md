# Tools / Công cụ

Bộ công cụ tiện ích — A collection of utility tools.

---

## Cách sử dụng / Usage

### Chạy menu chính / Run main menu

```bash
./run.sh
# hoặc / or
bash run.sh
```

Chọn số tương ứng với tool cần dùng, nhấn Enter để chạy.

Select the number for the tool you want to run, then press Enter.

---

## Danh sách tools / Tool list

### 1. jsonToCSV

**Tiếng Việt:** Chuyển đổi file JSON sang định dạng CSV. Hỗ trợ object lồng nhau (flatten) và mảng.

**English:** Convert JSON files to CSV format. Supports nested objects (flattened) and arrays.

#### Chạy qua menu / Run via menu

Chọn `1` trong `run.sh`.

Select `1` in `run.sh`.

#### Chạy trực tiếp / Run directly

```bash
cd jsonToCSV
python3 jsonToCSV.py <input.json> -o <output.csv>
```

**Ví dụ / Example:**

```bash
python3 jsonToCSV.py data.json -o data.csv
```

**Đọc từ stdin / Read from stdin:**

```bash
cat data.json | python3 jsonToCSV.py -o data.csv
```

**Tham số / Arguments:**

| Tham số / Param | Mô tả / Description |
|-----------------|---------------------|
| `input` | Đường dẫn file JSON (tùy chọn, mặc định: stdin) / JSON file path (optional, default: stdin) |
| `-o`, `--output` | File CSV đầu ra (tùy chọn, mặc định: stdout) / Output CSV file (optional, default: stdout) |

---

## Yêu cầu / Requirements

- Bash
- Python 3
