import os


def list_ignored(file_or_folder, output_file, gitignore_file):
    ignored_patterns = set()  # Tạo một set để lưu trữ các mẫu bỏ qua duy nhất

    # Duyệt qua tất cả các thư mục con và thư mục cha để kiểm tra mẫu .gitignore
    for root, dirs, files in os.walk(file_or_folder, topdown=True):
        if gitignore_file in files:
            with open(os.path.join(root, gitignore_file), 'r') as f:
                for line in f:
                    pattern = line.strip()
                    if not pattern.startswith("#"):  # Bỏ qua các dòng comment
                        # Thêm mẫu bỏ qua vào set
                        ignored_patterns.add(os.path.join(root, pattern))
    # Loại bỏ phần đường dẫn trùng với file_or_folder và trả về các mẫu bỏ qua dưới dạng yêu cầu
    ignored_patterns = [pattern.replace(file_or_folder, '').lstrip(
        '\\') for pattern in sorted(ignored_patterns)]
    for pattern in sorted(ignored_patterns):
        output_file.write(pattern + '\n')
    return ignored_patterns


current_directory = os.getcwd()
print(f"current_directory: {current_directory}")
# Tạo file đầu ra
output_filename = 'ignored_patterns.txt'

with open(output_filename, 'w') as output_file:
    list_ignored(
        current_directory, output_file, gitignore_file=".gitignore")

print(f'Các mẫu bỏ qua đã được lưu vào file {output_filename}')
