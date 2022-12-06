class Solution:
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(letter) <= magazine.count(letter) 
                      for letter in set(ransomNote)
                  )