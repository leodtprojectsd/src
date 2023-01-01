# Example for Stack overflow 

The obejective of this repo is to arrive at a standard structure for multiple mains (analysis) that use the same function. 

I want to: 
 - complete main_one_age_00_and_01_and_02, main_one_height_00_and_01_and_02, main_display_combined, so that they run within their folders (not ROOT) 
 - Run the single blocks of a main eg"import_and_clean_age_00.py" as main directly. 

eg: this should work 
 from display_data import display_data
```python
def display_data_main_one(age_mean):
    return display_data.common_function_display_data(age_mean)
     
if __name__ == '__main__': 
    display_data("path to age mean")
    
 OUT: 
 ModuleNotFoundError: No module named 'display_data'
 ```
 - use a standard way of writing the file "path_for_data_etc.py" that contains all the paths to import/export data. 
 - write pyproject.toml/setup.py/ or any other file that is necessary so that the project can be considered complete. 
