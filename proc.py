import os
# *.md    -> *.zh.md
# *_en.md -> *.md

def rename_files_recursively(directory):
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for filename in files:
            if filename.endswith(".md"):
                new_filename = filename.replace("_en", "").replace(".md", ".zh.md")
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    target_directory = "./."
    rename_files_recursively(target_directory)

