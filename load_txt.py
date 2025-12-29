import os
import hashlib

class LoadTxtFromFolder:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "txt_folder": ("STRING", {"default": "", "multiline": False}),
                "index": ("INT", {"default": 0, "min": 0, "max": 999999, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("text", "file_name")
    FUNCTION = "load_txt"
    CATEGORY = "text"

    def load_txt(self, txt_folder: str, index: int):
        # 1. Validation
        if not txt_folder or not txt_folder.strip():
            raise ValueError("Folder path is empty!")
        txt_folder = txt_folder.strip()
        if not os.path.isdir(txt_folder):
            raise ValueError(f"Folder does not exist: {txt_folder}")

        # 2. Filter for .txt files
        files = [
            f for f in os.listdir(txt_folder)
            if os.path.splitext(f)[1].lower() == '.txt'
            and os.path.isfile(os.path.join(txt_folder, f))
        ]
        
        if not files:
            raise ValueError(f"No .txt files found in: {txt_folder}")

        # 3. Sort and handle Index Wrapping
        files.sort(key=lambda x: x.lower())
        if index >= len(files):
            index = index % len(files) if files else 0

        selected_file = files[index]
        file_path = os.path.join(txt_folder, selected_file)

        # 4. Read Text Content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            raise ValueError(f"Failed to read file {selected_file}: {e}")

        name_without_ext = os.path.splitext(selected_file)[0]

        return (content, name_without_ext)

    @classmethod
    def IS_CHANGED(cls, txt_folder: str, index: int):
        # Checks for file changes so the node updates when you add new files or change the index
        if not txt_folder or not os.path.isdir(txt_folder):
            return "invalid"
        try:
            files = [
                f for f in os.listdir(txt_folder) 
                if os.path.splitext(f)[1].lower() == '.txt' 
                and os.path.isfile(os.path.join(txt_folder, f))
            ]
            files.sort(key=str.lower)
            
            # Create a unique hash based on file names and the most recent modification time
            hash_str = ''.join(files)
            hash_val = hashlib.md5(hash_str.encode()).hexdigest()
            mtime = max(os.path.getmtime(os.path.join(txt_folder, f)) for f in files) if files else 0
            
            return f"{hash_val}_{mtime}_{index}"
        except:
            return "error"

# Node Registration
NODE_CLASS_MAPPINGS = {
    "Load Txt From Folder": LoadTxtFromFolder
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Load Txt From Folder": "Load Txt From Folder"
}