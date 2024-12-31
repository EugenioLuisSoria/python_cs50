user_file = input("Ingrese su archivo: ").lower().replace(" ","")

puntos = user_file.count(".")


if puntos == 1:
    user_file = user_file.split(".")[1]
    match user_file:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case "bin":
            print("application/octet-stream")
        case _:
            print("no corresponde")
    
elif puntos == 2:
    user_file = user_file.split(".")[2]
    match user_file:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case "bin":
            print("application/octet-stream")
        case _:
            print("no corresponde")

else:
    print("application/octet-stream")



    

        
        