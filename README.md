# ComfyUI-Load-txt-From-Folder

A simple and efficient custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to batch load text (`.txt`) files from a specific folder.

## Features

* **Batch Loading:** Reads all `.txt` files in a specified directory.
* **Index Control:** Selects files via an integer index (0, 1, 2...), making it compatible with `Primitive` nodes for iterating or batch processing.
* **Auto-Cycling:** If the index exceeds the number of files, it automatically wraps around (modulo), ensuring your workflow never errors out due to index bounds.
* **Outputs:** Returns the raw text content and the filename (without extension).

## Installation

### Method 1: Manual Installation (Recommended)
1.  Navigate to your ComfyUI `custom_nodes` folder.
2.  Clone this repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/ComfyUI-Load-txt-From-Folder.git](https://github.com/YOUR_USERNAME/ComfyUI-Load-txt-From-Folder.git)
    ```
3.  Restart ComfyUI.

### Method 2: Manager (If added to registry)
* If this node is added to the ComfyUI-Manager registry in the future, you can install it by searching for "Load Txt From Folder".

## Usage

1.  **Add Node:** Double-click on the ComfyUI canvas and search for **"Load Txt From Folder"**.
2.  **Configuration:**
    * **txt_folder:** Paste the full absolute path to the folder containing your text files.
    * **index:** The number of the file to load (starts at 0).
3.  **Outputs:**
    * **text:** Connect this to any node that accepts a `STRING` input (e.g., CLIP Text Encode, Show Text, etc.).
    * **file_name:** The name of the file (useful for saving outputs with matching names).

## Node Inputs & Outputs

| Type | Name | Description |
| :--- | :--- | :--- |
| **Input** | `txt_folder` | The absolute path to the directory containing `.txt` files. |
| **Input** | `index` | The integer index of the file to load. Increment this to cycle through files. |
| **Output** | `text` | The content of the text file as a string. |
| **Output** | `file_name` | The filename (e.g., "my_prompt" from "my_prompt.txt"). |

## Troubleshooting

* **"Folder path is empty!"**: Ensure you have pasted a path into the widget.
* **"Folder does not exist"**: Check that the path is correct and accessible by the OS.
* **"No .txt files found"**: The folder exists, but it contains no files ending in `.txt`.

---

## License

This project is open-source and available under the MIT License.

## Credits

Created for the ComfyUI community.
