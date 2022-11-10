class binary_tree:
  """
  __init__(self, root = None)
  クラスに初期登録したときに行う関数。
  object.value = None
  object.left = None
  object.right = None
  """
  def __init__(self, root = None):
    self.value = root
    self.left = None
    self.right = None

  """
  insert_left(self, insert)
  class登録は複数の値を持つボックスの登録に等しい。
  もしすでにleftに登録されている場合、入れ替える。
  """
  def insert_left(self, insert):
    if self.left == None:
      self.left = binary_tree(insert)
    else:
      t = binary_tree(insert)
      t.left = self.left
      self.left = t

  """
  insert_right(self, insert)
  class登録は複数の値を持つボックスの登録に等しい。
  もしすでにrightに登録されている場合、入れ替える。
  """
  def insert_right(self, insert):
    if self.right == None:
      self.right = binary_tree(insert)
    else:
      t = binary_tree(insert)
      t.right = self.right
      self.right = t

  """
  下層のオブジェクトの値の確認
  """
  def get_left(self):
    return self.left

  def get_right(self):
    return self.right

  """
  上層の値の設定
  """
  def put_root(self, obj):
    self.value = obj

  """
  上層の値の確認
  """
  def get_root(self):
    return self.value


ROOT = binary_tree()
print(ROOT.value)

ROOT.insert_left("f_left")
print(ROOT.get_left)
