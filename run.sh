#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

show_menu() {
    echo "=========================================="
    echo "  Chọn tool cần chạy:"
    echo "=========================================="
    echo "  1) jsonToCSV - Chuyển JSON sang CSV"
    echo "  0) Thoát"
    echo "=========================================="
}

run_jsonToCSV() {
    cd "$SCRIPT_DIR/jsonToCSV" || exit 1
    python3 jsonToCSV.py data.json -o data.csv
}

main() {
    while true; do
        show_menu
        read -rp "Nhập số: " choice

        case $choice in
            1)
                run_jsonToCSV
                ;;
            0)
                echo "Thoát."
                exit 0
                ;;
            *)
                echo "Lựa chọn không hợp lệ. Thử lại."
                ;;
        esac

        echo ""
        read -rp "Nhấn Enter để tiếp tục..."
    done
}

main
