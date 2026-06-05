from PIL import Image
import os


def merge_images(image_folder, output_path):
    # Lấy danh sách các file hình ảnh trong thư mục
    image_files = [
        f
        for f in os.listdir(image_folder)
        if f.lower().endswith(("png", "jpg", "jpeg"))
    ]

    if len(image_files) < 4:
        print("Cần ít nhất 4 hình ảnh để ghép.")
        return

    # Đọc 4 hình ảnh đầu tiên
    images = [Image.open(os.path.join(image_folder, image_files[i])) for i in range(4)]

    # Lấy kích thước của hình ảnh đầu tiên
    width, height = images[0].size

    # Tạo một hình ảnh mới với kích thước gấp đôi chiều rộng và chiều cao của một hình ảnh
    merged_image = Image.new("RGB", (width * 2, height * 2))

    # Dán các hình ảnh vào hình ảnh mới
    merged_image.paste(images[0], (0, 0))
    merged_image.paste(images[1], (width, 0))
    merged_image.paste(images[2], (0, height))
    merged_image.paste(images[3], (width, height))

    # Lưu hình ảnh đã ghép
    merged_image.save(output_path)
    print(f"Hình ảnh đã được ghép và lưu tại: {output_path}")


if __name__ == "__main__":
    image_folder = "datasets/images"
    output_path = "datasets/images/merged_image.jpg"
    merge_images(image_folder, output_path)
