
from js import document


grade7 = {"Pearl Sumbillo", "Caela Regulacion", "Aphia Batican", "Soap"}
grade8 = {"Dezzarae Almirol", "Harley Malonso", "Cheska Torres", "Gabriel Ferrer"}
grade9 = {"Kean Lardizabal", "Nastasia Tanglao", "Aubrey Cabrera", "Bella Canlas"}
grade10 = {"Megan Tan", "Mica Frigilana", "Alysha aguilar", "Lucas Tanglao", "Raji Santos"}


new_members = set()


def update_display():
    all_members = grade7 | grade8 | grade9 | grade10 | new_members

    members_list = "<br>".join(all_members)

    document.getElementById("results").innerHTML = f"""
        All members:<br>
        {members_list}<br>
        Total members: {len(all_members)}
    """


def add_member(event):
    first = document.getElementById("first").value
    last = document.getElementById("last").value

    new_members.add(f"{first} {last}")

    update_display()


update_display()
