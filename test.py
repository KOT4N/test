def test():
  with open("t.py") as f:
    if len(f.read()) > 0:
      return True
    else:
      sys.exit()
