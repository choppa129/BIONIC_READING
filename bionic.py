# import os
# from bs4 import BeautifulSoup
# import zipfile
#
# # 指定 EPUB 文件路径
# epub_file_path = 'F:/Why Nations Fail The Origins of Power, Prosperity, and Poverty (Daron Acemoglu, James Robinson) (Z-Library).epub'  # 替换为你的 EPUB 文件路径
#
# # 修改后缀为 .zip
# zip_file_path = epub_file_path.replace('.epub', '.zip')
#
# # 重命名 EPUB 文件为 ZIP 文件
# os.rename(epub_file_path, zip_file_path)
#
# # 从 ZIP 文件名中提取文件名（去掉后缀），作为解压缩目录名
# base_name = os.path.splitext(os.path.basename(zip_file_path))[0]
# output_directory = os.path.join(os.path.dirname(zip_file_path), base_name)
#
# # 创建输出目录（如果不存在）
# os.makedirs(output_directory, exist_ok=True)
#
# # 解压缩 ZIP 文件
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(output_directory)
#
# print(f"已将 ZIP 文件解压缩到: {output_directory}")
#
#
# # Bionic Reading转换函数
# def bionic_reading(text):
#     words = text.split()
#     bionic_text = []
#     for word in words:
#         if len(word) > 3:
#             bold_part = word[:len(word)//2]  # 取前一半加粗
#             rest_part = word[len(word)//2:]
#             bionic_text.append(f"<b>{bold_part}</b>{rest_part}")
#         else:
#             bold_part = word[0]  # 取前一半加粗
#             rest_part = word[1:]
#             bionic_text.append(f"<b>{bold_part}</b>{rest_part}")
#     return ' '.join(bionic_text)
#
# # 存储找到的 .htm 文件路径
# htm_files = []
#
# # 遍历目录及其子目录
# for root, dirs, files in os.walk(output_directory):
#     for file in files:
#         if file.endswith('.htm') or file.endswith('.html'):
#             htm_files.append(os.path.join(root, file))
#
# # 对每个找到的 .htm 文件进行 Bionic Reading 转换
# for htm_file in htm_files:
#     # 加载HTML文件内容
#     with open(htm_file, 'r', encoding='utf-8') as f:
#         content = f.read()
#
#     # 使用BeautifulSoup解析HTML
#     soup = BeautifulSoup(content, 'html.parser')
#
#     # 遍历所有段落并进行Bionic Reading转换
#     for p in soup.find_all('p'):
#         if p.get_text():  # 检查段落是否有文本内容
#             new_content = bionic_reading(p.get_text())
#             p.clear()  # 清除原有内容
#             p.append(BeautifulSoup(new_content, 'html.parser'))  # 添加新的HTML内容
#
#     # 输出转换后的HTML，文件名加上前缀 bionic_
#     output_filename = f"{os.path.basename(htm_file)}"
#     output_path = os.path.join(os.path.dirname(htm_file), output_filename)
#
#     # 保存处理后的内容
#     with open(output_path, 'w', encoding='utf-8') as f:
#         f.write(str(soup))
#
#     print(f"Bionic Reading HTML已保存至: {output_path}")
#
# # 指定输出 ZIP 文件的路径
# bionic_zip_file_path = os.path.join(os.path.dirname(zip_file_path), f"bionic_{base_name}.zip")  # 生成新的 ZIP 文件路径
#
# # 创建 ZIP 文件
# with zipfile.ZipFile(bionic_zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
#     # 遍历输出目录，添加文件到 ZIP 文件
#     for root, dirs, files in os.walk(output_directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             # 将文件相对路径添加到 ZIP 文件中
#             zipf.write(file_path, os.path.relpath(file_path, output_directory))
#
# print(f"已将内容压缩为 ZIP 文件: {bionic_zip_file_path}")
#
# # 如果需要将 ZIP 文件重命名为 EPUB 文件
# bionic_epub_file_path = bionic_zip_file_path.replace('.zip', '.epub')
# os.rename(bionic_zip_file_path, bionic_epub_file_path)
# print(f"已将 ZIP 文件重命名为 EPUB 文件: {bionic_epub_file_path}")
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
from bs4 import BeautifulSoup

def select_file():
    # 打开文件选择对话框，选择 EPUB 文件
    file_path = filedialog.askopenfilename(
        title="选择 EPUB 文件",
        filetypes=[("EPUB Files", "*.epub")]
    )
    if file_path:
        # 显示选择的文件路径
        entry.delete(0, tk.END)  # 清空现有内容
        entry.insert(0, file_path)  # 在文本框中插入选择的文件路径

def process_file():
    # 获取用户选择的 EPUB 文件路径
    epub_file_path = entry.get()
    if not epub_file_path:
        messagebox.showerror("错误", "请选择一个 EPUB 文件！")
        return

    try:
        # 这里可以调用你的 EPUB 处理逻辑
        # 修改后缀为 .zip
        zip_file_path = epub_file_path.replace('.epub', '.zip')

        # 重命名 EPUB 文件为 ZIP 文件
        os.rename(epub_file_path, zip_file_path)

        # 从 ZIP 文件名中提取文件名（去掉后缀），作为解压缩目录名
        base_name = os.path.splitext(os.path.basename(zip_file_path))[0]
        output_directory = os.path.join(os.path.dirname(zip_file_path), base_name)

        # 创建输出目录（如果不存在）
        os.makedirs(output_directory, exist_ok=True)

        # 解压缩 ZIP 文件
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_directory)

        print(f"已将 ZIP 文件解压缩到: {output_directory}")

        # 存储找到的 .htm 文件路径
        htm_files = []

        # 遍历目录及其子目录
        for root, dirs, files in os.walk(output_directory):
            for file in files:
                if file.endswith('.htm') or file.endswith('.html'):
                    htm_files.append(os.path.join(root, file))

        # 对每个找到的 .htm 文件进行 Bionic Reading 转换
        for htm_file in htm_files:
            # 加载HTML文件内容
            with open(htm_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 使用BeautifulSoup解析HTML
            soup = BeautifulSoup(content, 'html.parser')

            # 遍历所有段落并进行Bionic Reading转换
            for p in soup.find_all('p'):
                if p.get_text():  # 检查段落是否有文本内容
                    new_content = bionic_reading(p.get_text())
                    p.clear()  # 清除原有内容
                    p.append(BeautifulSoup(new_content, 'html.parser'))  # 添加新的HTML内容

            # 输出转换后的HTML，文件名加上前缀 bionic_
            output_filename = f"{os.path.basename(htm_file)}"
            output_path = os.path.join(os.path.dirname(htm_file), output_filename)

            # 保存处理后的内容
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))

            print(f"Bionic Reading HTML已保存至: {output_path}")

        # 指定输出 ZIP 文件的路径
        bionic_zip_file_path = os.path.join(os.path.dirname(zip_file_path), f"bionic_{base_name}.zip")  # 生成新的 ZIP 文件路径

        # 创建 ZIP 文件
        with zipfile.ZipFile(bionic_zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 遍历输出目录，添加文件到 ZIP 文件
            for root, dirs, files in os.walk(output_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    # 将文件相对路径添加到 ZIP 文件中
                    zipf.write(file_path, os.path.relpath(file_path, output_directory))

        print(f"已将内容压缩为 ZIP 文件: {bionic_zip_file_path}")

        # 如果需要将 ZIP 文件重命名为 EPUB 文件
        bionic_epub_file_path = bionic_zip_file_path.replace('.zip', '.epub')
        os.rename(bionic_zip_file_path, bionic_epub_file_path)
        print(f"已将 ZIP 文件重命名为 EPUB 文件: {bionic_epub_file_path}")

    except Exception as e:
        messagebox.showerror("处理错误", f"发生错误: {e}")

# Bionic Reading转换函数
def bionic_reading(text):
    words = text.split()
    bionic_text = []
    for word in words:
        if len(word) > 3:
            bold_part = word[:len(word)//2]  # 取前一半加粗
            rest_part = word[len(word)//2:]
            bionic_text.append(f"<b>{bold_part}</b>{rest_part}")
        else:
            bionic_text.append(word)
    return ' '.join(bionic_text)

# 创建主窗口
root = tk.Tk()
root.title("EPUB 处理工具")

# 创建并配置输入框
entry = tk.Entry(root, width=80)
entry.pack(pady=10)

# 创建选择文件按钮
select_button = tk.Button(root, text="选择 EPUB 文件", command=select_file)
select_button.pack(pady=5)

# 创建处理文件按钮
process_button = tk.Button(root, text="处理文件", command=process_file)
process_button.pack(pady=5)

# 运行主事件循环
root.mainloop()
