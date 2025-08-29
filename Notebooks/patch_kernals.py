import json
import sys

def patch_language(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    if 'metadata' in nb and 'kernelspec' in nb['metadata']:
        ks = nb['metadata']['kernelspec']
        if 'language' not in ks:
            ks['language'] = 'python'  # change if your kernel is not Python
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1)
            print(f"Patched: {filepath}")
        else:
            print("Already has 'language'.")
    else:
        print("kernelspec missing")
        # Optionally add full kernelspec here if needed.
        
# Usage:
# python3 patch_language.py Chap04/4_1_Composing_Networks.ipynb
if __name__ == "__main__":
    patch_language(sys.argv[1])
