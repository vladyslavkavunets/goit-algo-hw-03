import shutil
import sys
from pathlib import Path

def copy_files_recursively(source_dir, dest_dir="dist"):
    try:
        source_path = Path(source_dir)
        dest_path = Path(dest_dir)
        
        if not source_path.exists():
            print(f"Помилка: Директорія '{source_dir}' не існує!")
            return
        
        if not source_path.is_dir():
            print(f"Помилка: '{source_dir}' не є директорією!")
            return
        
        dest_path.mkdir(exist_ok=True)
        print(f"Створено директорію призначення: {dest_path.absolute()}")
        
        def read_directory(current_dir):
            try:
                for item in current_dir.iterdir():
                    if item.is_dir():
                        print(f"Входимо в піддиректорію: {item.name}")
                        read_directory(item)
                    elif item.is_file():
                        copy_file(item, dest_path)
            except PermissionError:
                print(f"Немає доступу до директорії: {current_dir}")
            except Exception as e:
                print(f"Помилка при читанні директорії {current_dir}: {e}")
        
        def copy_file(file_path, destination_root):
            try:
                file_extension = file_path.suffix.lower()
                
                if file_extension:
                    subdir_name = file_extension[1:]
                else:
                    subdir_name = "no_extension"
                
                target_subdir = destination_root / subdir_name
                target_subdir.mkdir(exist_ok=True)
                
                target_file = target_subdir / file_path.name
                
                if target_file.exists():
                    base_name = file_path.stem
                    extension = file_path.suffix
                    counter = 1
                    while target_file.exists():
                        new_name = f"{base_name}_{counter}{extension}"
                        target_file = target_subdir / new_name
                        counter += 1
                
                shutil.copy2(file_path, target_file)
                print(f"Скопійовано: {file_path.name} -> {subdir_name}/{target_file.name}")
                
            except Exception as e:
                print(f"Помилка при копіюванні файлу {file_path}: {e}")
        
        print(f"Починаємо обробку директорії: {source_dir}")
        print("-" * 60)
        
        read_directory(source_path)
        
        print("-" * 60)
        print("Копіювання завершено успішно!")
        
    except Exception as e:
        print(f"Критична помилка: {e}")

def main():
    if len(sys.argv) < 2:
        print("Вкажіть папку для обробки!")
        print("Приклад: python3 directory_file_sorter.py dist")
        sys.exit(1)
    
    source_directory = sys.argv[1]
    
    if len(sys.argv) >= 3:
        destination_directory = sys.argv[2]
    else:
        destination_directory = "dist"
    
    print("=" * 60)
    print("РЕКУРСИВНЕ КОПІЮВАННЯ ТА СОРТУВАННЯ ФАЙЛІВ")
    print("=" * 60)
    print(f"Вихідна директорія: {source_directory}")
    print(f"Директорія призначення: {destination_directory}")
    print("=" * 60)
    
    copy_files_recursively(source_directory, destination_directory)

if __name__ == "__main__":
    main()