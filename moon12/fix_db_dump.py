open("artful.db.utf8.json","wb").write(open("artful.db.json").read().decode("unicode_escape").encode("utf8"))
