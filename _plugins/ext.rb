# Monkey-patch for Ruby 3.4+/4.0 compatibility with older Jekyll/liquid gems
# String#tainted? and friends were removed in Ruby 3.4

class String
  def tainted?
    false
  end
  def taint
    self
  end
  def untaint
    self
  end
  def untrusted?
    false
  end
  def untrust
    self
  end
  def trust
    self
  end
end
