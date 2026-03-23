#!/bin/bash

if [ "$(whoami)" != "root" ]; then
    echo "Chạy với root: sudo bash $0"
    exit 1
fi

GIT_HOME=$(eval echo ~git)
REPOS_DIR="$GIT_HOME/repos"

read -p "Nhập tên folder repo: " folder_name
read -p "Nhập đường dẫn TARGET (VD: /home/bmdapp-322admin/htdocs/bmdapp-322admin.net/backend): " TARGET_PATH
read -p "Nhập group (VD: bmdapp-322admin): " group_name
read -p "Nhập PATH_BASE (VD: /home/bmdapp-322admin/htdocs/bmdapp-322admin.net): " PATH_BASE

REPO_PATH="$REPOS_DIR/$folder_name"

sudo -u git bash -c "
    mkdir -p $REPOS_DIR      # Tạo thư mục repos nếu chưa có (-p: không lỗi nếu đã tồn tại)
    cd $REPOS_DIR            # Di chuyển vào repos
    mkdir -p $folder_name    # Tạo folder repo (VD: bmdapp-322admin-backend)
    cd $folder_name          # Vào folder vừa tạo
    git init --bare          # Khởi tạo repo bare (chỉ chứa .git, không có working tree)
"

cat > "$REPO_PATH/hooks/post-receive" << EOF
#!/bin/bash
TARGET="$TARGET_PATH"                    # Nơi code được checkout ra (thư mục chạy app)
GIT_DIR="\$(pwd)"                       # Đường dẫn repo bare (pwd khi hook chạy)
BRANCH="master"

echo "🚀 Deploying branch \$BRANCH to \$TARGET ..."
mkdir -p "\$TARGET"                     # Tạo thư mục target nếu chưa có
git --work-tree="\$TARGET" --git-dir="\$GIT_DIR" checkout -f "\$BRANCH"  # Checkout code ra target, -f ghi đè
echo "✅ Deploy completed!"
EOF

chmod +x "$REPO_PATH/hooks/post-receive"
chown -R git:git "$REPO_PATH"

# ========== CẤU HÌNH QUYỀN (chạy với root) ==========
usermod -aG "$group_name" git

chown -R "$group_name:$group_name" "$PATH_BASE"
chmod -R 775 "$PATH_BASE/../"

echo ""
SERVER_IP=$(hostname -I | awk '{print $1}')
echo "✅ Hoàn tất! Remote: git@$SERVER_IP:/home/git/repos/$folder_name"
