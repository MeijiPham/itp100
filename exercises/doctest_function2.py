def remove_sub(sub, main):
    """
      >>> remove_sub("an", "banana")
      'bana'
      >>> remove_sub("cyc", "bicycle")
      'bile'
      >>> remove_sub("iss", "Mississippi")
      'Missippi'
      >>> remove_sub("egg", "bicycle")
      'bicycle'
    """
    new_string =  main.replace(sub, "", 1)
    return new_string











if __name__ == "__main__":
    import doctest
    doctest.testmod()
