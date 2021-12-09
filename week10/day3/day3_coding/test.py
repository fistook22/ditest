# f = open("secrets.txt")
# secret_data = f.read()
#
# f.close()
#
# print(secret_data)

# best practice

# with open("secrets.txt", mode="r+") as f:
#     secret_data = f.read()
#     f.write("my name is actually fistook")
#     print(secret_data)
with open("secrets.txt", mode="r+") as f:
    secret_data = f.readlines()

    for i in range(len(secret_data)):
        secret_data[i] = secret_data[i].split("\n")[0]

        print(f"this is the 5th word {secret_data[4]}")

    count_darth = 0

    for name in secret_data:
        if name == "Darth":
            count_darth += 1

        print(count_darth)

    f.write("\nfistook")

    for name in range(len(secret_data)):
        if secret_data[name] == "Luke":
            secret_data[name] += " Skywalker"
        print(secret_data)

