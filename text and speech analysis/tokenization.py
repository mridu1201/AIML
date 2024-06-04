import re
def detect_word_patterns(text,pattern):
  matches = re.findall(pattern,text)
  return matches
def tokenize_text(pattern,text):
  matcher=re.findall(pattern,text)
  return matcher
if __name__ == "__main__":
  text_1 ="The prefix pre is present in words like preheat and preview."
  pattern_1=r'\bpre\w+'
  matches1=detect_word_patterns(text_1,pattern_1)
  print("word patterns:", matches1)
  text_2="This is a sample sentence, with mageshBabu!"
  pattern_2=r'\b\w+\b|[^\w\s]'
  matches_2=tokenize_text(pattern_2,text_2);
  print(matches_2);