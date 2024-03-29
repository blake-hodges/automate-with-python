lorem_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

arr = lorem_text.split(" ")

arr_len = len(arr)

i = 0
while i < arr_len - 1:
    text = arr[i].capitalize() + " " + arr[i + 1].capitalize()
    cleaned = text.replace(".", "").replace(",", "")
    list_item = "<li>" + cleaned + "</li>"
    print(list_item)
    i+=2
