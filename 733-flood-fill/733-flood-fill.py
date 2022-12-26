class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def flood(sr, sc):
            image[sr][sc] = newColor
            
            if sr > 0 and image[sr - 1][sc] == old:
                flood(sr - 1, sc)

            if sr < leny and image[sr + 1][sc] == old:
                flood(sr + 1, sc)

            if sc > 0 and image[sr][sc- 1] == old:
                flood(sr, sc - 1)

            if sc < lenx and image[sr][sc + 1] == old:
                flood(sr, sc + 1)

        if image[sr][sc] == newColor:
            return image

        lenx, leny = len(image[0]) - 1, len(image) - 1
        old = image[sr][sc]
        flood(sr, sc)
        return image
        