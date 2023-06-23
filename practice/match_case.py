def do_that():
    print("Doing that!")

def do_this():
    print("Doing this!")

match input("Doing this or that?"):
    case "this":
        do_this()
    case "that":
        do_that()