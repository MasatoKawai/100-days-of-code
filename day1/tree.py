class binary_tree:
  def __init__(self, root = None):
    self.value = root
    self.left = None
    self.right = None

  def insert_left(self, insert):
    if self.left == None:
      self.left = binary_tree(insert)
    else:
      t = binary_tree(insert)
      t.left = self.left
      self.left = t

  def insert_right(self, insert):
    if self.right == None:
      self.right = binary_tree(insert)
    else:
      t = binary_tree(insert)
      t.right = self.right
      self.right = t

  def get_left(self):
    return self.left

  def get_right(self):
    return self.right

  def put_root(self, obj):
    self.value = obj

  def get_root(self):
    return self.value
