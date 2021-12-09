cpu_score = 0
user_score  = 0

def add_cpu_score():
  global cpu_score
  cpu_score += 1

def add_user_score():
  global user_score
  user_score += 1

def get_cpu_score():
  return cpu_score

def get_user_score():
  return user_score