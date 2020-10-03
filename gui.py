import tkinter as tk
import requests


win = tk.Tk()
win.title("CRUD_API_TKINTER")
win.geometry("450x450")

BASE = "http://127.0.0.1:5000/"


def create():
    name = name_field.get()
    views = views_field.get()
    likes = likes_field.get()
    data = {"name": name, "views": views, "likes": likes}
    response = requests.put(BASE + "video/1", data)
    print(response.json())

    name_field.delete(0, tk.END)
    views_field.delete(0, tk.END)
    likes_field.delete(0, tk.END)


def get():
    id = get_id_field.get()
    response = requests.get(BASE + "video/" + str(id))
    print(response.json())

    get_id_field.delete(0, tk.END)


def delete():
    id = get_id_field.get()
    response = requests.delete(BASE + "video/" + str(id))
    print(response)

    get_id_field.delete(0, tk.END)


def edit():
    id = get_id_field.get()
    response = requests.get(BASE + 'video/' + str(id))
    r = response.json()

    if not r.get('message') == 'Video not found...':
        global editor
        editor = tk.Tk()
        editor.title("Edit Record")
        editor.geometry("350x300")

        editor_frame = tk.Frame(editor, padx=10, pady=10, bd=1, relief="sunken")
        editor_frame.grid(row=1, column=2, padx=10, pady=10)

        global e_name_field
        global e_views_field
        global e_likes_field

        e_name_label = tk.Label(editor_frame, text="Name")
        e_name_field = tk.Entry(editor_frame, width=30)
        e_views_label = tk.Label(editor_frame, text="Views")
        e_views_field = tk.Entry(editor_frame, width=30)
        e_likes_label = tk.Label(editor_frame, text="Likes")
        e_likes_field = tk.Entry(editor_frame, width=30)

        e_name_label.grid(row=1, column=1)
        e_name_field.grid(row=1, column=2, padx=5, pady=5)
        e_views_label.grid(row=2, column=1)
        e_views_field.grid(row=2, column=2, padx=5, pady=5)
        e_likes_label.grid(row=3, column=1)
        e_likes_field.grid(row=3, column=2, padx=5, pady=5)

        name = r['name']
        views = r['views']
        likes = r['likes']
        e_name_field.insert(0, name)
        e_views_field.insert(0, views)
        e_likes_field.insert(0, likes)

        update_button = tk.Button(editor_frame, text="Update Record", command=update)
        update_button.grid(row=4, column=2, pady=10)

    else:
        print(r)


def update():
    id = get_id_field.get()
    edited_name = e_name_field.get()
    edited_views = e_views_field.get()
    edited_likes = e_likes_field.get()
    data = {"name": edited_name, "views": edited_views, "likes": edited_likes}
    response = requests.patch(BASE + "video/" + str(id), data)
    print(response.json())

    e_name_field.delete(0, tk.END)
    e_views_field.delete(0, tk.END)
    e_likes_field.delete(0, tk.END)
    editor.destroy()


# Create Frame
create_frame = tk.Frame(win, padx=10, pady=10, bd=1, relief="sunken")
create_frame.grid(row=1, column=2, padx=10, pady=10)

name_label = tk.Label(create_frame, text="Name")
name_field = tk.Entry(create_frame, width=30)
views_label = tk.Label(create_frame, text="Views")
views_field = tk.Entry(create_frame, width=30)
likes_label = tk.Label(create_frame, text="Likes")
likes_field = tk.Entry(create_frame, width=30)

name_label.grid(row=1, column=1)
name_field.grid(row=1, column=2, padx=5, pady=5)
views_label.grid(row=2, column=1)
views_field.grid(row=2, column=2, padx=5, pady=5)
likes_label.grid(row=3, column=1)
likes_field.grid(row=3, column=2, padx=5, pady=5)

create_button = tk.Button(create_frame, text="Add New Record", command=create)
create_button.grid(row=4, column=1, pady=10, columnspan=2)


# Read and Delete Frame
get_frame = tk.Frame(win, padx=10, pady=10, bd=1, relief="sunken")
get_frame.grid(row=2, column=2, padx=10, pady=10)

get_id_label = tk.Label(get_frame, text="Enter ID")
get_id_field = tk.Entry(get_frame, width=30)
get_id_label.grid(row=1, column=1, padx=5, pady=5)
get_id_field.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

search_button = tk.Button(get_frame, text="Search Record", command=get)
search_button.grid(row=2, column=1, pady=10)

delete_button = tk.Button(get_frame, text="Delete Record", command=delete)
delete_button.grid(row=2, column=2, pady=10)

update_button = tk.Button(get_frame, text="Edit Record", command=edit)
update_button.grid(row=2, column=3, pady=10)


# Message / Output Frame
out_frame = tk.Frame(win, padx=10, pady=10, bd=1, relief="sunken")
out_frame.grid(row=1, column=1, padx=10, pady=10)


win.mainloop()