b1: dùng user git `su git`
b2: cd vào folder của user git `cd ~`
b3: tạo folder repos (nếu chưa có)
b4: cd vào repos và tạo folder git theo cấu trúc: {domain}-{mã_project}-{module}: `mkdir {ten_folder}`
b5: cd vào folder vừa tạo, run lệnh `git init --bare`
b6: tạo file hook `nano ./hooks/post-receive`
b7: copy nội dung bên dưới vào file, nhớ chỉnh sửa target, gitdir lại cho đúng
/home/bmdapp-report/htdocs/report.bmdapp.store/backend
`#!/bin/bash

# Đường dẫn thư mục deploy thực tế (source chạy app)

TARGET="/home/vnship-api/htdocs/api.vnship.net/backend"
GIT_DIR="$(pwd)"
BRANCH="master"

echo "🚀 Deploying branch $BRANCH to $TARGET ..."

# Checkout code

git --work-tree=$TARGET --git-dir=$GIT_DIR checkout -f $BRANCH

echo "✅ Deploy completed!"
`

b8: lưu lại file
b9: cấp quyền execute cho file `chmod +x ./hooks/post-receive`
b9: add user git vo group `sudo bmdapp-321admin git`

b10: Cấp quyền cho user domain
sudo chown -R bmdapp-303intage:bmdapp-303intage /home/bmdapp-321admin/htdocs/bmdapp-321admin.net
sudo chmod -R 775 /home/bmdapp-321admin/htdocs

// mở port 
```sh
sudo ufw status # kiểm tra trạng thái firewall
sudo ufw allow 2222/tcp # mở port 2222
sudo ufw reload # reload firewall
```