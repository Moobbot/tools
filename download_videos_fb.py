import sys
import subprocess
import yt_dlp

# Tự động cập nhật yt-dlp lên bản mới nhất
print("Đang kiểm tra và cập nhật yt-dlp...")
try:
    subprocess.run([sys.executable, "-m", "pip", "install", "-U", "yt-dlp"], check=True)
    print("Cập nhật yt-dlp thành công!\n")
except Exception as e:
    print(f"Không thể cập nhật yt-dlp: {e}\n")

# Thử cả URL gốc và URL dạng embed (thường dễ tải hơn)
urls = [
    "https://www.facebook.com/watch/?v=3772940872836098",
    "https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=3772940872836098"
]

browsers = ['chrome', 'edge', 'firefox', 'opera']
success = False

for url in urls:
    if success:
        break
    print(f"==================================================")
    print(f"ĐANG THỬ TẢI URL: {url}")
    print(f"==================================================")
    
    # 1. Thử các trình duyệt lấy cookies
    for browser in browsers:
        print(f"\n[?] Đang thử với cookies từ trình duyệt: {browser}...")
        ydl_opts = {
            "outtmpl": "%(title)s.%(ext)s",
            "cookiesfrombrowser": (browser,),
            "ignoreerrors": True,  # Không dừng script khi gặp lỗi nhỏ
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.download([url])
                if result == 0:
                    success = True
                    print(f"--> [OK] Tải thành công bằng cookies từ {browser}!")
                    break
                else:
                    print(f"--> [FAIL] Thử với {browser} không thành công (Exit code: {result})")
        except BaseException as e:
            print(f"--> [ERROR] Thử với {browser} lỗi: {e}")
            
    # 2. Thử tải không dùng cookies
    if not success:
        print("\n[?] Đang thử tải không sử dụng cookies...")
        ydl_opts = {
            "outtmpl": "%(title)s.%(ext)s",
            "ignoreerrors": True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.download([url])
                if result == 0:
                    success = True
                    print("--> [OK] Tải thành công không cần cookies!")
                    break
                else:
                    print(f"--> [FAIL] Tải không dùng cookies không thành công (Exit code: {result})")
        except BaseException as e:
            print(f"--> [ERROR] Tải không dùng cookies lỗi: {e}")

print(f"\n==================================================")
if success:
    print("QUÁ TRÌNH TẢI HOÀN TẤT THÀNH CÔNG!")
else:
    print("KẾT THÚC: Không thể tải video bằng bất kỳ phương thức nào.")
    print("Gợi ý: Hãy đảm bảo video ở chế độ công khai và bạn đã đăng nhập Facebook trên trình duyệt tương ứng.")
print(f"==================================================")
